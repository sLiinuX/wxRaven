'''
Created on 20 déc. 2021

@author: slinux
'''
import datetime
import logging



class RVNpyRPC_Utils():
    '''
    classdocs
    '''
    RPCconnexion = None
    
    def __init__(self,connexion, parent):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent
        self.logger = logging.getLogger('wxRaven')
    """
    
    End user and sys, return direct usable datas most of the time
    
    """
    
    
    def info(self):
        pass
    
    
    def __repr__(self): 
        return ""
    
    def __str__(self): 
        return  ""
    
    #
    #shortcut for outside the lib
    #
    
    def RVN_balance_friendly(self,balance):
        return self.RVNpyRPC.wallet.RVN_balance_friendly(balance)
    
    def RVN_hashrate_friendly(self,hashrate):
        return self.RVNpyRPC.network.RVN_hashrate_friendly(hashrate)
    
    def RVN_difficulty_friendly(self,diff):
        return self.RVNpyRPC.network.RVN_difficulty_friendly(diff)
    
    
    
    
    
    
    
    
    def GetTransaction(self, txid):
        _result = None
        
        try:
            datasRes = self.RPCconnexion.gettransaction(txid)
            if datasRes['result'] != None:
                _result = datasRes['result']
            
        except Exception as e:
            self.logger.info(f"DecodeTransaction() ERROR {e}.") 
    
        return _result
    
    
    
    def DecodeTransaction(self, raw):
        _result = None
        
        try:
            datasRes = self.RPCconnexion.decoderawtransaction(raw)
            if datasRes['result'] != None:
                _result = datasRes['result']
            
        except Exception as e:
            self.logger.info(f"DecodeTransaction() ERROR {e}.") 
    
        return _result
    
    
    
    
    
    
    def blockHeightToDate(self, height):
        _defaultTime = "???????"
        try:
            blockHash = self.RPCconnexion.getblockhash(height)['result']
            blockDateTime = self.RPCconnexion.getblock(blockHash, 2 )['result']['time']
            ts = datetime.datetime.fromtimestamp(blockDateTime).strftime('%Y-%m-%d %H:%M:%S')
            _defaultTime = ts
        except Exception as e:
            self.logger.info("blockHeightToDate() error.")    
            
        return _defaultTime
        