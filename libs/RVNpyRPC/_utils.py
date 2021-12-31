'''
Created on 20 déc. 2021

@author: slinux
'''
import datetime


class RVNpyRPC_Utils():
    '''
    classdocs
    '''
    RPCconnexion = None
    
    def __init__(self,connexion):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
    
    
    """
    
    End user and sys, return direct usable datas most of the time
    
    """
    
    
    def info(self):
        pass
    
    
    def __repr__(self): 
        return ""
    
    def __str__(self): 
        return  ""
    
    
    def blockHeightToDate(self, height):
        _defaultTime = "???????"
        try:
            blockHash = self.RPCconnexion.getblockhash(height)['result']
            blockDateTime = self.RPCconnexion.getblock(blockHash, 2 )['result']['time']
            ts = datetime.datetime.fromtimestamp(blockDateTime).strftime('%Y-%m-%d %H:%M:%S')
            _defaultTime = ts
        except Exception as e:
            print("blockHeightToDate() error.")    
            
        return _defaultTime
        