'''
Created on 8 janv. 2022

@author: slinux
'''
import requests
from libs.RVNpyRPC import RVNpyRPC


from ._atomicSwapTradeAndTransactions import SwapTrade

import urllib, json
#from jsonrpcclient.requests import Request
from requests import post, get
from decimal import *
from ast import literal_eval

import ast

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
    
        
    
    def CleanAndCast(self):
        self._adAssetQt = float(self._adAssetQt)
        self._adPrice = float(self._adPrice)
    
    
    def isEmptyTxData(self):
        _empty=True 
        if self._adTxDatas != None: 
            if self._adTxDatas != {}: 
                _empty=False
                
        return _empty
        
    def __repr__(self, *args, **kwargs):
        return str(self.JSON())
        
            
    def GetType(self):      
        return  _P2PMARKET_ADTYPES_[self._adType] 
    
    
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
                
            
                }    
    
    
    
    def SetAddress(self, ad):
        self._adAddress = ad
    
    def Load_JSON(self, jsonData):
        print(f"{type(jsonData)}")
        print(f"{jsonData}")
        if True:
            if str(type(jsonData)) == "<class 'str'>":
                jsonData = ast.literal_eval(jsonData)
                print(f"{type(jsonData)}")
            #    parsed_data = jsonData.replace("'", '"')
            #    jsonData = json.loads(parsed_data)
        
            #jsonData = ast.literal_eval(json.dumps(jsonData))
        
            #if not jsonData.__contains__('price_asset'):
            #    jsonData['price_asset'] = 'RVN'
            #if not jsonData.__contains__('orders'):
            #    jsonData['orders'] = 0
            
            #print(jsonData[0])
            
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
            
            print(f"OK {jsonData}")

    
class RVNpyRPC_P2P_Marketplace():
    '''
    classdocs
    '''
    RPCconnexion = None
    
    SQUAWKER_PROTOCOLE_MARKET_LISTING_AMMOUNT = 0.2
    SQUAWKER_PROTOCOLE_MARKET_LISTING_SATOSHIS = 20000000
    
    def __init__(self,connexion, parent:RVNpyRPC):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent
        
    
    
        
        
        
    def PublishNewP2PAd(self, ChannelAsset, Destination, P2PAdFileHash, ChangeAddress, expiration=200000000 ):
        #transfer "asset_name" qty "to_address" "message" expire_time "change_address" "asset_change_address"
        
        if Destination != "":
            self.RPCconnexion.transfer(ChannelAsset, self.SQUAWKER_PROTOCOLE_MARKET_LISTING_AMMOUNT, Destination,P2PAdFileHash, expiration, ChangeAddress,ChangeAddress )
        else :
            print( "destination must be non empty")


    
    
    def CreateAtomicSwapTransaction(self, marketAd:RavencoinP2PMarketPlaceAd, pw=''):
        marketAd._adTxDatas = None 
        
        #self.RVNpyRPC.atomicswap.CreateAtomicBuy(self, total_price, asset_name,quantity , order_count=1, destination='', pw=''):
        #self.RVNpyRPC.atomicswap.CreateAtomicSell(self, total_price, asset_name,quantity , order_count=1, destination='', pw=''):
        #self.RVNpyRPC.atomicswap.CreateAtomicSwap(self, own_asset_name, own_quantity, want_asset_name,want_quantity, order_count, destination, pw=''):
        #_atomicSwapTrade:SwapTrade
        #_atomicSwapTrade = None
        _atomicSwapTrade = {}
        
        marketAd.CleanAndCast()
        
        if marketAd._adType == 1:
            print(f"CreateAtomicBuy( {marketAd._adPrice}  , {marketAd._adAsset}, {marketAd._adAssetQt} , {marketAd._adOrders}, '', pw=pw)")
            _atomicSwapTrade = self.RVNpyRPC.atomicswap.CreateAtomicBuy( marketAd._adPrice, marketAd._adAsset,marketAd._adAssetQt , marketAd._adOrders, destination='', pw=pw)
        elif marketAd._adType == 0:
            print(f"CreateAtomicSell( {marketAd._adPrice},{ marketAd._adAsset} , {marketAd._adAssetQt} , {marketAd._adOrders}, destination='', pw=pw)")
            
            _atomicSwapTrade = self.RVNpyRPC.atomicswap.CreateAtomicSell(marketAd._adPrice,marketAd._adAsset,  marketAd._adAssetQt, marketAd._adOrders, destination='', pw=pw)
        elif  marketAd._adType == 2:    
            print(f"CreateAtomicSwap( {marketAd._adAsset}, {marketAd._adAssetQt}, {marketAd._adPriceAsset}, {marketAd._adPrice}, {marketAd._adOrders}, destination='', pw=pw)")
             
            _atomicSwapTrade = self.RVNpyRPC.atomicswap.CreateAtomicSwap( marketAd._adAsset, marketAd._adAssetQt, marketAd._adPriceAsset,marketAd._adPrice, marketAd._adOrders, destination='', pw=pw)
        else:
            print(f'unknown type {marketAd._adType}')
    
        #if _txGenerateResult
        #if _atomicSwapTrade != None:
        #    pass
        
        print(f'Returning the SWAP {_atomicSwapTrade}')
        
        
        marketAd._adTxDatas = _atomicSwapTrade
        
        return marketAd
    
    
    

    
    def __Load_IPFS_Message__(self, _hash , ipfs_gateway="https://ravencoinipfs-gateway.com/ipfs/"):
        print(f"loading JSONA {_hash}...")
        url = ipfs_gateway+_hash
        print(f"loading url {url}...")
        
        try:
            r = requests.get(url, timeout=4)
        except Exception as e:
            return None
        
        print(f" R {r}...")
       
        _parsed=False
        _result = None
        if r.status_code == 200:
            _result = r.content
        
            try:
                _result = r.json()
                _parsed = True
            except Exception as e:
                print("error parsing JSON ")
            
            if not _parsed or str(type(_result)) == "<class 'str'>":
                print("2nd parsing JSON ")
                try:
                    new_str = _result.decode('utf-8')
                    _result = json.loads(new_str)
                    #my_json = r.content.decode('utf8').replace("'", '"')
                    #data = literal_eval(r.content.decode('utf8'))
                    #_resultI = json.dumps(data, indent=4, sort_keys=True)
                    #_result = json.loads(_resultI)
                except Exception as e:
                    print("error parsing DICT ")    
                    
            
            #d=r.json()
            print(f"JSON DATA {type(_result)} = {_result} ")
        return _result
    
    
    
    def VerifyMarketplaceAdTxDatas(self, marketplaceAd:RavencoinP2PMarketPlaceAd):
        
        _atLeastOneValid = False
        if marketplaceAd._adTxDatas != None:
            for _order in marketplaceAd._adTxDatas:
                _orderTx = marketplaceAd._adTxDatas[_order]
                
                isValid, Datas = self.RVNpyRPC.atomicswap.GetAtomicSwap(_orderTx)
                if isValid :
                    _atLeastOneValid = True
            
        return _atLeastOneValid
    
    
    
    def GetP2PMarketAdsIPFSListingDatas(self,asset="WXRAVEN/P2P_MARKETPLACE", count=100 , ipfs_gateway="https://ravencoinipfs-gateway.com/ipfs/", blacklist=[], includeNoneTxDatas=False, verifyTx=False, whitelist=[]):
        
        print("GetP2PMarketAdsIPFSListingDatas")
        #
        #
        # Retrieve raw datas with filters blacklist / whitelist
        #
        _RawListing = self.GetP2PMarketAdsRawListing(asset=asset, count=count, blacklist=blacklist, whitelist=whitelist)
        print(f"RAW={_RawListing}")
        _MarketList = {}
        _cursor = 0
        
        for item in _RawListing:
            _origin = item['address']
            _hasMessage = item.__contains__('message')
            
            if _hasMessage :
                
                #
                # Load IPFS datas
                #                
                _listingElem = self.__Load_IPFS_Message__(item['message'],ipfs_gateway)
                if _listingElem==None:
                    continue
                
                #print(_listingElem)
                #print(f"Creating elem from {_listingElem}")
                #convertedData = json.loads(_listingElem)
                
                
                
                #
                # To verify how safe it works !!!
                #
                res= _listingElem
                try:
                    res = ast.literal_eval(_listingElem.decode('utf-8'))
                except Exception as e:
                    print("error last clean")    
                    
                    
                
                
                    
                _newAd = RavencoinP2PMarketPlaceAd()
                print("loading JSON datas to obj")
                _newAd.Load_JSON(res)
                print("Set add")
                _newAd.SetAddress(_origin[0])
                
                
                
                
                if _newAd.isEmptyTxData() and not includeNoneTxDatas:
                    print("Filtering ad, no tx datas found")
                    continue
                
                
                
                
                
                if verifyTx:
                    _valid = self.VerifyMarketplaceAdTxDatas(_newAd)
                    
                    if not _valid:
                        print("Filtering ad, no valid tx datas found")
                        continue
                
                
                
                
                
                
                print("Set add in market")
                _MarketList[_cursor] = _newAd
                _cursor = _cursor+1
                
                
        return   _MarketList      
    
    
    
    
    def GetP2PMarketAdsRawListing(self, asset="WXRAVEN/P2P_MARKETPLACE", count=100, msgType = 20000000, blacklist=[] ,whitelist=[]):
        
        latest = []
        messages = dict()
        messages["addresses"] = list(self.RPCconnexion.listaddressesbyasset(asset, False)["result"])
        messages["assetName"] = asset
        deltas = self.RPCconnexion.getaddressdeltas(messages)["result"]
        #print(f"deltas {deltas}")
        if deltas != None:
            for tx in deltas:
                
                print(tx)
                
                
                #
                #
                # Check blacklist
                #
                if blacklist.__contains__(tx["address"]):
                    print(f"blacklist {tx}")
                    continue
                
                
                #
                #
                # Check whitelist
                #
                #
                if len(whitelist) > 0:
                    if not whitelist.__contains__(tx["address"]):
                        print(f"not whitelist {tx}")
                        continue
                
                
                
                _matchType = (tx["satoshis"] == msgType)
                _matchSelf = self.tx_to_self(tx, size=0.2)
                
                
                print(f"_matchType {_matchType}")
                print(f"_matchSelf {_matchSelf}")
                
                
                if _matchType and _matchSelf==1 : #and self.tx_to_self(tx, size=0.2):
                    transaction = self.RPCconnexion.decoderawtransaction(self.RPCconnexion.getrawtransaction(tx["txid"])["result"])["result"]
                    for vout in transaction["vout"]:
                        vout = vout["scriptPubKey"]
                        if vout["type"] == "transfer_asset" and vout["asset"]["name"] == asset and vout["asset"]["amount"] == 0.2:
                            kaw = {"address": vout["addresses"], "message": vout["asset"]["message"], "block": transaction["locktime"]}
                            latest.append(kaw)
                else:
                    print(f"excluded {tx}")
            _data = []
            
            if len(latest)>1:
                try:
                    _data = sorted(latest[:count], key=lambda message: message["block"], reverse=True)
                except Exception as e:
                    print("error sorted GetP2PMarketAdsRawListing") 
            else:
                _data =  latest
                
                
                
            return _data
        return None








    def tx_to_self(self, tx, size=0.2):
        print(f"tx_to_self {size}")
        messages = dict()
        messages["addresses"] = [tx["address"]]
        messages["assetName"] = tx["assetName"]
        deltas = self.RPCconnexion.getaddressdeltas(messages)["result"]
        neg_delta = [(a["satoshis"], a["address"]) for a in deltas if a["txid"] == tx["txid"] and a["satoshis"] < -((size * 100000000)-1)]
        print(f"neg_delta {neg_delta}")
        return len(neg_delta)
    
    
    
    




 
            
                