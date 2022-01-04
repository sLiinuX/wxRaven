'''
Created on 18 déc. 2021

@author: slinux
'''


from .wxRavenTutorialPluginDesign import *

import threading
import time 



class MyTutorialView_WithLogic(MyTutorialView):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Tutorial View"
    view_name = "Tutorial View"
    parent_frame = None
    default_position = "main"
    icon = 'help_view'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, position = "main", viewName= "Tutorial View", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Tutorial View"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        
        
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
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.UpdateView,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
    
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self):
        
        self.UpdateDataFromPluginDatas()
        self.Layout()
            
            
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        
        try:
       
            myPluginData = self.parent_frame.GetPluginData("Tutorial","myPluginData2")
            myPluginSetting =  self.parent_frame.GetPluginSetting("Tutorial","booleansetting")#SavePanelSettings GetPluginSetting
            #
            #Update your panel
            #       
            
            
            textToPrint = " booleansetting = " + str(myPluginSetting)
            textToPrint = textToPrint + "\n\n myPluginData2 = " + str(myPluginData)
             
            self.m_staticText2.SetLabel(str(textToPrint)) 
             
                
        except Exception as e:
            self.parent_frame.Log("Unable to load tutorial datas" , type="warning")
                    
            
            
            
            
            
            
            
            
            
            