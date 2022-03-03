'''
Created on 4 janv. 2022

@author: slinux
'''
#wxRavenDebugConsolePanel
import threading
import time 

import wx 
import sys

from .wxRavenGeneralDesign import wxRavenDebugConsolePanel

class wxRavenDebugConsole(wxRavenDebugConsolePanel):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Debug"
    view_name = "Debug"
    parent_frame = None
    default_position = "mgr"
    icon = 'debug_exc'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, position = "mgr", viewName= "Debug", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Debug"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        
        wx.LogTextCtrl(self.m_debugLog)
        
        #self._oldOut = sys.stdout
        #self._oldErr = sys.stderr
        
        
        #if parentFrame.GetPluginSetting("General",'debug_out') == 'stderr':
        #    sys.stderr=self.m_debugLog
        #else:
        #sys.stdout=self.m_debugLog
        
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
    
            
    
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.waitApplicationReady()
    
    
    
    def OnClose(self, evt):
        print("OnDebugClose!")
        #sys.stdout=self._oldOut
        #sys.stderr=self._oldErr
    
    
    
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.UpdateView,), daemon=True)
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
    
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        print("update view !!!")
        self.UpdateDataFromPluginDatas()
        self.Layout()
            
            
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        
        try:
       
            #myPluginData = self.parent_frame.GetPluginData("Tutorial","myPluginData2")
            #myPluginSetting =  self.parent_frame.GetPluginSetting("Tutorial","booleansetting")#SavePanelSettings GetPluginSetting
            #
            #Update your panel
            #       
            
            
            #textToPrint = " booleansetting = " + str(myPluginSetting)
            #textToPrint = textToPrint + "\n\n myPluginData2 = " + str(myPluginData)
            pass 
            #self.m_staticText2.SetLabel(str(textToPrint)) 
             
                
        except Exception as e:
            self.parent_frame.Log("Unable to load debug datas" , type="warning")
                    
            
            
            
            
            