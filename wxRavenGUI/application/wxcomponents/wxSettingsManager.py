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

        #resumeViewOnStartup = str(self.parentframe.wxRavenMenuBar_Window_Perspectives.IsChecked(self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.GetId()))
        #print("Save resumeViewOnStartup = " +resumeViewOnStartup)
        self._SaveGeneralSettings(Config)
        self._SaveConnexionSettings(Config)
        

        #Config.set('General','connexionChangedCallbackInSafeMode',str(self.connexionChangedCallbackInSafeMode))

        Config.write(cfgfile)
        cfgfile.close()
    
    
    def _SaveGeneralSettings(self, configObj):
        
        resumeViewOnStartup = str(self.parentframe.wxRavenMenuBar_Window_Perspectives.IsChecked(self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.GetId()))
        #print("Save resumeViewOnStartup = " +resumeViewOnStartup)
        
        configObj.add_section('General')
        configObj.set('General','resumeViewOnStartup',resumeViewOnStartup)
        configObj.set('General','forceInPrincipalAuiManager',str(self.forceInPrincipalAuiManager))
        configObj.set('General','resumePluginState',str(self.resumePluginState))
        configObj.set('General','safeMode',str(self.safeMode))
        
        
    def _SaveConnexionSettings(self, configObj):
         
        
        configObj.add_section('Connexions')
        for key in self.allconnexions:
            
            data = self.allconnexions[key]
            configObj.set('Connexions',key,data)
    
    
    
    
    def LoadSettingsFromFile(self):    
        
        Config = ConfigParser()
        Config.read(self.CONFIG_PATH+self.application_config_file)
        
        
        self._LoadGeneralConfig(Config)
        self._LoadConnexionSettings(Config)
    
    
    
    
    def _LoadGeneralConfig(self, configObj):
        
        self.resumeViewOnStartup = configObj.getboolean("General", "resumeViewOnStartup")
        self.parentframe.wxRavenMenuBar_Window_Perspectives.Check(self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.GetId(), self.resumeViewOnStartup )
        
        self.forceInPrincipalAuiManager = configObj.getboolean("General", "forceInPrincipalAuiManager") 
        self.resumePluginState= configObj.getboolean("General", "resumePluginState") 
        self.resumePluginState= configObj.getboolean("General", "safeMode") 
    
    
    def _LoadConnexionSettings(self, configObj):
        _raw = configObj['Connexions'] 
        self.allconnexions = _raw
        #for key in _raw:
            #print(key)
        #print("_LoadConnexionSettings")
    
    
    
    
    
        
        
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
        