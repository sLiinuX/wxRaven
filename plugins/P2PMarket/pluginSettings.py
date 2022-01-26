'''
Created on 9 janv. 2022

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import PluginSettingsPanelObject
import wx

import os
from .wxRavenP2PMarketDesign import *

from wxRavenGUI.application.wxcustom import UserError,UserInfo, UserQuestion,RequestUserWalletPassword

class wxP2PMarket_GeneralSettings_WithLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenP2PMarket_Settings(parent) 
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
        #self.parent = parent
        #_Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
        
        
        self._Panel.m_forceNetwork.Bind( wx.EVT_CHECKBOX, self.OnChanged ) 
        self._Panel.searchopt_strictmode.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        
        self._Panel.searchopt_includeNoneData.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        self._Panel.searchopt_checkTx.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        self._Panel.searchopt_OnlyVerifiedSellers.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        
        
        
        self._needReboot=True
        
        self._Panel.m_buttonCleanCache.Bind( wx.EVT_BUTTON, self.ClearInvalidCache )
        
        
        self._Panel.searchopt_maxresults.Bind( wx.EVT_TEXT, self.OnChanged )
        
        
        
        #self._Panel.searchopt_onlymain.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        
        
        #self._Panel.searchopt_onlymain.Bind( wx.EVT_CHECKBOX, self.toggleAssetTypeList )
    
        self.Layout()
        
        
        
        
    def ClearInvalidCache(self, evt):
        rootp = self.parentFrame.Paths['USERDATA']
        file = rootp +'marketplace_invalid_cache.p'
        try:
            os.remove(file )  
            UserInfo(self._Panel, "Cache clear !")  
        except Exception as e:
            UserError(self._Panel, "Unable to clear cache file !")  
            pass
        
        
        
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        #_newValueForBoolSetting = self._Panel.booleansetting.IsChecked()
        strictname = self._Panel.searchopt_strictmode.GetValue()
        assetsearchlimit = self._Panel.searchopt_maxresults.GetValue()
        #mainOnly = self._Panel.searchopt_onlymain.IsChecked()
        
        p2p_markets_force_network = self._Panel.m_forceNetwork.GetValue()    
        p2p_markets_force_network_value = self._Panel.m_NetworkChoice.GetString(self._Panel.m_NetworkChoice.GetCurrentSelection())      
            
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        
        
        include_none_tx = self._Panel.searchopt_includeNoneData.GetValue()  
        verify_tx = self._Panel.searchopt_checkTx.GetValue()  
        only_trusted = self._Panel.searchopt_OnlyVerifiedSellers.GetValue()  
        
        
        
        
        myPlugin.PLUGIN_SETTINGS["search_limit"] = int(assetsearchlimit)
        myPlugin.PLUGIN_SETTINGS["p2p_markets_enable"] = strictname
        myPlugin.PLUGIN_SETTINGS["include_none_tx"] = include_none_tx
        myPlugin.PLUGIN_SETTINGS["verify_tx"] = verify_tx
        myPlugin.PLUGIN_SETTINGS["only_trusted"] = only_trusted
        
        
        
        
        print(f"search_limit = {assetsearchlimit}")
        print(f"p2p_markets_enable = {strictname}")
        print(f"include_none_tx = {include_none_tx}")
        print(f"verify_tx = {verify_tx}")
        print(f"only_trusted = {only_trusted}")
        
        
        
        if p2p_markets_force_network == True:
            myPlugin.PLUGIN_SETTINGS["p2p_markets_force_network"] = p2p_markets_force_network_value
        else:
            myPlugin.PLUGIN_SETTINGS["p2p_markets_force_network"] = ''
        
        #p2p_markets_force_network

        
        print('SavePanelSettings P2P market !')
          
        """
        strictname = self.searchopt_strictmode.GetValue()
        assetsearchlimit = self.searchopt_maxresults.GetValue()
        mainOnly = self.searchopt_onlymain.GetValue()
        
        """
        #now its up to the dev to chose how to take this information
        #in our demo lets do simple and just change the  booleansetting in PLUGIN_SETTINGS
        
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin.PLUGIN_SETTINGS['booleansetting'] = _newValueForBoolSetting
    
        #print("SavePanelSettings" + str(_newValueForBoolSetting))
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        assetsearchlimit = myPlugin.PLUGIN_SETTINGS["search_limit"]
        strictname =  myPlugin.PLUGIN_SETTINGS["p2p_markets_enable"] 
        p2p_markets_force_network =  myPlugin.PLUGIN_SETTINGS["p2p_markets_force_network"] 
        
        
        include_none_tx =  myPlugin.PLUGIN_SETTINGS["include_none_tx"] 
        verify_tx =  myPlugin.PLUGIN_SETTINGS["verify_tx"] 
        only_trusted =  myPlugin.PLUGIN_SETTINGS["only_trusted"] 
        
        
        
        #print(assetsearchlimit)
        #print(strictname)
        #print(mainOnly)
        
        
        allNetworks = self.parentFrame.ConnexionManager.getAllConnexions()
        for net in allNetworks:
            self._Panel.m_NetworkChoice.Append(net)
            
        
        #print(self.parent_frame.GetPlugin("Ravencore") )
        self._Panel.searchopt_strictmode.SetValue(strictname)
        self._Panel.searchopt_maxresults.SetValue(str(assetsearchlimit))
        
        
        self._Panel.searchopt_includeNoneData.SetValue(include_none_tx)
        self._Panel.searchopt_checkTx.SetValue(verify_tx)
        self._Panel.searchopt_OnlyVerifiedSellers.SetValue(only_trusted)
        
        
        
        
        
        if p2p_markets_force_network != '':
            self._Panel.m_forceNetwork.SetValue(True)
            self._Panel.m_NetworkChoice.Enable(True)
            
            _dc = self._Panel.m_NetworkChoice.FindString(p2p_markets_force_network)
            if _dc != wx.NOT_FOUND:
                self._Panel.m_NetworkChoice.SetSelection(_dc)
        
        print("LoadPanelSettings")
        #self.initListAssetType()
        
        

    def OnChanged(self, evt):
        self._settingsHasChanged = True
        
        p2p_markets_force_network = self._Panel.searchopt_maxresults.GetValue()    
        if p2p_markets_force_network:
            self._Panel.m_NetworkChoice.Enable(True)
        else:
            self._Panel.m_NetworkChoice.Enable(False)



    



class wxP2PMarket_BookmarksSettings_WithLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenP2PMarket_MarketsBookmarks(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
        #_Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
        
        
        
        
        _Panel.Bind( wx.EVT_BUTTON, self.OnAddProvider,id = _Panel.bookmark_addbt.GetId()  )
        _Panel.Bind( wx.EVT_BUTTON, self.OnRemoveProvider,id = _Panel.bookmark_rembt.GetId()  )
        #_Panel.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp,id = _Panel.ipfs_provider_upbt.GetId()  )
        
        
        """
        _Panel.ipfs_provider_addbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        #_Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        _Panel.ipfs_provider_rembt.Bind( wx.EVT_BUTTON, self.OnRemoveProvider )
        
        
        _Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp )
        """
    
    
    
    
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        #_newValueForBoolSetting = self._Panel.booleansetting.IsChecked()
        
        allProviders = []
        
        for i in range(0, self._Panel.bookmark_list.Count):
            allProviders.append(self._Panel.bookmark_list.GetString(i)) 
        
        
        #default =    allProviders[0] 
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]    = default
        myPlugin.PLUGIN_SETTINGS["p2p_markets"]  = allProviders
        #print(allProviders)
        #print(default)
        
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #ipfsgateway_default = myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]
        bookmark_list_s =  myPlugin.PLUGIN_SETTINGS["p2p_markets"] 
        
        #for i in ipfsgateway_providers:
        self._Panel.bookmark_list.InsertItems(bookmark_list_s, 0)
        
        #print("LoadPanelSettings")     
        
        
        self._Panel.Layout()
        
        
    def OnAddProvider(self, evt):    
        
        newp  = self._Panel.bookmark_text_area.GetValue()
        self._Panel.bookmark_list.InsertItems([newp], self._Panel.bookmark_list.Count)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnRemoveProvider(self, evt):    
        x = self._Panel.bookmark_list.GetSelection()
        self._Panel.bookmark_list.Delete(x)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnMoveProviderUp(self, evt): 
        x = self._Panel.bookmark_list.GetSelection()
        #self._Panel.ipfs_provider_list.SetFirstItem(x)
        #print(x)
        
        _itemTopromote = self._Panel.bookmark_list.GetString(x)
        self._Panel.bookmark_list.Delete(x)
        
        self._Panel.bookmark_list.InsertItems([_itemTopromote], 0)
        
        self._settingsHasChanged = True
        self._Panel.Layout()






class wxP2PMarket_BlacklistSettings_WithLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenP2PMarket_AddressesBlackList(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
        #_Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
        
        
        
        
        _Panel.Bind( wx.EVT_BUTTON, self.OnAddProvider,id = _Panel.bookmark_addbt.GetId()  )
        _Panel.Bind( wx.EVT_BUTTON, self.OnRemoveProvider,id = _Panel.bookmark_rembt.GetId()  )
        #_Panel.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp,id = _Panel.ipfs_provider_upbt.GetId()  )
        
        
        """
        _Panel.ipfs_provider_addbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        #_Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        _Panel.ipfs_provider_rembt.Bind( wx.EVT_BUTTON, self.OnRemoveProvider )
        
        
        _Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp )
        """
    
    
    
    
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        #_newValueForBoolSetting = self._Panel.booleansetting.IsChecked()
        
        allProviders = []
        
        for i in range(0, self._Panel.bookmark_list.Count):
            allProviders.append(self._Panel.bookmark_list.GetString(i)) 
        
        
        #default =    allProviders[0] 
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]    = default
        myPlugin.PLUGIN_SETTINGS["p2p_blacklist_addresses"]  = allProviders
        #print(allProviders)
        #print(default)
        
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #ipfsgateway_default = myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]
        bookmark_list_s =  myPlugin.PLUGIN_SETTINGS["p2p_blacklist_addresses"] 
        
        #for i in ipfsgateway_providers:
        if bookmark_list_s != []:
            self._Panel.bookmark_list.InsertItems(bookmark_list_s, 0)
        
        #print("LoadPanelSettings")     
        
        
        self._Panel.Layout()
        
        
    def OnAddProvider(self, evt):    
        
        newp  = self._Panel.bookmark_text_area.GetValue()
        self._Panel.bookmark_list.InsertItems([newp], self._Panel.bookmark_list.Count)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnRemoveProvider(self, evt):    
        x = self._Panel.bookmark_list.GetSelection()
        self._Panel.bookmark_list.Delete(x)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnMoveProviderUp(self, evt): 
        x = self._Panel.bookmark_list.GetSelection()
        #self._Panel.ipfs_provider_list.SetFirstItem(x)
        #print(x)
        
        _itemTopromote = self._Panel.bookmark_list.GetString(x)
        self._Panel.bookmark_list.Delete(x)
        
        self._Panel.bookmark_list.InsertItems([_itemTopromote], 0)
        
        self._settingsHasChanged = True
        self._Panel.Layout()







class wxP2PMarket_TrustedPeers_WithLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenP2PMarket_TrustedSellers(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
        self.parent = parent
        #_Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
        
        
        
        
        _Panel.Bind( wx.EVT_BUTTON, self.OnAddProvider,id = _Panel.bookmark_addbt.GetId()  )
        _Panel.Bind( wx.EVT_BUTTON, self.OnRemoveProvider,id = _Panel.bookmark_rembt.GetId()  )
        #_Panel.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp,id = _Panel.ipfs_provider_upbt.GetId()  )
        
        
        """
        _Panel.ipfs_provider_addbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        #_Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        _Panel.ipfs_provider_rembt.Bind( wx.EVT_BUTTON, self.OnRemoveProvider )
        
        
        _Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp )
        """
    
    
    
    
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        #_newValueForBoolSetting = self._Panel.booleansetting.IsChecked()
        
        allProviders = {}
        
        appSettings = self.parentFrame.Settings
        _newList = {}
        _errorsParsing = False
        for i in range(0, self._Panel.bookmark_list.Count):
            
            
            _con = self._Panel.bookmark_list.GetString(i)
             
            try:
                _conArr = _con.split('=')
                _name = _conArr[0]
                _val = _conArr[1]
                print(f"addin {_name} as {_val}") 
                _newList[_name] = _val

                
            except Exception as e:
                _errorsParsing = True
                print(f"erreur in the connexion '{_con}', data will not be saved")
            
        
        if not _errorsParsing:    
            
            myPlugin = self.parentFrame.GetPlugin(self.pluginName)
            print(f"addin {allProviders} ") 
            #myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]    = default
            myPlugin.PLUGIN_SETTINGS["p2p_trusted_addresses"]  = _newList
        #print(allProviders)
        #print(default)
        
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #ipfsgateway_default = myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]
        bookmark_list_s =  myPlugin.PLUGIN_SETTINGS["p2p_trusted_addresses"] 
        
        #for i in ipfsgateway_providers:
        if bookmark_list_s != []:
            
            
            _dispArray = []
            for key in bookmark_list_s:
                _val=bookmark_list_s[key]
                strCon = str(key) + " = " + str(_val)
                _dispArray.append(strCon)
            
            if len(_dispArray) > 0:
                self._Panel.bookmark_list.InsertItems(_dispArray, 0)
        
        #print("LoadPanelSettings")     
        
        
        self._Panel.Layout()
        
        
    def OnAddProvider(self, evt):    
        
        newp  = self._Panel.bookmark_text_area.GetValue()
        self._Panel.bookmark_list.InsertItems([newp], self._Panel.bookmark_list.Count)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnRemoveProvider(self, evt):    
        x = self._Panel.bookmark_list.GetSelection()
        self._Panel.bookmark_list.Delete(x)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnMoveProviderUp(self, evt): 
        x = self._Panel.bookmark_list.GetSelection()
        #self._Panel.ipfs_provider_list.SetFirstItem(x)
        #print(x)
        
        _itemTopromote = self._Panel.bookmark_list.GetString(x)
        self._Panel.bookmark_list.Delete(x)
        
        self._Panel.bookmark_list.InsertItems([_itemTopromote], 0)
        
        self._settingsHasChanged = True
        self._Panel.Layout()



















class wxP2PMarket_MyMarketPlaceSettings_WithLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenP2PMarket_MyMarketSettings(parent) 
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
        #_Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
        
        self.parent = parent
        self._Panel.m_sameAddressChangeOpt.Bind( wx.EVT_CHECKBOX, self.OnChanged ) 
        self._Panel.m_defaultListingChanel.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        
        self._Panel.m_AddressChoice.Bind( wx.EVT_CHOICE, self.OnChanged )
        self._Panel.m_changeAddressChoiceOpt.Bind( wx.EVT_CHOICE, self.OnChanged )
        self._Panel.m_NetworkChoice.Bind( wx.EVT_CHOICE, self.OnChanged )
        
        self._Panel.m_AddressSwap.Bind( wx.EVT_CHOICE, self.OnChanged )
        
        self._Panel.m_keeplocks.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        
        self._Panel.m_keeplocks.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        
        
        self._Panel.m_importButton.Bind( wx.EVT_BUTTON, self.OnDoImportTradeSessions )
        self._Panel.m_wipeButton.Bind( wx.EVT_BUTTON, self.OnDoWipeTradeSessions )
        self._Panel.m_unlockAll.Bind( wx.EVT_BUTTON, self.OnDoUnlockAll )
        self._Panel.m_initMyMarketPlace.Bind( wx.EVT_BUTTON, self.OnDoInitMyMarketPlace )
        
        
        
        
        self.destfile= os.getcwd() + "/userdata/atomicswap_session.cache"
        self.Layout()
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        
        #include_none_tx = self._Panel.searchopt_includeNoneData.GetValue()  
        
        
        p2p_channel_asset_target_address = self._Panel.m_AddressChoice.GetString(self._Panel.m_AddressChoice.GetCurrentSelection()) 
        p2p_market_change_address =  self._Panel.m_changeAddressChoiceOpt.GetString(self._Panel.m_changeAddressChoiceOpt.GetCurrentSelection())
        
        if self._Panel.m_sameAddressChangeOpt.GetValue()== True:
            market_change_address =  p2p_channel_asset_target_address
        
         
        p2p_channel_asset_default =  self._Panel.m_NetworkChoice.GetString(self._Panel.m_NetworkChoice.GetCurrentSelection())
        
        p2p_market_swap_address =  self._Panel.m_AddressSwap.GetString(self._Panel.m_AddressSwap.GetCurrentSelection())
        
        
        
        
        myPlugin.PLUGIN_SETTINGS["p2p_channel_asset_target_address"] = p2p_channel_asset_target_address
        myPlugin.PLUGIN_SETTINGS["p2p_market_change_address"] = p2p_market_change_address
        myPlugin.PLUGIN_SETTINGS["p2p_channel_asset_default"] = p2p_channel_asset_default
        myPlugin.PLUGIN_SETTINGS["p2p_market_swap_address"] = p2p_market_swap_address
        
        keep_trades_locked = self._Panel.m_keeplocks.GetValue() 
        myPlugin.PLUGIN_SETTINGS["keep_trades_locked"] = keep_trades_locked
        print('SavePanelSettings P2P market !')
          

    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        
        
        
        p2p_channel_asset_target_address = myPlugin.PLUGIN_SETTINGS["p2p_channel_asset_target_address"]
        p2p_market_change_address =  myPlugin.PLUGIN_SETTINGS["p2p_market_change_address"] 
        p2p_channel_asset_default =  myPlugin.PLUGIN_SETTINGS["p2p_channel_asset_default"] 
        
        p2p_market_swap_address =  myPlugin.PLUGIN_SETTINGS["p2p_market_swap_address"] 
        
        
        _isSame = False
        
        if p2p_market_change_address == p2p_channel_asset_target_address:
            _isSame = True
            self._Panel.m_changeAddressChoiceOpt.Enable(False)
        
        ravencoin = myPlugin.__getNetwork__()
        
        
        
        keep_trades_locked = myPlugin.PLUGIN_SETTINGS["keep_trades_locked"]
        self._Panel.m_keeplocks.SetValue(keep_trades_locked)
        
        
        #print(assetsearchlimit)
        #print(strictname)
        #print(mainOnly)
        
        _allNotAdmins= None
        _allmyAddress = None
        
        
        try:
            _allNotAdmins= ravencoin.asset.GetAllMyAssets(_excludeAdmin=True)
            _allmyAddress = ravencoin.wallet.getAllWalletAddresses()
        except Exception as e:
            print('unable to retreive asset and wallet datas for settings')
        
        
        
        
        if _allNotAdmins != None:
            for net in _allNotAdmins:
                self._Panel.m_NetworkChoice.Append(net)
            
        
        #print(self.parent_frame.GetPlugin("Ravencore") )
        self._Panel.m_sameAddressChangeOpt.SetValue(_isSame)
        
        
        
        if p2p_channel_asset_default != "":
            self._Panel.m_defaultListingChanel.SetValue(True)
            _dc = self._Panel.m_NetworkChoice.FindString(p2p_channel_asset_default)
            if _dc != wx.NOT_FOUND:
                self._Panel.m_NetworkChoice.SetSelection(_dc)
        
        
        
        
        
        
        
        
        if _allmyAddress!= None:
            for ad in _allmyAddress:
                self._Panel.m_AddressChoice.Append(ad)
                self._Panel.m_changeAddressChoiceOpt.Append(ad)
                self._Panel.m_AddressSwap.Append(ad)
                
            
        
        
        if p2p_channel_asset_target_address != "":
            _dc = self._Panel.m_AddressChoice.FindString(p2p_channel_asset_target_address)
            if _dc != wx.NOT_FOUND:
                self._Panel.m_AddressChoice.SetSelection(_dc)
                
        if p2p_market_change_address != "":
            _dc = self._Panel.m_changeAddressChoiceOpt.FindString(p2p_market_change_address)
            if _dc != wx.NOT_FOUND:
                self._Panel.m_changeAddressChoiceOpt.SetSelection(_dc)
        
        if p2p_market_swap_address != "":
            _dc = self._Panel.m_AddressSwap.FindString(p2p_market_swap_address)
            if _dc != wx.NOT_FOUND:
                self._Panel.m_AddressSwap.SetSelection(_dc)
        
            
        print("LoadPanelSettings")
        #self.initListAssetType()
    
    
    
    
    
    def OnDoInitMyMarketPlace(self, evt):
        
        pwd = RequestUserWalletPassword(self._Panel)
        
        self.__checkAddressSetup__(True, pwd)
        
        
        """
        p2p_channel_asset_target_address = self._Panel.m_AddressChoice.GetString(self._Panel.m_AddressChoice.GetCurrentSelection()) 
        p2p_channel_asset_default =  self._Panel.m_NetworkChoice.GetString(self._Panel.m_NetworkChoice.GetCurrentSelection())
        
        
        ravencoin = self.parentFrame.getRvnRPC()
        _setupResult = ravencoin.p2pmarket.CheckP2PAnnouncerAccount(p2p_channel_asset_target_address, p2p_channel_asset_default, setupIfNotReady=True , password=pwd)
        
        
        if _setupResult:
            UserInfo(self._Panel, "Announcer Account Ready !")
        else:
            UserError(self._Panel, "Error : Announcer Account Not Ready !")
            
        """    
    
    
    
    def OnDoUnlockAll(self, evt):
        if UserQuestion(self._Panel, "Do you confirm the trade session wipe ?"):
            ravencoin = self.parentFrame.getRvnRPC()
            ravencoin.wallet.__UnlockAll__()
    
    
    
    def OnDoImportTradeSessions(self, evt):
        wildcard = "Cache file (*.cache)|*.cache|"       \
           "All files (*.*)|*.*"
        
        
        #dest= os.getcwd() + "/userdata/atomicswap_session.cache"   
           
        dlg = wx.FileDialog(
            self.parent, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | 
                  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                  wx.FD_PREVIEW
            )
        
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            paths = dlg.GetPaths()
            #print(file)
            file = paths[0]
            print(file)
            print(f'to copy in {self.destfile}')
            #print(paths[1])
            import shutil
            shutil.copy2(file, self.destfile)
            
            UserInfo(self._Panel, "Trade session imported !")
            
            
        
    
    def OnDoWipeTradeSessions(self,evt):
        if UserQuestion(self._Panel, "Do you confirm the trade session wipe ?"):
            #sessionfile = os.getcwd() + f"/userdata/atomicswap_session.cache" 
            sessionfile=self.destfile
            
            try:
                os.remove(sessionfile)
                UserInfo(self._Panel, "Trade session wiped !")
            except Exception as e:
                UserError(self._Panel, "Unable to wipe trade file")    



    
    
    def __checkAddressSetup__(self, doSetup=False, pwd=''):
        p2p_channel_asset_target_address = self._Panel.m_AddressChoice.GetString(self._Panel.m_AddressChoice.GetCurrentSelection()) 
        p2p_channel_asset_default =  self._Panel.m_NetworkChoice.GetString(self._Panel.m_NetworkChoice.GetCurrentSelection())
        
        
        
        _res = False
        try:
            ravencoin = self.parentFrame.getRvnRPC()
            _res = ravencoin.p2pmarket.CheckP2PAnnouncerAccount(p2p_channel_asset_target_address, p2p_channel_asset_default, setupIfNotReady=doSetup , password=pwd)
        except Exception as e:
            _res = False
       

        if _res:
            self._Panel.m_accountstatusBitmap.SetBitmap(self.parentFrame.RessourcesProvider.GetImage('passed'))
        else:
            
            self._Panel.m_accountstatusBitmap.SetBitmap(self.parentFrame.RessourcesProvider.GetImage('warning_2'))
            
            
        if doSetup:
            if _res:
                UserInfo(self._Panel, "Announcer Account Ready !")
            else:
                UserError(self._Panel, "Error : Announcer Account Not Ready !")




    def OnChanged(self, evt=None):
        self._settingsHasChanged = True
        
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        
        

        
        if self._Panel.m_sameAddressChangeOpt.GetValue()== True:
            self._Panel.m_changeAddressChoiceOpt.Enable(False)
        else:
            self._Panel.m_changeAddressChoiceOpt.Enable(True)

        
        
        if self._Panel.m_defaultListingChanel.GetValue()== True:
            self._Panel.m_NetworkChoice.Enable(False)
        else:
            self._Panel.m_NetworkChoice.Enable(True)



        self.__checkAddressSetup__(False)




        