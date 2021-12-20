'''
Created on 20 déc. 2021

@author: slinux
'''



from .wxRavenGeneralDesign import GeneralSettingPanel

from wxRavenGUI.application.pluginsframework import PluginSettingsPanelObject


class wxRavenGeneralSettingPanel(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _panel = GeneralSettingPanel(parent)
        PluginSettingsPanelObject.__init__(self,_panel, parentFrame, pluginName)
    
    
    
    
    
    
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