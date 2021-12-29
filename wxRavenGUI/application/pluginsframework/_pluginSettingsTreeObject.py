'''
Created on 19 déc. 2021

@author: slinux
'''

from ._pluginSettingPanel import wxRavenNotAvailableSettingPanel
#
#
# PluginTreeObject for the settings
#
class PluginSettingsTreeObject(object):
    '''
    classdocs
    '''


    _name = ""
    _classPanel = None
    _icon = None
    
    _childs = []
    

    def __init__(self, name, icon=None, classPanel=None, _childs=None):
        '''
        Constructor
        '''
        
        
        self._name = name
        
        if classPanel == None:
            classPanel = wxRavenNotAvailableSettingPanel
        
        self._classPanel = classPanel
        self._icon = icon
        self._childs = _childs
        if _childs == None:
            self._childs = []
        
        
        
    