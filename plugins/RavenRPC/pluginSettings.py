'''
Created on 27 déc. 2021

@author: slinux
'''
from wxRavenGUI.application.pluginsframework import PluginSettingsPanelObject
from .wxRavenShellDesign import wxRavenShell_SettingsPanel
import wx
class wxRavenRPCPluginSettings(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenShell_SettingsPanel(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
        _Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
    
        
        #self._Panel.booleansetting.Bind( wx.EVT_CHECKBOX, self.OnChanged )
    
    
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        pass
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        pass
        
        
        