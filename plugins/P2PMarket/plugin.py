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
#used for long datas requests
import threading



from .pluginSettings import *
from plugins.P2PMarket.wxRavenP2PMarket_ViewTxInfosPanel import wxRavenP2PMarket_ViewTexInfosDialog
from ast import literal_eval
import ast

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
        _atomicIconNew =self.RessourcesProvider.GetImage('atomic_swap') 
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
                     'icon':_rawDataIcon, 
                     'class': wxRavenP2PMarket_ViewTexInfosDialog,
                     'default':False,
                     'multipleViewAllowed':False
                     }
                     
                     
                    
        
                    
                ]
        
        
        
        
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
               'search_limit' : 500,
               'search_fields' : ['title', 'asset', 'price_asset' , 'desc', 'keywords'],
               
               'p2p_blacklist_addresses' : [],
               'p2p_trusted_addresses' : {},
               'include_none_tx' : False,
               'verify_tx' : False,
               'only_trusted' : False,
               'keep_trades_locked' : True
            }
        
        
        
        
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
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.RequestMarketUpdate_T,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parentFrame._isReady:
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
    
    
    
    
    
    
    
    
    
    
    
    def isBlackList(self, add):
        p2p_blacklist_addresses = self.PLUGIN_SETTINGS['p2p_blacklist_addresses']
        return p2p_blacklist_addresses.__contains__(add)
    
    
    def isTrusted(self, add):
        p2p_trusted_addresses = self.PLUGIN_SETTINGS['p2p_trusted_addresses']
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
    
    
    
    
    
    
    
      
    def DecodeTx(self,txdata):
        ravencoin = self.__getNetwork__()  
        return ravencoin.atomicswap.GetAtomicSwap(txdata)
    
    def ShowTxInfos(self, txdatas="", openIfnotExist=True):
        
        _newView = self.parentFrame.Views.OpenView("View TX Infos", "P2PMarket", openIfnotExist)
        
        #if txdatas !="":
        if True:
            _v=self.parentFrame.Views.SearchDialog("View TX Infos")
            print(">txdatas setup requested")
            if _v!=None:
                _v._Panel.SetRaw(txdatas)
      
      
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
        
    def RequestMarketUpdate_T(self, evt=None ):  
        t=threading.Thread(target=self.__DoRefreshAllMarkets__)
        t.start()        
        
    def OnNetworkChanged_T(self, networkName=""):  
        
        if self.PLUGIN_SETTINGS['p2p_markets_force_network'] == "": 
            t=threading.Thread(target=self.__DoRefreshAllMarkets__)
            t.start()
        
    
    
    
    def __searchInField__(self, fieldname, keywords, itemJson, _caseSensitive=False):
        _match = False
        print('__searchInField__')
        print(itemJson)
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
                print(f" searching {keyw} in {str(_fieldValueArray)}")
                if _fieldValueArray.__contains__(keyw.lower()):
                    _match = True 
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
                print(f" no keyword given match true")
                
            if len(keywords) == 0:
                _match = True
                print(f" no keyword given match true")
            
            if len(keywords) == 1 and keywords[0] == "*":
                _match = True
                print(f" * keyword given match true")
            
            
            #
            #Do search only if keywords are non empty or not *
            if not _match:
                for _field in searchFields:
                    _match = self.__searchInField__(_field, keywords, itemJson)
            
            
            
            
            
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
                print(f'start search in  {_market}')
                if _chanelsDatas.__contains__(_market):
                    marketDatas = _chanelsDatas[_market]
                    P2P_Market_Search_Result[_market] = self.__searchInMarket__(marketDatas,keywords, searchFields )
                    
                
                
            self.setData("P2P_Market_Search_Result", P2P_Market_Search_Result)
             
            
        except Exception as e:
            self.RaisePluginLog( "Unable to perform market search :"+ str(e), type="error")
        
        
        wx.CallAfter(self.UpdateActiveViews, ())
        self.setData("search_running", False)
    
    
    
    
        
    def __DoRefreshAllMarkets__(self, _specificMarket=""):
        
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
        
        
        try:
        #if True:  
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
                _chanelListing = ravencoin.p2pmarket.GetP2PMarketAdsIPFSListingDatas(asset=market_chanel, count=search_limit, includeNoneTxDatas=include_none_tx, verifyTx=verify_tx, whitelist=_whiteList) 
                
                print(f"LOADED ! market_chanel : {market_chanel} = {_chanelListing}")
                
                _chanelsDatas[market_chanel] = _chanelListing
                
                self.setData("P2P_Market_Listing", _chanelsDatas)
            
            
            
            
            #self.setData("myPluginData2", myPluginData2)
            self.RaisePluginLog( f"P2P markets informations retreived with success on Channel '{market_chanel}'", type="msg")
            #When datas are loaded, add a call after to trigger plugins view update
            wx.CallAfter(self.RequestMarketSearch_T, ())
            
        except Exception as e:
            self.RaisePluginLog( "Unable to retreive p2p market informations :"+ str(e), type="error")
        
        
        self.setData("thread_running", False)    
            
        
        
        