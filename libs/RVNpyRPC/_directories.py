'''
Created on 23 janv. 2022

@author: slinux
'''

import datetime
import logging
import time
from datetime import date, datetime

class RVNpyRPC_Directories():
    '''
    classdocs
    '''
    RPCconnexion = None
    
    MAX_RPC_RETURN = 50000
    
    def __init__(self,connexion, parent):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent
        self.logger = logging.getLogger('wxRaven')
    
    
    
    
    
    
    
    
    
    def GetAddressTransactionList(self,addressesArray, _fullScan=False, start_date=None, stop_date=None):
        _args = {'addresses':addressesArray }
        _resList = []
        _AddressTxLList = self.RPCconnexion.getaddresstxids(_args, True)
        _startDateInt=0
        _stopDateInt=time.time()
        
        if _AddressTxLList['error'] != None:
            _msg =  _AddressTxLList['error']['message']
            self.logger.error(f"{_msg}")
            raise Exception(f"{_msg}")
        #self.logger.info(f" y {start_date.year} m {start_date.month} d {start_date.day}")
        
        if start_date != None:
            #_startDateInt = start_date.timestamp()
            self.logger.info(f" y {start_date.year} m {start_date.month} d {start_date.day}")
            
            dt = datetime(
                    year=start_date.year,
                    month=start_date.month+1,
                    day=start_date.day
                 )
            #timestamp = int(dt.timestamp())
            _startDateInt= int(dt.timestamp())
            
        if stop_date != None:
            self.logger.info(f" y {stop_date.year} m {stop_date.month} d {stop_date.day}")
            
            dt = datetime(
                    year=stop_date.year,
                    month=stop_date.month+1,
                    day=stop_date.day
                 )
            _stopDateInt = int(dt.timestamp())
            
        
            
        _founds= len(_AddressTxLList['result'])
        _cursor  = 0
        self.logger.info(f" {_founds} Transactions Found !")
        
        #_transactions_list = {}
        #_transactions_count= 0
        
        for _tx in _AddressTxLList['result']:
            
            
            
            #
            # add a print or progress
            #
            #
            
            if not _fullScan:
                _resList.append(_tx)
                
            else:
                
                self.logger.info(f" Inspecting Transactions ({_cursor} / {_founds})")
                
                
                
                
                _txDatas = self.RVNpyRPC.utils.GetRawTransaction(_tx ,True,  addressesArray)
                #_txDatas = self.RPCconnexion.getrawtransaction (_tx, True)['result']
                #_txDatas = self.RVNpyRPC.utils.AnalyseTransaction(_txDatas, addressesArray)
                if  _txDatas['blocktime'] < _startDateInt:
                    self.logger.info(f"skipped tx  {_txDatas['blocktime']} < {_startDateInt}")
                    continue
                    
            
            
                if _txDatas['blocktime'] > _stopDateInt:
                    self.logger.info(f"skipped tx  {_txDatas['blocktime']} > {_stopDateInt}")
                    continue
                
                '''
                _txDatas = self.RVNpyRPC.utils.InspectTransaction(_txDatas, addressesArray)
                #_totalIn = 0.0
                #_totalOut = 0.0
                

                #
                _txDatas['datetime'] = datetime.fromtimestamp(_txDatas['blocktime']).strftime('%Y-%m-%d %H:%M:%S')
                
                if not _txDatas.__contains__('fee'):
                    _txDatas['fee'] = 0.0
                
                if not _txDatas.__contains__('address'):
                    _txDatas['address'] = addressesArray
                
                
                if not _txDatas.__contains__('category'):
                    _txDatas['category'] = "Unknown"  
                    
                      
                if not _txDatas.__contains__('amount'):
                    _txDatas['amount'] = 0.0   
                
                
                '''    
                    
                _objectData = _txDatas
                _resList.append(_objectData)
                _cursor = _cursor + 1
                
                
        
        
        return _resList
    
    
    def GetAddressUnspentList(self, addressesArray, asset="*", _excludeAsset=''):
        _args = {'addresses':addressesArray, 'chainInfo': True, 'assetName'  : asset}
        
        _resList = []
        
        
        res = self.RPCconnexion.getaddressutxos(_args)
       
        _AddressUnspentList = res['result']
        #print(_AddressUnspentList)
        if _AddressUnspentList == None and res['error'] != None:
            _msg =  res['error']['message']
            raise Exception(f"{_msg}")
        
            
            
        for _utxo in _AddressUnspentList['utxos']:
            if _excludeAsset != '':
                if _excludeAsset == _utxo['assetName']:
                    continue
                
                
            if asset !='*':
                if asset != _utxo['assetName']:
                    continue
                
            
            _resList.append(_utxo)
        
        
        return _resList
        
        
        
    def GetAssetOwnerAddressList(self, assetname, detailed=False):
        
        
        _ownerAddrCount = self.RPCconnexion.listaddressesbyasset(assetname, True)['result'] 
        _adList= []
        if detailed:
            _adList = {}
        _rList=None
        if _ownerAddrCount == None:
            return _adList
        
        self.logger.info(f'GetAssetOwnerAddress {assetname} : {_ownerAddrCount}')
        if _ownerAddrCount < self.MAX_RPC_RETURN:
            _adListRaw = self.RPCconnexion.listaddressesbyasset(assetname, False)['result'] 
            if not detailed:
                for ad in _adListRaw:
                    _adList.append(ad)
            else:
                for ad in _adListRaw:
                    _adList[ad] = _adListRaw[ad]
        
        else:
            
            _cursorStart=0
            _cursorStop = 0
            #steps = self.MAX_RPC_RETURN
            
            while _cursorStart < _ownerAddrCount:
                self.logger.info(f' Cursor {_cursorStart}')
                _adListRaw = self.RPCconnexion.listaddressesbyasset(assetname, False, self.MAX_RPC_RETURN, _cursorStart)['result'] 
                
                if not detailed:
                    for ad in _adListRaw:
                        _adList.append(ad)
                        
                else:
                    for ad in _adListRaw:
                        _adList[ad] = _adListRaw[ad]
                
                _cursorStart = _cursorStart + self.MAX_RPC_RETURN
                _cursorStop = _cursorStart + self.MAX_RPC_RETURN
                
        if not detailed :         
            _rList = list(dict.fromkeys(_adList))        
        else:
            _rList =  _adList   
                
        return _adList
    
    
    
    def GetAllAssetOwners(self, mainasset, _includeSub=False):
        _adList= [] 
        
        if not mainasset.__contains__('*') and _includeSub:
            mainasset = mainasset + '*'
        
        _allResultAsset = self.RVNpyRPC.asset.SearchAsset(mainasset, limit=999999, details=False, datetime=False)
        
        
        for _asset in _allResultAsset:
            _assetName = _allResultAsset[_asset]['name']
            self.logger.info(f' Scanning {_assetName}')
            _adListAsset = self.GetAssetOwnerAddressList(_assetName)
            if len(_adListAsset) >0:
                _adList = _adList+_adListAsset
        
        
        return _adList