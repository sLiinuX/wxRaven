'''
Created on 2 janv. 2022

@author: slinux
'''

#import ipfshttpclient
#import ipfsapi


#from libs import ipfshttpclient


from ._IPFSrpcClient import IPFS_RPC_Client

import logging




class RavenPyIPFS(object):
    '''
    classdocs
    '''
    IPFSserverConnexion = None
    IPFSDefaultCon = "/ip4/127.0.0.1/tcp/5001"
    IPFS_RPC_Client = None
    
    
    KNOWN_SERVERS = ['ec2-18-221-126-115.us-east-2.compute.amazonaws.com','172.105.7.111']
    
    def __init__(self, ConString="/ip4/127.0.0.1/tcp/5001", rpcServer="ec2-18-221-126-115.us-east-2.compute.amazonaws.com", rpcPort=9000):
        '''
        Constructor
        '''
        
        self.logger = logging.getLogger('wxRaven')
        
        
        try:
            
            self.IPFS_RPC_Client = IPFS_RPC_Client(rpcServer,rpcPort )
            
            #self.IPFSDefaultCon = ConString
            #self.IPFSserverConnexion = ipfshttpclient.connect(ConString)
            #self.IPFSserverConnexion = ipfsapi.connect('127.0.0.1', 5001)
            #self.logger.info(self.IPFSserverConnexion )
        except Exception as e:
            self.logger.error(str(e))
            #self.IPFS_RPC_Client = None
            
        '''   
        try:
            #self.IPFS_RPC_Client = IPFS_RPC_Client(rpcServer,rpcPort 
            self.IPFSDefaultCon = ConString
            self.IPFSserverConnexion = ipfshttpclient.connect(ConString)
            #self.IPFSserverConnexion = ipfsapi.connect('127.0.0.1', 5001)
            #self.logger.info(self.IPFSserverConnexion )
        except Exception as e:
            self.logger.error(str(e))
            self.IPFSserverConnexion = None
        '''
    
    def __useDirectApi__(self, filename='',jsonD=''):
        _hash = None
        if self.IPFSserverConnexion !=None:
            try:
                
                if filename != '':
                    _hash = self.IPFSserverConnexion.add(filename)
                
                elif jsonD != '':
                    _hash = self.IPFSserverConnexion.add_json(jsonD)
                
                try:
                    self.IPFSserverConnexion.pin.add(_hash)
                except Exception as e:
                    self.logger.error(str(e))
            except Exception as e:
                self.logger.error(str(e))
        return _hash
            
    
    
    
    
    def __fallback__Upload__File__(self, filename):
        self.logger.info("__fallback__Upload__ > Using Known servers")
        _hash = None
        
        
        for s in self.KNOWN_SERVERS  :
            try: 
                self.IPFS_RPC_Client = IPFS_RPC_Client(s,'9000' )
                self.logger.info(f'Trying with {s}...')
                
                _hash = self.UploadFile(filename,_fallback=False)
                #self.IPFSDefaultCon = ConString
                #self.IPFSserverConnexion = ipfshttpclient.connect(ConString)
                #self.IPFSserverConnexion = ipfsapi.connect('127.0.0.1', 5001)
                #self.logger.info(self.IPFSserverConnexion )
            except Exception as e:
                self.logger.error(f"Error upload : {e}")
                #self.IPFS_RPC_Client = None
                
                
            if _hash != None:
                break    
    
    
    
        return _hash
    
    
            
    def UploadFile(self, filename, _fallback=True):
        _hash = None
        
        
        if self.IPFS_RPC_Client !=None:
            
            
            try:
                _hash = self.IPFS_RPC_Client.sendFile(filename)
            except Exception as e:
                self.logger.error("Unable to send on RPC : "+str(e))
                
                
        
        
        if _hash == None:
            if _fallback:
                _hash = self.__fallback__Upload__File__(filename )
                
        return   _hash  
        #else:
        #    return self.__useDirectApi__(filename=filename)
    
    
    
    def __fallback__Upload__Ad__(self, datas):
        self.logger.info("__fallback__Upload__ > Using Known servers")
        _hash = None
        for s in self.KNOWN_SERVERS  :
            try: 
                self.IPFS_RPC_Client = IPFS_RPC_Client(s,'9000' )
                self.logger.info(f'Trying with {s}...')
                
                _hash = self.UploadP2PMarketAd(datas,_fallback=False)
                #self.IPFSDefaultCon = ConString
                #self.IPFSserverConnexion = ipfshttpclient.connect(ConString)
                #self.IPFSserverConnexion = ipfsapi.connect('127.0.0.1', 5001)
                #self.logger.info(self.IPFSserverConnexion )
            except Exception as e:
                self.logger.error(f"Error upload : {e}")
                #self.IPFS_RPC_Client = None
                
                
            if _hash != None:
                break    
    
    
    
        return _hash
            
    
    def UploadP2PMarketAd(self, datas, _fallback=True):
        
        _hash = None
        
        if self.IPFS_RPC_Client !=None:
            try:
                _hash = self.IPFS_RPC_Client.sendJSON(datas)
            except Exception as e:
                self.logger.error("Unable to send on RPC : "+str(e))
            
            
        if _hash == None:
            if _fallback:
                _hash= self.__fallback__Upload__Ad__(datas )    
        return   _hash 
        #else:
        #    return self.__useDirectApi__(filename='', jsonD=datas)
        