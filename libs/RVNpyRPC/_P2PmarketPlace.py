'''
Created on 8 janv. 2022

@author: slinux
'''
import requests
from libs.RVNpyRPC import RVNpyRPC


from ._atomicSwapTradeAndTransactions import SwapTrade
import logging
import urllib, json
#from jsonrpcclient.requests import Request
from requests import post, get
from decimal import *
from ast import literal_eval
import pickle
import ast


import os

_P2PMARKET_ADTYPES_ = {
    0:'Sell',
    1:'Buy',
    2:'Trade'
    }


_P2PMARKET_TXTYPES_ = {
    0:'Atomic Swap',
    1:'P2SH',
    }

_P2PMARKET_ID_ = {
    'Atomic Swap':0,
    'P2SH':1,
    }

class RavencoinP2PMarketPlaceAd(object):
    '''
    classdocs
    '''


    _adType = 0
    _adAddress = None
    _adTitle = None
    _adAsset = None
    _adAssetQt = None
    _adPrice = None
    _adExternalLink = None
    _adDescription = None
    _adKeywords = None
    _adPriceAsset = "RVN"
    _adTxType = None
    _adTxDatas = None
    _adOrders = 1
    _adP2PChannelAsset = None
    
    
    _SquawkerProtocolVersion='0.1'
    
    def __init__(self):
        '''
        Constructor
        '''
        self._adType = ""
        self._adAddress = ""
        self._adTxType = ""
        self._adTxDatas = {}
        self._adTitle = ""
        self._adAsset = ""
        self._adAssetQt = ""
        self._adPrice = ""
        self._adPriceAsset = "rvn"
        self._adOrders = 1
        self._adExternalLink = ""
        self._adDescription = ""
        self._adKeywords = ""
        self._adP2PChannelAsset = ""
        
        self.logger = logging.getLogger('wxRaven')
    
        
    
    def CleanAndCast(self):
        self._adAssetQt = float(self._adAssetQt)
        self._adPrice = float(self._adPrice)
    
    
    def __rebuildListIndex__(self):
        newlist = {}
        cursor = 0
        for key in self._adTxDatas:
            _d =  self._adTxDatas[key]
            newlist[cursor] = _d
            cursor = cursor +1
            
        self._adTxDatas=newlist
    
    def isEmptyTxData(self):
        _empty=True 
        if self._adTxDatas != None: 
            if self._adTxDatas != {}: 
                _empty=False
                
        return _empty
        
    def __repr__(self, *args, **kwargs):
        return str(self.JSON())
        
    
    def GetAvailableOrders(self):
        return len(self._adTxDatas)
            
    def GetType(self):      
        return  _P2PMARKET_ADTYPES_[self._adType] 
    
    def GetProtocolVersion(self):
        return self._SquawkerProtocolVersion
    
    def GetMethod(self):      
        return  _P2PMARKET_TXTYPES_[self._adTxType] 
            
    def JSON(self):
        
        return {
                'address':self._adAddress,
                'type':self._adType,
                'txType':self._adTxType,
                'txDatas':self._adTxDatas,
                'title':self._adTitle,
                'asset':self._adAsset,
                'qt':self._adAssetQt,
                'orders':self._adOrders,
                'price':self._adPrice,
                'price_asset':self._adPriceAsset,
                'link':self._adExternalLink,
                'desc':self._adDescription,
                'keywords':self._adKeywords,
                'channel':self._adP2PChannelAsset,
                'sqp2p_ver':self._SquawkerProtocolVersion
            
                }    
    
    
    
    def SetAddress(self, ad):
        self._adAddress = ad
    
    def Load_JSON(self, jsonData):
        #self.logger.info(f"{type(jsonData)}")
        #self.logger.info(f"{jsonData}")
        try:
        #if True:
            if str(type(jsonData)) == "<class 'str'>":
                jsonData = ast.literal_eval(jsonData)
                #self.logger.info(f"{type(jsonData)}")
            #    parsed_data = jsonData.replace("'", '"')
            #    jsonData = json.loads(parsed_data)
        
            #jsonData = ast.literal_eval(json.dumps(jsonData))
        
            #if not jsonData.__contains__('price_asset'):
            #    jsonData['price_asset'] = 'RVN'
            #if not jsonData.__contains__('orders'):
            #    jsonData['orders'] = 0
            
            #self.logger.info(jsonData[0])
            
            self._adType = jsonData['type'] if jsonData.__contains__('type') else 0
            self._adTxType = jsonData['txType']
            self._adTxDatas = jsonData['txDatas']
            self._adTitle = jsonData['title']
            self._adAsset = jsonData['asset']
            self._adAssetQt = jsonData['qt']
            self._adOrders = jsonData['orders'] if jsonData.__contains__('orders') else 0
            self._adPrice = jsonData['price']
            self._adPriceAsset =  jsonData['price_asset'] if jsonData.__contains__('price_asset') else 'RVN'
            self._adExternalLink = jsonData['link']
            self._adDescription = jsonData['desc']
            self._adKeywords = jsonData['keywords']
            self._adP2PChannelAsset = jsonData['channel']
            
            self._SquawkerProtocolVersion = jsonData['sqp2p_ver'] if jsonData.__contains__('sqp2p_ver') else '0.0'
            return True
        except Exception as e:
            self.logger.error(f"Invalid JSON Data.")  
            return False   
            
            #self.logger.info(f"OK {jsonData}")

    
class RVNpyRPC_P2P_Marketplace():
    '''
    classdocs
    '''
    RPCconnexion = None
    
    ANNOUNCER_MARKET_LISTING_MIN_AMMOUNT = 5
    SQUAWKER_PROTOCOLE_MARKET_LISTING_AMMOUNT = 0.2
    SQUAWKER_PROTOCOLE_MARKET_LISTING_SATOSHIS = 20000000
    
    
    __INVALID__CACHE__ = {}
    
    def __init__(self,connexion, parent:RVNpyRPC):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent
        self.logger = logging.getLogger('wxRaven')
        
        self.__userdata_path__ = self.RVNpyRPC.__userdata_path__
        self.__INVALID__CACHE__ = []
        
    
    
    """
    
    Var Saving management (for the view persistence)
    
    """
    
    def __saveCache__(self):
        try:
            self.logger.info("P2P Marketplace Saving invalid cache file")
            print(self.__INVALID__CACHE__ )
            pickle.dump( self.__INVALID__CACHE__ , open(self.__userdata_path__+"/marketplace_invalid_cache.p", "wb" ) )
        except Exception as e:
            self.logger.info(e) 
    
    def __LoadCache__(self):
        result = []
        try:
            self.logger.info("P2P Marketplace Loading invalid cache file")
            self.__INVALID__CACHE__  = pickle.load( open( self.__userdata_path__+"/marketplace_invalid_cache.p", "rb" ) )
        except Exception as e:
            self.logger.info(e) 
        
        return result
    
    
    
    
    """
    
    Lib start
    
    """
    
    
    
    def GetAllAdsInCache(self):
        
        cached_ads_list = {}
        count = 0
        
        _ads_path = self.__userdata_path__+"/p2pmarket/"
        
        for filename in os.listdir(_ads_path):
            f = os.path.join(_ads_path, filename)
            # checking if it is a file
            
            _nameAndExt = str(filename).split('.')
            if os.path.isfile(f):
                if _nameAndExt[1] == 'json':
                    f = open(f, "r")
                    datas =f.read()
                    
                    _cached_ad = RavencoinP2PMarketPlaceAd()
                    if _cached_ad.Load_JSON(datas):
                        cached_ads_list[count] = _cached_ad
                        count = count+1
                        
                        
        return cached_ads_list
    
    def LoadInvalidCache(self):
        pass
    
    
    def CheckP2PAnnouncerAccount(self, AnnouncerAddress, AnnouncerChannel, setupIfNotReady=False , password=""):
        addressBalance = self.RVNpyRPC.wallet.getaddressbalance(walletAdress=AnnouncerAddress, showAsset=True)['result']
        
        _assetChannelPresent = False 
        _suffisiantFund = False 
        
        _valid=False
        
        
        for _itemBal in addressBalance:
            if _itemBal['assetName'] == AnnouncerChannel:
                if _itemBal['balance'] >= self.SQUAWKER_PROTOCOLE_MARKET_LISTING_SATOSHIS:
                    _assetChannelPresent = True
                    
                
        
            if _itemBal['assetName'] == "RVN":
                if _itemBal['balance'] >= self.ANNOUNCER_MARKET_LISTING_MIN_AMMOUNT:
                    _suffisiantFund = True
        
        
        if not _suffisiantFund or not _assetChannelPresent:
            _valid = False
        else:
            _valid = True
        
        self.logger.info(f"_suffisiantFund = {_suffisiantFund}")
        self.logger.info(f"_assetChannelPresent = {_assetChannelPresent}")
            
            
        if not _valid and setupIfNotReady:
            self.logger.info("Account not completely setup for p2pmarket, trying now.")
            if not _suffisiantFund:
                self.RVNpyRPC.wallet.sendRVN( AnnouncerAddress, 5, fromAd="", pwd=password)
                
                
            if not _assetChannelPresent:
                self.RVNpyRPC.wallet.sendAsset(AnnouncerChannel, AnnouncerAddress, 1, password)
            
            
            _valid = True
            
        return _valid
            
        
    def PublishNewP2PAd(self, ChannelAsset, Destination, P2PAdFileHash, ChangeAddress, expiration=200000000 ):
        #transfer "asset_name" qty "to_address" "message" expire_time "change_address" "asset_change_address"
        
        if Destination != "":
            #ravencoin.p2pmarket.PublishNewP2PAd(self._newAdObject._adP2PChannelAsset, p2p_channel_asset_target_address, _hashFile, p2p_market_change_address, expiration=200000000 )
            #self.RPCconnexion.transfer(ChannelAsset, self.SQUAWKER_PROTOCOLE_MARKET_LISTING_AMMOUNT, Destination,P2PAdFileHash, expiration, ChangeAddress,ChangeAddress )
            return self.RPCconnexion.transferfromaddress(ChannelAsset,Destination, self.SQUAWKER_PROTOCOLE_MARKET_LISTING_AMMOUNT, Destination, P2PAdFileHash,expiration, ChangeAddress,ChangeAddress)
        
        
        else :
            self.logger.info( "destination must be non empty")
            return None


    
    
    
    
    
    def CreateAtomicSwapTransaction(self, marketAd:RavencoinP2PMarketPlaceAd, pw=''):
        marketAd._adTxDatas = None 
        
        #self.RVNpyRPC.atomicswap.CreateAtomicBuy(self, total_price, asset_name,quantity , order_count=1, destination='', pw=''):
        #self.RVNpyRPC.atomicswap.CreateAtomicSell(self, total_price, asset_name,quantity , order_count=1, destination='', pw=''):
        #self.RVNpyRPC.atomicswap.CreateAtomicSwap(self, own_asset_name, own_quantity, want_asset_name,want_quantity, order_count, destination, pw=''):
        #_atomicSwapTrade:SwapTrade
        #_atomicSwapTrade = None
        _atomicSwapTrade = {}
        
        marketAd.CleanAndCast()
        
        #try:
        if True:
        
            if marketAd._adType == 1:
                self.logger.info(f"CreateAtomicBuy( {marketAd._adPrice}  , {marketAd._adPriceAsset}, {marketAd._adAssetQt} , {marketAd._adOrders}, '', pw=pw)")
                _atomicSwapTrade = self.RVNpyRPC.atomicswap.CreateAtomicBuy( marketAd._adPrice, marketAd._adPriceAsset,marketAd._adAssetQt , marketAd._adOrders, destination='', pw=pw)
            elif marketAd._adType == 0:
                self.logger.info(f"CreateAtomicSell( {marketAd._adPrice},{ marketAd._adAsset} , {marketAd._adAssetQt} , {marketAd._adOrders}, destination='', pw=pw)")
                
                _atomicSwapTrade = self.RVNpyRPC.atomicswap.CreateAtomicSell(marketAd._adPrice,marketAd._adAsset,  marketAd._adAssetQt, marketAd._adOrders, destination='', pw=pw)
            elif  marketAd._adType == 2:    
                self.logger.info(f"CreateAtomicSwap( {marketAd._adAsset}, {marketAd._adAssetQt}, {marketAd._adPriceAsset}, {marketAd._adPrice}, {marketAd._adOrders}, destination='', pw=pw)")
                 
                _atomicSwapTrade = self.RVNpyRPC.atomicswap.CreateAtomicSwap( marketAd._adAsset, marketAd._adAssetQt, marketAd._adPriceAsset,marketAd._adPrice, marketAd._adOrders, destination='', pw=pw)
            else:
                self.logger.info(f'unknown type {marketAd._adType}')
    
        #except Exception as e:
        #    self.logger.error(f'CreateAtomicSwapTransaction ERROR : {e}')
    
    
        #if _txGenerateResult
        #if _atomicSwapTrade != None:
        #    pass
        
        self.logger.info(f'Returning the SWAP {_atomicSwapTrade}')
        
        
        marketAd._adTxDatas = _atomicSwapTrade
        
        return marketAd
    
    
    

    
    def __Load_IPFS_Message__(self, _hash , ipfs_gateway="https://ravencoinipfs-gateway.com/ipfs/"):
        
        #print(ipfs_gateway)
        #print(_hash)
        
        #self.logger.info(f"loading JSONA {_hash}...")
        url = ipfs_gateway+_hash
        self.logger.info(f"loading url {url}...")
        
        try:
            r = requests.get(url, timeout=4)
        except Exception as e:
            return None
        
        #self.logger.info(f" R {r}...")
       
        _parsed=False
        _result = None
        if r.status_code == 200:
            _result = r.content
        
            try:
                _result = r.json()
                _parsed = True
            except Exception as e:
                pass
                #self.logger.error("error parsing JSON ")
            
            if not _parsed or str(type(_result)) == "<class 'str'>":
                #self.logger.info("2nd parsing JSON ")
                try:
                    new_str = _result.decode('utf-8')
                    _result = json.loads(new_str)
                    _parsed = True
                    #my_json = r.content.decode('utf8').replace("'", '"')
                    #data = literal_eval(r.content.decode('utf8'))
                    #_resultI = json.dumps(data, indent=4, sort_keys=True)
                    #_result = json.loads(_resultI)
                except Exception as e:
                    pass
                    #self.logger.error("error parsing DICT ")    
                    
            
            #d=r.json()
            #self.logger.info(f"JSON DATA {type(_result)} = {_result} ")
        if not   _parsed:
            self.logger.error("error parsing datas ")  
            
        
        return _result
    
    
    
    
    
    def VerifyMarketplaceAdTxDatas(self, marketplaceAd:RavencoinP2PMarketPlaceAd, clearList=True, _skipWhenValidCountReached=10):
        
        
      
        _iList=[]
        _atLeastOneValid = False
        _scanValidCount = 0
        if marketplaceAd._adTxDatas != None:
            for _order in marketplaceAd._adTxDatas:
                _orderTx = marketplaceAd._adTxDatas[_order]
                  
                
                isValid, Datas = self.RVNpyRPC.atomicswap.GetAtomicSwap(_orderTx)
                if isValid :
                    _atLeastOneValid = True
                    
                    
                    if _scanValidCount > _skipWhenValidCountReached:
                        break
                    
                    _scanValidCount = _scanValidCount+1
                    
                if not isValid:
                    _iList.append(_order)
        
        _hasInvalid=False
        if clearList:
            for i in _iList:
                _hasInvalid=True
                marketplaceAd._adTxDatas.pop(i)
        
        if _hasInvalid:
            marketplaceAd.__rebuildListIndex__()       
            
        return _atLeastOneValid
    
    
    
    def GetP2PMarketAdsIPFSListingDatas(self,asset="WXRAVEN/P2P_MARKETPLACE", count=100 , ipfs_gateway="https://ravencoinipfs-gateway.com/ipfs/", blacklist=[], includeNoneTxDatas=False, verifyTx=False, whitelist=[], _fallbackIpfsGateways=[]):
        
        
        self.__LoadCache__()
        
        
        self.logger.info("GetP2PMarketAdsIPFSListingDatas")
        #
        #
        # Retrieve raw datas with filters blacklist / whitelist
        #
        _RawListing = self.GetP2PMarketAdsRawListing(asset=asset, count=count, blacklist=blacklist, whitelist=whitelist)
        #self.logger.info(f"RAW={_RawListing}")
        _MarketList = {}
        _cursor = 0
        
        for item in _RawListing:
            
            #self.logger.info(item)
            _origin = item['address']
            _hasMessage = item.__contains__('message')
            #_txId = item["txid"]
            
            
            if _hasMessage :
                
                
                if self.__INVALID__CACHE__.__contains__(item['message']):
                    self.logger.info(f"Known invalid message ; {item['message']}")
                    continue
                
                
                
                
                
                #
                # Load IPFS datas
                #   
                _listingElem = None
                try:            
                    _listingElem = self.__Load_IPFS_Message__(item['message'],ipfs_gateway)
                except Exception as e:
                    #self.logger.error("error __Load_IPFS_Message__")  
                    pass  
                if _listingElem==None:
                    self.__addTxInInvalidCacheIfNotExist__(item['message'])
                    continue
                
                #self.logger.info(_listingElem)
                #self.logger.info(f"Creating elem from {_listingElem}")
                #convertedData = json.loads(_listingElem)
                
                
                
                #
                # To verify how safe it works !!!
                #
                res= _listingElem
                try:
                    res = ast.literal_eval(_listingElem.decode('utf-8'))
                except Exception as e:
                    self.logger.error("error last clean")    
                    
                    
                
                
                    
                _newAd = RavencoinP2PMarketPlaceAd()
                #self.logger.info("loading JSON datas to obj")
                _newAd.Load_JSON(res)
                #self.logger.info("Set add")
                _newAd.SetAddress(_origin[0])
                
                
                
                
                if _newAd.isEmptyTxData() and not includeNoneTxDatas:
                    self.logger.info("Filtering ad, no tx datas found")
                    self.__addTxInInvalidCacheIfNotExist__(item['message'])
                    continue
                
                
                
                
                
                if verifyTx:
                    #self.logger.info(f"verifying {_newAd.JSON()}")
                    _valid = self.VerifyMarketplaceAdTxDatas(_newAd)
                    
                    if not _valid:
                        self.logger.info(f"Filtering ad , no valid tx datas found")
                        self.__addTxInInvalidCacheIfNotExist__(item['message'])
                        continue
                
                
                
                
                
                
                self.logger.info(f"Set add {item['message']} in market")
                _MarketList[_cursor] = _newAd
                _cursor = _cursor+1
                
            else:
                pass
                #self.__addTxInInvalidCacheIfNotExist__
                
        #self.__saveCache__()            
        return   _MarketList      
    
    
    
    
    
    def __addTxInInvalidCacheIfNotExist__(self, txid):
        if not self.__INVALID__CACHE__.__contains__(txid):
            self.__INVALID__CACHE__.append(txid)
            self.logger.info(f"adding  {txid} in invalid cache")
            self.__saveCache__() 
            
            
    
    def GetP2PMarketAdsRawListing(self, asset="WXRAVEN/P2P_MARKETPLACE", count=100, msgType = 20000000, blacklist=[] ,whitelist=[]):
        
        
        #Temp speedup process!
        self.__LoadCache__()
        
        
        latest = []
        messages = dict()
        messages["addresses"] = list(self.RPCconnexion.listaddressesbyasset(asset, False)["result"])
        messages["assetName"] = asset
        deltas = self.RPCconnexion.getaddressdeltas(messages)["result"]
        #self.logger.info(f"deltas {deltas}")
        if deltas != None:
            for tx in deltas:
                
                #self.logger.info(tx)
                
                _txId = tx["txid"]
                
                #
                #
                # Check Cache Invalid
                #
                if self.__INVALID__CACHE__.__contains__(_txId):
                    self.logger.info(f"invalid cache {tx}")
                    continue
                
                
                
                #
                #
                # Check blacklist
                #
                if blacklist.__contains__(tx["address"]):
                    self.logger.info(f"blacklist {tx}")
                    self.__addTxInInvalidCacheIfNotExist__(_txId)
                    continue
                
                
                #
                #
                # Check whitelist
                #
                #
                if len(whitelist) > 0:
                    if not whitelist.__contains__(tx["address"]):
                        self.logger.info(f"not whitelist {tx}")
                        self.__addTxInInvalidCacheIfNotExist__(_txId)
                        continue
                
                
                
                _matchType = (tx["satoshis"] == msgType)
                _matchSelf = self.tx_to_self(tx, size=0.2)
                
                
                #self.logger.info(f"_matchType {_matchType}")
                #self.logger.info(f"_matchSelf {_matchSelf}")
                
                
                if _matchType and _matchSelf==1 : #and self.tx_to_self(tx, size=0.2):
                    transaction = self.RPCconnexion.decoderawtransaction(self.RPCconnexion.getrawtransaction(tx["txid"])["result"])["result"]
                    for vout in transaction["vout"]:
                        vout = vout["scriptPubKey"]
                        if vout["type"] == "transfer_asset" and vout["asset"]["name"] == asset and vout["asset"]["amount"] == 0.2:
                            kaw = {"address": vout["addresses"], "message": vout["asset"]["message"], "block": transaction["locktime"]}
                            latest.append(kaw)
                else:
                    pass
                    #self.logger.info(f"excluded {tx}")
                    #self.__addTxInInvalidCacheIfNotExist__(_txId)
            _data = []
            
            if len(latest)>1:
                try:
                    _data = sorted(latest[:count], key=lambda message: message["block"], reverse=True)
                except Exception as e:
                    self.logger.error("error sorted GetP2PMarketAdsRawListing") 
            else:
                _data =  latest
                
               
                
            return _data
        
        #self.__saveCache__()    
        
        
        return None








    def tx_to_self(self, tx, size=0.2):
        #self.logger.info(f"tx_to_self {size}")
        messages = dict()
        messages["addresses"] = [tx["address"]]
        messages["assetName"] = tx["assetName"]
        deltas = self.RPCconnexion.getaddressdeltas(messages)["result"]
        neg_delta = [(a["satoshis"], a["address"]) for a in deltas if a["txid"] == tx["txid"] and a["satoshis"] < -((size * 100000000)-1)]
        #self.logger.info(f"neg_delta {neg_delta}")
        return len(neg_delta)
    
    
    
    




 
            
                