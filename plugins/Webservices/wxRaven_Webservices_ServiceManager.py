'''
Created on 8 févr. 2022

@author: slinux
'''

import threading

import time
from _ast import alias

from .FlaskEngine import *


class wxRaven_Webservices_BackgroundServiceManager(object):
    '''
    classdocs
    '''
    
    parent_frame = None
    plugin = None
    
    _isRunning = False
    
    _StopRequested = False
    
    
    def __init__(self, parentFrame, pluginInstance):
        '''
        Constructor
        '''
        self.parent_frame = parentFrame
        self._isRunning = False
        self._StopRequested = False
        self.logger = logging.getLogger('wxRaven')
        
        self.plugin = pluginInstance
        
        self.thread = None
        
        
        _ip = pluginInstance.PLUGIN_SETTINGS['webservice_server_ip']
        _port = pluginInstance.PLUGIN_SETTINGS['webservice_server_port']
        _path = pluginInstance.PLUGIN_SETTINGS['webservice_server_path']
        _forceNetwork = pluginInstance.PLUGIN_SETTINGS['webservice_force_network']
        _admin_token = pluginInstance.PLUGIN_SETTINGS['webservice_server_admin_token']
        #_user_token = pluginInstance.PLUGIN_SETTINGS['webservice_server_user_token']
        
        self.serviceInstance = wxRaven_Webservices_FlaskDaemon(parentFrame, _ip, _port, _path, _forceNetwork , _admin_token)
        
        
        
    def StartService(self):
        
        self.logger.info(" wxRaven_Webservices Starting")
        if not self._isRunning:
            #print("GO")
            self._StopRequested = False
            
            t=threading.Thread(target=self.Service_Run_T, daemon=True)
            t.start()
            self.parent_frame.GetPlugin("RavenRPC").addLocalVarInShell(  t, "webserviceDaemonTH")
            self.thread = t
            self.logger.info(" wxRaven_Webservices STARTED")
            self.plugin.setData("_status", "RUNNING")
            
            
    
    
    
    def __monitoring_loop__(self):        
        while self.thread.is_alive():
            time.sleep(2)
            self.logger.info(' webservice __monitoring_loop__')
            self.plugin.setData("_status", "RUNNING")
            
            
        self.plugin.setData("_status", "STOPPED")
    
    def __service_ended__(self):
        self.plugin.setData("_status", "STOPPED")
        self._isRunning = False
        
            
    def Service_Run_T(self, evt=None):
        self._isRunning = True
        self.plugin.setData("_status", "RUNNING")
        
        self.serviceInstance.StartWebService()
        self.__service_ended__()
        #self.plugin.setData("_status", "STOPPED")
        #self.__monitoring_loop__()
        
        
        
        
    
    
    
    