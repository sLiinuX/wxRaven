'''
Created on 20 déc. 2021

@author: slinux
'''



from .wxRavenTutorialPluginDesign import MyTutorialSettingPanel

from wxRavenGUI.application.pluginsframework import PluginSettingsPanelObject

import wx
class MyTutorialSettingPanel_WithLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = MyTutorialSettingPanel(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
    
        
        self._Panel.booleansetting.Bind( wx.EVT_CHECKBOX, self.OnChanged )
    
    
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        _newValueForBoolSetting = self._Panel.booleansetting.IsChecked()
        
        #now its up to the dev to chose how to take this information
        #in our demo lets do simple and just change the  booleansetting in PLUGIN_SETTINGS
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        myPlugin.PLUGIN_SETTINGS['booleansetting'] = _newValueForBoolSetting
    
        print("SavePanelSettings" + str(_newValueForBoolSetting))
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        _currentValue = myPlugin.PLUGIN_SETTINGS['booleansetting']
        
        self._Panel.booleansetting.SetValue(_currentValue)
        
        print("LoadPanelSettings" + str(_currentValue))
        
        
        
        
        
        
        
        
        