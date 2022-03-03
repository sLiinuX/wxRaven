'''
Created on 15 déc. 2021

@author: slinux
'''

from wxRavenGUI.view import wxRavenSplashScreen
from wxRavenGUI.view import wxRavenDisclaimerDialogLogic

from plugins.ProfileManager.wxRaven_ProfileManager_ProfileSelector import wxRavenProfileManager_ProfileSelectorDialogLogic


import wx
import wxRavenGUI.application
import logging
import os



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
    
    def __init__(self, parentObj,parentframe=None, profile=None):
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
        self.doStart = True
        
        self._profile = profile
        
        
        
        
    
        
    def Show(self):
        
        
        self.sc.Show(show=1)
        
        
    def Close(self):
        self.sc.Close()
        
        
        
    def InitParentFrame(self, profilePath =''):
        x  =  wxRavenGUI.application.wxRavenApp.wxRavenAppMainFrame(_ProfilePath = profilePath, mainApp=self.parentObj)
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
                
                
                if self._profile == None:
                    self._profile = self.__ProfileSelector__()
                    if self._profile != None:
                        if self._profile != '':
                            self.doStart = True
                    
                    print(f"Profile Selector Returned = {self._profile}")
                
                
                
                
                print(f"Starting Logs in = {self._profile}")
                print(f"Do Start Result = {self.doStart}")
                #
                # Change Log direction
                #
                self.parentObj.stop_logging()
                self.parentObj.setup_logging(forcePath=self._profile)
                
                
                
                
                
                
                if self.doStart:
                    print(f"Profile = {self._profile}")
                    self.__InitializeApplication__(self._profile)
                    
                    
                    _log_mode = self.parentframe.GetPluginSetting("General", 'log_mode')
                    _debug_mode = self.parentframe.GetPluginSetting("General", 'debug_mode')
                    logging.info(f"Application Started, changing log configuration log_mode={_log_mode} , debug_mode= {_debug_mode}")
                    
                    self.parentObj.stop_logging()
                    if _log_mode:
                        self.parentObj.setup_logging(forcePath=self._profile, _debugMode=_debug_mode)
                    
                    
                    
                    
                    
                    
                    
                else:
                    self.doStart=False
                    self.parentObj.doStart=False
                    _show = False
                    self.sc.m_timer1.Stop()
                    self.sc.Destroy()
                    return
                '''
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
            
                '''
                
                
                
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
        
        
     
     
    
    
    
    def __ProfileSelector__(self):
        _profileDialog = wxRavenProfileManager_ProfileSelectorDialogLogic(None)
        _profileResp = _profileDialog.ShowModal()
        
        _profile = _profileDialog._panel.selection
        
        _profileDialog.Destroy()
        
        
        if _profileResp != 5100:
            self.doStart=False
            
        return _profile
    
    def __InitializeApplication__(self, profilePath=''):
        
        _application=None
        _show = True
        #try:
        if True:
            print(f'InitParentFrame : {profilePath}') 
            _application = self.InitParentFrame(profilePath)
            _show = True
        #except Exception as e:
        #    print(f'ERROR InitParentFrame : {e}')        
        
        
        
        
        
        
        
        
                
        if _application.GetPluginSetting('General', 'show_disclaimer'):
            disclaimer = wxRavenDisclaimerDialogLogic(_application)
            dis = disclaimer.ShowModal()
            disclaimer.Destroy()     
            print(f"Disclaimer User Result = {dis}")
                    
            if dis != wx.OK:
                print(f"Disclaimer REFUSED ")
                _application.ForceClose()
                self.doStart=False
                self.parentObj.doStart=False
                _show = False
                self.sc.m_timer1.Stop()
                self.sc.Destroy()
       
       
            else:
                print(f"Disclaimer ACCEPTED ")
                
            
            
        else:
            pass
        
        
        
        _application.SetReady()
            
        if _show:
            _application.Show()