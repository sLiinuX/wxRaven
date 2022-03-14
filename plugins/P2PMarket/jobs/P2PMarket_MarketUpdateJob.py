'''
Created on 28 févr. 2022

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import *


class Job_MarketUpdate(Job):
    '''
    classdocs
    '''


    def __init__(self,plugin,_specificMarket='', viewCallback=None, safeMode=True):
        '''
        Constructor
        '''
        
        Job.__init__(self, plugin.parentFrame, plugin, viewCallback, safeMode)
        #self._chanelsDatas = plugin.getData("P2P_Market_Listing")
        self._specificMarket=_specificMarket
        
        #self.addExportParam('_chanelsDatas') 
        self.addExportParam('_specificMarket') 
        self.setAllowRemoteExecution(True)
        
        self.jobName = f"Market Listing Update"
        
        
        _forceNetwork = self.plugin.PLUGIN_SETTINGS['p2p_markets_force_network'] 
        self.setNetwork(_forceNetwork)
        
        self.jobId = f"{self.jobName} - {self.getNetworkName()}"
        
    
    
    def JobProcess(self):
        
        #self.setData("myPluginData", {})
        #self.setData("myPluginData2", False)
        _chanelsDatas = self.plugin.getData("P2P_Market_Listing")
        
        _specificMarket = self._specificMarket
        
        
        
        _forceNetwork = self.plugin.PLUGIN_SETTINGS['p2p_markets_force_network'] 
        self.setNetwork(_forceNetwork)
        
        market_chanels =[]
        if _specificMarket != "":
            market_chanels.append(_specificMarket)
        else:
            market_chanels = self.plugin.GetAllMarketChannels()
        
        search_limit = self.plugin.PLUGIN_SETTINGS['search_limit']
        include_none_tx  = self.plugin.PLUGIN_SETTINGS['include_none_tx']
        verify_tx  = self.plugin.PLUGIN_SETTINGS['verify_tx']
        only_trusted  = self.plugin.PLUGIN_SETTINGS['only_trusted']
        multiple_ipfs_check_if_none = self.plugin.PLUGIN_SETTINGS['multiple_ipfs_check_if_none']
        
        
        ipfsFallbacks = []
        if multiple_ipfs_check_if_none :
            _ipfsList =  self.parentFrame.GetPluginSetting('Ravencore', "ipfsgateway_providers")
            ipfsFallbacks = _ipfsList
        
        
        
        
        print(f"__DoRefreshAllMarkets__")
        print(f"market_chanels {market_chanels}")
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
        self.setProgress(f'P2P Market listing started')
        
        try:
        #if True:  
            ravencoin = self.plugin.__getNetwork__()
            
            
            _ipfsDefault =  self.parentFrame.GetPluginSetting('Ravencore', "ipfsgateway_default")
            
            _blacklistedAddresses = self.plugin.PLUGIN_SETTINGS['p2p_blacklist_addresses'] 
            _p2p_trusted_addresses = self.plugin.PLUGIN_SETTINGS['p2p_trusted_addresses'] 
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
                #print(f"loading {market_chanel}")
                self.setProgress(f'P2P Market listing {market_chanel}')
                _chanelsDatas[market_chanel] = []
                #_chanelListing = ravencoin.p2pmarket.GetP2PMarketAdsIPFSListingDatas(asset=market_chanel, count=search_limit, ipfs_gateway="specialip", includeNoneTxDatas=include_none_tx) 
                _chanelListing = ravencoin.p2pmarket.GetP2PMarketAdsIPFSListingDatas(asset=market_chanel, count=search_limit, ipfs_gateway=_ipfsDefault, includeNoneTxDatas=include_none_tx, verifyTx=verify_tx, whitelist=_whiteList, _fallbackIpfsGateways=ipfsFallbacks) 
                
                #print(f"LOADED ! market_chanel : {market_chanel} = {_chanelListing}")
                
                _chanelsDatas[market_chanel] = _chanelListing
                
                #self.plugin.setData("P2P_Market_Listing", _chanelsDatas)
            
            
            
            
            #self.setData("myPluginData2", myPluginData2)
            self.setProgress(f'P2P Market listing complete')
            self.setResult(_chanelsDatas)
            #self.RaisePluginLog( f"P2P markets informations retreived with success on Channel '{market_chanel}'", type="msg")
            #When datas are loaded, add a call after to trigger plugins view update
            #wx.CallAfter(self.RequestMarketSearch_T, ())
            
        except Exception as e:
            self.plugin.RaisePluginLog( "Unable to retreive p2p market informations :"+ str(e), type="error")
            self.setError(e)
        
        
        
    def SaveResult(self):
        self.plugin.setData("P2P_Market_Listing", self.getResult())
        
        
        