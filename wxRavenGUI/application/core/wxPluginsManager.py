'''
Created on 10 déc. 2021

@author: slinux
'''
import importlib
import os
from wxRavenGUI.application.pluginsframework import *
import inspect
import logging


from plugins.configurations import __wxraven_configurations_list__,__wxraven_configurations_default__

class pluginsManager(object):
    '''
    classdocs
    '''
    plugins = {}

    
    
    new_view_callbacks = []
    
    
    
    pluginDirectory = ""
    appmainframe = None
    
    resumestate = True
    
   
    
    safemode = True
    
    
    _exclude_list =[]
    _include_only_list =[]
    _detected_plugin_list=[]
    
    

    def __init__(self, pluginRootDir, contextAppMainFrame,resumestate=True , loadPath=True, _exclude=[], _includeOnly=[]):
        '''
        Constructor
        '''
        self.pluginDirectory = pluginRootDir
        self.appmainframe = contextAppMainFrame
        
        self.plugins = {}
        self.new_view_callbacks = []
        
        self.resumestate = resumestate
        
        self.safemode = contextAppMainFrame.Settings.safemode
        
        self.logger = logging.getLogger('wxRaven')
        self._exclude_list = _exclude
        self._include_only_list = _includeOnly
        
        #self.LoadPlugin("plugins.General.plugin.*")
        
        #self.LoadGeneralPlugins()
        
        self.LoadPlugin("plugins.General.plugin.*")
        
        
        
        
        if loadPath:
            #self.LoadPlugin("plugins.General.plugin.*")
            self.LoadFromPluginDirectory()
    
    
    
    def Initialize(self, loadDefaultViews=True):
        self.LoadFromPluginDirectory()
        
        if loadDefaultViews:
            for p in self.plugins:
                pinst = self.plugins[p]
                pinst.LoadPluginFrames()
                
                
    def RestorePluginsDatas(self, datas):
        
    
        for p in datas:
            
            try:
                pinst = self.plugins[p]
                pinst.LoadPluginFrames(datas[p])
            except Exception as e:
                self.logger.error("RestorePluginsDatas() Unable to find plugin : " + str(e))
    
    def RaisePluginError(self, message):
        try:
            _source = str(inspect.stack()[0][0])
            self.appmainframe.Log( message, source=str(_source), type="error")
            _caller = str(inspect.stack()[1][0])
            self.appmainframe.Log( message, source=str(_caller), type="error")
        except Exception as e:
            self.logger.error("RaisePluginError() " + str(e))
                    
                    
    def ReportPluginInfo(self, message):
        try:
            _source = str(inspect.stack()[1][0])
            self.appmainframe.Log( message, source=str(_source), type="info")
        except Exception as e:
            self.logger.error("ReportPluginInfo() " + str(e))                
                    
                    
    
    
    def getAvailablePluginsViews(self, pluginname):
        viewlist = []
        
        if self.plugins.__contains__(pluginname):
        
            pinst = self.plugins[pluginname]
            pviews = pinst.PLUGINS_VIEWS
            
            for p in pviews:
                viewlist.append(p)
        
        
        
        return viewlist
    
    
    
    def getAllAvailablePlugins(self):
        viewlist = []
        for p in self.plugins:
            viewlist.append(p)
        return viewlist
    
    
    def getAllAvailableViews(self):
        viewlist = []
        
         
        for p in self.plugins:
            pinst = self.plugins[p]
            pviews = pinst.PLUGINS_VIEWS
            
            viewlist = viewlist + pviews
    
    
        return viewlist
                    
    
    def getAllActiveViews(self):
        viewlist = []
        
         
        for p in self.plugins:
            pinst = self.plugins[p]
            pviews = pinst.VIEWS_INSTANCES
            
            viewlist = viewlist + pviews
    
    
        return viewlist
    
    
    def GetViewNameInstance(self, viewName):
        allV = self.getAllActiveViews()
        
        result = None
        for v in allV:
            vname = v['name']
            
            if vname == viewName:
                result = v
    
        return result
    
    
    
    
    
    
    
    
    
    def DeleteViewInstance(self, viewname):
        
 
        for p in self.plugins:
            pinst = self.plugins[p]
            pviews = pinst.VIEWS_INSTANCES
            
            
            toremove = {}
            
            for view in pviews:
                df_name = view['name']
                
                
                if df_name == viewname:
                    toremove = view
                    #self.logger.info( "Removed !" + str(toremove))
    
            
            if toremove != {}:
                pinst.VIEWS_INSTANCES.remove(toremove)
                #self.logger.info("Removed !")
                #self.logger.info( "Removed !" + str(toremove))
    
        wx.CallAfter(self.appmainframe.Views.__refreshGUI_Job__, ())
    #def LoadNewView(self, viewName, position):
    #    new_view_callbacks = []
    
    
    
    
    
    def CloseAllPlugin(self):
        for p in self.plugins:
            pinst = self.plugins[p]
            pinst._stop = True
            #pinst.StopAllServices()
    
    
    
    
    def SaveAllPluginState(self, virtual=False):
        
        all_plugins_state = {}
        for p in self.plugins:
            #self.logger.info("saving plugin state : " + p) 
            self.ReportPluginInfo(f"Saving plugins {p} state [Virtual={virtual}]..." )
            
            pinst = self.plugins[p]
            _state = pinst.SavePluginFrames(virtual=virtual)
            
            all_plugins_state[p] = _state
    
    
        return all_plugins_state
    
    def LoadFromPluginDirectory(self):
        
        #self.logger.info(self.pluginDirectory)
        subfolders = [ f.name for f in os.scandir(self.pluginDirectory ) if f.is_dir() ]
        
        self.ReportPluginInfo("Initialize plugin list from " + self.pluginDirectory )
        
        
        self.logger.info(subfolders)
        
        for s in subfolders:
            
            
            if s == "General" or s == "__pycache__":
                continue
            
            self._detected_plugin_list.append(s)
            
            if len(self._include_only_list) > 0:
                if s not in self._include_only_list:
                    self.ReportPluginInfo(f"The plugin {s} has not been initialized (INITITALIZE ONLY in preferences). ")
                    continue
            
            if s in self._exclude_list:
                self.ReportPluginInfo(f"The plugin {s} has not been initialized (DISABLED in preferences). ")
                continue
            
            fname = 'plugins/'+s+"/plugin/<ALLCLASSES>"
            pname = fname.replace("/",".")
            
            
            
            
            if s != "__pycache__":
                
                #self.LoadPlugin(pname)
                
                if not self.safemode:
                
                    self.LoadPlugin(pname)
                    
                else:
                    try:
                        self.LoadPlugin(pname)
                    except Exception as e:
                        
                        self.RaisePluginError( "Error occurs while loading Plugin '"+s+"' :" + str(e))
                
                
            #self.classes.append(c)
        
        self.ReportPluginInfo("All plugin has been initialized. ")
        
    
    
    def GetPlugin(self, pluginName, loadIfNone=False):
        
        p = None
        
        s = {}
        if self.plugins.__contains__(pluginName):
            p = self.plugins[pluginName]
            
            
        
        if p == None and loadIfNone:
            
            try:
                self.LoadPlugin(pluginName)  
            except Exception as e:
                #source = str(inspect.stack()[1][0])
                self.RaisePluginError( "Error occurs retrieving Plugin '"+pluginName+"' :" + str(e))
     
        return p
    
    
    
    #
    #
    # Note : this method 
    #
    """
    def _LoadPluginSettings(self, pname, pinstance:PluginObject):
        _recordedSettings = self.appmainframe.Settings._GetPluginSettings(pname)
        
        
        for key in _recordedSettings:
            pinstance.PLUGIN_SETTINGS[key] = _recordedSettings[key]
    
        return pinstance
    
    
    """
    """
    def LoadGeneralPlugins(self):
        self.LoadPlugin("plugins.General.plugin.*")
        
        _gp = self.appmainframe.GetPlugin("General")
        if _gp != None:
            self._exclude_list = _gp.PLUGIN_SETTINGS['disable_plugins']
    """        
    
    
    def SetSwConfiguration(self):
        _gp = self.appmainframe.GetPlugin("General")
        if _gp != None:
            swconfiguration = _gp.PLUGIN_SETTINGS['sw_configuration']
            self.logger.info(f"Loading {swconfiguration} ...")
            
            #self.logger.info(f"available {__wxraven_configurations_list__} ...")
            
            if __wxraven_configurations_list__.__contains__(swconfiguration):
                self._include_only_list = __wxraven_configurations_list__[swconfiguration]
            else:
                self._include_only_list = __wxraven_configurations_list__[__wxraven_configurations_default__]
                self.logger.warning(f"Configuration {swconfiguration} does not exist anymore, loading std...")
   
    def SetExclusionList(self):
        _gp = self.appmainframe.GetPlugin("General")
        if _gp != None:
            self._exclude_list = _gp.PLUGIN_SETTINGS['disable_plugins']
            self.logger.info(f"Plugin exclusion list detected ! {self._exclude_list}")
            
    
    def LoadPlugin(self, pname):
        
        
        plugin_module = self.__LoadPluginModule__(pname)
        plugin_instance = None
        
        if plugin_module != None:
        
        
            plugin_init_classe = getattr(plugin_module, 'wxRavenPlugin')
            #fake obj for casting
            plugin_instance = PluginObject(self.appmainframe)
            
            plugin_instance = plugin_init_classe(self.appmainframe)
            plugin_name = plugin_instance.PLUGIN_NAME
            
            
            #plugin_instance = self._LoadPluginSettings(pname,plugin_instance )
            plugin_instance.__ApplyDefaultSettingsJSON__()
            plugin_instance._LoadPluginSettings()
            #
            
            
            #self.logger.info("Loading Plugin : " + plugin_name)
            #self.logger.info("    - Class : " + str(plugin_init_classe) )
            self.plugins[plugin_name] = plugin_instance
        
        return plugin_instance
        
    
    """
        plugin_module = self.__LoadPluginModule__(pname)
        plugin_name = getattr(plugin_module, 'PLUGIN_NAME')
        
        
        plugin_instance= initClass(self.appmainframe)
                

        self.classes[pluginName] = initClass
        self.plugins[pluginName] = module
        self.instances[pluginName] = plugin_instance
    """
    
    
    
    def __LoadPluginModule__(self, full_class_string):
        """
        dynamically load a class from a string
        """
        class_data = full_class_string.split(".")
        module_path = ".".join(class_data[:-1])
        class_str = class_data[-1]
        
        #self.logger.info('loading module in :' + module_path)
        #self.logger.info('loading class :' + class_str)
        module = importlib.import_module(module_path)
        # Finally, we retrieve the Class
        #return getattr(module, class_str)  
        return module
    
    
      