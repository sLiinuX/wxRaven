'''
Created on 15 déc. 2021

@author: slinux
'''

from wxRavenGUI.view import wxRavenSplashScreen
from wxRavenGUI.view import wxRavenDisclaimerDialogLogic

import wx
import wxRavenGUI.application

class splashScreen(wxRavenSplashScreen):
    
    parentframe=None
    def __init__(self, parentframe):
        '''
        Constructor
        '''
        
        super().__init__(parentframe)
        self.parentframe = parentframe
    
        
        
        
    



class SplashScreenMgr():
    '''
    classdocs
    '''

    parentframe=None
    sc = None
    
    tickCount = 0
    showntickCount = 0
    parentObj = None
    
    started=False
    
    
    confirmation_tick_count = 2
    
    
    
    max_tick_count = 60
    
    
    progress_array_cursor = 0
    progress_array_text = ["Loading WxRaven.","Loading WxRaven..","Loading WxRaven..." ]
    
    done_text  = "WxRaven Loaded !" 
    
    def __init__(self, parentObj,parentframe=None):
        '''
        Constructor
        '''
        self.parentObj = parentObj
        self.parentframe = parentframe
        self.started=False
        self.sc = splashScreen(self.parentframe)
        self.sc.Bind( wx.EVT_TIMER, self.OnTimerTick, id=wx.ID_ANY )
        self.tickCount=0
        self.showntickCount=0
        self.sc.Show(show=1)
        
    
        
    def Show(self):
        self.sc.Show(show=1)
        
        
    def Close(self):
        self.sc.Close()
        
        
        
    def InitParentFrame(self):
        x  =  wxRavenGUI.application.wxRavenApp.wxRavenAppMainFrame()
        self.parentObj.appmainframe  =  x
        self.parentframe = x
        return self.parentObj.appmainframe
    
    
    
    def changeLoadText(self, txt=""):
        
        
        if txt == "":
            newTxt = self.progress_array_text[self.progress_array_cursor]
            self.sc.m_staticText1.SetLabel(newTxt)
            
            self.progress_array_cursor = self.progress_array_cursor + 1
            
            if self.progress_array_cursor > len(self.progress_array_text)-1:
                self.progress_array_cursor=0
            
        else:
            self.sc.m_staticText1.SetLabel(txt)
            
        wx.GetApp().Yield()
    
        
    def OnTimerTick(self, event):
        print("init...")
        self.tickCount = self.tickCount+1
        
        if self.showntickCount != self.confirmation_tick_count:
            self.changeLoadText()
        
        if self.parentframe == None:
            #print("tick parentframe none!")
            
            
            if not self.started:
                self.started=True
                
                
                p = self.InitParentFrame()
                _show = True
                
                
                if p.GetPluginSetting('General', 'show_disclaimer'):
                    disclaimer = wxRavenDisclaimerDialogLogic(p)
                    dis = disclaimer.ShowModal()
                    
                    print(f"Disclaimer User Result = {dis}")
                    
                    if dis != wx.OK:
                        p.ForceClose()
                        self.doStart=False
                        self.parentObj.doStart=False
                        _show = False
                        self.sc.m_timer1.Stop()
                        self.sc.Destroy()
                
                
                if _show:
                    p.Show()
            
            
            return 
        
        
        
        isShown = self.parentframe.IsShown()
        #print("tick parentframe exist !" + str(isShown))
        
        if isShown:
            #print("tick shown !")
            self.showntickCount = self.showntickCount+1
            
            
            
        if self.showntickCount == self.confirmation_tick_count-1:
            self.changeLoadText(self.done_text)
            
            
        if self.showntickCount == self.confirmation_tick_count:
            
            self.sc.m_timer1.Stop()
            self.sc.Destroy()
        
        if self.showntickCount > self.max_tick_count:
            self.sc.m_timer1.Stop()
            self.sc.Destroy()
            
        
        
        event.Skip()
        
        
        
        