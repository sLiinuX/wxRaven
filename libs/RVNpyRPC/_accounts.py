'''
Created on 9 mars 2022

@author: slinux
'''


import datetime
import logging



class RVNpyRPC_Accounts():
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
        
        
        
        
    def __AccountNameExist__(self, accountName):
        _e = False
        _rpcdatas = self.RPCconnexion.getaddressesbyaccount(accountName)    
        if _rpcdatas['result'] != None:
            if len(_rpcdatas['result']) > 0:
                _e = True
        return _e    
        
    def CreateNewAccount(self, accountName):
        _exist = False
        _accountAddress = []
        
        if self.__AccountNameExist__(accountName):
            _exist = True
            _accountAddress= self.RPCconnexion.getaddressesbyaccount(accountName)['result']  
            
        else:
            _newAddress = self.RPCconnexion.getaccountaddress(accountName)['result'] 
            _accountAddress.append(_newAddress)     
        
        _result = ''
        if len(_accountAddress) > 0:
            _result = _accountAddress[0]
        
        return _exist,_result

     
    def GetAccountAddresses(self, accountName):
        _res= None
        _res = self.RPCconnexion.getaddressesbyaccount(accountName)['result']
        return _res
            
    def GetFirstAccountAddress(self, accountName):
        _res= None
        _alldatas = self.RPCconnexion.getaddressesbyaccount(accountName)['result']    
        if len(_alldatas) > 0:
            _res = _alldatas[0]
        return _res
    
    
    def GetAccountBalance(self, accountName, _includeAsset=False):
        self.logger.info(f'GetAccountBalance {accountName}')
        _accAddress = self.GetAccountAddresses(accountName)
        self.logger.info(f'GetAccountBalance {_accAddress}')
        _alldatas = self.RVNpyRPC.wallet.getAddressBalance(_accAddress,_includeAsset)
        return _alldatas
        