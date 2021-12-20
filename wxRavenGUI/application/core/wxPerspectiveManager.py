'''
Created on 12 déc. 2021

@author: slinux
'''
import os
import wx
import pickle
import inspect 


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
        
        self.lastperspectivefilename = self.configpath+"perspective.last"
        self.lastsizefilename = self.configpath+"window.last"
        
        self.perspective_additional_data = {}
        
        if loadLastView:
            self.LoadLastPerspective()
    
    
    
    def RaisePerspectiveLog(self, message, type="error"):
        try:
            _source = str(inspect.stack()[1][0])
            self.parentframe.Log( message, source=str(_source), type=type)
        except Exception as e:
            print("RaisePerspectiveLog() " + str(e))  
    
    
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
                    #print(all_panes[ii])
                    capt = all_panes[ii].caption
                    na = all_panes[ii].name
                    
                    #print(capt)
                    #print(na)
                    #print(ic)
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
                    all_panes[ii].Show()
            
            
            
            
            
            
        else:
            #print("file not found!")    
            self.RaisePerspectiveLog("No last perspective found.", "info")  
            
        self.parentframe.m_mgr.Update()
        
        
            
    def LoadLastPerspective(self):
        self.loadWindowsSize()
        self.LoadPerspectiveFromFile(self.lastperspectivefilename)
        
        
    
    
    
    
    
    
    
    
    def __saveVar__(self, varName, varData):
        try:
            print(""+varName+" : "+str(varData))
            pickle.dump( varData, open(varName+".p", "wb" ) )
        except Exception as e:
            print(e) 
    
    def __LoadVar__(self, varName, defaultTeturn=None):
        result = defaultTeturn
        try:
            result = pickle.load( open(varName+".p", "rb" ) )
        except Exception as e:
            print(e) 
        
        return result    
        