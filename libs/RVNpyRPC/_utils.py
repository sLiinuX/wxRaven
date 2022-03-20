'''
Created on 20 déc. 2021

@author: slinux
'''
import datetime
import logging
from datetime import date, datetime as dt
from ._addressesDatamining import *

class RVNpyRPC_Utils():
    '''
    classdocs
    '''
    RPCconnexion = None
    AddressesDatamining = None
    
    def __init__(self,connexion, parent):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent
        self.logger = logging.getLogger('wxRaven')
        self.AddressesDatamining = AddressesDataMining(connexion, parent)
        
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
    
    
    
    def GetVout(self, txId, vout):
        _result=None
        
        _txDatas = self.RPCconnexion.getrawtransaction (txId, True)['result']
        if _txDatas != None:
            
            for _vout in  _txDatas["vout"] :
                if _vout['n'] == vout:
                    _result = _vout
                    break
        
        return _result
    
    
    def InspectTransaction(self, txInDatas, addressesPOV=[] ):
        
        #self.logger.info(f"AnalyseTransaction start")
        
        txDatas = {}
        txDatas['category'] = 'Unknown'
        
        _totalIn = 0.0
        _totalOut = 0.0
        
        _addressPovIn = 0.0
        _addressPovOut = 0.0
        
        _containsAsset = False
        _types = []
        
        
        _AssetsVouts = []
        _AddressesIn= []
        _AddressesOut= []
        
        _AddressesInInfos= {}
        _AddressesOutInfos= {}
        
        #_vinsDecoded = []
        #_voutsDecoded = []
        
        _detailsDatas = []
        _AssetDetailsDatas = []
        #
        # 1 Extraction of datas
        #
        
        for _vin in txInDatas['vin']:
            #self.logger.info(_vin)

            #self.logger.info(f"GetVout = {_vin['txid']} - { _vin['vout']}")
            
            _infoVin = self.GetVout(_vin['txid'], _vin['vout'])
            
            
            
            _totalIn = _totalIn + _infoVin['value']
            
            
            _ad = ''
            
            _adresseInfosVin = {
                'asset':'RVN',
                'amount':_infoVin['value']
                }
            
            
            
            if _infoVin !=None:
                for _ad in _infoVin['scriptPubKey']['addresses']:
                    
                    #_AddressesInInfos.append({_ad:_infoVin['value']})
                    
                    
                    if _ad in addressesPOV:
                        _addressPovIn = _addressPovIn + _infoVin['value']
                    else:
                        if not _AddressesIn.__contains__(_ad):
                            _AddressesIn.append(_ad)
                #datasRes = self.RPCconnexion.getrawtransaction(txid, decoded)
            
            
            if _infoVin['scriptPubKey'].__contains__('asset'):
                
                _AssetDetailsDatas.append({
                    "account" :'',
                   "address" : _ad, 
                   "destination" : _ad, 
                   "category" :'send' ,
                   "amount" : _infoVin['scriptPubKey']['asset']['amount'],
                   "asset_type" :  _infoVin['scriptPubKey']['type'] ,
                    "asset_name" :  _infoVin['scriptPubKey']['asset']['name'] 
                }) 
                
                
                _adresseInfosVin['asset'] = str(_infoVin['scriptPubKey']['asset']['name'])
                _adresseInfosVin['amount'] = str(_infoVin['scriptPubKey']['asset']['amount'])
                _adresseInfosVin['asset_type'] = str( _infoVin['scriptPubKey']['type'])
                
                
                
            
            else:
                
                _detailsDatas.append({
                        "account" :'',
                       "address" : _ad, 
                       "category" :'send' ,
                       "amount" : _infoVin['value'],
                    })    
            
            
            #
            #using multiple vin from the same address
            if  _AddressesInInfos.__contains__(_ad):
                _oldAmount = float(_AddressesInInfos[_ad]['amount'])
                _additionalAmount= float(_adresseInfosVin['amount'])
                
                _adresseInfosVin['amount'] = str(_oldAmount+_additionalAmount)
              
            _AddressesInInfos[_ad]   = _adresseInfosVin
              
              
              
                
                
        for _vout in txInDatas['vout']:
            _totalOut = _totalOut + _vout['value']
            _ad=''
            
            _adresseInfosVout = {
                'asset':'RVN',
                'amount':_vout['value']
                }
            
            if _vout['scriptPubKey'].__contains__('addresses'):
                for _ad in _vout['scriptPubKey']['addresses']:
                    
                    #_AddressesInInfos.append({_ad:_vout['value']})
                    
                    
                    if _ad in addressesPOV:
                        _addressPovOut = _addressPovOut + _vout['value']
                    else:
                        _AddressesOut.append(_ad)
            
            
            _types.append( _vout['scriptPubKey']['type'] )
            
            
            
            _more = ''
            if _vout['scriptPubKey'].__contains__('asset'):
                
                _containsAsset = True
                _more = '' + str(_vout['scriptPubKey']['asset']['amount']) + ' ' + str(_vout['scriptPubKey']['asset']['name']) 
                
                
                
                _adresseInfosVout['asset'] = str(_vout['scriptPubKey']['asset']['name'])
                _adresseInfosVout['amount'] = str(_vout['scriptPubKey']['asset']['amount'])
                _adresseInfosVout['asset_type'] = str( _vout['scriptPubKey']['type'])
                
                
                
                _AssetDetailsDatas.append({
                    "account" :'',
                   "address" : _ad, 
                   "destination" : _ad, 
                   "category" :'receive' ,
                   "amount" : _vout['scriptPubKey']['asset']['amount'],
                   "asset_type" :  _vout['scriptPubKey']['type'] ,
                    "asset_name" :  _vout['scriptPubKey']['asset']['name'] 
                }) 
            
            
            else:
                #this is a raven tx
                _detailsDatas.append({
                    "account" :'',
                   "address" : _ad, 
                   "category" :'receive' ,
                   "amount" : _vout['value']

                })
            
            
            
            if  _AddressesOutInfos.__contains__(_ad):
                _oldAmount = float(_AddressesOutInfos[_ad]['amount'])
                _additionalAmount= float(_adresseInfosVout['amount'])
                
                _adresseInfosVout['amount'] = str(_oldAmount+_additionalAmount)
              
            #_AddressesInInfos[_ad]   = _adresseInfosVin
                
            _AssetsVouts.append(_more)    
            _AddressesOutInfos[_ad] = _adresseInfosVout
        
        
        #
        # 2 Interpretations
        #
        
        txDatas['addresses_out'] = _AddressesOut
        txDatas['addresses_in'] = _AddressesIn
        #txDatas['address'] = list(dict.fromkeys(_AddressesIn + _AddressesOut))#set(_AddressesIn +_AddressesOut)
        
        '''
        _srcTextResume = str(_AddressesIn)
        _trgTextResume = str(_AddressesOut)
        if len(_AddressesIn) > 2:
            _srcTextResume = '[*]'
        if len(_AddressesOut) > 2:
            _trgTextResume = '[*]'
        txDatas['address'] = _srcTextResume +' => '+ _trgTextResume
        '''
        
        
        
            
        _povIncount = 0
        _povOutcount = 0
            
        for _ad in addressesPOV:
            if _ad in _AddressesInInfos:
                _povIncount = _povIncount+1
                    
        
        _resumeTx = ''
        txDatas['amount'] = 0.0
        
                    
        if  _povIncount == 0 :
            txDatas['category'] = 'receive'
            
            _countReceive = 0
            _resumeTx = "Transaction from " + str(_AddressesIn)
            
            _am = 0.0
            for _ad in addressesPOV:
                if _AddressesOutInfos.__contains__(_ad):
                    _receivedInfosPOV =  _AddressesOutInfos[_ad]
                    _am = _am + float(_receivedInfosPOV['amount'])
            txDatas['amount'] = _am
            
            '''
            for _ad in addressesPOV:
                _receivedInfosPOV =  _AddressesOutInfos[_ad]
                
                if _countReceive>0:
                    _resumeTx = _resumeTx + ' , '
                
                _resumeTx = _resumeTx + ''+ str(_receivedInfosPOV['amount']) + ' ' + str(_receivedInfosPOV['asset'])
                _countReceive = _countReceive+1
            '''
            
            
        else:
            txDatas['category'] = 'send'
            _resumeTx = "Transaction to " + str(_AddressesOut)    
            if len(_AddressesOut) > 10:
                _resumeTx = "Transaction to " + str(len(_AddressesOut)) + " Addresses"   
                #address  --> IN and OUT
                
            _am = 0.0
            for _ad in addressesPOV:
                if _AddressesInInfos.__contains__(_ad):
                    _sentInfosPOV =  _AddressesInInfos[_ad]
                    _am = _am + float(_sentInfosPOV['amount'])
            txDatas['amount'] = _am
            #address
        
        txDatas['address'] = _resumeTx
        txDatas['types'] = _types     
        
        txDatas['asset_transfered'] = _containsAsset  
        if _containsAsset:
            txDatas['asset_summary'] = _AssetsVouts  
            
        
        
        
        #Fake Resume
        #
        txResultDatas = txInDatas
        
        
        
        
        
        #
        # to standardize ?
        #
        
        txResultDatas['category'] = txDatas['category']
        txResultDatas['amount'] = txDatas['amount']
        txResultDatas['address'] = txDatas['address']
        
        txResultDatas['addresses_in'] = txDatas['addresses_in']
        txResultDatas['addresses_out'] = txDatas['addresses_out']
        
        txResultDatas['addresses_in_details'] = _AddressesInInfos
        txResultDatas['addresses_out_details'] = _AddressesOutInfos
        
        
        #
        # Mapped
        #
        
        
        txResultDatas['details'] = _detailsDatas  
        if _containsAsset:  
            txResultDatas['asset_details'] = _AssetDetailsDatas
        
        #self.logger.info(f"Analyze done.")
        #self.logger.info(f"Analyze done : {txResultDatas}")
            
        return txResultDatas
    
    
    
    def GetRawTransaction(self, txid, decoded=True, addressesPOV=[] , inspect=False):
        _result = None
        
        if True:
        #try:
            datasRes = self.RPCconnexion.getrawtransaction(txid, decoded)
            #print(datasRes)
            if datasRes['result'] != None:
                _result = datasRes['result']
                
                
                if decoded:
                    _hex = _result['hex']
                    #self.logger.info(f"GetRawTransaction() try to decode {_hex}.")    
                    
                    _dataDecode  = self.DecodeTransaction(_hex)
                    if _dataDecode != None:
                        _result = _dataDecode
                        
                        if inspect:
                            _result = self.InspectTransaction(_result, addressesPOV)
            
                        _result['blocktime'] = datasRes['result']['blocktime']
                        _result['time'] = datasRes['result']['blocktime']
                        _result['hex'] = _hex
                        _result['confirmations'] = datasRes['result']['confirmations']
                        _result['blockhash'] = datasRes['result']['blockhash']
            
                    else:
                        self.logger.error(f"GetRawTransaction() _dataDecode none.")    
                
            
        #except Exception as e:
            #self.logger.error(f"GetRawTransaction() ERROR {e}.") 
    
        return _result
    
    
    
    
    def GetAndScanRawTransaction(self, txid,addressesArray,cleanData = False , cleanDetails = False, cleanInOutsDetails=False):
        
        _txDatas = self.GetRawTransaction(txid ,True,  addressesArray)       
        _txDatas = self.InspectTransaction(_txDatas, addressesArray)
        _txDatas['datetime'] = dt.fromtimestamp(_txDatas['blocktime']).strftime('%Y-%m-%d %H:%M:%S')    
          
        if not _txDatas.__contains__('fee'):
            _txDatas['fee'] = 0.0
                
        if not _txDatas.__contains__('address'):
            _txDatas['address'] = addressesArray
                
                
        if not _txDatas.__contains__('category'):
            _txDatas['category'] = "Unknown"  
                    
                      
        if not _txDatas.__contains__('amount'):
            _txDatas['amount'] = 0.0   
        
        
        if cleanData:
            _txDatas['hex']=''
            _txDatas['vin']=''
            _txDatas['vout']=''
        
        if cleanDetails:
            _txDatas['details']=[]
            _txDatas['asset_details']=[]
        
        
        if cleanInOutsDetails:
            _txDatas['addresses_out']=[]
            _txDatas['addresses_in']=[]
            
            _txDatas['addresses_in_details']={}
            _txDatas['addresses_out_details']={}
        
        
        
        return _txDatas
    
    
    def GetTransaction(self, txid, addressesPOV=[] ):
        _result = None
        #self.logger.info(f"GetTransaction().") 
        try:
            datasRes = self.RPCconnexion.gettransaction(txid)
            #self.logger.info(f"GetTransaction() {datasRes}.") 
            if datasRes['result'] != None:
                _result = datasRes['result']
                return _result
            else:
                if    datasRes['error']['message'] == 'Invalid or non-wallet transaction id':
                    #self.logger.info(f"GetRawTransaction().") 
                    _result = self.GetRawTransaction(txid, True, addressesPOV)
                    return _result
                
                
                
        except Exception as e:
            self.logger.error(f"GetTransaction() ERROR {e}.") 
    
        return _result
    
    
    
    def DecodeTransaction(self, raw):
        _result = None
        
        try:
            datasRes = self.RPCconnexion.decoderawtransaction(raw)
            
            #self.logger.info(f"DecodeTransaction() {datasRes}.") 
            if datasRes['result'] != None:
                _result = datasRes['result']
            
        except Exception as e:
            self.logger.error(f"DecodeTransaction() ERROR {e}.") 
    
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
        