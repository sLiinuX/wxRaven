'''
Created on 4 janv. 2022

@author: slinux
'''

import wx
from wx import InfoBar

class wxNotificationBar(InfoBar):
    '''
    classdocs
    '''


    _timer = None 
    
    _timerDuration = 2000
    
    
    def __init__(self, parent, defaultNotificationTime=5000, additionalBt=False, additionalBtText="", additionalBtCallback=None):
        '''
        Constructor
        '''
        
        
        wx.InfoBar.__init__(self, parent )
        self.SetShowHideEffects( wx.SHOW_EFFECT_EXPAND, wx.SHOW_EFFECT_ROLL_TO_TOP )
        self.SetEffectDuration( 500 )
        #parentSizer.Add( self._notification_bar, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        parent.Bind( wx.EVT_TIMER, self.OnTimerTick, id=wx.ID_ANY )
        
        self._timer = wx.Timer()
        self._timer.SetOwner( parent, wx.ID_ANY )
        
        self._timerDuration = defaultNotificationTime
        
        
        self._btText =additionalBtText
        self._btCallback = additionalBtCallback
        
        if additionalBt:
            self.addNotificationButton()
    
    
    def addNotificationButton(self):
        btnId = wx.NewId()
        self.info.AddButton(btnId, self._btText)
        self.info.Bind(wx.EVT_BUTTON, self._btCallback , id=btnId)
    
    
    
        
        
    def ShowNotification(self, message, msgType=wx.ICON_INFORMATION, noDelay=False):
        #print(f'ShowNotification  {noDelay}')
        if noDelay == False:
            #print('timer started')
            self._timer.Start(milliseconds=self._timerDuration, oneShot=True)
        
        self.ShowMessage(message, flags=msgType)
        
        
        
    
    
    
    
    def OnTimerTick(self, evt):
        #print('timer tick')
        self.Dismiss()
        self._timer.Stop()    
        