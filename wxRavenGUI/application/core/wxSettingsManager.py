'''
Created on 14 déc. 2021

@author: slinux
'''
import os
from configparser import *
import inspect





class SettingsManager(object):
    '''
    classdocs
    '''
    
    CONFIG_PATH = os.getcwd() + "/config/"
    PLUGIN_PATH = os.getcwd() + "/plugins/"
    
    
    application_config_file = "config.ini"
    
    ConfigFileInstance = None
    
    
    
    resumeViewOnStartup = False
    forceInPrincipalAuiManager = False
    resumePluginState = True
    safeMode = True
    
    
    allconnexions = {}
    
    
    parentframe = None
    
    
    
    
    
    

    def __init__(self, parentframe, configpath="", pluginpath="", cfgfile = "config.ini"):
        '''
        Constructor
        '''
        self.parentframe = parentframe
        
        
        if configpath!="":
            self.CONFIG_PATH = configpath
        else:
            self.CONFIG_PATH = os.getcwd() + "/config/"
        
        if pluginpath!="":
            self.PLUGIN_PATH = configpath
        else:
            self.PLUGIN_PATH = os.getcwd() + "/plugins/"
        
        self.application_config_file = cfgfile
        
        
        self.allconnexions = {}
        self.ConfigFileInstance = ConfigParser()
        
        try:
            self.LoadSettingsFromFile()
        except Exception as e:
            print(e)
            self.RaiseSettingsLog("Unable to load settings from file : " + str(e), "warning") 
        
    
    
    
    
    def RaiseSettingsLog(self, message, type="error"):
        try:
            _source = str(inspect.stack()[1][0])
            self.parentframe.Log( message, source=str(_source), type=type)
        except Exception as e:
            print("RaiseSettingsLog() " + str(e))  
            
            
            
            
            
            
    
    def SaveSettingsToFile(self):
        cfgfile = open(self.CONFIG_PATH+self.application_config_file ,'w')
        
        Config = ConfigParser()
        
        #Config.exist

        #resumeViewOnStartup = str(self.parentframe.wxRavenMenuBar_Window_Perspectives.IsChecked(self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.GetId()))
        #print("Save resumeViewOnStartup = " +resumeViewOnStartup)
        self._SaveGeneralSettings(Config)
        self._SaveConnexionSettings(Config)
        
        self._SaveAllPluginsSettings(Config)
        

        #Config.set('General','connexionChangedCallbackInSafeMode',str(self.connexionChangedCallbackInSafeMode))

        Config.write(cfgfile)
        cfgfile.close()
    
    
    def _SaveGeneralSettings(self, configObj):
        
        resumeViewOnStartup = str(self.parentframe.wxRavenMenuBar_Window_Perspectives.IsChecked(self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.GetId()))
        #print("Save resumeViewOnStartup = " +resumeViewOnStartup)
        
        configObj.add_section('Application')
        configObj.set('Application','resumeViewOnStartup',resumeViewOnStartup)
        configObj.set('Application','forceInPrincipalAuiManager',str(self.forceInPrincipalAuiManager))
        configObj.set('Application','resumePluginState',str(self.resumePluginState))
        configObj.set('Application','safeMode',str(self.safeMode))
        
        
        return configObj
        
        
    def _SaveConnexionSettings(self, configObj):
         
        
        configObj.add_section('Connexions')
        for key in self.allconnexions:
            
            data = self.allconnexions[key]
            configObj.set('Connexions',key,data)
    
    
    
    def _SavePluginSettings(self, pname, _pInstance, conf):
        
        
        for key in _pInstance.PLUGIN_SETTINGS:
            conf.set(pname,key,str(_pInstance.PLUGIN_SETTINGS[key]))
        
        
        return  conf   
    
    
    def _SaveAllPluginsSettings(self, configObj):
        
        
        for _p in self.parentframe.Plugins.plugins:
            
            _plugin_instance = self.parentframe.Plugins.GetPlugin(_p)
            if _plugin_instance != None:
                
                try:
                    configObj.add_section(_p)
                except:
                    pass
                
                
                self._SavePluginSettings(_p , _plugin_instance, configObj)
                
                
        return  configObj     
            
    
    
    
    
    
    def LoadSettingsFromFile(self):    
        
        Config = ConfigParser()
        Config.read(self.CONFIG_PATH+self.application_config_file)
        
        
        self._LoadGeneralConfig(Config)
        self._LoadConnexionSettings(Config)
    
        self.ConfigFileInstance = Config
    
    
    def _LoadGeneralConfig(self, configObj):
        #
        # View options
        #
        self.resumeViewOnStartup = configObj.getboolean("Application", "resumeViewOnStartup", fallback = False)
        self.parentframe.wxRavenMenuBar_Window_Perspectives.Check(self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.GetId(), self.resumeViewOnStartup )
        
        self.resumePluginState= configObj.getboolean("Application", "resumePluginState", fallback = True) 
        
        #
        # Hidden configuration for dev purpose
        #
        self.forceInPrincipalAuiManager = configObj.getboolean("Application", "forceInPrincipalAuiManager", fallback = False) 
        self.resumePluginState= configObj.getboolean("Application", "safeMode", fallback = True) 
    
    
    def _LoadConnexionSettings(self, configObj):
        #_raw = configObj.get('Connexions', fallback={}) 
        _raw = configObj['Connexions'] 
        self.allconnexions = _raw
    
    
    
    def _GetPluginSettings(self, pluginName):
        _pluginsSettings = {}
        
        
        if self.ConfigFileInstance.__contains__(pluginName):
            for key in self.ConfigFileInstance[pluginName]:
                _pluginsSettings[key] = self.ConfigFileInstance.get(pluginName, key)
    
        return _pluginsSettings
    
    
        
        
    def ConfigSectionMap(self, config, section):
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
                if dict1[option] == -1:
                    #DebugPrint("skip: %s" % option)
                    pass
            except:
                print("exception on %s!" % option)
                
                dict1[option] = None
        return dict1    
        