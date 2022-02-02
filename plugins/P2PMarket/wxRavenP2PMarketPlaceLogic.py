'''
Created on 8 janv. 2022

@author: slinux
'''

#from .wxRavenTutorialPluginDesign import *

import threading
import time 

from .wxRavenP2PMarketDesign import * 
from wxRavenGUI.application.wxcustom.CustomLoading import *
import wx.lib.mixins.listctrl as listmix 


from .wxRavenP2PMarket_AdRightClickPopupMenu import *


class wxRavenP2PMarket_MarketPlaceListingWithLogic(wxRavenP2PMarket_MarketPlaceListingPanel, listmix.ColumnSorterMixin):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "P2P Marketplace Listing" 
    view_name = "P2P Marketplace Listing"
    parent_frame = None
    default_position = "main"
    icon = 'p2p_icon'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, position = "main", viewName= "P2P Marketplace Listing", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "P2P Marketplace Listing"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.allIcons = {}
        
        self.m_toggleBtn2.SetBitmap(parentFrame.RessourcesProvider.GetImage('filter_ps'))
        
        #self.m_KawButton.SetBitmap(parentFrame.RessourcesProvider.GetImage('ravencoin'))
        #self.m_KawButton.SetLabel('KAW !')
        self.searchOptionsPanel.Hide()
        self._filterPanelVisible = False
        self._loadingPanel = None
        
        self._currentMarket = ""
        
        self._datacache = {}
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        
        
        if not self.parent_frame.GetPluginSetting("P2PMarket","p2p_markets_enable") :
            self.m_infoCtrl1.ShowMessage("The P2P Market Place is disabled, changes settings in preferences in order to use this view.")
        
        
        
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.m_listCtrl1)
        self.m_listCtrl1.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)
        self.m_listCtrl1.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OnRightClick)
        #self.m_listCtrl1.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)
        
        
        self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated)
        
        
        self.setupTableview()
        self.setupMarketList()
        self.setupFilterDefault()
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
    
    
    
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.Layout()
        self.waitApplicationReady()
    
    
    
    def OnRightClick(self, event):
        
        menuAsset = MarketPlaceAdRightclickPopupMenu(self, self.parent_frame, self._currentItemData)
        
    
    def OnItemActivated(self, event):
        #self.OpenTxViewAd()
        self.OpenAdDetails()
        
        
        
    
    def OnItemSelected(self, event):
        ##print(event.GetItem().GetTextColour())
        #_is = self.m_listCtrl1.GetFirstSelected()
        #print(f"current _is  {_is}")
        print(f"current event  {event.Index}")
        self._currentItem = event.Index
        self._currentItem = self.m_listCtrl1.GetItemData(event.Index)
        print(f"_currentItem  {self._currentItem}")
        #GetFirstSelected
        
        itemData = self._datacache[self._currentItem]
        self._currentItemData = itemData
        #print(f"current item changed {len(self._currentItemData._adTxDatas)}")
        #print(f"current item changed {type(self._currentItemData._adTxDatas)}")
        #self.ChangeTxViewIfOpen()
        #
    
    
    
    
    def OpenAdDetails(self):
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        #adData:RavencoinP2PMarketPlaceAd
        myPlugin.OpenAdDetails(self._currentItemData)
    
    
    
    
    def OpenTxViewAd(self):
        itemData = self._currentItemData
        print(f"{itemData}")
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        _dataEmpty=True
        if itemData._adTxDatas != None:
            if itemData._adTxDatas != {}:
                myPlugin.ShowAdInfos(itemData, openIfnotExist=True)
                _dataEmpty=False
        
        
        if _dataEmpty :
            if self.parent_frame.Views.SearchDialog("View TX Infos") != None:
                myPlugin.ShowAdInfos(None,openIfnotExist=False )
    
    
    
    
    def ChangeTxViewIfOpen(self):
        itemData = self._currentItemData
        print(f"{itemData}")
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        _dataEmpty=True
        if itemData._adTxDatas != None:
            if itemData._adTxDatas != {}:
                myPlugin.ShowTxInfos(itemData._adTxDatas[0], openIfnotExist=False)
                _dataEmpty=False
        
        
        if _dataEmpty :
            if self.parent_frame.Views.SearchDialog("View TX Infos") != None:
                myPlugin.ShowTxInfos("",openIfnotExist=False )
    
    
    
    def GetFilterFields(self):
        _currentDisableValueIndex = self.m_AdInformationsFilter.GetCheckedStrings()
        #print(_currentDisableValueIndex)
        _toSaveArray = []
        for _val in _currentDisableValueIndex:
            _toSaveArray.append(_val)
    
        return _toSaveArray
    
    def GetFilterTypes(self):
        _currentDisableValueIndex = self.m_adTypeFilter.GetCheckedStrings()
        #print(_currentDisableValueIndex)
        _toSaveArray = []
        for _val in _currentDisableValueIndex:
            _toSaveArray.append(_val)
    
        return _toSaveArray
    
        
    def OnFeelLuck(self, event):
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        myPlugin.RequestMarketUpdate_T()
        self.ShowLoading()
    
    def OnKaw(self, event):
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        #myPlugin.RequestMarketUpdate_T() 
        
        
        allKeywordsStr = self.m_searchCtrl1.GetValue()
        allKeywordsArray = []
        
        # ['title', 'asset', 'price_asset' , 'desc', 'keywords']
        if allKeywordsStr != "":
            allKeywordsArray = allKeywordsStr.split(' ')
        
        searchFields = self.GetFilterFields()
        
        print(f"search allKeywordsArray = {allKeywordsArray}")
        #myPlugin.SearchInMarkets(self, keywords=[], _specificMarket="" , searchFields=[]):
        myPlugin.RequestMarketSearch_T( allKeywordsArray, _specificMarket=self._currentMarket  , searchFields=searchFields)
        
        
        self.ShowLoading()
    
    
    
    def OnAdTypeFilterChanged(self, evt):
        self.adTypeFilter =  self.m_adTypeFilter.GetCheckedStrings()
        print(self.adTypeFilter)
    
    
    def OnAdTxMethodChanged(self, evt):
        self.adMethodFilter = self.m_txTypeFilter.GetCheckedStrings()
        print(self.adMethodFilter)
    
    
    def OnToggleFilterButtonClicked(self, evt):
        _toggled = self.m_toggleBtn2.GetValue()
        
        if _toggled:
            self.searchOptionsPanel.Show()
        else:
            self.searchOptionsPanel.Hide()
            
        self.Layout()
    
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetListCtrl(self):
        return self.m_listCtrl1
    
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetSortImages(self):
        return (self.allIcons['sort_down_2'], self.allIcons['sort_up_2'])
    
    
    
    
    def setupFilterDefault(self):
        
        self.adTypeFilter = ["Buy", "Sell", 'Trade']
        self.m_adTypeFilter.SetCheckedStrings(self.adTypeFilter)
        
        
        self.adMethodFilter = ["Atomic Swap", "P2SH"]
        self.m_txTypeFilter.SetCheckedStrings(self.adMethodFilter)
        
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        search_fields = myPlugin.PLUGIN_SETTINGS['search_fields']
        
        self.m_AdInformationsFilter.SetCheckedStrings(search_fields)
    
    
    def setupMarketList(self):
        #self.m_marketChoice.Clear()
        
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        defaultChannel = myPlugin.PLUGIN_SETTINGS['p2p_markets']
        
        
        for key in defaultChannel:    
            self.m_marketChoice.Append(key)
            
        myPlugin.setData("market_chanel", '')
        
        
    
    
    def setupTableview(self):
        
        
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "Title"
        self.m_listCtrl1.InsertColumn(0, info)

        info.Align = 0#wx.LIST_FORMAT_RIGHT
        info.Text = "Type"
        self.m_listCtrl1.InsertColumn(1, info)

        info.Align = 0
        info.Text = "Tx Type"
        self.m_listCtrl1.InsertColumn(2, info)
        
        info.Align = 0
        info.Text = "Address"
        self.m_listCtrl1.InsertColumn(3, info)
        
        info.Align = 0
        info.Text = "Asset"
        self.m_listCtrl1.InsertColumn(4, info)
        
        info.Align = 0
        info.Text = "Price"
        self.m_listCtrl1.InsertColumn(5, info)
        
        
        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "Qt"
        self.m_listCtrl1.InsertColumn(6, info)
        
        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "Orders"
        self.m_listCtrl1.InsertColumn(7, info)
        
        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "ID"
        self.m_listCtrl1.InsertColumn(8, info)
        
        self.il = wx.ImageList(16, 16)
        

        
        self.allIcons['buy'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('asset_ravencoin-blue') )
        self.allIcons['sell'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('asset_ravencoin-red') )
        
        self.allIcons['asset'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('asset_ravencoin-blue') )
        self.allIcons['info'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('info_obj') )
        
        self.allIcons['sort_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up') )
        self.allIcons['sort_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down') )
        self.allIcons['sort_up_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up_2') )
        self.allIcons['sort_down_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down_2') )
        
        self.allIcons['alphab_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_up') )
        self.allIcons['alphab_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_co') )
        

        print("Table setup")
        self.m_listCtrl1.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
    
    
    def ClearResults(self):
        self.m_listCtrl1.DeleteAllItems()
        
        
        
        
    def ShowLoading(self, evt=None):
        
        #print('LOADER ON !')
        
        if self._loadingPanel  == None:
            self._loadingPanel =  wxBackgroundWorkerAnimation(self.m_listCtrl1)
        
        
        self._loadingPanel.Show(show=True)
        
        #self._loadingPanel.Popup()
        self.Layout()
        
    def HideLoading(self,evt=None):
        if self._loadingPanel  != None:
            self._loadingPanel.Hide()
            self.Layout()
           
        
        
        
        
        
        
    
    def OnMarketplaceChanged(self, evt):
        print("OnMarketplaceChanged")
        _market = self.m_marketChoice.GetString(self.m_marketChoice.GetCurrentSelection())   
        print(_market)
        self._currentMarket = _market
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        if  _market != "All Marketplaces":
            print("Market Updated")
            myPlugin.setData("market_chanel", _market)
        else:
            myPlugin.setData("market_chanel", "")
            
            
        self.UpdateView(None)
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.UpdateView,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
        
        
            
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        #myPlugin.RequestMarketUpdate_T()    
        #while myPlugin.getData("thread_running"):
        #    time.sleep(2)
        #if myPlugin.PLUGIN_SETTINGS['p2p_markets_force_network'] != "": 
        #    myPlugin.RequestMarketUpdate_T()    
        
        if myPlugin.getData("thread_running"):
            
            wx.CallAfter(self.ShowLoading, ()) 
        else:
            wx.CallAfter(callback, ()) 
    
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        
        self.ShowLoading()
        self.UpdateDataFromPluginDatas()
        
        self.HideLoading()    
        self.Layout()
            
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self, evt=None):  
        
        #self.ShowLoading()
        print("UpdateDataFromPluginDatas : p2p market")
        
        self.m_listCtrl1.Freeze()
        self.ClearResults()
        self._datacache = {}
        self.itemDataMap = {}     
        
        
        #market = self.parent_frame.GetPlugin("P2PMarket").GetCurrentMarketChannel()
        
        
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        market = myPlugin.getData("market_chanel")
        
        results = self.parent_frame.GetPluginData("P2PMarket","P2P_Market_Listing") 
        
        
        _search = self.parent_frame.GetPluginData("P2PMarket","P2P_Market_Search_Result") 
        if _search != None:
            if _search != {}:
                print("Search data found, using them")
                results  = _search
        #print(f"Market results = {results}")
        #print(f"Current market = {market}")
        
        
        
        self._cursor = 0
        
        
        for m in results:
            if market != '' :
                if market != m:
                    continue
            
            marketDatas = results[m]
            self.displayMarketInList(marketDatas)
        
        
        
        
        self.m_listCtrl1.SetColumnWidth(1, 70)
        self.m_listCtrl1.SetColumnWidth(2,wx.LIST_AUTOSIZE)
        self.m_listCtrl1.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.m_listCtrl1.SetColumnWidth(4, wx.LIST_AUTOSIZE)
        self.m_listCtrl1.SetColumnWidth(5, wx.LIST_AUTOSIZE)
        self.m_listCtrl1.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.m_listCtrl1.SetColumnWidth(7, 75)
        self.m_listCtrl1.SetColumnWidth(8, 20)
        
        self.m_listCtrl1.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        listmix.ColumnSorterMixin.__init__(self, 9)    
        
 
        self.m_listCtrl1.Thaw()
            
        self.HideLoading()        
    
    
    
    
    def displayMarketInList(self, marketDatas):
        
        _displayTypes = self.GetFilterTypes()
        
        
        for itemIndex in marketDatas :
                    
            item = marketDatas[itemIndex]
            
            
            
            if item.GetType() not in _displayTypes:
                continue
            
                    
            _baseicon = self.allIcons['sell']
            if item._adType == 0:
                _baseicon = self.allIcons['sell']
            else:
                _baseicon = self.allIcons['buy']
                    
            index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),item._adTitle, self.allIcons['asset'] )
                    
            self.m_listCtrl1.SetItem(index,1, item.GetType())
            self.m_listCtrl1.SetItem(index,2, item.GetMethod())
                    
                    
            self.m_listCtrl1.SetItem(index,3, str(item._adAddress))        
            
            
            priceComplete = str(item._adPrice) + ' ' + str(item._adPriceAsset)
                    
            self.m_listCtrl1.SetItem(index,4, item._adAsset)
            self.m_listCtrl1.SetItem(index,5, str(priceComplete))
            self.m_listCtrl1.SetItem(index,6, str(item._adAssetQt))
            #print(str(item._adOrders))
            
            _avCount = item.GetAvailableOrders()
            _avorderCol = f"{_avCount}/{item._adOrders}"
            
            self.m_listCtrl1.SetItem(index,7, str(_avorderCol))      
            
            self.m_listCtrl1.SetItem(index,8, str(self._cursor))    
                    
            self.m_listCtrl1.SetItemData(index, self._cursor)
                    
            self._datacache[self._cursor] = item
            self.itemDataMap[self._cursor] = (item._adTitle, item._adType,item._adTxType, str(item._adAddress) ,item._adAsset, float(item._adPrice) ,float(item._adAssetQt), int(_avCount), int(self._cursor))
                    
                    
            #print(f"{self._cursor}  {item}")
            self._cursor = self._cursor+1
    
    
    
    
    
            
            