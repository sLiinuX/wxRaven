'''
Created on 12 févr. 2022

@author: slinux
'''


from .wxRavenProfileManagerDesign import *


from wxRavenGUI.application.pluginsframework import PluginSettingsPanelObject

import wx
from wxRavenGUI.application.wxcustom import *


class wxRaven_ProfileManager_SettingPanel_Logic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRaven_ProfileManager_SettingPanel(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
        self.ressourcesPath = self.parentFrame.GetPath('PLUGIN') + 'ProfileManager/avatars/avatar_1.png'
        self.userImage = self.parentFrame.GetPath('USERDATA') + 'avatar.png'
        
        #self._Panel.booleansetting.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        #self._Panel.m_slider1.SetTickFreq(1)
        #self._Panel.m_slider1.SetRange(-100,100)
        
        self._Panel.m_PathText.SetLabel(self.parentFrame.GetPath('USERDATA'))
        
        self._Panel.m_bitmap2.SetBitmap(wx.Image(self.userImage, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
        
        self._Panel.m_saveButton.Enable(False)
        self._Panel.m_buttonReload.Enable(False)
        self._Panel.m_saveButton.Bind(wx.EVT_BUTTON, self.SaveAvatar )
        self._Panel.m_slider1.Bind( wx.EVT_SCROLL, self.OnSlideChangeHUE )
        
        self._Panel.m_sliderR.Bind( wx.EVT_SCROLL, self.OnSlideChangeSAT )
        self._Panel.m_sliderG.Bind( wx.EVT_SCROLL, self.OnSlideChangeSAT )
        self._Panel.m_sliderB.Bind( wx.EVT_SCROLL, self.OnSlideChangeSAT )
        
        self._Panel.m_buttonReload.Bind(wx.EVT_BUTTON, self.ResetAvatar )
        
        self.lastcustom = None
    
    
    
    
    def ResetAvatar(self, evt):
        self._Panel.m_bitmap2.SetBitmap(wx.Image(self.userImage, wx.BITMAP_TYPE_ANY).ConvertToBitmap())
        self._Panel.m_saveButton.Enable(False)
        self._Panel.m_buttonReload.Enable(False)
           
    
    def SaveAvatar(self, evt):
        '''
        val = self._Panel.m_slider1.GetValue()
        
        realValHue = val / 100
        print(realValHue)
        custom = self.GetImageBase()
        custom.RotateHue(realValHue)
        
        '''
        self.lastcustom.SaveFile(self.userImage, wx.BITMAP_TYPE_PNG)
        
        UserAdvancedMessage(self.parentFrame, f"Avatar saved in {self.userImage}", 'success')
    
    
    def GetImageBase(self):
        #print(self.ressourcesPath )
        return wx.Image(self.ressourcesPath, wx.BITMAP_TYPE_ANY)
    
    
    
    def OnSlideChangeHUE(self, evt):
        self.ComputeNewImage()
        
      
    def OnSlideChangeSAT(self, evt):
        #print(self._Panel.m_slider2.GetValue())
        self.ComputeNewImage()
    
    
    def ComputeNewImage(self):    
        valR = self._Panel.m_sliderR.GetValue()
        valG = self._Panel.m_sliderG.GetValue()
        valB = self._Panel.m_sliderB.GetValue()
        
        realValHueR = valR / 200
        realValHueG = valG / 200
        realValHueB = valB / 200
        custom = self.GetImageBase()
        
        val = self._Panel.m_slider1.GetValue()
        
        realValHue = val / 100
        #print(realValHue)
        #custom = self.GetImageBase()
        custom.RotateHue(realValHue)
        
        
        custom = custom.AdjustChannels(realValHueR, realValHueG, realValHueB, factor_alpha=1.0)
        self.lastcustom = custom
        
        self._Panel.m_bitmap2.SetBitmap(custom.ConvertToBitmap())
        self._Panel.m_saveButton.Enable(True)
        self._Panel.m_buttonReload.Enable(True)
        self.Layout()
        
  
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        #_newValueForBoolSetting = self._Panel.booleansetting.IsChecked()
        
        #now its up to the dev to chose how to take this information
        #in our demo lets do simple and just change the  booleansetting in PLUGIN_SETTINGS
        
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin.PLUGIN_SETTINGS['booleansetting'] = _newValueForBoolSetting
    
        print("SavePanelSettings" )
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #_currentValue = myPlugin.PLUGIN_SETTINGS['booleansetting']
        
        #self._Panel.booleansetting.SetValue(_currentValue)
        
        print("LoadPanelSettings")
        
        
    #
    #
    # method called when closing in case of thread or anything
    #     
    def safeClose(self):
        pass    
        
        