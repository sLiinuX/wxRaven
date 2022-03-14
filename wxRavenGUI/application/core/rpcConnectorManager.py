'''
Created on 10 déc. 2021

@author: slinux
'''

#
#
#    Replace RPC original lib with an extended version of it
#
#

#from ravenrpc import Ravencoin
from libs.RVNpyRPC.RVNpyRPC import Ravencoin
import logging

from libs.wxRaven_Webservices import wxRaven_RPC_WebserviceClient
import wx
import time
from datetime import timedelta
import _thread

import inspect

class RvnRPC_ConnectorManager(object):
    '''
    classdocs
    '''
    rpc_connectors = {}
    rpc_current = None
    
    
    #net_icon = None
    net_active = False
    
    parentObjSynch=None
    
    
    networkChangeCallbacks=[]
    
    
    safemode = True
    
    

    def __init__(self ,parentObjSynch):
        '''
        Constructor
        '''
        
        if parentObjSynch != None:
            self.parentObjSynch = parentObjSynch
            
            
        self.logger = logging.getLogger('wxRaven')
            
        self.net_icon = parentObjSynch.RessourcesProvider.GetImage('network')# wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY )    
        self.safemode =  parentObjSynch.Settings.safemode 
         
         
        try:
            self.LoadConnexionFromSettings()
        except Exception as e:
            self.logger.error(e)
            self.RaiseConnexionError("Unable to load connexions settings" , "error")     
        
        
        #self.__initDemo__()
    
    
    
    
    
    def LoadConnexionFromSettings(self):
        
        defaultConnectors = {}
        defaultCurrent = ""
        
        isFirst=True
        
        
        #self.logger.info("sadasd " )
        
        if self.parentObjSynch != None: 
            allCons = self.parentObjSynch.Settings.allconnexions
            
            #self.logger.info(allCons )
            
            for conName in allCons:
                #pass
                data = allCons[conName]
                #self.logger.info(conName + " -- > "+ data )
                
                
                if isFirst:
                    #self.logger.info("set current " + conName)
                    defaultCurrent = conName
                    isFirst = False
                
                _creds = data.split("@")
                _loginPwd = _creds[0].split(":")
                _hostPort = _creds[1].split(":")
                
                newCon = Ravencoin(username=_loginPwd[0], password=_loginPwd[1],host=_hostPort[0],port=_hostPort[1])
                
                
                defaultConnectors[conName] = newCon
                
        
        
        #self.logger.info("defau"  + defaultCurrent)
        self.rpc_connectors = defaultConnectors
        self.rpc_current = defaultCurrent
            
        if defaultCurrent == "":
            self.__initDemo__()    
            
            
        '''    
        self._wxRavenws = wxRaven_RPC_WebserviceClient()
        self.rpc_connectors['NO WALLET MODE'] = self._wxRavenws
        '''    
            
    
    def __initDemo__(self):    
        rvnMAINNET = Ravencoin(username='rpcAPI', password='rpcAPI',host="127.0.0.1",port=8766)
        rvnSERVER = Ravencoin(username='rpcAPI', password='rpcAPI',host="127.0.0.1",port=18766)
        rvnERROR = Ravencoin(username='rpcAPI', password='rpcAPI',host="127.0.0.1",port=66666)
        
 
        defaultConnectors = {}
        defaultConnectors['mainnet_localhost'] = rvnMAINNET
        defaultConnectors['testnet_localhost'] = rvnSERVER
        
        defaultConnectors['ERROR Serv'] = rvnERROR
        
        defaultConnectors['testnet_10.0.0.91 - pwd'] = Ravencoin(username='wrongLogin', password='wrongLogin',host="10.0.0.91",port=18766)
        defaultConnectors['testnet_localhost - pwd'] = Ravencoin(username='wrongLogin', password='wrongLogin',host="127.0.0.1",port=18766)
        
        
        self.rpc_connectors = defaultConnectors
        self.rpc_current = 'testnet_localhost'
        
        
    
    
    
    
    def RaiseConnexionError(self, message, type="error"):
        try:
            _source = str(inspect.stack()[1][0])
            self.parentObjSynch.Log( message, source=str(_source), type=type)
        except Exception as e:
            self.logger.error("RaiseConnexionError() " + str(e))  
    
    
    """
    
    Callbacks when connexion change
    
    """
    
    
    
    def RegisterOnConnexionChanged(self, callback):
    
        if not self.networkChangeCallbacks.__contains__(callback):
            self.networkChangeCallbacks.append(callback)
    
    
    
    def UnregisterOnConnexionChanged(self, callback):

        if self.networkChangeCallbacks.__contains__(callback):
            self.networkChangeCallbacks.remove(callback)
            
            
            
            
    def SafeCallbackLoop(self, connexionName=""):
        
        
        for c in self.networkChangeCallbacks:
            
            
            cb_duration = 0
            start = time.time()
            
            
            if self.safemode :
            
                try:
                    #c(connexionName)
                    #_thread.start_new_thread( c, ( ) )
                    c()
                    wx.GetApp().Yield()
                    
                except Exception as e:
                    self.logger.error(str(e) + " in " + str(c))
                    self.RaiseConnexionError(""+ str(e))
                    
            else:
                c()
                wx.GetApp().Yield()

            
            end = time.time()
            cb_duration = end-start
            #self.logger.info("cb="+str(cb_duration))
            if cb_duration > 2:
                self.RaiseConnexionError("Network Change Callback exceed 2seconds, watch for threading it. : " + str(cb_duration) +"" + str(c), 'warning')
                #self.logger.info("Callback exceed 2seconds, watch for threading it. : " + str(cb_duration) +"" + str(c))
            
    
    
    
    
    
    
    def CheckConnexionStatus(self, networkName):
        
        network  = self.getConnexion(networkName)
        isActive= False
        try:
            resultTest = network.help()
            if resultTest['result'] != None:
                isActive = True
                #self.logger.info("CheckConnexionStatus OK> " +resultTest)
        except Exception as e:
            self.RaiseConnexionError("RPC Connexion Failed : "+ str(e))
            #self.logger.info("CheckConnexionStatus ERROR> " + str(e))
        
        return isActive
    
    
    
    def SaveCurrentConnexion(self):
        
        p = self.parentObjSynch.GetPlugin("General")
        p.PLUGIN_SETTINGS['last_network'] = self.rpc_current
        #self.ConnexionManager.setCurrentConnexion(last_network)
    
    
    """
    
    Connexion setters and getters
    
    """
    
    def __iconCompute__(self, networkName, checkIt=False):
        icon = self.parentObjSynch.RessourcesProvider.GetImage('network')#wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY )
        
        if networkName.__contains__("mainnet"):
            icon = self.parentObjSynch.RessourcesProvider.GetImage('mainnet')#wx.Bitmap( u"res/default_style/normal/mainnet.png", wx.BITMAP_TYPE_ANY )
        if networkName.__contains__("testnet"):
            icon = self.parentObjSynch.RessourcesProvider.GetImage('testnet')#wx.Bitmap( u"res/default_style/normal/testnet.png", wx.BITMAP_TYPE_ANY )  
        
        
        if networkName == 'NO WALLET MODE' or networkName == 'OFFLINE-MODE' or networkName.__contains__('Relay'):
            icon =  self.parentObjSynch.RessourcesProvider.GetImage('network_limited')
        
        
        if checkIt:  
            
            isActive = self.CheckConnexionStatus(networkName)
              
            if not isActive:
                icon = self.parentObjSynch.RessourcesProvider.GetImage('network_fail')#wx.Bitmap( u"res/default_style/normal/network_fail.png", wx.BITMAP_TYPE_ANY )
        
        
            if networkName == self.rpc_current:
                self.net_active = isActive
        
            
        return icon
    
    
    def getIcon(self, networkName=""):
        
        
        if networkName != "" and networkName != self.rpc_current:
            return self.__iconCompute__(networkName, checkIt=False)
       
        
        return self.net_icon
    
    
    
    def setIconCurrent(self, networkName):
        
        
        icon = self.__iconCompute__(networkName, checkIt=True)
            
            
        self.net_icon =  icon
        return icon
        
    def setCurrentConnexion(self, connexionName):
        if self.rpc_connectors.__contains__(connexionName):
            self.rpc_current = connexionName
            self.setIconCurrent(connexionName)
            #self.parentObjSynch.setStatusBarActiveNetwork(connexionName)
            
            self.SafeCallbackLoop(connexionName)
            
            return True
        
        return False
        
    def getConnexion(self, connexionName):
        if self.rpc_connectors.__contains__(connexionName):
            return self.rpc_connectors[connexionName]
        return None
    
    
    def getConnexionType(self, connexionName):
        if self.rpc_connectors.__contains__(connexionName):
            return self.rpc_connectors[connexionName]._type
    
    
    def getConnexionScheme(self, connexionName):
        if self.rpc_connectors.__contains__(connexionName):
            _type= self.rpc_connectors[connexionName]._type
            _secure='None'
            _local = False
            _relay = False
            _url = self.rpc_connectors[connexionName].rpc_url()
            _pic = 'connexion_use_remote_s'
            _title = f'{connexionName} ({_type})'
            _desc = ""
            if _url.__contains__('https'):
                _secure = True
                _local = False
            
            if _url.__contains__('127.0.0.1'):
                _local = True
                _pic = 'connexion_use_local_s'
                
            
            
            if _url.__contains__('8766'):
                _relay = False
            
            if _url.__contains__('9090'):
                _relay = True
                _pic = 'connexion_use_relay_s'
                _secure = False
            
            
            if _url.__contains__('wxraven.link') :
                _local = False
                _relay = True
                _pic = 'connexion_use_relay_s'
            
            #_schemePicture = self.parentObjSynch.RessourcesProvider.GetImage(_pic)
            
            _trgStr = 'local'
            if not _local:
                _trgStr = 'remote'
            
            if _relay:
                _desc = f"Connexion to a {_trgStr} relay that retreive datas on the blockchain for you.\n"
                _desc = _desc + 'In order to provide the best performance to all wxRaven Users, The connexion and functionalities may be limited.'
            else:
                _desc = f"Connexion to a {_trgStr} ravencore that retreive datas on the blockchain for you.\n"
                _desc = 'If you are having issues to connect, verify ravencore settings and password (see user manual)\n'
                if not _local:
                    _desc = _desc + 'Non-local connexion are at risk, specially only HTTP-RPC only, Make sure that you are using a secure connexion to reach this wallet using SSH and Tunnelings'
            
            
            
            return {
                'name':connexionName,
                'title':_title,
                'type':_type,
                'secure':_secure,
                'local':_local,
                'relay':_relay,
                'url':_url,
                'scheme':_pic,
                'desc':_desc,
                }    
                
        
    def getAllConnexions(self):
        return self.rpc_connectors
    
    def getCurrent(self):
        return self.rpc_current
        
    def getCurrentConnexion(self):
        return self.rpc_connectors[self.rpc_current]
    
    
    
    