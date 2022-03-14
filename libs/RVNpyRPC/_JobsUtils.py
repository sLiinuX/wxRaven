'''
Created on 9 mars 2022

@author: slinux
'''

import datetime
import logging



class RVNpyRPC_JobsUtils():
    '''
    classdocs
    '''
    RPCconnexion = None
    
    SATOSHIS_CONVERT = 100000000
    
    def __init__(self,connexion, parent):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent
        self.logger = logging.getLogger('wxRaven')
        
        
        
    def NewJobReceiveAddress(self, jobUniqueReference):
        _e, _ads=self.RVNpyRPC.accounts.CreateNewAccount(jobUniqueReference)
        return _ads
    
    
    def GetJobReceiveAddress(self, jobUniqueReference):
        _ads=self.RVNpyRPC.accounts.GetFirstAccountAddress(jobUniqueReference)
        return _ads
    
    
    
    def GetJobAddressBalance(self, jobUniqueReference, includeAssets=False):
        return self.RVNpyRPC.accounts.GetAccountBalance(jobUniqueReference, includeAssets)
    
    
    def IsJobFunded(self,jobUniqueReference, minAmount,satoshis=False, assetName='RVN'):
        
        self.logger.info(f"IsJobFunded {jobUniqueReference}")
         
        _funded=False
        _allFunds = self.GetJobAddressBalance(jobUniqueReference,  includeAssets=True)
        _fbal = 0.0
        
        if _allFunds != None:
            for _row in _allFunds:
                _asset = _row['assetName']
                _balance = _row['balance']
                _balanceCmp = _balance
                
                self.logger.info(f"IsJobFunded _allFunds {_asset} {_balance}")
                
                if _asset == assetName:
                    
                    if satoshis:
                        minAmount = minAmount * self.SATOSHIS_CONVERT
                        
                    
                    _balanceCmp = _balance/self.SATOSHIS_CONVERT
                    
                    
                        
                    if _balanceCmp>=minAmount:
                        _funded = True
                        _fbal = _balanceCmp
            
        self.logger.info(f"IsJobFunded {_funded} {_fbal}")        
        return  _funded, _fbal
    
    
       
    def CheckJobTx(self, jobUniqueReference,txid):
        _foundTx = False
        _received = False
        _confirmations = 0
        _spendable = False
        _txList = []
        
        
        _ad= self.GetJobReceiveAddress(jobUniqueReference)
        
        if _ad!=None:
            
            txDatas = self.RVNpyRPC.utils.GetRawTransaction( txid, decoded=True, addressesPOV=[] , inspect=False)
        
            if txDatas!= None:
                _foundTx = True
                _confirmations =  txDatas['confirmations'] 
                
                if txDatas['confirmations'] > 1:
                    _checkIfReceived, _unspentList = self.RVNpyRPC.wallet.SearchUnspentTxfromTxId(txid, [_ad])
                    
                    if not _checkIfReceived:     
                        pass
                    else:
                        _received = True
                        
                        for _row in _unspentList:
                            _spendable = _row['spendable']
        
                   
                        _txList = _unspentList
        
        _res = {
            'found':_foundTx,
            'received':_received,
            'confirmations' : _confirmations,
            'spendable': _spendable,
            'tx_list':_txList
                }
        
        return _res
    
    
    
    
    def PurgeJobUTXOs(self,jobUniqueReference, dest, txid=None):
        _ad= self.GetJobReceiveAddress(jobUniqueReference)
        _utxoList = self.RVNpyRPC.wallet.GetUnspentList( _OnlySpendable=True, _IncludeOnlyAddresses=[_ad], _fullDatas=True)
        
        
        for _txRow in _utxoList:
            
        
            self.RVNpyRPC.wallet.sendFromAccount(jobUniqueReference, dest ,_txRow['amount'])
    
            
    
    
    
    
    
        