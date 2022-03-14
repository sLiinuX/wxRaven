'''
Created on 20 déc. 2021

@author: slinux
'''




from wxRavenGUI.view import wxRavenNotAvailablePanel

import wx



#
#
# Plugin Setting panel object to create as basic setting panel for your plugin
#

class PluginSettingsPanelObject(object):
    '''
    classdocs
    '''
    
    parentFrame = None
    pluginName = None
    
    _Panel = None
    _settingsHasChanged = False
    _needReboot = False

    def __init__(self, _panel,parentFrame, pluginName):
        '''
        Constructor
        '''
        self.parentFrame = parentFrame
        self.pluginName = pluginName
        
        self._Panel = _panel
        
        self._settingsHasChanged = False
        self._needReboot = False
        
        
        try:
            parentFrame.RessourcesProvider.ApplyThemeOnSettingsPanel(self)
        
        except Exception as e:
            pass
        
    def Layout(self):
        self._Panel.Layout()
        self.parentFrame.Layout()

    def Show(self):
        self._Panel.Show()
        
    def Hide(self):
        self._Panel.Hide()
    
    
    
    def OnChanged(self, evt):
        self._settingsHasChanged = True
    
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
    
    
    #
    #
    # method to be called at panel deletion so it can remove safely pending stuff
    # 
    def safeClose(self):
        pass
    
    
class wxRavenNotAvailableSettingPanel(PluginSettingsPanelObject):
    
    
    def __init__(self,parent, parentFrame, pluginName):
        
        _panel = wxRavenNotAvailablePanel(parent)
        PluginSettingsPanelObject.__init__(self,_panel, parentFrame, pluginName)









