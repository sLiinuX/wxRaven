'''
Created on 12 déc. 2021

@author: slinux
'''
import os
import wx
import pickle
import inspect 
import logging

from wxRavenGUI.application.wxcustom.CustomUserIO import UserAdvancedMessage, RequestUserTextInput

class perspectiveContentDescriptor(object):
    
    
    
    _initialized=False
    _name = ''
    
    mgr_perspective_datas=''
    plugins_datas={}
    
     
    def __init__(self):
        pass
    
    def ExportPerspective(self, _name='wxRavenPerpective'):
        return {
            'name' : _name,
            'mgr_perspective':self.mgr_perspective_datas,
            'plugins':self.plugins_datas
            }
        
        
        
    def SnapshotPerspective(self, parentframe):
        self.mgr_perspective_datas = parentframe.m_mgr.SavePerspective()
        self.plugins_datas = parentframe.Plugins.SaveAllPluginState(virtual=True)
        self._initialized= True
        
        return self._initialized
        
        
    def SaveUserPerspective(self, path, name='wxRavenPerpective'):
        logger = logging.getLogger('wxRaven')
        _saved = False
        if self._initialized==False:
            logger.error('Invalid or null perspective.') 
            return
        
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            
            logger.info(f'Saving user perspective {name} in {path}...')
            pickle.dump( self.ExportPerspective(name), open(path+name+".perspective", "wb" ) )
            _saved = True
        except Exception as e:
            logger.error(e) 
            
        return _saved
        
        
    def LoadUserPerspective(self, perspective_filename):    
        logger = logging.getLogger('wxRaven')
        
        try:
            
            
            logger.info(f'Loading user perspective {perspective_filename}...')
            result = pickle.load( open(perspective_filename, "rb" ) )
            
            self.mgr_perspective_datas = result['mgr_perspective']
            self.plugins_datas = result['plugins']
            self._name = result['name']
            self._initialized= True
        
            
        except Exception as e:
            logger.error(e)
            
        return self._initialized
    
    
    
    def RestoreSnapshot(self, parentframe):
        logger = logging.getLogger('wxRaven')
        _saved = False
        if self._initialized==False:
            logger.error('Invalid or null perspective.') 
            return
        
        
        parentframe.Plugins.RestorePluginsDatas(self.plugins_datas)
        parentframe.m_mgr.LoadPerspective(self.mgr_perspective_datas)
        
    
        
    #self.PerspectiveManager.SaveLastPerspective()
    #self.Plugins.SaveAllPluginState()





class perspectiveManager(object):
    '''
    classdocs
    '''
    parentframe = None
    configpath = None
    
    lastperspectivefilename = ""
    lastsizefilename = ""
    
    
    
    perspective_additional_data = {}
    

    def __init__(self, parentframe, configpath, loadLastView=False):
        '''
        Constructor
        '''
        self.parentframe = parentframe
        self.configpath = configpath
        
        self.logger = logging.getLogger('wxRaven')
        
        self.lastperspectivefilename = self.configpath+"perspective.last"
        self.lastsizefilename = self.configpath+"window.last"
        
        
        self.userperspectivepath = parentframe.GetPath('USERDATA')+'perspectives/'
        if not os.path.exists(self.userperspectivepath):
            os.makedirs(self.userperspectivepath)
        
        self.perspective_additional_data = {}
        
        
        self.parentframe.wxRavenMenuBar_Window_Perspectives.Bind( wx.EVT_MENU, self.OnResumeMenuOptionChanged, id = self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.GetId() )
        self.parentframe.wxRavenMenuBar_Window_Perspectives.Bind( wx.EVT_MENU, self.OnSaveMenuOptionChanged, id = self.parentframe.wxRavenMenuBar_Window_Perspectives_SaveOnClose.GetId() )
        
        if loadLastView:
            self.LoadLastPerspective()
    
    
    
    
    def OnResumeMenuOptionChanged(self, evt):
        #_s = self.wxRavenMenuBar_Window_Perspectives.IsChecked(self.wxRavenMenuBar_Window_Perspectives_SaveOnClose.GetId())
        _s = self.parentframe.wxRavenMenuBar_Window_Perspectives.IsChecked(self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.GetId())
        self.ToggleResumeViewSettings( _s, True)
    
    
    def OnSaveMenuOptionChanged(self, evt):
        #_s = self.wxRavenMenuBar_Window_Perspectives.IsChecked(self.wxRavenMenuBar_Window_Perspectives_SaveOnClose.GetId())
        _s = self.parentframe.wxRavenMenuBar_Window_Perspectives.IsChecked(self.parentframe.wxRavenMenuBar_Window_Perspectives_SaveOnClose.GetId())
        self.ToggleSaveViewSettings( _s, True)
        
    
    def ToggleResumeViewSettings(self, _tValue=True, _fromEvent=False):
        print(f"ToggleResumeViewSettings {_tValue} {_fromEvent}")
        self.parentframe.Settings.resumeviewonstartup = _tValue
        self.parentframe.Settings.resumepluginstate = _tValue
        #self.parentframe.Settings.
        #self.parentframe.Settings.resumeviewonstartup = _tValue
        if not _fromEvent:
            self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.Check( _tValue )
        #self.parentframe.wxRavenMenuBar_Window_Perspectives_SaveOnClose.Check( True )
    
    
    def ToggleSaveViewSettings(self, _tValue=True, _fromEvent=False):
        print(f"ToggleSaveViewSettings {_tValue} {_fromEvent}")
        p = self.parentframe.GetPlugin('General')
        p.PLUGIN_SETTINGS['save_on_close'] = _tValue
        #self.parentframe.Settings.resumeviewonstartup = _tValue
        #self.parentframe.Settings.resumeviewonstartup = _tValue
        if not _fromEvent:
            self.parentframe.wxRavenMenuBar_Window_Perspectives_SaveOnClose.Check( _tValue )
    
    
    
    
    
    
    
    def RaisePerspectiveLog(self, message, type="error"):
        try:
            _source = str(inspect.stack()[1][0])
            self.parentframe.Log( message, source=str(_source), type=type)
        except Exception as e:
            self.logger.error("RaisePerspectiveLog() " + str(e))  
    
    
    def saveWindowsSize(self):
        
        
        currentSize = self.parentframe.GetSize()
        currentPosition = self.parentframe.GetScreenPosition()
        
        self.perspective_additional_data["windowSize"] = currentSize
        self.perspective_additional_data["windowPosition"] = currentPosition
        
        
        
        #self.__saveVar__(self.lastsizefilename, currentSize)
        self.__saveVar__(self.lastsizefilename, self.perspective_additional_data)
        
        
    
    
    def loadWindowsSize(self):
        
        self.perspective_additional_data = self.__LoadVar__(self.lastsizefilename, {'windowSize':(800,600), 'windowPosition': (0,0)})
        
        
        #width, height = self.__LoadVar__(self.lastsizefilename, (800,600))
        
        width, height = self.perspective_additional_data['windowSize']
        x = self.perspective_additional_data['windowPosition']
        
        self.parentframe.SetSize(wx.Size(width, height))
        
        
        #self.parentframe.FloatingPosition(x)
        
        #self.parentframe.Centre( wx.BOTH )   
        
        
        
    def SavePerspectiveToFile(self, filename):
        s = self.parentframe.m_mgr.SavePerspective()
        f = open(filename, "w")
        f.write(s)
        f.close()
    
    
    
        
        
    def SaveLastPerspective(self):
        self.SavePerspectiveToFile(self.lastperspectivefilename)
        self.saveWindowsSize()
        
        
    def DeleteLastPerspective(self):
        os.remove(self.lastperspectivefilename)   
        #wx.MessageBox("Last perspective has been purged.")  
        self.RaisePerspectiveLog("Last perspective has been purged.", "msg")
        
    
    
    
    
        
    def LoadPerspectiveFromFile(self, filename):    
        if os.path.isfile(filename) :
            f = open(filename, "r")
            lp = f.read()
            
            self.parentframe.m_mgr.LoadPerspective(lp, True)
            
            
            
            
            #fix icons
            
            all_panes = self.parentframe.m_mgr.GetAllPanes()
            for ii in range(len(all_panes)):
                
                if not all_panes[ii].IsToolbar():
                    #self.logger.info(all_panes[ii])
                    capt = all_panes[ii].caption
                    na = all_panes[ii].name
                    
                    #self.logger.info(capt)
                    #self.logger.info(na)
                    #self.logger.info(ic)
                    #icon = wx.Bitmap( u"res/default_style/normal/view_default_frame.png", wx.BITMAP_TYPE_ANY )
                    
                    icon = self.parentframe.Plugins.GetViewNameInstance(na)
                    #self.parentframe.Plugins.GetViewNameInstance(na)
                    
                    if icon == None:
                        icon = self.parentframe.RessourcesProvider.GetImage('view_default_frame')
                        #icon = wx.Bitmap( u"res/default_style/normal/view_default_frame.png", wx.BITMAP_TYPE_ANY )
                    else:
                        icon = icon['icon']
                        
                    self.parentframe.m_mgr.GetPane(na).Icon(icon)
            
                else:
                    all_panes[ii].Hide()
                    all_panes[ii].Float()
                    all_panes[ii].Dock()
                    all_panes[ii].Show()
            
            
            
            
            
            
            
            
            
        else:
            #self.logger.info("file not found!")    
            self.RaisePerspectiveLog("No last perspective found.", "info")  
            
        self.parentframe.m_mgr.Update()
        self.parentframe.Layout()
    
    
    
    def GetPerspectiveList(self):
        perspective_list = [ f.name for f in os.scandir(self.userperspectivepath ) if f.is_file() ] 
        
        list_clean = {}
        for p in perspective_list:
            name_ext = p.split('.')
            if name_ext[1] != 'perspective':
                continue
            
            list_clean[name_ext[0]] = self.userperspectivepath+p
            
            
        return   list_clean  
           
            
    def LoadLastPerspective(self):
        self.loadWindowsSize()
        self.LoadPerspectiveFromFile(self.lastperspectivefilename)
        
    
    def LoadUserPerspective(self, perspective_name):
        path = self.parentframe.GetPath('USERDATA')+'perspectives/'+perspective_name+'.perspective'
        
        _newPerspective= perspectiveContentDescriptor()
        if _newPerspective.LoadUserPerspective(path):
            _newPerspective.RestoreSnapshot(self.parentframe)
        
        
        
    
    def SaveCurrentPerspective(self):
        
        _name = RequestUserTextInput(self.parentframe, "Input a perspective name", 'Input a perspective name')
        
        if _name!= '':
            
            _currentPerspective= perspectiveContentDescriptor()
            _currentPerspective.SnapshotPerspective(self.parentframe)
            _res = _currentPerspective.SaveUserPerspective(self.parentframe.GetPath("USERDATA")+'perspectives/', _name)
            
            
            if _res:
                UserAdvancedMessage(self.parentframe, f"Perspective {_name} saved with success !", 'success', self.parentframe.GetPath("USERDATA")+'perspectives/'+_name+'.perspective')
            else:
                UserAdvancedMessage(self.parentframe, f"Unable to save Perspective {_name} !", 'error', self.parentframe.GetPath("USERDATA")+'perspectives/'+_name+'.perspective')
        
        
        
        #_currentPerspective.SnapshotPerspective(self.parentframe)
    
    
    
    
    
    def __saveVar__(self, varName, varData):
        try:
            self.logger.info(""+varName+" : "+str(varData))
            pickle.dump( varData, open(varName+".p", "wb" ) )
        except Exception as e:
            self.logger.error(e) 
    
    def __LoadVar__(self, varName, defaultTeturn=None):
        result = defaultTeturn
        try:
            result = pickle.load( open(varName+".p", "rb" ) )
        except Exception as e:
            self.logger.error(e) 
        
        return result    
        