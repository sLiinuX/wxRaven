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
            
            
            
        self.net_icon = parentObjSynch.RessourcesProvider.GetImage('network')# wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY )    
        self.safemode =  parentObjSynch.Settings.safemode 
         
         
        try:
            self.LoadConnexionFromSettings()
        except Exception as e:
            print(e)
            self.RaiseConnexionError("Unable to load connexions settings" , "error")     
        
        
        #self.__initDemo__()
    
    
    
    
    
    def LoadConnexionFromSettings(self):
        
        defaultConnectors = {}
        defaultCurrent = ""
        
        isFirst=True
        
        
        #print("sadasd " )
        
        if self.parentObjSynch != None: 
            allCons = self.parentObjSynch.Settings.allconnexions
            
            #print(allCons )
            
            for conName in allCons:
                #pass
                data = allCons[conName]
                #print(conName + " -- > "+ data )
                
                
                if isFirst:
                    #print("set current " + conName)
                    defaultCurrent = conName
                    isFirst = False
                
                _creds = data.split("@")
                _loginPwd = _creds[0].split(":")
                _hostPort = _creds[1].split(":")
                
                newCon = Ravencoin(username=_loginPwd[0], password=_loginPwd[1],host=_hostPort[0],port=_hostPort[1])
                
                
                defaultConnectors[conName] = newCon
                
        
        
        #print("defau"  + defaultCurrent)
        self.rpc_connectors = defaultConnectors
        self.rpc_current = defaultCurrent
            
        if defaultCurrent == "":
            self.__initDemo__()    
            
            
    
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
            print("RaiseConnexionError() " + str(e))  
    
    
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
                    print(str(e) + " in " + str(c))
                    self.RaiseConnexionError(""+ str(e))
                    
            else:
                c()
                wx.GetApp().Yield()

            
            end = time.time()
            cb_duration = end-start
            #print("cb="+str(cb_duration))
            if cb_duration > 2:
                self.RaiseConnexionError("Network Change Callback exceed 2seconds, watch for threading it. : " + str(cb_duration) +"" + str(c), 'warning')
                #print("Callback exceed 2seconds, watch for threading it. : " + str(cb_duration) +"" + str(c))
            
    
    
    
    
    
    
    def CheckConnexionStatus(self, networkName):
        
        network  = self.getConnexion(networkName)
        isActive= False
        try:
            resultTest = network.help()['result']
            if resultTest != None:
                isActive = True
                #print("CheckConnexionStatus OK> " +resultTest)
        except Exception as e:
            self.RaiseConnexionError("RPC Connexion Failed : "+ str(e))
            #print("CheckConnexionStatus ERROR> " + str(e))
        
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
        
    def getAllConnexions(self):
        return self.rpc_connectors
    
    def getCurrent(self):
        return self.rpc_current
        
    def getCurrentConnexion(self):
        return self.rpc_connectors[self.rpc_current]
    
    
    
    