'''
Created on 20 janv. 2022

@author: slinux
'''


from .wxRavenRavencoreDesign import *
import threading
import time 

from wxRavenGUI.application.wxcustom.CustomLoading import *
import wx.lib.mixins.listctrl as listmix 
from .wxRavenRavencore_UTXOManager_ListRightClickMenu import *
from .wxRavenRavencore_UTXOManager_TxHistoryRightClickMenu import *
from datetime import date
import datetime


class wxRavenRavencore_UTXOManagerLogic(wxRaven_RavencoreUTXOManager):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Wallet"
    view_name = "Wallet"
    parent_frame = None
    default_position = "main"
    icon = 'wallet'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, position = "main", viewName= "Wallet", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Wallet"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self._allTabs= {}
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
        
        #self.LoadSearchOptions()
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
    
    
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.waitApplicationReady()
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.setupPanels,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
    
     
    
    def setupPanels(self, evt=None):
        self.createUtxoPanels()
        self.createTxHistoryPanel()
        
        self.createAddinsPanels()
        
    
     
    def createUtxoPanels(self, evt=None):
        
        
        _rvnUTXOPanel = wxRavenRavencore_UTXOManager_RVN_ViewLogic(self, self.parent_frame, isInternalPluginView=True)
        _icon = self.parent_frame.RessourcesProvider.GetImage('ravencoin')
        self.m_auinotebook1.AddPage(_rvnUTXOPanel, "Wallet UTXO's", bitmap = _icon)
        self._allTabs["Wallet UTXO's"] = _rvnUTXOPanel
        
        
        self.Layout()
        
        
    def createTxHistoryPanel(self, evt=None):   
        
        _rvnHistoryPanel = wxRavenRavencore_UTXOManager_HISTORY_ViewLogic(self, self.parent_frame, isInternalPluginView=True)
        _icon = self.parent_frame.RessourcesProvider.GetImage('calendar_icon')
        self.m_auinotebook1.AddPage(_rvnHistoryPanel, "Transactions History", bitmap = _icon)
        self._allTabs["Transactions History"] = _rvnHistoryPanel
        
        
        self.Layout() 
    
    def createAddinsPanels(self, evt=None):
        ravencorep = self.parent_frame.GetPlugin("Ravencore")
        _adds_callbacks = ravencorep.getData("_utxo_manager_views_addons_callbacks") 
        
        
        for cb in _adds_callbacks:
            try:
                cb()
            except Exception as e:
                self.parent_frame.Log("Unable to load UTXO addins tab: " + str(e) , type="warning")
                
                
            
    
    def createNewPluginPanel(self, panelName, panelClass, pannelIcon):    
        
        if not self._allTabs.__contains__(panelName):
            _Panel = panelClass(self, self.parent_frame, isInternalPluginView=True)
            _icon = self.parent_frame.RessourcesProvider.GetImage(pannelIcon)
            self.m_auinotebook1.AddPage(_Panel, panelName, bitmap = _icon)
            self._allTabs[panelName] = _Panel
        
        
        self.Layout() 
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        
        self.UpdateDataFromPluginDatas()
        self.Layout()
            
            
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        if True:
        #try:
            
            
            for t in self._allTabs:
                
                if True:
                #try:
                    self._allTabs[t].UpdateView()
                #except Exception as e:
                #    self.parent_frame.Log("Unable to UpdateView for tab : " + str(t) , type="warning")   
            #ravencoin = self.parent_frame.getRvnRPC()
            
            #myPluginData = self.parent_frame.GetPluginData("Tutorial","myPluginData2")
            #myPluginSetting =  self.parent_frame.GetPluginSetting("Tutorial","booleansetting")#SavePanelSettings GetPluginSetting
            #
            #Update your panel
            #       
            #_netinfos = ravencoin.network.GetNetworkInfos()
            
            #if _netinfos != None:
            #    self.m_textCtrl30.SetValue(str(_netinfos['blocks']))
            #    self.m_textCtrl3011.SetValue(str(_netinfos['difficulty'][2]))
            #    self.m_textCtrl301.SetValue(str(_netinfos['networkhashps'][2]))
            #textToPrint = " booleansetting = " + str(myPluginSetting)
            #textToPrint = textToPrint + "\n\n myPluginData2 = " + str(myPluginData)
             
            #self.m_staticText2.SetLabel(str(textToPrint)) 
            
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
             
                
        #except Exception as e:
        #    self.parent_frame.Log("Unable to UpdateView for tab: " + str(e) , type="warning")
                    
            
            
















class wxRavenRavencore_UTXOManager_RVN_ViewLogic(wxRaven_RavencoreUTXOManager_RVN_View, listmix.ColumnSorterMixin):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Wallet UTXO's"
    view_name = "Wallet UTXO's"
    parent_frame = None
    default_position = "main"
    icon = 'wallet'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent,  parentFrame, position = "main", viewName= "Wallet UTXO's", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        self.parent=parent
        self.view_base_name = "Wallet UTXO's"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.allIcons  = {}
        self.itemDataMap = {}
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
        
        
        
        self.setupListFilter()
        self.setupListControl()
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.m_listCtrl1)
        self.m_listCtrl1.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)
        self.m_listCtrl1.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OnRightClick)
        
        self.m_filterAddress.Bind(wx.EVT_CHOICE, self.ChangeMode)
        self.m_showLocked.Bind(wx.EVT_CHECKBOX, self.UpdateView)
        self.m_showUnlock.Bind(wx.EVT_CHECKBOX, self.UpdateView)
        self.m_addressFilterText.Bind(wx.EVT_TEXT, self.UpdateView)
        
        
        self.waitApplicationReady()
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.DoRequestUpdateUTXO,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
    
    
    def DoRequestUpdateUTXO(self, evt=None):
        myPlugin = self.parent_frame.GetPlugin('Ravencore')
        myPlugin.OnUTXORequested_T()
        self.ShowLoading()
    
    
    
    
    def ChangeMode(self, evt):
        
        _filterAdressValue = self.m_filterAddress.GetString(self.m_filterAddress.GetCurrentSelection())
        #self.m_addressFilterText.SetValue('')
        
        _colText= "Account"
        
        if  _filterAdressValue == "RVN":
            self.m_bitmap34.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('ravencoin'))
            
            
        elif  _filterAdressValue == "ASSETS":
            self.m_bitmap34.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('asset'))  
            _colText= "Asset"
        
        
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = _colText
        self.m_listCtrl1.SetColumn(2, info)
        
        self.m_addressFilterText.SetValue('')  
          
            
        self.UpdateView(None)  
        
        
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
        
        if True:
        #try:
            
            '''
            ravencoin = self.parent_frame.getRvnRPC()
            _filterAdressValue = self.m_filterAddress.GetString(self.m_filterAddress.GetCurrentSelection())
            '''
            _IncludeAddresses = []
            _ExlcudeAddresses = []
            
            '''
            if _filterAdressValue != "All UTXO's":
                _IncludeAddresses.append(_filterAdressValue)
            '''
            
            _filterText = self.m_addressFilterText.GetValue()
            
            
            _showLocked = self.m_showLocked.GetValue()
            _showUnlocked = self.m_showUnlock.GetValue()
            
            
            _filterTYPEValue = self.m_filterAddress.GetString(self.m_filterAddress.GetCurrentSelection())
            
            _listRawAll = self.parent_frame.GetPluginData('Ravencore', '_AllUTXOs')
            _listRaw = _listRawAll[_filterTYPEValue]
            
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
            
            
            for row in _listRaw:
                #print(row)
                _locked = row['locked']
                _icon = "rvn"
                if _filterTYPEValue == 'ASSETS':
                    _icon = "asset"
                
                _firstCol = 'No'
                if _locked:
                    _icon = "locked"
                    _firstCol = 'Yes'
                    
                    
                if   not _showLocked and   _locked:
                    
                    continue
                
                if   not _showUnlocked and  not _locked:
                    continue    
                
                _address= row['address']
                
                if len(_IncludeAddresses) > 0:
                    if not _IncludeAddresses.__contains__(_address):
                        continue
                
                
                if len(_ExlcudeAddresses) > 0:
                    if _ExlcudeAddresses.__contains__(_address):
                        continue
                
                
                _ac = str(row['account']) if row.__contains__('account') else ""
                
                if _filterText!= '':
                    _foundinfields=False
                    
                    if str(row['address']).__contains__(_filterText):
                        _foundinfields = True
                
                    if str(_ac).__contains__(_filterText):
                        _foundinfields = True
                    
                    if str(row['txid']).__contains__(_filterText):
                        _foundinfields = True
                         
                    if str(row['amount']).__contains__(_filterText):
                        _foundinfields = True
                             
                        
                    if not _foundinfields:
                        continue    
                        
                    
                #print(row)
                index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),_firstCol, self.allIcons[_icon] )
                
                
                #_ac = str(row['account']) if row.__contains__('account') else ""
                
                self.m_listCtrl1.SetItem(index,1, str(row['amount']))
                
                
                self.m_listCtrl1.SetItem(index,2, str(_ac) )
                self.m_listCtrl1.SetItem(index,3, str(row['address']))
                self.m_listCtrl1.SetItem(index,4, str(row['confirmations']))
                self.m_listCtrl1.SetItem(index,5, str(row['txid']))
                self.m_listCtrl1.SetItem(index,6, str(row['vout']))
                
                self.m_listCtrl1.SetItemData(index, _cursor)
                
                self._datacache[_cursor] = row
                self.itemDataMap[_cursor] = (str(_firstCol), float(row['amount']), str(_ac), str(row['address']) ,int(row['confirmations']), str(row['txid']),int(row['vout']) )
                    
                    
                _cursor= _cursor + 1
        
        
            self.m_listCtrl1.SetColumnWidth(0, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(1, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(2, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(3, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(5, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(6, 25)
            
            #self.m_listCtrl1.itemDataMap = self._datacache
            listmix.ColumnSorterMixin.__init__(self, 7)
                  
            
                
                
                
        #except Exception as e:
        #    self.parent_frame.Log("Unable to load RVN UTXO infos datas : " + str(e) , type="warning")
                    
            
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
        #_hasIpfs =  _data['has_ipfs']
        
        #menuAsset = RavencoreAssetRightclickPopupMenu(self, self.parent_frame, _data)    
        menuAsset = RavencoreUTXORightclickPopupMenu(self, self.parent_frame, _data)    
        
        
        
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
        info.Text = "Locked"
        self.m_listCtrl1.InsertColumn(0, info)

        info.Align = 0#wx.LIST_FORMAT_RIGHT
        info.Text = "Amount"
        self.m_listCtrl1.InsertColumn(1, info)

        info.Align = 0
        info.Text = "Account"
        self.m_listCtrl1.InsertColumn(2, info)
        
        info.Align = 0
        info.Text = "Address"
        self.m_listCtrl1.InsertColumn(3, info)
        
        info.Align = 0
        info.Text = "Confirmations"
        self.m_listCtrl1.InsertColumn(4, info)
        
        info.Align = 0
        info.Text = "Txid"
        self.m_listCtrl1.InsertColumn(5, info)
        
        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "Vout"
        self.m_listCtrl1.InsertColumn(6, info)
        
        
        
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
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
import wx.adv



class wxRavenRavencore_UTXOManager_HISTORY_ViewLogic(wxRaven_RavencoreUTXOManager_TxHistory_View, listmix.ColumnSorterMixin):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Transactions History"
    view_name = "Transactions History"
    parent_frame = None
    default_position = "main"
    icon = 'calendar_icon'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent,  parentFrame, position = "main", viewName= "Transactions History", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        self.parent=parent
        self.view_base_name = "Transaction History"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.allIcons  = {}
        self.itemDataMap = {}
        
        self._totalIn = 0.0
        self._totalOut = 0.0
        self._totalFees = 0.0
        
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
        
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.m_listCtrl1)
        self.m_listCtrl1.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)
        self.m_listCtrl1.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OnRightClick)
        
        
        self.m_addressFilterText.Bind(wx.EVT_TEXT, self.UpdateView)
        
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
        
        
        
        self.m_addressFilterText.Bind(wx.EVT_TEXT, self.UpdateView)
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
        myPlugin = self.parent_frame.GetPlugin('Ravencore')
        
        myPlugin.OnHISTORYRequested_T()
        self.ShowLoading()
        
    
    
    def StartDateChanged(self, evt):
        d = self.m_datePicker1.GetValue()
        if self.m_startDCheck.GetValue():
            myPlugin = self.parent_frame.GetPlugin('Ravencore')  
            myPlugin.setData("_tx_history_start", d)    
            #self.DoRequestUpdateHistory()
   
   
            
    def StopDateChanged(self, evt):
        
        d = self.m_datePicker2.GetValue()
        if self.m_stopDCheck.GetValue():
            myPlugin = self.parent_frame.GetPlugin('Ravencore')  
            myPlugin.setData("_tx_history_stop", d)    
            #self.DoRequestUpdateHistory()    
        
        
    def ChangeMode(self, evt):
        
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
            
        
        '''
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = _colText
        self.m_listCtrl1.SetColumn(2, info)
        '''
            
        self.m_addressFilterText.SetValue('')  
        
        
        myPlugin = self.parent_frame.GetPlugin('Ravencore')  
        myPlugin.setData("_tx_history_category", str(_type_filter) )    
        #self.DoRequestUpdateHistory()
        #self.UpdateView(None)  
    
    
    
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
            
            _filterText = self.m_addressFilterText.GetValue()
            
            
            #_showLocked = self.m_showLocked.GetValue()
            #_showUnlocked = self.m_showUnlock.GetValue()
            
            
            #_filterTYPEValue = self.m_filterAddress.GetString(self.m_filterAddress.GetCurrentSelection())
            
            _listRawAll = self.parent_frame.GetPluginData('Ravencore', '_tx_history')
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
                
                
                
                if _filterText != '':
                    
                    
                    
                    _foundinfields=False
                    
                    if str(rowData['address']).__contains__(_filterText):
                        _foundinfields = True
                
                    if str(rowData['address']).__contains__(_filterText):
                        _foundinfields = True
                    
                    if str(rowData['txid']).__contains__(_filterText):
                        _foundinfields = True
                         
                    if str(rowData['amount']).__contains__(_filterText):
                        _foundinfields = True
                        
                    if rowData.__contains__('fee'):
                        if str(rowData['amount']).__contains__(_filterText):
                            _foundinfields = True
                    
                    if str(rowData['blocktime']).__contains__(_filterText):
                        _foundinfields = True
                        
                    if str(rowData['datetime']).__contains__(_filterText):
                        _foundinfields = True
                        
                                     
                        
                    if not _foundinfields:
                        continue    
                
                
                
                
                
                
                #print('adding')
                index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),str(row), self.allIcons[rowData['category']] )
                
                
                #_ac = str(row['account']) if row.__contains__('account') else ""
                
                self.m_listCtrl1.SetItem(index,1, str(rowData['category']))
                
                _fee = 0.0
                if rowData.__contains__('fee'):
                    _fee = rowData['fee']
                
                self.m_listCtrl1.SetItem(index,2, str(rowData['address']) )
                self.m_listCtrl1.SetItem(index,3, str(rowData['amount']))
                self.m_listCtrl1.SetItem(index,4, str(_fee))
                
                self.m_listCtrl1.SetItem(index,5, str(rowData['blocktime']))
                self.m_listCtrl1.SetItem(index,6, str(rowData['datetime']))
                self.m_listCtrl1.SetItem(index,7, str(rowData['txid']))
                
                #print('SetItemData')
                self.m_listCtrl1.SetItemData(index, _cursor)
                
                
                if rowData['category'] == 'send':
                    self._totalOut = self._totalOut + float(rowData['amount']).__abs__()
                    self._totalOut = self._totalOut.__round__(8)
                    
                    self._totalFees = self._totalFees  + float(_fee).__abs__()
                    self._totalFees = self._totalFees.__round__(8)
                    
                    
                
                if rowData['category'] == 'receive':
                    self._totalIn = self._totalIn + float(rowData['amount']).__abs__()
                    self._totalIn = self._totalIn.__round__(8)
                
                
                
                
                
                
                
                #print('_datacache')
                self._datacache[_cursor] = rowData#str(rowData['txid'])
                self.itemDataMap[_cursor] = (int(row), str(rowData['category']), str(rowData['address']), float(rowData['amount']),float(_fee) ,int(rowData['blocktime']), str(rowData['datetime']), str(rowData['txid'])  )
                    
                    
                _cursor= _cursor + 1
        
        
            self.m_listCtrl1.SetColumnWidth(0, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(1, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(2, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(3, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(4, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(5, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(6, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(7, wx.LIST_AUTOSIZE)
            #self.m_listCtrl1.itemDataMap = self._datacache
            listmix.ColumnSorterMixin.__init__(self, 8)
                  
            
                
                
                
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
        menuAsset = RavencoreUTXOHistoryRightclickPopupMenu(self, self.parent_frame, _data)   
        
        
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
        info.Text = "Address"
        self.m_listCtrl1.InsertColumn(2, info)
        
        info.Align = 0
        info.Text = "Amount"
        self.m_listCtrl1.InsertColumn(3, info)
        
        info.Align = 0
        info.Text = "Fee"
        self.m_listCtrl1.InsertColumn(4, info)
        
        info.Align = 0
        info.Text = "Blocktime"
        self.m_listCtrl1.InsertColumn(5, info)
        
        info.Align = 0
        info.Text = "Datetime"
        self.m_listCtrl1.InsertColumn(6, info)
        
        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "TxId"
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
            