'''
Created on 11 févr. 2022

@author: slinux
'''

from .wxRavenP2PMarketDesign import wxRavenP2PMarket__RavencoreUTXOManager_TradesHistory_View   
            
import wx           
import wx.adv

from datetime import date
import datetime

import wx.lib.mixins.listctrl as listmix 
from wxRavenGUI.application.wxcustom.CustomLoading import *
import threading
import time 

class wxRavenP2PMarket__Ravencore_UTXOManager_TradesHistory_ViewLogic(wxRavenP2PMarket__RavencoreUTXOManager_TradesHistory_View, listmix.ColumnSorterMixin):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Trades History"
    view_name = "Trades History"
    parent_frame = None
    default_position = "main"
    icon = 'trade_history'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent,  parentFrame, position = "main", viewName= "Trades History", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        self.parent=parent
        self.view_base_name = "Trades History"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.allIcons  = {}
        self.itemDataMap = {}
        
        self._totalIn = 0.0
        self._totalOut = 0.0
        self._totalFees = 0.0
        
        
        #self.FILTER_STATUS = ''
        #self.FILTER_TEXT = ''
        self._listInit = False
        
        self._datacache = {}
        self._loadingPanel = None
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
        
        #self.LoadSearchOptions()
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        
        _stDate = datetime.datetime.strptime('01012018', "%d%m%Y").date()
        self.m_datePicker1.SetValue(_stDate)
        self.m_datePicker2.SetValue(date.today())
        self.m_filterAddress.Bind(wx.EVT_CHOICE, self.ChangeMode)
        
        self.Bind(wx.adv.EVT_DATE_CHANGED, self.StartDateChanged, self.m_datePicker1)
        self.Bind(wx.adv.EVT_DATE_CHANGED, self.StopDateChanged, self.m_datePicker2)
        
        self.m_startDCheck.Bind(wx.EVT_CHECKBOX, self.StartDateChanged)
        self.m_stopDCheck.Bind(wx.EVT_CHECKBOX, self.StopDateChanged)
        
        self.Bind(wx.EVT_BUTTON, self.OnRefreshClicked ,self.m_refreshButton)
        
        self.m_addressFilterText.Bind(wx.EVT_TEXT, self.UpdateView)
        self.m_choiceStatus.Bind(wx.EVT_CHOICE, self.UpdateView)
        
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.m_listCtrl1)
        #self.m_listCtrl1.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)
        #self.m_listCtrl1.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OnRightClick)
        
        self.setupListFilter()
        self.setupListControl()
        '''
        
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.m_listCtrl1)
        self.m_listCtrl1.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)
        self.m_listCtrl1.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OnRightClick)
        
        
        
        
        '''
        
        self.waitApplicationReady()
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.DoRequestUpdateHistory,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
    
    
    def DoRequestUpdateHistory(self, evt=None):
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        myPlugin.RequestMarketTradesHistory_T(callback=self.UpdateView)
        self.ShowLoading()
        
    
    
    def StartDateChanged(self, evt):
        d = self.m_datePicker1.GetValue()
        if self.m_startDCheck.GetValue():
            myPlugin = self.parent_frame.GetPlugin('Ravencore')  
            #myPlugin.setData("_tx_history_start", d)    
            #self.DoRequestUpdateHistory()
   
   
            
    def StopDateChanged(self, evt):
        
        d = self.m_datePicker2.GetValue()
        if self.m_stopDCheck.GetValue():
            myPlugin = self.parent_frame.GetPlugin('Ravencore')  
            #myPlugin.setData("_tx_history_stop", d)    
            #self.DoRequestUpdateHistory()    
    
    
    
    
        
        
    def ChangeMode(self, evt):
        _filterAdressValue = self.m_filterAddress.GetString(self.m_filterAddress.GetCurrentSelection())
        self.m_addressFilterText.SetValue('')
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        _img_filter = 'trade_history'
        
        
        if _filterAdressValue == "ALL":
            myPlugin.setData("_tx_history_skip_swap", False)
            myPlugin.setData("_tx_history_skip_ads", False)
            
        elif _filterAdressValue == "SWAP CACHE":
            myPlugin.setData("_tx_history_skip_swap", False)
            myPlugin.setData("_tx_history_skip_ads", True)
            
            _img_filter = 'atomic_swap_log'
            
        elif _filterAdressValue == "ADS CACHE":
            myPlugin.setData("_tx_history_skip_swap", True)
            myPlugin.setData("_tx_history_skip_ads", False)
            
            _img_filter = 'p2p_logs'
            
        else:
            myPlugin.setData("_tx_history_skip_swap", False)
            myPlugin.setData("_tx_history_skip_ads", False)
            
        self.m_bitmap34.SetBitmap(self.parent_frame.RessourcesProvider.GetImage(_img_filter))    
            
        '''
        
        _filterAdressValue = self.m_filterAddress.GetString(self.m_filterAddress.GetCurrentSelection())
        #self.m_addressFilterText.SetValue('')
        type_mapping = {'ALL':'',
                   'SENT': 'send',
                   'RECEIVED':'receive'}
        
        img_mapping = {'ALL':'tx_vinout',
                   'SENT': 'vout_icon1',
                   'RECEIVED':'vin_icon1'}
        
        
        _type_filter = type_mapping[_filterAdressValue]
        _img_filter = img_mapping[_filterAdressValue]
        
        _colText= "Account"
        
        
        self.m_bitmap34.SetBitmap(self.parent_frame.RessourcesProvider.GetImage(_img_filter))
            
            
        self.m_addressFilterText.SetValue('')  
        
        
        myPlugin = self.parent_frame.GetPlugin('Ravencore')  
        myPlugin.setData("_tx_history_category", str(_type_filter) )    
        #self.DoRequestUpdateHistory()
        #self.UpdateView(None)  
        '''
    
    
    def OnRefreshClicked(self, evt=None):
        self.DoRequestUpdateHistory()
        
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        
        self.UpdateDataFromPluginDatas()
        self.Layout()  
            
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        
        #print('UpdateDataFromPluginDatas')
        self.ShowLoading()
        self.m_listCtrl1.Freeze()
        self.ClearResults()
        
        self._totalIn = 0.0
        self._totalOut = 0.0
        self._totalFees = 0.0
        
        
        if True:
        #try:
            
            '''
            ravencoin = self.parent_frame.getRvnRPC()
            _filterAdressValue = self.m_filterAddress.GetString(self.m_filterAddress.GetCurrentSelection())
            '''
            #_IncludeAddresses = []
            #_ExlcudeAddresses = []
            
            '''
            if _filterAdressValue != "All UTXO's":
                _IncludeAddresses.append(_filterAdressValue)
            '''
            FILTER_STATUS = self.m_choiceStatus.GetString(self.m_choiceStatus.GetCurrentSelection())
            FILTER_TEXT = self.m_addressFilterText.GetValue()
            
            
            #_showLocked = self.m_showLocked.GetValue()
            #_showUnlocked = self.m_showUnlock.GetValue()
            
            
            #_filterTYPEValue = self.m_filterAddress.GetString(self.m_filterAddress.GetCurrentSelection())
            
            _listRawAll = self.parent_frame.GetPluginData('P2PMarket', '_tx_history')
            #_listRaw = _listRawAll[_filterTYPEValue]
            
            #print(f'LIST RAW = {_listRaw}')
            
            '''
            _listRaw = []
            
            
            if _showLocked and _showUnlocked:
                print('Both')
                _listRaw = ravencoin.wallet.GetUnspentList(_OnlySpendable=True, _ExlcudeAddresses=_ExlcudeAddresses,_IncludeOnlyAddresses=_IncludeAddresses, _fullDatas=True , _includeLocked=True)
            
            elif _showLocked:
                print('Locked only')
                _listRaw = ravencoin.wallet.GetLockedUnspentList(_ExlcudeAddresses=_ExlcudeAddresses, _IncludeOnlyAddresses=_IncludeAddresses, _fullDatas=True)
            
            
            elif _showUnlocked:
                print('Unlocked only')
                _listRaw = ravencoin.wallet.GetUnspentList(_OnlySpendable=True, _ExlcudeAddresses=_ExlcudeAddresses,_IncludeOnlyAddresses=_IncludeAddresses, _fullDatas=True , _includeLocked=False)
            '''
            
            #
            #
            #
            # LIST DISPLAY
            #
            
            _listToDisplay = {}
            _cursor=0
            self.itemDataMap = {}
            self.ClearResults()
            self._datacache = {}
            
            
            for row in _listRawAll:
                #print(row)
                
                #print(row)
                rowData = _listRawAll[row]
                
                
                if FILTER_STATUS != '' and FILTER_STATUS!=  'ALL':
                    if rowData['status'] != FILTER_STATUS:
                        continue
                
                
                
                if FILTER_TEXT!= '':
                    _foundinfields=False
                    
                    if str(rowData['description'].lower()).__contains__(FILTER_TEXT.lower()):
                        _foundinfields = True
                      
                        
                    if not _foundinfields:
                        continue    
                
                
                
                
                
                
                
                _icon =  self.allIcons['trade'] 
                if rowData['status'] != 'NOT FOUND':
                    _icon =  self.allIcons[rowData['status']] 
                else:
                    if rowData['cache_type'] == 'SWAP':
                        _icon =  self.allIcons['atomic_swap'] 
                    else:
                        _icon =  self.allIcons['trade'] 
                #print('adding')
                index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),str(row), _icon )
                
                
                #_ac = str(row['account']) if row.__contains__('account') else ""
                
                self.m_listCtrl1.SetItem(index,1, str(rowData['type'].upper()))
                
                '''
                if rowData['type'] == 'buy':
                    _description = f"BUYING {rowData['out_quantity']} {rowData['out_type']}"
                if rowData['type'] == 'sell':
                    _description = f"SELLING {rowData['in_quantity']} {rowData['in_type']}"
                if rowData['type'] == 'trade':
                    _description = f"TRADING {rowData['in_quantity']} {rowData['in_type']}  <-> {rowData['out_quantity']} {rowData['out_type']}"
                '''
                
                _description = rowData['description']
                _unresolved = rowData['unresolved']
                _status = rowData['status']
                
                
                self.m_listCtrl1.SetItem(index,2, _description )
                self.m_listCtrl1.SetItem(index,3, str(len(rowData['order_utxos'])))
                self.m_listCtrl1.SetItem(index,4, str( _unresolved))
                
                self.m_listCtrl1.SetItem(index,5, str(len(rowData['executed_utxos'])))
                self.m_listCtrl1.SetItem(index,6, str(len(rowData['transactions'])))
                self.m_listCtrl1.SetItem(index,7, str(_status))
                
                #print('SetItemData')
                self.m_listCtrl1.SetItemData(index, _cursor)
                
                
                if rowData['type'].lower() == 'buy':
                    #self._totalOut = self._totalOut + float(rowData['in_quantity']).__abs__()
                    self._totalOut = self._totalOut + 1
                    
                    
                
                if rowData['type'].lower() == 'sell':
                    #self._totalIn = self._totalIn + float(rowData['amount']).__abs__()
                    #self._totalIn = self._totalIn.__round__(8)
                    self._totalIn = self._totalIn  +1
                
                if rowData['type'].lower() == 'sell':
                    self._totalFees = self._totalFees +1
                
                
                
                #print('_datacache')
                self._datacache[_cursor] = rowData#str(rowData['txid'])
                self.itemDataMap[_cursor] = (int(row), str(rowData['type']), str(_description), int(len(rowData['order_utxos'])),int(_unresolved) ,int(len(rowData['executed_utxos'])), str(len(rowData['transactions'])), str(_status)  )
                    
                    
                _cursor= _cursor + 1
        
        
            self.m_listCtrl1.SetColumnWidth(0, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(1, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(2, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(3, 75)#wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(4, 75)#wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(5, 75)#wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(6, 75)#wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(7, wx.LIST_AUTOSIZE)
            #self.m_listCtrl1.itemDataMap = self._datacache
            if not self._listInit:
                listmix.ColumnSorterMixin.__init__(self, 8)
                self._listInit = True
                  
            
                
                
                
        #except Exception as e:
        #   self.parent_frame.Log("Unable to load Wallet History infos datas : " + str(e) , type="warning")
                    
        
        
        self.m_textTotalIn.SetValue(str(self._totalIn.__round__(2)))
        self.m_textTotalOut.SetValue(str(self._totalOut.__round__(2)))
        self.m_textFee.SetValue(str(self._totalFees.__round__(2)))
            
        self.HideLoading()        
        self.m_listCtrl1.Thaw()
        self.SetAutoLayout(True)
        self.Layout()    
    
    
    
    
    
    def OnItemSelected(self, event):
        ##print(event.GetItem().GetTextColour())
        print(f"current event  {event.Index}")
        self._currentItem = event.Index
        self._currentItem = self.m_listCtrl1.GetItemData(event.Index)
        print(f"_currentItem  {self._currentItem}")
        itemData = self._datacache[self._currentItem]
        
    def OnRightClick(self, event):
        _data= self._datacache[self._currentItem]
        print(_data)
        #_hasIpfs =  _data['has_ipfs']
        
        #menuAsset = RavencoreAssetRightclickPopupMenu(self, self.parent_frame, _data)    
        
        #menuAsset = RavencoreUTXORightclickPopupMenu(self, self.parent_frame, _data)    
        #menuAsset = RavencoreUTXOHistoryRightclickPopupMenu(self, self.parent_frame, _data)   
        
        
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetListCtrl(self):
        return self.m_listCtrl1
    
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetSortImages(self):
        return (self.allIcons['sort_down_2'], self.allIcons['sort_up_2'])
    
    
    
    def setupListFilter(self):
        ravencoin = self.parent_frame.getRvnRPC()
        try:
            #_allNotAdmins= ravencoin.asset.GetAllMyAssets(_excludeAdmin=True)
            #_allmyAddress = ravencoin.wallet.getAllWalletAddresses()
            pass
            #self.m_filterAddress.Clear()
            #self.m_filterAddress.Append("All UTXO's")
            #for net in _allmyAddress:
            #    self.m_filterAddress.Append(net)
        except Exception as e:
            print('unable to retreive address list')
            
            
        
    
    
    def setupListControl(self):
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "Id"
        self.m_listCtrl1.InsertColumn(0, info)

        info.Align = 0#wx.LIST_FORMAT_RIGHT
        info.Text = "Type"
        self.m_listCtrl1.InsertColumn(1, info)

        info.Align = 0
        info.Text = "Trade Description"
        self.m_listCtrl1.InsertColumn(2, info)
        
        info.Align = 0
        info.Text = "Orders"
        self.m_listCtrl1.InsertColumn(3, info)
        
        info.Align = 0
        info.Text = "Unresolved"
        self.m_listCtrl1.InsertColumn(4, info)
        
        info.Align = 0
        info.Text = "Executed"
        self.m_listCtrl1.InsertColumn(5, info)
        
        info.Align = 0
        info.Text = "Transactions"
        self.m_listCtrl1.InsertColumn(6, info)
        
        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "Status"
        self.m_listCtrl1.InsertColumn(7, info)
        
        
        
        """
            Result RVN
            [                   (array of json object)
              {
                "txid" : "txid",          (string) the transaction id 
                "vout" : n,               (numeric) the vout value
                "address" : "address",    (string) the raven address
                "account" : "account",    (string) DEPRECATED. The associated account, or "" for the default account
                "scriptPubKey" : "key",   (string) the script key
                "amount" : x.xxx,         (numeric) the transaction output amount in RVN
                "confirmations" : n,      (numeric) The number of confirmations
                "redeemScript" : n        (string) The redeemScript if scriptPubKey is P2SH
                "spendable" : xxx,        (bool) Whether we have the private keys to spend this output
                "solvable" : xxx,         (bool) Whether we know how to spend this output, ignoring the lack of keys
                "safe" : xxx              (bool) Whether this output is considered safe to spend. Unconfirmed transactions
                                          from outside keys and unconfirmed replacement transactions are considered unsafe
                                          and are not eligible for spending by fundrawtransaction and sendtoaddress.
              }
              ,...
            ]
            
        """
        
        """
        
        self.m_listCtrl1.SetColumnWidth(0, 350)
        self.m_listCtrl1.SetColumnWidth(1, 100)
        self.m_listCtrl1.SetColumnWidth(2, 100)
        self.m_listCtrl1.SetColumnWidth(3, 100)
        self.m_listCtrl1.SetColumnWidth(4, 100)
        """
        
        self.il = wx.ImageList(16, 16)
        

        self.allIcons['locked'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('lock_icon') )
        self.allIcons['locked_trade'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('lock_pen') )
        self.allIcons['unlocked'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('unlock') )
        
        
        self.allIcons['trade'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('p2p_icon') )
        self.allIcons['atomic_swap'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('atomic_swap') )
        
        
        self.allIcons['COMPLETE'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('task_done') )
        self.allIcons['WAITING'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('task_pending') )
        self.allIcons['UNRESOLVED'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('task_unresolved') )
        self.allIcons['NOT FOUND'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('task_error') )
        self.allIcons['?'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('task_unresolved') )
        
       
        
        self.allIcons['wallet_in_out'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('wallet_in_out') )
        self.allIcons['wallet_in'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('wallet_in') )
        self.allIcons['wallet_out'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('wallet_out') )
        
        self.allIcons['send'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('vout_icon1') )
        self.allIcons['receive'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('vin_icon1') )
        
        
        self.allIcons['RVN'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('ravencoin') )
        self.allIcons['rvn'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('ravencoin') )
        
        self.allIcons['asset'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('asset') )
        self.allIcons['info'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('info_obj') )
        
        self.allIcons['sort_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up') )
        self.allIcons['sort_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down') )
        self.allIcons['sort_up_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up_2') )
        self.allIcons['sort_down_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down_2') )
        
        self.allIcons['alphab_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_up') )
        self.allIcons['alphab_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_co') )
        
        
        
        
        self.m_listCtrl1.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        
        
    def ClearResults(self):
        self.m_listCtrl1.DeleteAllItems()
                            
    
    def ShowLoading(self):
        if self._loadingPanel  == None:
            self._loadingPanel =  wxBackgroundWorkerAnimation(self.m_listCtrl1)
        
        self._loadingPanel.Show(show=True)
        self.Layout()
        
    def HideLoading(self):
        if self._loadingPanel  != None:
            self._loadingPanel.Hide()
            self.Layout()
            