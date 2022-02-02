'''
Created on 12 déc. 2021

@author: slinux
'''
import os
import wx
import pickle
import inspect 
import logging

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
        
            
    def LoadLastPerspective(self):
        self.loadWindowsSize()
        self.LoadPerspectiveFromFile(self.lastperspectivefilename)
        
        
    
    
    
    
    
    
    
    
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
        