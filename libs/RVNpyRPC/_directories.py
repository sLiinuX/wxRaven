'''
Created on 23 janv. 2022

@author: slinux
'''

import datetime
import logging



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
        
        
    def GetAssetOwnerAddressList(self, assetname):
        
        
        _ownerAddrCount = self.RPCconnexion.listaddressesbyasset(assetname, True)['result'] 
        _adList= []
        
        if _ownerAddrCount == None:
            return _adList
        
        self.logger.info(f'GetAssetOwnerAddress {_ownerAddrCount}')
        if _ownerAddrCount < self.MAX_RPC_RETURN:
            _adListRaw = self.RPCconnexion.listaddressesbyasset(assetname, False)['result'] 
            
            for ad in _adListRaw:
                _adList.append(ad)
        
        else:
            
            _cursorStart=0
            _cursorStop = 0
            #steps = self.MAX_RPC_RETURN
            
            while _cursorStop < _ownerAddrCount:
                self.logger.info(f' Cursor {_cursorStart}')
                _adListRaw = self.RPCconnexion.listaddressesbyasset(assetname, False, self.MAX_RPC_RETURN, _cursorStart)['result'] 
                
                for ad in _adListRaw:
                    _adList.append(ad)
                
                _cursorStart = _cursorStart + self.MAX_RPC_RETURN
                _cursorStop = _cursorStart + self.MAX_RPC_RETURN
                
                  
        mylist = list(dict.fromkeys(_adList))        
                
                
        return mylist
    
    
    
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