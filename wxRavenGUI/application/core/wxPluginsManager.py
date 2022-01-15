'''
Created on 10 déc. 2021

@author: slinux
'''
import importlib
import os
from wxRavenGUI.application.pluginsframework import *
import inspect

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
    
    _detected_plugin_list=[]
    
    

    def __init__(self, pluginRootDir, contextAppMainFrame,resumestate=True , loadPath=True, _exclude=[]):
        '''
        Constructor
        '''
        self.pluginDirectory = pluginRootDir
        self.appmainframe = contextAppMainFrame
        
        self.plugins = {}
        self.new_view_callbacks = []
        
        self.resumestate = resumestate
        
        self.safemode = contextAppMainFrame.Settings.safemode
        
        
        self._exclude_list = _exclude
        
        
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
    
    
    def RaisePluginError(self, message):
        try:
            _source = str(inspect.stack()[1][0])
            self.appmainframe.Log( message, source=str(_source), type="error")
        except Exception as e:
            print("RaisePluginError() " + str(e))
                    
                    
    def ReportPluginInfo(self, message):
        try:
            _source = str(inspect.stack()[1][0])
            self.appmainframe.Log( message, source=str(_source), type="info")
        except Exception as e:
            print("ReportPluginInfo() " + str(e))                
                    
                    
    
    
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
                    #print( "Removed !" + str(toremove))
    
            
            if toremove != {}:
                pinst.VIEWS_INSTANCES.remove(toremove)
                #print("Removed !")
                #print( "Removed !" + str(toremove))
    
        wx.CallAfter(self.appmainframe.MenusAndTool.refreshViewsListMenu, ())
    #def LoadNewView(self, viewName, position):
    #    new_view_callbacks = []
    
    
    
    
    
    def CloseAllPlugin(self):
        for p in self.plugins:
            pinst = self.plugins[p]
            pinst._stop = True
            #pinst.StopAllServices()
    
    
    
    
    def SaveAllPluginState(self):
        
        for p in self.plugins:
            #print("saving plugin state : " + p) 
            self.ReportPluginInfo("Saving plugins state..." )
            
            pinst = self.plugins[p]
            pinst.SavePluginFrames()
    
    
    def LoadFromPluginDirectory(self):
        
        #print(self.pluginDirectory)
        subfolders = [ f.name for f in os.scandir(self.pluginDirectory ) if f.is_dir() ]
        
        self.ReportPluginInfo("Initialize plugin list from " + self.pluginDirectory )
        
        
        print(subfolders)
        
        for s in subfolders:
            
            
            if s == "General" or s == "__pycache__":
                continue
            
            self._detected_plugin_list.append(s)
            
            
            
            if s in self._exclude_list:
                self.ReportPluginInfo(f"The plugin {s} has not been initialized (DISABLED in preferences). ")
                continue
            
            fname = 'plugins/'+s+"/plugin/<ALLCLASSES>"
            pname = fname.replace("/",".")
            
            
            
            
            if s != "__pycache__":
                
                
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
   
   
    def SetExclusionList(self):
        _gp = self.appmainframe.GetPlugin("General")
        if _gp != None:
            self._exclude_list = _gp.PLUGIN_SETTINGS['disable_plugins']
            print(f"Plugin exclusion list detected ! {self._exclude_list}")
            
    
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
            plugin_instance._LoadPluginSettings()
            
            #print("Loading Plugin : " + plugin_name)
            #print("    - Class : " + str(plugin_init_classe) )
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
        
        #print('loading module in :' + module_path)
        #print('loading class :' + class_str)
        module = importlib.import_module(module_path)
        # Finally, we retrieve the Class
        #return getattr(module, class_str)  
        return module
    
    
      