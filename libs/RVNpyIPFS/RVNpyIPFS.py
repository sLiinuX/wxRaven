'''
Created on 2 janv. 2022

@author: slinux
'''

#import ipfshttpclient
#import ipfsapi


#from libs import ipfshttpclient


from ._IPFSrpcClient import IPFS_RPC_Client






class RavenPyIPFS(object):
    '''
    classdocs
    '''
    IPFSserverConnexion = None
    IPFSDefaultCon = "/ip4/127.0.0.1/tcp/5001"
    IPFS_RPC_Client = None
    
    
    def __init__(self, ConString="/ip4/127.0.0.1/tcp/5001", rpcServer="192.168.1.12", rpcPort=9000):
        '''
        Constructor
        '''
        
        
        try:
            
            self.IPFS_RPC_Client = IPFS_RPC_Client(rpcServer,rpcPort )
            
            #self.IPFSDefaultCon = ConString
            #self.IPFSserverConnexion = ipfshttpclient.connect(ConString)
            #self.IPFSserverConnexion = ipfsapi.connect('127.0.0.1', 5001)
            #print(self.IPFSserverConnexion )
        except Exception as e:
            print(str(e))
            
            
        #try:
            #self.IPFS_RPC_Client = IPFS_RPC_Client(rpcServer,rpcPort 
            #self.IPFSDefaultCon = ConString
            #self.IPFSserverConnexion = ipfshttpclient.connect()
            #self.IPFSserverConnexion = ipfsapi.connect('127.0.0.1', 5001)
            #print(self.IPFSserverConnexion )
        #except Exception as e:
        #    print(str(e))
            
    
    
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
                    print(str(e))
            except Exception as e:
                print(str(e))
        return _hash
            
            
    def UploadFile(self, filename):
        if self.IPFS_RPC_Client !=None:
            return self.IPFS_RPC_Client.sendFile(filename)
        else:
            return self.__useDirectApi__(filename=filename)
            
    
    def UploadP2PMarketAd(self, datas):
        if self.IPFS_RPC_Client !=None:
            return self.IPFS_RPC_Client.sendJSON(datas)
        else:
            return self.__useDirectApi__(filename='', jsonD=datas)
        