'''
Created on 17 févr. 2022

@author: slinux
'''

from .wxRavenShellDesign import wxRaven_General_CodeBrowser
import threading
import time 

from wxRavenGUI.application.wxcustom import *
import wx.lib.mixins.listctrl as listmix 

from datetime import date
import datetime



class wxRaven_General_CodeBrowserLogic(wxRaven_General_CodeBrowser):
    '''
    classdocs
    '''
    view_base_name = "Source Code Browser"
    view_name = "Source Code Browser"
    parent_frame = None
    default_position = "main"
    icon = 'folder_python_browser'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, position = "main", viewName= "Source Code Browser", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Source Code Browser"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self._allTabs= {}
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
        
        #self.LoadSearchOptions()
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        self.defaultRoot = parentFrame.GetPath('ROOT')
        self.m_pythonSourceCodeExplorer.SetPath(self.defaultRoot)
        self.m_pythonSourceCodeExplorer.SetDefaultPath(self.defaultRoot)
        
        
        self.m_pythonSourceCodeExplorer.Bind(wx.EVT_DIRCTRL_FILEACTIVATED, self.OnFileClicked)
        
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.waitApplicationReady()
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.setupPanels,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
    
     
    
    def OnFileClicked(self, evt):
        _file = self.m_pythonSourceCodeExplorer.GetFilePath()
        print(f"file clicked {_file}")
        
        if _file != None:
            plugin = self.parent_frame.GetPlugin('RavenRPC')
            plugin.OpenCodeEditor(_file)
        
    
    
    def UpdateView(self, evt=None):
        pass
    
    def setupPanels(self, evt=None):
        pass
        