'''
Created on 18 janv. 2022

@author: slinux
'''

'''
Created on 10 janv. 2022

@author: slinux
'''
import threading
import time 

#from .wxRavenP2PMarketDesign import * 
from wxRavenGUI.application.wxcustom import *

#from libs.RVNpyRPC._P2PmarketPlace import 

from .wxRavenRavencoreDesign import wxRaven_RavencoreTxReader


import datetime

import os
import time


class wxRavenP2PMarket_RavencoreTxViewerWithLogic(wxRaven_RavencoreTxReader):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Transactions Viewer"
    view_name = "Transactions Viewer"
    parent_frame = None
    default_position = "main"
    icon = 'inspect_file'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame,  position = "main", viewName= "Transactions Viewer", isInternalPluginView=False, isInternalPanel=False, parentDataObj=None):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Transactions Viewer"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parentFrame
        
        self.isInternalPluginView = isInternalPluginView
        self.isInternalPanel = isInternalPanel
        self.parentDataObj = parentDataObj
        self.allIcons = {}
        
        self._currentTxID = ''
        self._currentTxHEX = ''
        
        self._INPUT_TREAT = False
        
        self.SizerObj= None
        #isInternalPanel= True
        
        
        self.m_toggleBtnVIN.SetBitmap(parentFrame.RessourcesProvider.GetImage('tx_vinout'))
        self.m_toggleBtnDetails.SetBitmap(parentFrame.RessourcesProvider.GetImage('wallet_in_out'))
        self.m_toggleBtnAssetDetails.SetBitmap(parentFrame.RessourcesProvider.GetImage('asset_trade'))
        
        self.setupInputOutputTable()
        self.setupInputOutputAssetTable()
        
        
        self.m_txDetailsAdvanced.Hide()
        self.m_txDetailsPanel.Hide()
        self.m_txDetailsPanel1.Hide()
        
        if isInternalPanel:
            pass
            
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
            #w, h = self.GetSize()
            #w = h
            #panel.SetSize(w, h)
            
            #self.Fit()
            #self.Sizer = wx.BoxSizer( wx.VERTICAL )
            #self.Sizer .Add( self._Panel, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.setupPanel()
        #self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
        #self.Fit()
        try:
            self.parent.ResizeDialog()
        except Exception as e:
            pass
        self.Layout()
        
        
    def LockPanel(self, locking): 
        print('pannel locked to avoid user modifications')
        
        if    locking:
            self.Enable(enable=False)
        else:
            self.Enable(enable=True)
        
        
    def setupPanel(self):
        ravencoin = self.parent_frame.getRvnRPC()
        if not ravencoin.test_rpc_status():
            UserError(self.parent_frame, "You must have an active connexion !")
        
        
     
    def OnToggleChanged(self, evt):
        
        
        _showVins= self.m_toggleBtnVIN.GetValue()
        _showDetails = self.m_toggleBtnDetails.GetValue()
        _showAssets = self.m_toggleBtnAssetDetails.GetValue()
        
        
        
        
        if _showVins:
            self.m_txDetailsAdvanced.Show()
        else:
            self.m_txDetailsAdvanced.Hide()
            
            
        if _showDetails:
            self.m_txDetailsPanel.Show()
        else:
            self.m_txDetailsPanel.Hide()
            
            
        if _showAssets:
            self.m_txDetailsPanel1.Show()
        else:
            self.m_txDetailsPanel1.Hide()
            
        
        if not _showAssets and  not _showVins and  not _showDetails :
            self.m_scrolledWindow1.Hide()
        else:
            self.m_scrolledWindow1.Show()
            
        
        #self.m_scrolledWindow1.FitInside()
        #self.FitInside()
        
        #self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
        try:
            pass
            #self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
            #self.Fit()
            #self.parent.ResizeDialog()
        except Exception as e:
            pass
        self.Layout()
        
        
    def setupInputTable(self):
        
        
        pass
    
    
    
    
    def setupOutputTable(self):
        
        pass    
        
    
    
    
    def setupInputOutputTable(self):
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "Address"
        self.m_listCtrlInputs.InsertColumn(0, info)
        self.m_listCtrOutputs.InsertColumn(0, info)

        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "Quantity"
        self.m_listCtrlInputs.InsertColumn(1, info)
        self.m_listCtrOutputs.InsertColumn(1, info)
        
        self.il = wx.ImageList(16, 16)
        
        self._curColumnSort = 0
        
        self.allIcons['wallet'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('wallet') )
        
        self.allIcons['asset'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('asset') )
        self.allIcons['rvn'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('ravencoin') )
        
        self.allIcons['sort_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up') )
        self.allIcons['sort_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down') )
        self.allIcons['sort_up_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up_2') )
        self.allIcons['sort_down_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down_2') )
        
        self.allIcons['alphab_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_up') )
        self.allIcons['alphab_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_co') )
        
        
        self.m_listCtrlInputs.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        self.m_listCtrOutputs.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
    
    
    
    
    def setupInputOutputAssetTable(self):
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "Address"
        self.m_listCtrlInputs1.InsertColumn(0, info)
        self.m_listCtrOutputs1.InsertColumn(0, info)

        info.Text = "Asset"
        self.m_listCtrlInputs1.InsertColumn(1, info)
        self.m_listCtrOutputs1.InsertColumn(1, info)


        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "Quantity"
        self.m_listCtrlInputs1.InsertColumn(2, info)
        self.m_listCtrOutputs1.InsertColumn(2, info)
    
        
        self.m_listCtrlInputs1.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        self.m_listCtrOutputs1.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        '''
        self.m_AdAssetChoice.Clear()
        #self.m_AdAssetChoice_Receive.Clear()
        
        
        _allAdmins= ravencoin.asset.GetAllMyAssets()
        _allNotAdmins= ravencoin.asset.GetAllMyAssets(_excludeAdmin=True)
        #print(_allAdmins)
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        
        for key in _allAdmins:
            
            self.m_AdAssetChoice.Append(key)
        
        '''
    
    
    
    
    def OnHexTextChanged(self, evt):
        if self._INPUT_TREAT:
            return
        self._INPUT_TREAT = True
        print("OnHexTextChanged")
        self._currentTxHEX = str(self.m_HEXText.GetValue())
        
        
        self.m_txIdText.SetValue("")
        #print("OnHexTextChanged")
        if self._currentTxHEX  != '':
            self._currentTxID = ''      
        
        self._INPUT_TREAT = False
        
        
        self.UpdateView()
    
    
    
    def SetTxId(self, txid):
        self.m_txIdText.SetValue(txid)
        
    
    def OnTxIdChanged(self, evt):
        if self._INPUT_TREAT:
            return
        self._INPUT_TREAT = True
        print("OnTxIdChanged")
        self._currentTxID = str(self.m_txIdText.GetValue())
        
        
        self.m_HEXText.SetValue('')
        if self._currentTxID  != '':
            self._currentTxHEX = ''
            
        #self.m_AssetNameTxt.SetValue(self._currentName)
        #self.computeAssetFullName()
        self._INPUT_TREAT = False
    
    
        self.UpdateView()
    
    
    
    
    def OnGenerateAtomicSwap(self, evt):
        #
        # Todo all checks
        #
        pass
        '''
        _synthesis = 'Atomic Swap Datas'
        _userQuestion = UserQuestion(self, f"Generate the {_synthesis} ?")
        
        
        
        if _userQuestion:
            ravencoin = self.parent_frame.getRvnRPC()
            
            passw=''
            if ravencoin.wallet.__requires_unlock__():
                passw = RequestUserWalletPassword(self)
            
            _AdWithDatas=ravencoin.p2pmarket.CreateAtomicSwapTransaction(self._newAdObject, passw)
            
            
            if _AdWithDatas != None:
                self._newAdObject = _AdWithDatas
                self.m_txDatas.SetValue(str(self._newAdObject._adTxDatas))
                
                #UserInfo(self, str(self._newAdObject._adTxDatas) )
            else:
                UserError(self, "Error, cannot create atomic swap.")
        '''
    
    
    def ClearTx(self):
        self.m_hashText.SetValue('')
        self.m_timestampText.SetValue('')
        self.m_locktimeText.SetValue('')
        self.m_ConfirmationsText.SetValue('')
        
        #
        # clear lisrs
        #
        
        self.m_VINsText.SetValue('')
        self.m_VOUTsText.SetValue('')
        

    
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        
        self.ClearTx()
        self.UpdateDataFromPluginDatas()
        self.Layout()
        #self.setupPanel()
    
    
    
    
    
    
    def ShowDecodeTx(self):
        #self.m_txDetailsPanel.Hide()
        #self.m_txDetailsAdvanced.Show()
        
        
        self._INPUT_TREAT = True
        
        
        self.m_txIdText.SetValue(self.LastDecode['txid'])
        self.m_hashText.SetValue(self.LastDecode['hash'])
        
        
        
        #blockhash
        #blocktime
        #blockhash
        #confirmations
        
        
        #details
        #asset_details
        
        self.m_VINsText.SetValue(str(self.LastDecode['vin']))
        self.m_VOUTsText.SetValue(str(self.LastDecode['vout']))
        
       
        
        self._INPUT_TREAT = False
    
        
        
        
    
    
    
    def ShowTx(self):
        #self.m_txDetailsPanel.Show()
        #self.m_txDetailsAdvanced.Show()
    
    
        self._INPUT_TREAT = True
        
        
        self.m_txIdText.SetValue(self.LastTx['txid'])
        #self.m_hashText.SetValue(self.LastTx['blockhash'])
        
        _time = '???'
        _fee = '???'
        _confs = '???'
        if  self.LastTx.__contains__('blocktime'):
            _time =  datetime.datetime.fromtimestamp(self.LastTx['blocktime']).strftime('%Y-%m-%d %H:%M:%S')
        
        
        if  self.LastTx.__contains__('fee'):
            _fee = str(self.LastTx['fee'].__abs__())
            
        if  self.LastTx.__contains__('confirmations'):
            _confs = str(self.LastTx['confirmations'].__abs__())
            
            
        self.m_timestampText.SetValue(_time)
        self.m_locktimeText.SetValue(_fee)
        self.m_ConfirmationsText.SetValue(_confs)
        
        
        
        self.LoadTxDetailsTableDatas(self.m_listCtrlInputs, self.m_sentPanel, "send")
        self.LoadTxDetailsTableDatas(self.m_listCtrOutputs, self.m_ReceivedPanel, "receive")
        
        self.LoadTxDetailsAssetTableDatas(self.m_listCtrlInputs1, self.m_sentPanel1, "send")
        self.LoadTxDetailsAssetTableDatas(self.m_listCtrOutputs1, self.m_ReceivedPanel1, "receive")
        
        
        #blockhash
        #blocktime
        #blockhash
        #confirmations
        
        
        #details
        #asset_details
        
        self.m_HEXText.SetValue(self.LastTx['hex'])
        
        #hex
        
        self._INPUT_TREAT = False
    
            
            
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        if True:
        #try:
            
            ravencoin = self.parent_frame.getRvnRPC()
            
            #self.LastTx= None
            
            if self._currentTxID  != '':
                self.LastTx = ravencoin.utils.GetTransaction(self._currentTxID )
                print("GetTX")
                print(self.LastTx)
                if self.LastTx != None:
                    self.ShowTx()
                    
                    
                    self.LastDecode = ravencoin.utils.DecodeTransaction(self.LastTx['hex'] )
                    if self.LastDecode != None:
                        self.ShowDecodeTx()
               
                    
                    
                    
                    
                else:
                    self.parent_frame.Log("Unable to load transaction datas" , type="warning")
                
            
            
            
            
                
            elif self._currentTxHEX!= '':
                
                
                self.LastDecode = ravencoin.utils.DecodeTransaction(self._currentTxHEX )
                print("DECODE")
                print(self.LastDecode)
                
                if self.LastDecode != None:
                    self.ShowDecodeTx()
                    
                    
                    self.LastTx = ravencoin.utils.GetTransaction(self.LastDecode['txid'] )
                    if self.LastTx != None:
                        self.ShowTx()
                    
                    
                    
                else:
                    self.parent_frame.Log("Unable to decode transaction " , type="warning")
                
                
            #myPluginData = self.parent_frame.GetPluginData("Tutorial","myPluginData2")
            #myPluginSetting =  self.parent_frame.GetPluginSetting("Tutorial","booleansetting")#SavePanelSettings GetPluginSetting
            #
            #Update your panel
            #       
            
            
            #textToPrint = " booleansetting = " + str(myPluginSetting)
            #textToPrint = textToPrint + "\n\n myPluginData2 = " + str(myPluginData)
             
            #self.m_staticText2.SetLabel(str(textToPrint)) 
            pass
             
                
        #except Exception as e:
        #    self.parent_frame.Log("Unable to load transaction datas" , type="warning")
                    
    
    
    
            
    def LoadTxDetailsTableDatas(self, list, panel, category='send'):
        
        
        list.Freeze()
        panel.itemDataMap={}
        panel.cursor = 0
        
        
        list.DeleteAllItems()
        
        for _det in self.LastTx['details']:
            if _det['category'] != category:
                continue
            
            
            index = list.InsertItem(list.GetItemCount(),str(_det['address']), self.allIcons['rvn'] )
            list.SetItem(index,1, str(_det['amount'].__abs__()))
            list.SetItemData(index, panel.cursor)
            panel.itemDataMap[panel.cursor] = ( str(_det['address'] ),str( _det['amount'].__abs__() ) )
                                                
            panel.cursor = panel.cursor+1
        
        
        
        
        
        
               
        list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        list.SetColumnWidth(1, 100)      
        
        panel.list= list
        panel.allIcons = self.allIcons
        listmix.ColumnSorterMixin.__init__(panel, 2)
        listmix.ColumnSorterMixin.SortListItems(panel, col=1, ascending=0)
        
        list.Thaw()
        self.Layout() 
    
    
    
    def LoadTxDetailsAssetTableDatas(self, list, panel, category='send'):
        
        
        list.Freeze()
        panel.itemDataMap={}
        panel.cursor = 0
        
        
        list.DeleteAllItems()
        
        for _det in self.LastTx['asset_details']:
            if _det['category'] != category:
                continue
            
            
            index = list.InsertItem(list.GetItemCount(),str(_det['destination']), self.allIcons['asset'] )
            list.SetItem(index,1, str(_det['asset_name']))
            list.SetItem(index,2, str(_det['amount'].__abs__()))
            list.SetItemData(index, panel.cursor)
            panel.itemDataMap[panel.cursor] = ( str(_det['destination'] ),str(_det['asset_name']),str( _det['amount'].__abs__() ) )
                                                
            panel.cursor = panel.cursor+1
        
        
        
        
        
        
               
        list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        list.SetColumnWidth(2, 150)      
        
        panel.list= list
        panel.allIcons = self.allIcons
        listmix.ColumnSorterMixin.__init__(panel, 3)
        listmix.ColumnSorterMixin.SortListItems(panel, col=2, ascending=0)
        
        list.Thaw()
        self.Layout()     