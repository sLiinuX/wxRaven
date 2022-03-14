'''
Created on 8 févr. 2022

@author: slinux
'''

'''
Created on 18 déc. 2021

@author: slinux



This file contains the main class to define the plugin
Each plugin must have a plugin.py file which declare a class wxRavenPlugin(PluginObject)


'''


#import the class form above level, it contains predefined functions to overwrite.
#from plugins.pluginObjectTemplate import * 
from wxRavenGUI.application.pluginsframework import *
#import the design of your plugin made in FormBuilder
from .wxRaven_Webservices_ServiceManager import wxRaven_Webservices_BackgroundServiceManager
from .pluginSettings import wxRaven_Webservices_SettingsPanelLogic, wxRaven_Webservices_RemoteJobs_SettingsPanelLogic
#used for long datas requests
import threading
import time


from libs.wxRaven_Webservices.wxRaven_Flask_Webservice import wxRaven_Flask_WebserviceClient


class wxRavenPlugin(PluginObject):
    '''
    classdocs
    '''


    def __init__(self, parentFrame, position="mgr"):
        
        
        #Call the parent class with ParentFrame and Position
        #This object is the plugin instance and will manage all views internally.
        PluginObject.__init__(self, parentFrame, position=position)
        
        
       
        self.PLUGIN_NAME = "Webservices"
        self.PLUGIN_ICON = self.RessourcesProvider.GetImage('connexion_share_1') #wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
        
        
        
        
        #
        #    View Object declare all the 'Views' that can be instanciated
        #    {
        #             'viewid':                  a unique id for the view
        #             'name':                    a name for the view
        #             'title':                   a title id for the view
        #             'position':, 
        #             'icon':
        #             'class': 
        #             'default':                 Boolean to determine if the view is open by default at startup
        #             'multipleViewAllowed':     Boolean to determine if the view allow multiple instance of it 
        #}
        #        
        
        
        self.PLUGINS_VIEWS= [ 
                    
                    
                   
        
                    
                ]
        

        
        #
        #    Setting Object declare all the 'default settings' 
        #    Once the plugin loaded for the first time, those settings will be saved
        #    in the config.ini file in a dedicated section when app close.
        #
        #    On next plugin load, if the config file contains plugins settings
        #    those will be overwritten in the _LoadPluginSettings() function
        #    
        #    you need to declare your own function as later in the file to CAST datas 
        #    that come from the ConfigParser in String only
        #
        #    {
        #             'key':                 value
        #    }
        #        
        
        defaultPath = self.parentFrame.GetPath("USERDATA") + 'wxRaven_Webservices.log'
        
        self.PLUGIN_SETTINGS = {
                
                'webservice_server_enable' : False,
                'webservice_server_ip' : '127.0.0.1',
                'webservice_server_port' : 9090,
                'webservice_server_path' : defaultPath,
                'webservice_server_admin_token' : '',
                'webservice_server_user_token' : '',
                
                'webservice_force_network' : '',
                'webservice_exclude_services' : [],
                'webservice_exclude_remotejobs' : [],
                'webservice_exclude_remotejobs_redirection':'plugins.Webservices.jobs.RemoteJobs_NotAllowedJob.Job_NotAllowedRemoteJob'
                
            }
        
        
        
        
        #
        # Lets put some setting pannels from pluginsetting file (to define as well)
        #
        
        self.PLUGIN_SETTINGS_GUI = []
        
        _prefIcon = self.RessourcesProvider.GetImage('connexion_share_1')
        _MyTutorialSettingPanel_WithLogic = PluginSettingsTreeObject("Webservices", _prefIcon, classPanel=wxRaven_Webservices_SettingsPanelLogic, _childs=None)
        
        
        
        _Icon = self.RessourcesProvider.GetImage('job_remote_icon')
        _bmrkPannel = PluginSettingsTreeObject("Remote Jobs", _Icon, classPanel=wxRaven_Webservices_RemoteJobs_SettingsPanelLogic, _childs=None)
        
        
        _MyTutorialSettingPanel_WithLogic._childs.append(_bmrkPannel)
        
        
        self.PLUGIN_SETTINGS_GUI.append(_MyTutorialSettingPanel_WithLogic)
        
        
        
        #
        # Datas : In order to avoid each view to individually request the same data through RPC,
        #         the plugin can contains Global vars / datas shared to the views
        #         it also allow to request those big datas through thread and call update after
        #
        self.setData("webservicebackgroundManager", None)
        self.setData("webservice_daemon_instance", None)
        self.setData("_status", "STOPPED")
        self.backgroundService = None
        #self.setData("myPluginData2", False)
        
        
        #
        # Plugin can Register on callbacks like Connexion change in this case, it will start a thread to get datas
        #
        #self.parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        
        
        #
        # Finally, this last line is MANDATORY to load the default views.
        # REMOVED AND REPLACED BY AN AUTO LOAD
        #self.LoadPluginFrames()
        
        self.waitApplicationReady()
    
    #
    # Run a thread and wait app to be fully loaded
    #
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.__applicationReady__,))
        t.start()
        
    #
    #  thread to wait
    #    
    def __waitLoop_T__(self,callback):
        while not self.parentFrame._isReady:
            time.sleep(1)
            
        wx.CallAfter(callback, ()) 
        
        
        #self.initializeAssetManagerBackgroundService()
    
    #
    #  thread callback
    #
    def __applicationReady__(self, evt=None):
        
        
        _wsOn = self.PLUGIN_SETTINGS['webservice_server_enable']
        if _wsOn:
        #if True:
            self.backgroundService = wxRaven_Webservices_BackgroundServiceManager(self.parentFrame, self)
            self.StartWebService()
    
    
    
    
    
    
    
    
    
    
    def StartWebService(self, evt=None): 
        
        self.setData("_status", "STARTED")
        
        if self.backgroundService ==None:
            self.backgroundService = wxRaven_Webservices_BackgroundServiceManager(self.parentFrame, self)
            
        
        self.backgroundService.StartService()
        
        self.setData("webservicebackgroundManager", self.backgroundService)
    
    
    
    def StopWebService(self, evt=None):
        #from libs.wxRaven_Flask_Webservice import wx
        ws = wxRaven_Flask_WebserviceClient(self.PLUGIN_SETTINGS['webservice_server_ip'], self.PLUGIN_SETTINGS['webservice_server_port'])
        
        params = {'token':self.PLUGIN_SETTINGS['webservice_server_admin_token']}
        ws.get_query('/api/v1/admin/shutdown_server', params, auth=False)
        
        pass
    
    
    
    def GetServicesList(self):
        API_Services_Path = self.parentFrame.GetPath("PLUGIN") + '/Webservices/FlaskEngine/API_Services/'
        
        serviceList = []
        
        for filename in os.listdir(API_Services_Path):
            f = os.path.join(API_Services_Path, filename)
            # checking if it is a file
            _nameAndExt = str(filename).split('.')
            
            if os.path.isfile(f):
                if filename == 'wxFlaskCustomView.py':
                    continue
                
                else:
                    serviceList.append(_nameAndExt[0])
                
                
        return serviceList
    
    
    
    def GetWebserviceDaemonInstance(self):
        return self.getData( "webservice_daemon_instance")
    
    
    
    
    
    """
    
    Plugins setting management
    
    Note, this method must be overwritten on plugins that use settings since
    config parser only use STRING values.
    
    
    """
    
    #
    # Seems not mandatory with new LoadSetting Generic function but in case of specific
    # Types, better redeclare it!
    #
    
    """
    def _LoadPluginSettings(self):
        _recordedSettings = self.parentFrame.Settings._GetPluginSettings(self.PLUGIN_NAME)
        
        
        for key in _recordedSettings:
            
            
            #
            # _recordedSettings[key] Return string only, do your own mapping for complex datastructure
            #
            self.PLUGIN_SETTINGS[key] = _recordedSettings[key]
            
            
    """        
                
        
    '''
    
    Plugin Triggers / Callbacks for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
     
    '''
        
            
        
    def OnNetworkChanged_T(self, networkName=""):   
        if not self.parentFrame._isReady:
            return None  
        t=threading.Thread(target=self.OnNetworkChanged)
        t.start()
        
        
    def OnNetworkChanged(self):
        
        #self.setData("myPluginData", {})
        #self.setData("myPluginData2", False)
        
        try:
            
            '''
            myPluginData = self.parentFrame.ConnexionManager.getAllConnexions()
            myPluginData2 = self.parentFrame.ConnexionManager.getCurrent()
            
            
            self.setData("myPluginData", myPluginData)
            self.setData("myPluginData2", myPluginData2)

            #When datas are loaded, add a call after to trigger plugins view update
            '''
            wx.CallAfter(self.UpdateActiveViews, ())
            
        except Exception as e:
            self.RaisePluginLog( "Unable to retreive connexion informations :"+ str(e), type="error")
            
            
        
        
        