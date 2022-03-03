'''
Created on 28 févr. 2022

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import *


class Job_TradeHistory(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin, viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        
        
        self.jobName = f"Trade History"
        self.jobId = f"{self.jobName} - {self.parentFrame.ConnexionManager.getCurrent()}"
    
    
    def JobProcess(self):
        #getting market network
        ravencoin = self.plugin.__getNetwork__()
        
        _tx_history_skip_swap = self.plugin.getData("_tx_history_skip_swap")
        _tx_history_skip_ads = self.plugin.getData("_tx_history_skip_ads")
        
        
        _final_datas= {}
        _data_cursor  = 0
        self.setProgress(f'Trade history listing ...')
        try:
        
            #Retreive CACHE
            _trade_cache = ravencoin.atomicswap.GetAtomicSessionCache_Trades()
            self.logger.info(f" {len(_trade_cache)} session trades.")
            
            
            #Retreives ADS
            _ads_cache = ravencoin.p2pmarket.GetAllAdsInCache()
            self.logger.info(f" {len(_ads_cache)} ads cache.")
            
            #CrossCheck and Analyse
            if not _tx_history_skip_swap:
                for _trId in _trade_cache:
                    _trade = _trade_cache[_trId]
                    
                    _trade['cache_type'] = 'SWAP'
                    _trade['description'] = '?'
                    if _trade['type'] == 'buy':
                        _trade['description'] = f"BUYING {_trade['out_quantity']} {_trade['out_type']}"
                    if _trade['type'] == 'sell':
                        _trade['description'] = f"SELLING {_trade['in_quantity']} {_trade['in_type']}"
                    if _trade['type'] == 'trade':
                        _trade['description'] = f"TRADING {_trade['in_quantity']} {_trade['in_type']}  <-> {_trade['out_quantity']} {_trade['out_type']}"
                        
                    
                    
                    
                    _trade['status'] = 'NOT FOUND'
                    _trade['ad'] = None
                    _trade['unresolved'] = 0
                    
                    
                    _found, _matchAd, _id = self.__searchMatchingAdInCache__(_trade, _ads_cache)
                    
                    if _found:
                        _ads_cache.pop(_id, None)
                        _trade['ad'] = _matchAd
                        _trade['status'] = 'WAITING'
                        
                    else:
                        _trade['unresolved'] = 1
                        
                        if len(_trade['executed_utxos']) > 0 :
                            _trade['status'] = 'COMPLETE'
                    
                    
                    
                    
                    
                    _final_datas[_data_cursor] = _trade
                    _data_cursor = _data_cursor+1
            
            
            
            
            self.logger.info(f" {len(_ads_cache)} has not been identified in transactions.")
            
            
            
            if not _tx_history_skip_ads:
                for _ad_cursor in _ads_cache:
                    _ad = _ads_cache[_ad_cursor]
                    
                    
                    _unresolvedTrade = {}
                    _unresolvedTrade['cache_type'] = 'AD'
                    _unresolvedTrade['description'] = _ad._adTitle
                    _unresolvedTrade['type'] = _ad.GetType()
                    if _ad.GetType().lower() == 'buy':
                        _unresolvedTrade['description'] = f"BUYING {_ad._adAssetQt} {_ad._adPriceAsset}"
                    if _ad.GetType().lower() == 'sell':
                        _unresolvedTrade['description'] = f"SELLING  {_ad._adAssetQt} {_ad._adAsset}"
                    if _ad.GetType().lower() == 'trade':
                        _unresolvedTrade['description'] = f"TRADING {_ad._adAssetQt} {_ad._adAsset}  <-> {_ad._adPrice} {_ad._adPriceAsset}"
                    
                    
                    '''
                    _unresolvedTrade['unresolved'] = 1
                    _unresolvedTrade['order_utxos'] = range(0, len(_ad._adTxDatas))
                    _unresolvedTrade['executed_utxos'] = []
                    _unresolvedTrade['transactions'] = []
                    '''
                        
                    complementData = self.__AnalyzeAdStatus__(_ad)    
                       
                    for key in   complementData:
                        _Data = complementData[key]
                        _unresolvedTrade[key] = _Data
                        
                    _unresolvedTrade['status'] = 'NOT FOUND'
                    
                    
                    
                        
                    if len(_unresolvedTrade['executed_utxos']) > 0 :
                        
                        if len(_unresolvedTrade['executed_utxos']) > len(_unresolvedTrade['transactions']):
                            _unresolvedTrade['status'] = 'COMPLETE'
                        else:
                            _unresolvedTrade['status'] = 'WAITING'
        
                    _final_datas[_data_cursor] = _unresolvedTrade
                    _data_cursor = _data_cursor+1
                
            
            
            
            
            #Save datas
            #self.setData("_tx_history", _final_datas)
            self.setProgress(f'Trade history listing complete')
            self.setResult(_final_datas)
        
        #self.setData("_tx_history_running", False)
        
        
        except Exception as e:
            self.plugin.RaisePluginLog( "Unable to get trade history : "+ str(e), type="error")
            self.setError(e)
        
        
        
        
        #
        #Update GUI
        #
        '''
        _ravenCorePlugin = self.parentFrame.GetPlugin('Ravencore')
        if _ravenCorePlugin != None:
            ut = _ravenCorePlugin.GetUTXOManager()
            if ut != None:
                #ut._allTabs['Trades History'].UpdateView()
                wx.CallAfter(ut._allTabs['Trades History'].UpdateView, ())
    
        '''
        
    def __AnalyzeAdStatus__(self, adObject):
        _AnalysisResult = {
            'executed_utxos':[],
            'order_utxos':[],
            'transactions':[],
            'unresolved' : 1
            }
        
        _order_utxos = []
        _executed_utxos = []
        _transactions = []
        
        for _txid in adObject._adTxDatas:
            _tx = adObject._adTxDatas[_txid]
            
            _valid, _data = self.plugin.DecodeTx(_tx)    
            
            #self.logger.info(f"TX ANALYSIS : {_valid} {_data}.")
            
            _obj = {'raw':_tx}
            
            if _valid:
                _transactions.append(_obj)
                _order_utxos.append('notfoundUTXO-1')
                
        
            else:
                if _data.__contains__('Has more than one vin/vout'):
                    #invalid issue
                    pass
                if _data.__contains__('this transaction may have been executed already'):
                    _executed_utxos.append(_obj)
        
        
        _AnalysisResult['executed_utxos'] = _executed_utxos
        _AnalysisResult['order_utxos'] = _order_utxos
        _AnalysisResult['transactions'] = _transactions
        
        return _AnalysisResult   
    
    
    def __searchMatchingAdInCache__(self, trade, _cache_list):
        
        
        '''
        if not trade.__contains__('transactions'):
            return None
        
        if len(trade['transactions']) == 0:
        '''
        _found = False
        _match_ad = None
        _id = None
        
        if len(trade['transactions']) > 0:
        
            for _tx in trade['transactions']:
                _rawSearch = _tx['raw']
        
        
                for _c in _cache_list:
                    _ad=_cache_list[_c]
                    
                    for _txAdCursor in _ad._adTxDatas:
                        _txAd = _ad._adTxDatas[_txAdCursor]
                        
                        if _txAd == _rawSearch:
                            _found = True
                            _match_ad = _ad
                            _id = _c
                            break
                        
                    if _found:
                        break
                
                if _found:
                    break
        
        
        
        if not _found:
            pass
        
        
        return (_found, _match_ad, _id)
    
     
        
    def SaveResult(self):
        self.plugin.setData("_tx_history", self.getResult())