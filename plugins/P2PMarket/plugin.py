'''
Created on 8 janv. 2022

@author: slinux
'''



#import the class form above level, it contains predefined functions to overwrite.
#from plugins.pluginObjectTemplate import * 
from wxRavenGUI.application.pluginsframework import *
#import the design of your plugin made in FormBuilder
from .wxRavenP2PMarketDesign import *
#import the logic of your plugin (inherit design class with logic)
#from .wxRavenTutorialPluginLogic import *

#import the plugin setting panels, from another file to be more simple
from .wxRavenP2PMarketPlaceLogic import *
from .wxRavenP2PMarketNewAdDialogLogic import *
from .wxRavenCreateAtomicSwapLogic import *
from .wxRavenP2PMarket_CreateUTXOLogic import *
from .wxRavenP2PMarket_ViewTxInfosPanel import *
from .wxRavenP2PMarket_AdDetailPanel import *
#from plugins.P2PMarket.wxRavenP2PMarket_CreateAirdropLogic import *


from .wxRavenP2PMarket_UTXOManager_TradesHistoryView_Logic import *


#used for long datas requests
import threading



from .pluginSettings import *
#from plugins.P2PMarket.wxRavenP2PMarket_ViewTxInfosPanel import wxRavenP2PMarket_ViewTexInfosDialog
from ast import literal_eval
import ast
#from plugins.P2PMarket import wxRavenP2PMarket_CreateAdvertisingLogic


from .jobs import *

class wxRavenPlugin(PluginObject):
    '''
    classdocs
    '''


    def __init__(self, parentFrame, position="mgr"):
        
        
        #Call the parent class with ParentFrame and Position
        #This object is the plugin instance and will manage all views internally.
        PluginObject.__init__(self, parentFrame, position=position)
        self.parentFrame = parentFrame
        
        #
        #ParentFrame is used to refer to the main app
        #Position is used to refer to the defaut position views are open.
        #
        
        
        
        #Define your plugin meta-datas :
        #
        # Name : Name of the plugin, It match the Plugin Folder name (not verified in other cases)
        # Icon
        # Views : All the views that contains the plugin
        
       
        self.PLUGIN_NAME = "P2PMarket"
        self.PLUGIN_ICON = self.RessourcesProvider.GetImage('p2p_icon') #wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
        _p2pIconNew =self.RessourcesProvider.GetImage('p2p_icon_new') 
        _atomicIconNew =self.RessourcesProvider.GetImage('atomic_swap_new') 
        _utxoIconNew =self.RessourcesProvider.GetImage('new_utxo') 
        _inspectSwap =self.RessourcesProvider.GetImage('inspect_swap') 
        _airdrop =self.RessourcesProvider.GetImage('airdrop_icon') 
        _advertise =self.RessourcesProvider.GetImage('advertiser_icon') 
        
        _rawDataIcon =  self.RessourcesProvider.GetImage('raw_datas') 
        
        
        #
        #    View Object declare all the 'Views' that can be instanciated
        #    {
        #             'viewid':                  a unique id for the view
        #             'name':                    a name for the view
        #             'title':                   a title id for the view
        #             'position':, 
        #             'icon':
        #             'class': 
        #             'default':                 Boolean to determine if the view is open by default at startup
        #             'multipleViewAllowed':     Boolean to determine if the view allow multiple instance of it 
        #}
        #        
        
        
        self.PLUGINS_VIEWS= [ 
                    
                    
                    {
                     'viewid':'P2P Marketplace Listing', 
                     'name':'P2P Marketplace Listing', 
                     'title':'P2P Marketplace Listing', 
                     'position':position, 
                     'icon':self.PLUGIN_ICON, 
                     'class': wxRavenP2PMarket_MarketPlaceListingWithLogic ,
                     'default':False,
                     'multipleViewAllowed':True
                     },
                    
                     {
                     'viewid':'New P2P Market Ad', 
                     'name':'New P2P Market Ad', 
                     'title':'New P2P Market Ad', 
                     'position':'dialog', 
                     'icon':_p2pIconNew, 
                     'class': wxRavenP2PMarket_NewAdWithLogic ,
                     'default':False,
                     'multipleViewAllowed':True
                     },
                     
                     
                     {
                     'viewid':'New Atomic Swap', 
                     'name':'New Atomic Swap', 
                     'title':'New Atomic Swap', 
                     'position':'dialog', 
                     'icon':_atomicIconNew, 
                     'class': wxRavenP2PMarket_NewAtomiSwapWithLogic,
                     'default':False,
                     'multipleViewAllowed':False
                     },
                     
                     {
                     'viewid':'View TX Infos', 
                     'name':'View TX Infos', 
                     'title':'View TX Infos', 
                     'position':'dialog', 
                     'icon':_inspectSwap, 
                     'class': wxRavenP2PMarket_ViewTexInfosDialog,
                     'default':False,
                     'multipleViewAllowed':False
                     }
                     
                     
                    ,
                     
                     {
                     'viewid':'Create UTXO', 
                     'name':'Create UTXO', 
                     'title':'Create UTXO', 
                     'position':'dialog', 
                     'icon':_utxoIconNew, 
                     'class': wxRavenP2PMarket_CreateUTXOWithLogic,
                     'default':False,
                     'multipleViewAllowed':False,
                     'toolbar_shortcut': False
                     }
                     
        
                    ,
                    
                    {
                     'viewid':'Ad Details', 
                     'name':'Ad Details', 
                     'title':'Ad Details', 
                     'position':'main', 
                     'icon':_utxoIconNew, 
                     'class': wxRavenP2PMarket_AdDetailsLogic,
                     'default':False,
                     'multipleViewAllowed':False,
                     'toolbar_shortcut': False,
                     'hidden_view': True,
                     'skip_save': True,
                     }
                     
        
                    ,
                    
                     
                     
                ]
        
        
        '''
                     {
                     'viewid':'Create Airdrop', 
                     'name':'Create Airdrop', 
                     'title':'Create Airdrop', 
                     'position':'dialog', 
                     'icon':_airdrop, 
                     'class': wxRavenP2PMarket_CreateAirdropWithLogic,
                     'default':False,
                     'multipleViewAllowed':False,
                     'toolbar_shortcut': True
                     }
                     ,
                     
                     
                     {
                     'viewid':'Create Advertising', 
                     'name':'Create Advertising', 
                     'title':'Create Advertising', 
                     'position':'dialog', 
                     'icon':_advertise, 
                     'class': wxRavenP2PMarket_CreateAdvertisingWithLogic,
                     'default':False,
                     'multipleViewAllowed':False,
                     'toolbar_shortcut': True
                     }
                     '''
        
        
        
        
        #
        #    Setting Object declare all the 'default settings' 
        #    Once the plugin loaded for the first time, those settings will be saved
        #    in the config.ini file in a dedicated section when app close.
        #
        #    On next plugin load, if the config file contains plugins settings
        #    those will be overwritten in the _LoadPluginSettings() function
        #    
        #    you need to declare your own function as later in the file to CAST datas 
        #    that come from the ConfigParser in String only
        #
        #    {
        #             'key':                 value
        #    }
        #        
        
        
        self.PLUGIN_SETTINGS = {
            
            
               'p2p_markets_enable':False,
               'p2p_markets_force_network':'',
               'p2p_channel_asset_default' :'WXRAVEN/P2P_MARKETPLACE',
               'p2p_markets' : ['WXRAVEN/P2P_MARKETPLACE', 'WXRAVEN/P2P_MARKETPLACE/TEST'],
               
               'p2p_channel_asset_target_address' : 'munRj4MDDka4nv9FnxUrSq6KF55DPpdCCi',
               'p2p_market_change_address' : "munRj4MDDka4nv9FnxUrSq6KF55DPpdCCi",
               'p2p_market_swap_address' : "",
               'search_limit' : 500,
               'search_fields' : ['title', 'asset', 'price_asset' , 'desc', 'keywords'],
               
               'p2p_blacklist_addresses' : [],
               'p2p_trusted_addresses' : {},
               'include_none_tx' : False,
               'verify_tx' : False,
               'multiple_ipfs_check_if_none' : True,
               'only_trusted' : False,
               'keep_trades_locked' : True,
               
               
               'market_webservice_enable' : False
            }
        
        
        
        
        
        
        
        self.registerJob(Job_MarketUpdate)
        self.registerJob(Job_TradeHistory)
        
        
        
        
        #
        # Lets put some setting pannels from pluginsetting file (to define as well)
        #
        self.PLUGIN_SETTINGS_GUI = []
        
        _prefIcon = self.RessourcesProvider.GetImage('p2p_icon')
        _MyTutorialSettingPanel_WithLogic = PluginSettingsTreeObject("P2P Market", _prefIcon, classPanel=wxP2PMarket_GeneralSettings_WithLogic, _childs=None)
        
        
        
        _prefIcon = self.RessourcesProvider.GetImage('p2p_icon2')
        _P2PMarketlistSettingPanel_WithLogic = PluginSettingsTreeObject("Markets", _prefIcon, classPanel=wxP2PMarket_BookmarksSettings_WithLogic, _childs=None)
        
        _prefIcon = self.RessourcesProvider.GetImage('blacklist')
        _P2PMarketblacklistSettingPanel_WithLogic = PluginSettingsTreeObject("Blacklist", _prefIcon, classPanel=wxP2PMarket_BlacklistSettings_WithLogic, _childs=None)
        
        _prefIcon = self.RessourcesProvider.GetImage('trusted_icon')
        _P2PMarketTrustedPeersPanel_WithLogic = PluginSettingsTreeObject("Trusted", _prefIcon, classPanel=wxP2PMarket_TrustedPeers_WithLogic, _childs=None)
        
        
        _prefIcon = self.RessourcesProvider.GetImage('my_marketplace')
        _MyMarketPlaceSettings_WithLogic = PluginSettingsTreeObject("My Marketplace", _prefIcon, classPanel=wxP2PMarket_MyMarketPlaceSettings_WithLogic, _childs=None)
        
        
        _MyTutorialSettingPanel_WithLogic._childs.append(_P2PMarketlistSettingPanel_WithLogic)
        _MyTutorialSettingPanel_WithLogic._childs.append(_P2PMarketblacklistSettingPanel_WithLogic)
        _MyTutorialSettingPanel_WithLogic._childs.append(_P2PMarketTrustedPeersPanel_WithLogic)
       
        
        
        _MyTutorialSettingPanel_WithLogic._childs.append(_MyMarketPlaceSettings_WithLogic)
        
        #wxP2PMarket_BlacklistSettings_WithLogic
        #wxP2PMarket_BookmarksSettings_WithLogic
        
        self.PLUGIN_SETTINGS_GUI.append(_MyTutorialSettingPanel_WithLogic)

        
        
        
        #
        # Datas : In order to avoid each view to individually request the same data through RPC,
        #         the plugin can contains Global vars / datas shared to the views
        #         it also allow to request those big datas through thread and call update after
        #
        self.setData("P2P_Market_Listing", {})
        self.setData("P2P_Market_Search_Result", {})
        self.setData("P2P_Market_Chanel", '')
        self.setData("thread_running", False)
        self.setData("search_running", False)
        
        self.setData("_tx_history", {})
        self.setData("_tx_history_running", False)
        self.setData("_tx_history_skip_swap", False)
        self.setData("_tx_history_skip_ads", False)
        
        self.setData("_storage", str(parentFrame.Paths['USERDATA']) + '')
        #self.setData("myPluginData2", False)
        
        
        #
        # Plugin can Register on callbacks like Connexion change in this case, it will start a thread to get datas
        #
        parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        
        
        #
        # Finally, this last line is MANDATORY to load the default views.
        # REMOVED AND REPLACED BY AN AUTO LOAD
        #self.LoadPluginFrames()
        self.waitApplicationReady()
    
    
    
    
    """
    
    Plugins setting management
    
    Note, this method must be overwritten on plugins that use settings since
    config parser only use STRING values.
    
    
    """
    
    #
    # Seems not mandatory with new LoadSetting Generic function but in case of specific
    # Types, better redeclare it!
    #
    
    """
    def _LoadPluginSettings(self):
        _recordedSettings = self.parentFrame.Settings._GetPluginSettings(self.PLUGIN_NAME)
        
        
        for key in _recordedSettings:
            
            
            #
            # _recordedSettings[key] Return string only, do your own mapping for complex datastructure
            #
            self.PLUGIN_SETTINGS[key] = _recordedSettings[key]
            
            
    """        
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.ApplicationReady,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parentFrame._isReady:
            time.sleep(2)
        time.sleep(2)
        wx.CallAfter(callback, ()) 
            
        #myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        #myPlugin.RequestMarketUpdate_T()    
        #while myPlugin.getData("thread_running"):
        #    time.sleep(2)
        #if myPlugin.PLUGIN_SETTINGS['p2p_markets_force_network'] != "": 
        #    myPlugin.RequestMarketUpdate_T()    
        
        #if myPlugin.getData("thread_running"):
        #    
        #    wx.CallAfter(self.ShowLoading, ()) 
        #else:
        #    wx.CallAfter(callback, ()) 
    
    
    
    
    
    
    def ApplicationReady(self, evt=None):
        
        if self.PLUGIN_SETTINGS['p2p_markets_enable']:
            self.RequestMarketUpdate_T()
        
        ravencorep=self.parentFrame.GetPlugin("Ravencore")
        
        if ravencorep !=None:
            _addins = ravencorep.getData("_utxo_manager_views_addons_callbacks") 
            _addins.append(self.OpenMarketHistoryDetails)
            ravencorep.setData("_utxo_manager_views_addons_callbacks", _addins) 
    
    
    
    
    def isBlackList(self, add):
        p2p_blacklist_addresses = self.PLUGIN_SETTINGS['p2p_blacklist_addresses']
        return p2p_blacklist_addresses.__contains__(add)
    
    
    def isTrusted(self, add):
        p2p_trusted_addresses = self.PLUGIN_SETTINGS['p2p_trusted_addresses']
        #print(p2p_trusted_addresses.__contains__(add))
        return p2p_trusted_addresses.__contains__(add)
    
    
    
    def AddAddressInTrusted(self, add, alias):
        p2p_trusted_addresses = self.PLUGIN_SETTINGS['p2p_trusted_addresses']
        p2p_trusted_addresses[add]=alias
        self.PLUGIN_SETTINGS['p2p_trusted_addresses'] = p2p_trusted_addresses
        self.RaisePluginLog( f" address '{add}' has been marked as trusted peer !", type="msg")
        
        
        
    
    def RemoveAddressFromTrusted(self, add):
        p2p_trusted_addresses = self.PLUGIN_SETTINGS['p2p_trusted_addresses']
        
        if p2p_trusted_addresses.__contains__(add):
            del p2p_trusted_addresses[add]
            self.PLUGIN_SETTINGS['p2p_trusted_addresses'] = p2p_trusted_addresses
            self.RaisePluginLog( f" address '{add}' has been removed from the trusted peer list !", type="msg")
            
    
    
    def AddAddressInBlacklist(self, add):
        p2p_blacklist_addresses = self.PLUGIN_SETTINGS['p2p_blacklist_addresses']
        p2p_blacklist_addresses.append(add)
        self.PLUGIN_SETTINGS['p2p_blacklist_addresses'] = p2p_blacklist_addresses
        self.RaisePluginLog( f" address '{add}' has been blacklisted !", type="msg")
    
    def RemoveAddressFromBlacklist(self, add):
        p2p_blacklist_addresses = self.PLUGIN_SETTINGS['p2p_blacklist_addresses']
        
        if p2p_blacklist_addresses.__contains__(add):
            p2p_blacklist_addresses.remove(add)
            self.PLUGIN_SETTINGS['p2p_blacklist_addresses'] = p2p_blacklist_addresses
            self.RaisePluginLog( f" address '{add}' has been removed from the blacklist !", type="msg")
    
    
    
    
    
    
    
    
    
    
    def __getNetwork__(self):
        ravencoin = self.parentFrame.getRvnRPC()
        _restrictNetwork = self.PLUGIN_SETTINGS['p2p_markets_force_network']
             
        if _restrictNetwork != '':
            ravencoin = self.parentFrame.getRvnRPC(_restrictNetwork)          
        return ravencoin
    
    
    
    
    def OpenAdDetails(self, adDatas):
        #_newView = self.LoadView(self.SearchPluginView("IPFS File Uploader"), "dialog")
        _newView = self.parentFrame.Views.OpenView("Ad Details", "P2PMarket", True)
        print(_newView)
        if _newView != None:
            
            _vi = self.parentFrame.Views.SearchViewInstance("Ad Details")
            
            _vi['instance'].Show()
            _vi['instance'].LoadAd(adDatas)
    
    
    def CreateNewUTXO(self, assetname='RVN'):
        _newView = self.parentFrame.Views.OpenView("Create UTXO", "P2PMarket", True)
        
    
    
    
    def OpenMarketHistoryDetails(self):
        plugin = self.parentFrame.GetPlugin('Ravencore')
        if plugin != None:
            _v = plugin.GetUTXOManager()
            _v.createNewPluginPanel( 'Trades History', wxRavenP2PMarket__Ravencore_UTXOManager_TradesHistory_ViewLogic, 'trade_history')  
    
    
    
    
      
    def DecodeTx(self,txdata):
        ravencoin = self.__getNetwork__()  
        return ravencoin.atomicswap.GetAtomicSwap(txdata)
    
    def ShowTxInfos(self, txdatas="", openIfnotExist=True):
        
        _newView = self.parentFrame.Views.OpenView("View TX Infos", "P2PMarket", openIfnotExist)
        
        #if txdatas !="":
        if True:
            _v=self.parentFrame.Views.SearchDialog("View TX Infos")
            print(f">txdatas setup requested {txdatas}")
            if _v!=None:
                _v._Panel.SetRaw(txdatas)
    
    
    
    def ShowAdInfos(self, ad, cursor=0, openIfnotExist=True):
        
        _newView = self.parentFrame.Views.OpenView("View TX Infos", "P2PMarket", openIfnotExist)
        
        #if txdatas !="":
        if True:
            _v=self.parentFrame.Views.SearchDialog("View TX Infos")
            print(f">txad setup requested {ad}")
            if _v!=None:
                _v._Panel.SetAd(ad, cursor)
    
      
      
    def GetCurrentMarketChannel(self):
        market_chanel = self.getData('P2P_Market_Chanel')
        #if market_chanel == "":
        #    market_chanel = self.PLUGIN_SETTINGS['p2p_channel_asset_default']
            
        return market_chanel
      
      
      
      
    def GetAllMarketChannels(self):
        
        market_chanel = self.PLUGIN_SETTINGS['p2p_markets']
            
        return market_chanel
      
      
      
      
        
    '''
    
    Plugin Triggers / Callbacks for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
     
    '''
    
    def RequestMarketTradesHistory_T(self, callback=None, evt=None):
        #GetAtomicSessionCache_Trades
        self.setData("_tx_history", {})
        #t=threading.Thread(target=self.__DoRetreiveMarketTradesHistory__)
        #t.start()  
        
        #
        #new job
    
        j = Job_TradeHistory(self, viewCallback=callback, safeMode=True)
        self.parentFrame.NewJob(j)
    
    
    '''
    def __searchMatchingAdInCache__(self, trade, _cache_list):
        
        
 
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
    '''    
        
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
            
            _valid, _data = self.DecodeTx(_tx)    
            
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
    
    '''
    
    
    
    def __DoRetreiveMarketTradesHistory__(self):
        
        pass
        '''
        if self.getData("_tx_history_running")==True:
            return
        
        self.setData("_tx_history_running", True)
        ravencoin = self.__getNetwork__()
        
        _tx_history_skip_swap = self.getData("_tx_history_skip_swap")
        _tx_history_skip_ads = self.getData("_tx_history_skip_ads")
        
        
        _final_datas= {}
        _data_cursor  = 0
        
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
        self.setData("_tx_history", _final_datas)
        
        
        self.setData("_tx_history_running", False)
        
        
        
        
        
        
        
        #
        #Update GUI
        #
        _ravenCorePlugin = self.parentFrame.GetPlugin('Ravencore')
        if _ravenCorePlugin != None:
            ut = _ravenCorePlugin.GetUTXOManager()
            if ut != None:
                #ut._allTabs['Trades History'].UpdateView()
                wx.CallAfter(ut._allTabs['Trades History'].UpdateView, ())
        
        '''
        
    def RequestMarketUpdate_T(self,callback=None, evt=None ):  
        #t=threading.Thread(target=self.__DoRefreshAllMarkets__)
        #t.start()     
        j = Job_MarketUpdate(self, _specificMarket='', viewCallback=callback, safeMode=True)   
        self.parentFrame.NewJob(j)
    
    
    
    
    def OnNetworkChanged_T(self, networkName=""):  
        if not self.parentFrame._isReady:
            return None 
        
        '''
        if self.PLUGIN_SETTINGS['p2p_markets_force_network'] == "": 
            t=threading.Thread(target=self.__DoRefreshAllMarkets__)
            t.start()
        
        '''
    
    
    def __searchInField__(self, fieldname, keywords, itemJson, _caseSensitive=False):
        _match = False
        #print('__searchInField__')
        #print(itemJson)
        try:
            _fieldValueArray = str(itemJson[fieldname]).split(' ')
            _fieldValueArrayLow = []
            
            for v in _fieldValueArray:
                _fieldValueArrayLow.append(v.lower())
            
            keywordsLow = []
            for v in keywords:
                keywordsLow.append(v.lower())
                
                
                    
            if not _caseSensitive:    
                _fieldValueArray = _fieldValueArrayLow
                keywords = keywordsLow
                
            
            for keyw in keywords:
                #print(f" searching {keyw} in {str(_fieldValueArray)}")
                if _fieldValueArray.__contains__(keyw.lower()):
                    _match = True 
                    #print(f"MATCH")
                    break
            
                for _fieldKeys in _fieldValueArray:
                    #print(f" searching {keyw} in {str(_fieldKeys)}")
                    if _fieldKeys.__contains__(keyw.lower()):
                        _match = True 
                        #print(f"MATCH")
                        break
            
             
            
        except Exception as e:
            print(str(e))    
            
        return _match
    
    def __searchInMarket__(self,  marketDatas, keywords=[], searchFields=[]): 
        market_cursor=0  
        match_results = {}
        
        
        if searchFields == []:
            searchFields  = self.PLUGIN_SETTINGS['search_fields']
        
        marketItem:RavencoinP2PMarketPlaceAd
        
        
        for marketItemIndex in marketDatas :
            marketItem = marketDatas[marketItemIndex]
            
            itemJson = marketItem.JSON()
            
            
            _match = False
            
            if keywords == []:
                _match = True
                #print(f" no keyword given match true")
                
            if len(keywords) == 0:
                _match = True
                #print(f" no keyword given match true")
            
            if len(keywords) == 1 and keywords[0] == "*":
                _match = True
                #print(f" * keyword given match true")
            
            
            #
            #Do search only if keywords are non empty or not *
            if not _match:
                for _field in searchFields:
                    _match = self.__searchInField__(_field, keywords, itemJson)
                    if _match:
                        break
            
            
            
            
            if _match:
                match_results[market_cursor] = marketItem
                market_cursor = market_cursor +1 
            
        return match_results    
            
            
    def RequestMarketSearch_T(self, keywords=[], _specificMarket="" , searchFields=[]):  
        t=threading.Thread(target=self.__SearchInMarkets__, args=(keywords, _specificMarket , searchFields))
        t.start()   
    
    def __SearchInMarkets__(self, keywords=[], _specificMarket="" , searchFields=[]):
        
        
        
        
        if self.getData("search_running") == True:
            return
        self.setData("P2P_Market_Search_Result", {})
        self.setData("search_running", True)
        
        
        #if True:
        try:
            market_chanels =[]
            if _specificMarket != "":
                market_chanels.append(_specificMarket)
            else:
                market_chanels = self.GetAllMarketChannels()
                
                
                
            P2P_Market_Search_Result = {}
            
            
            
            _chanelsDatas = self.getData("P2P_Market_Listing")
            
            
            
            for _market in market_chanels:
                #print(f'start search in  {_market}')
                if _chanelsDatas.__contains__(_market):
                    marketDatas = _chanelsDatas[_market]
                    P2P_Market_Search_Result[_market] = self.__searchInMarket__(marketDatas,keywords, searchFields )
                    
                
                
            self.setData("P2P_Market_Search_Result", P2P_Market_Search_Result)
             
            
        except Exception as e:
            self.RaisePluginLog( "Unable to perform market search :"+ str(e), type="error")
        
        
        wx.CallAfter(self.UpdateActiveViews, ())
        self.setData("search_running", False)
    
    
    
    
        
    def __DoRefreshAllMarkets__(self, _specificMarket=""):
        print('__DoRefreshAllMarkets__ DEPRECATED')
        pass
    
        '''
        if self.getData("thread_running") == True:
            return
        
        self.setData("thread_running", True)
        if self.PLUGIN_SETTINGS['p2p_markets_enable'] == False:
            print("p2p market is not active")
            return
        
        
        #self.setData("myPluginData", {})
        #self.setData("myPluginData2", False)
        _chanelsDatas = self.getData("P2P_Market_Listing")
        
        
        market_chanels =[]
        if _specificMarket != "":
            market_chanels.append(_specificMarket)
        else:
            market_chanels = self.GetAllMarketChannels()
        
        search_limit = self.PLUGIN_SETTINGS['search_limit']
        include_none_tx  = self.PLUGIN_SETTINGS['include_none_tx']
        verify_tx  = self.PLUGIN_SETTINGS['verify_tx']
        only_trusted  = self.PLUGIN_SETTINGS['only_trusted']
        multiple_ipfs_check_if_none = self.PLUGIN_SETTINGS['multiple_ipfs_check_if_none']
        
        
        ipfsFallbacks = []
        if multiple_ipfs_check_if_none :
            _ipfsList =  self.parentFrame.GetPluginSetting('Ravencore', "ipfsgateway_providers")
            ipfsFallbacks = _ipfsList
        
        print(f"__DoRefreshAllMarkets__")
        print(f"search_limit {search_limit}")
        print(f"search_limit {include_none_tx}")
        print(f"search_limit {include_none_tx}")
        print(f"search_limit {only_trusted}")
        
        
        #
        #
        #
        #    
        #    https://ravencoinipfs-gateway.com/ipfs/
        #
        #
        #
        
        
        #try:
        if True:  
            ravencoin = self.__getNetwork__()
            
            
            _ipfsDefault =  self.parentFrame.GetPluginSetting('Ravencore', "ipfsgateway_default")
            
            _blacklistedAddresses = self.PLUGIN_SETTINGS['p2p_blacklist_addresses'] 
            _p2p_trusted_addresses = self.PLUGIN_SETTINGS['p2p_trusted_addresses'] 
            _whiteList = []
            
            if only_trusted:
                for ad in _p2p_trusted_addresses:
                    _whiteList.append(ad)
                
           
            #RAW LISTING DEPRECATED
            #
            """
            _chanelListing = ravencoin.p2pmarket.GetP2PMarketAdsRawListing(asset=market_chanel, count=search_limit)
            #myPluginData = self.parentFrame.ConnexionManager.getAllConnexions()
            #myPluginData2 = self.parentFrame.ConnexionManager.getCurrent()
            _chanelsDatas[market_chanel] = _chanelListing
            self.setData("P2P_Market_Listing", _chanelsDatas)
            """
            
            for market_chanel in market_chanels:
                print(f"loading {market_chanel}")
                _chanelsDatas[market_chanel] = []
                #_chanelListing = ravencoin.p2pmarket.GetP2PMarketAdsIPFSListingDatas(asset=market_chanel, count=search_limit, ipfs_gateway="specialip", includeNoneTxDatas=include_none_tx) 
                _chanelListing = ravencoin.p2pmarket.GetP2PMarketAdsIPFSListingDatas(asset=market_chanel, count=search_limit, ipfs_gateway=_ipfsDefault, includeNoneTxDatas=include_none_tx, verifyTx=verify_tx, whitelist=_whiteList, _fallbackIpfsGateways=ipfsFallbacks) 
                
                print(f"LOADED ! market_chanel : {market_chanel} = {_chanelListing}")
                
                _chanelsDatas[market_chanel] = _chanelListing
                
                self.setData("P2P_Market_Listing", _chanelsDatas)
            
            
            
            
            #self.setData("myPluginData2", myPluginData2)
            self.RaisePluginLog( f"P2P markets informations retreived with success on Channel '{market_chanel}'", type="msg")
            #When datas are loaded, add a call after to trigger plugins view update
            wx.CallAfter(self.RequestMarketSearch_T, ())
            
        #except Exception as e:
        #    self.RaisePluginLog( "Unable to retreive p2p market informations :"+ str(e), type="error")
        
        
        self.setData("thread_running", False)    
            
        '''
        
        