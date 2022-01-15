'''
Created on 10 déc. 2021

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import *
import threading
from datetime import datetime
import inspect


from .wxRavenDebugConsoleLogic import *
from .wxRavenErrorLogConsoleLogic import *
from .wxNotebookToolbox import *
from .pluginSettings import *

from .wxRavenWelcomePanel import wxRavenWelcomeTabLogic

class wxRavenPlugin(PluginObject):
    
    
    
    
    def __init__(self, parentFrame, position="mgr"):
        PluginObject.__init__(self, parentFrame, position=position)
        
        
        self.PLUGIN_NAME = "General"
        #self.PLUGIN_ICON = wx.Bitmap( u"res/default_style/normal/dialog_default.png", wx.BITMAP_TYPE_ANY )
        self.PLUGIN_ICON = self.RessourcesProvider.GetImage('dialog_default')
        
        self.PLUGINS_VIEWS= [ 
                    {
                     'viewid':'Error Log Console', 
                     'name':'Error Log Console', 
                     'title':'Error Log Console', 
                     'position':'mgr', 
                     'icon':  self.RessourcesProvider.GetImage('error_console'), 
                     'class': RavenErrorLogConsole ,
                     'default':True,
                     'multipleViewAllowed':False
                     },
                    
                    {
                     'viewid':'Debug', 
                     'name':'Debug', 
                     'title':'Debug', 
                     'position':'mgr', 
                     'icon':  self.RessourcesProvider.GetImage('debug_exc'), 
                     'class': wxRavenDebugConsole ,
                     'default':False,
                     'multipleViewAllowed':False
                     },
                    
                    
                    {
                     'viewid':'Notebook Toolbox', 
                     'name':'Notebook Toolbox', 
                     'title':'Notebook Toolbox', 
                     'position':'mgr', 
                     'icon':   self.RessourcesProvider.GetImage('tab_view') , 
                     'class': RavenNotebookToolbox ,
                     'default':False,
                     'multipleViewAllowed':True,
                     'isArea':True
                     
                     },
                    
                    
                    
                     {
                     'viewid':'Welcome', 
                     'name':'Welcome', 
                     'title':'Welcome', 
                     'position':'main', 
                     'icon':   self.RessourcesProvider.GetImage('welcome16') , 
                     'class': wxRavenWelcomeTabLogic ,
                     'default':False,
                     'multipleViewAllowed':False,
                     'isArea':False,
                     
                     },
                    
                    
                ]
        
        
        
        self.PLUGIN_SETTINGS = {
                'showerror' : ['error','message', 'warning', 'infos'],
                'defaultviewarea':'main',
                'last_network':'mainnet_localhost',
                'disable_plugins' :[],
                'quick_links' :[]
            }
        
        
        
        
        """
        
        
        Settings pannel tree, using the objhect PluginSettingsTreeObject
        
        
        """
        self.PLUGIN_SETTINGS_GUI = []
        
        """
        _prefIcon = wx.Bitmap( u"res/default_style/normal/wizard-prefs.png", wx.BITMAP_TYPE_ANY )
        _viewIcon = wx.Bitmap( u"res/default_style/normal/perspective_default.png", wx.BITMAP_TYPE_ANY )
        _conIcon = wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY )
        _appIcon = wx.Bitmap( u"res/default_style/normal/frame_default.png", wx.BITMAP_TYPE_ANY )
        """
        
        _prefIcon = self.RessourcesProvider.GetImage('wizard-prefs')
        _viewIcon = self.RessourcesProvider.GetImage('perspective_default')
        _conIcon = self.RessourcesProvider.GetImage('network')
        _appIcon = self.RessourcesProvider.GetImage('frame_default')
        _pluginsIcon = self.RessourcesProvider.GetImage('install-handler')
        
        
        

        self.PLUGIN_SETTINGS_GUI.clear()
        
        
        _applicationPannel = PluginSettingsTreeObject("Application", _appIcon, classPanel=wxRavenApplicationSettingPanel, _childs=None)
        

        _generalPannel = PluginSettingsTreeObject("General", _prefIcon, classPanel=wxRavenGeneralSettingPanel, _childs=None)
        _viewPannel = PluginSettingsTreeObject("Views", _viewIcon, classPanel=None, _childs=None)
        _connexionPannel = PluginSettingsTreeObject("Connexions", _conIcon, classPanel=wxRavenConexionsSettingPanel, _childs=None)
        
        _pluginsPannel = PluginSettingsTreeObject("Plugins", _pluginsIcon, classPanel=wxRavenPluginsSettingPanel, _childs=None)
        
        
        
        
        _applicationPannel._childs.append(_generalPannel)
        _applicationPannel._childs.append(_viewPannel)
        _applicationPannel._childs.append(_connexionPannel)
        _applicationPannel._childs.append(_pluginsPannel)
        
        
        self.PLUGIN_SETTINGS_GUI.append(_applicationPannel)
        
        #self.PLUGIN_SETTINGS_GUI.append(_generalPannel)
        #self.PLUGIN_SETTINGS_GUI.append(_viewPannel)
        #self.PLUGIN_SETTINGS_GUI.append(_connexionPannel)
        
        
        
        
        """
        _prefIcon = self.RessourcesProvider.GetImage('wizard-prefs')
        _generalPannel = PluginSettingsTreeObject("General", _prefIcon, classPanel=None, _childs=None)
        self.PLUGIN_SETTINGS_GUI.append(_generalPannel)
       
        """
        
        
        

        self.ALLOW_MULTIPLE_VIEWS_INSTANCE = True
        
        
        self.parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        
        self.setData("allLogs", {})
        self.setData("_cursor",0)
        
        
        #self.LoadPluginFrames()
    
    
    
    
    
    
    def _LoadPluginSettings(self):
        _recordedSettings = self.parentFrame.Settings._GetPluginSettings(self.PLUGIN_NAME)
        
        
        for key in _recordedSettings:
            
            
            #
            # _recordedSettings[key] Return string only, do your own mapping for complex datastructure
            #
            self.PLUGIN_SETTINGS[key] = _recordedSettings[key]

            _str  = _recordedSettings[key]
            try:
                convertedData = json.loads(_str.replace('\'','"'))
                self.PLUGIN_SETTINGS[key] = convertedData
                
            except Exception as e:
                #print("NOT json data :" + str(e))
                pass
            
            if _str == "True":
                self.PLUGIN_SETTINGS[key] = True
            elif _str == "False":
                self.PLUGIN_SETTINGS[key] = False
                
                
            #print(key) 
            #print(self.PLUGIN_SETTINGS[key])
    
    
        
    '''
    
    Plugin Triggers for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
    '''
  
        
    def OnNetworkChanged_T(self, networkName=""):    
        t=threading.Thread(target=self.OnNetworkChanged)
        t.start()
        
        
    def OnNetworkChanged(self):
        
        self.Log("Network Changed !")
        
        """
        self.setData("globalBalance", 0.0)
        self.setData("allAccountsDatas", [])
        self.setData("globalAssetBalance", [])
        self.setData("allAddresses", [])
        """
            
        
    def Log(self, message , source="", timestamp=None, type="info"):
        
        
        existingLogs = self.getData("allLogs")
        _cursor = self.getData("_cursor")
        
        if timestamp == None:
            now = datetime.now()
            timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
         
        #print(str(inspect.stack()[0][0].f_code.co_name))
        #print(str(inspect.stack()[1][0].f_code.co_name))
        #print(str(inspect.stack()[2][0].f_code.co_name))
        
        #print(str(inspect.stack()[0][0]))
        #print(str(inspect.stack()[1][0]))
        #print(str(inspect.stack()[2][0]))
        if source == "":
            source = str(inspect.stack()[1][0])
         
        newLogLine = [type,str(message), source, timestamp]
        existingLogs[_cursor] = newLogLine
        self.setData("allLogs", existingLogs)
        
        _cursor = _cursor+1
        self.setData("_cursor", _cursor)
        wx.CallAfter(self.UpdateActiveViews, ())
        