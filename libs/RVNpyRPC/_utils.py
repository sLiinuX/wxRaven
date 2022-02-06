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
    
    
    
    
    def GetRawTransaction(self, txid, decoded=True):
        _result = None
        
        try:
            datasRes = self.RPCconnexion.getrawtransaction(txid, decoded)
            print(datasRes)
            if datasRes['result'] != None:
                _result = datasRes['result']
                
                
                if decoded:
                    _dataDecode = _decodedTx = self.DecodeTransaction(_result)
                    if _dataDecode['result'] != None:
                        _result = _dataDecode['result']
                
            
        except Exception as e:
            self.logger.error(f"GetRawTransaction() ERROR {e}.") 
    
        return _result
    
    
    
    def GetTransaction(self, txid):
        _result = None
        self.logger.info(f"GetTransaction().") 
        try:
            datasRes = self.RPCconnexion.gettransaction(txid)
            self.logger.info(f"GetTransaction() {datasRes}.") 
            if datasRes['result'] != None:
                _result = datasRes['result']
                return _result
            else:
                if    datasRes['error']['message'] == 'Invalid or non-wallet transaction id':
                    self.logger.info(f"GetRawTransaction().") 
                    _result = self.GetRawTransaction(txid, True)
                    return _result
                
                
                
        except Exception as e:
            self.logger.error(f"GetTransaction() ERROR {e}.") 
    
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
        blockHash = None
        try:
            blockHash = self.RPCconnexion.getblockhash(int(height))['result']
        except Exception as e:
            self.logger.info(f"blockHeightToDate() error blockHash : {e}")  
        
        
        if blockHash != None:
            try:
                #blockHash = self.RPCconnexion.getblockhash(int(height))['result']
                blockDateTime = self.RPCconnexion.getblock(blockHash, 2 )['result']['time']
                ts = datetime.datetime.fromtimestamp(blockDateTime).strftime('%Y-%m-%d %H:%M:%S')
                _defaultTime = ts
            except Exception as e:
                self.logger.info(f"blockHeightToDate() error : {e}")    
            
        return _defaultTime
        