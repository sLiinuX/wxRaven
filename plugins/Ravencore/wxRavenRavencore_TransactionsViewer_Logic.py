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

from .wxRavenRavencoreDesign import wxRaven_Ravencore_TxViewer

from .wxRavenRavencoreDesign import wxRaven_Ravencore_TxViewer_Asset_Panel
from .wxRavenRavencoreDesign import wxRaven_Ravencore_TxViewer_HEX_Panel
from .wxRavenRavencoreDesign import wxRaven_Ravencore_TxViewer_VINOUT_Panel , wxRaven_Ravencore_TxViewer_VINOUT_List_Panel
from .wxRavenRavencoreDesign import wxRaven_Ravencore_TxViewer_RVN_Panel

import datetime

import os
import time

from .jobs import *


class wxRavenP2PMarket_RavencoreTxViewerWithLogic(wxRaven_Ravencore_TxViewer ):
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
        
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        
        self.isInternalPluginView = isInternalPluginView
        self.isInternalPanel = isInternalPanel
        self.parentDataObj = parentDataObj
        self.allIcons = {}
        
        
        self._currentTxID = ''
        self._currentTxHEX = ''
        
        self._INPUT_TREAT = False
        
        self.SizerObj= None
        
        self._Tab_HexDecode = None
        self._Tab_RvnDecode = None
        self._Tab_AssetDecode = None
        self._Tab_VinoutsDecode = None
        self._Tab_VinoutsDecodeDetails = None
        #isInternalPanel= True
        
        '''
        self.m_toggleBtnVIN.SetBitmap(parentFrame.RessourcesProvider.GetImage('tx_vinout'))
        self.m_toggleBtnDetails.SetBitmap(parentFrame.RessourcesProvider.GetImage('wallet_in_out'))
        self.m_toggleBtnAssetDetails.SetBitmap(parentFrame.RessourcesProvider.GetImage('asset_trade'))
        
        self.setupInputOutputTable()
        self.setupInputOutputAssetTable()
        
        self.m_txDetailsAdvanced.Hide()
        self.m_txDetailsPanel.Hide()
        self.m_txDetailsPanel1.Hide()
        '''
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
        '''
        self.waitApplicationReady()
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.createUtxoPanels,))
        t.start()
        
    
        
            
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
        
    '''
        
            
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
            
        print('setup pannel')
        
        self._Tab_HexDecode = self.__SetupDynamicPanel__(wxRaven_Ravencore_TxViewer_HEX_PanelLogic)
        self._Tab_HexDecode.m_HEXText.Bind( wx.EVT_TEXT, self.OnHexTextChanged )
        
        
        
        self._Tab_VinoutsDecode = self.__SetupDynamicPanel__(wxRaven_Ravencore_TxViewer_VINOUT_PanelLogic)
        self._Tab_VinoutsDecodeDetails = self.__SetupDynamicPanel__(wxRaven_Ravencore_TxViewer_VINOUT_List_PanelLogic)
        
        self._Tab_RvnDecode = self.__SetupDynamicPanel__(wxRaven_Ravencore_TxViewer_RVN_PanelLogic)
        self._Tab_AssetDecode = self.__SetupDynamicPanel__(wxRaven_Ravencore_TxViewer_Asset_PanelLogic)
        
        
        self._Tab_VinoutsDecodeDetails.m_sentPanel._listInit = False
        self._Tab_VinoutsDecodeDetails.m_ReceivedPanel._listInit = False
        self._Tab_AssetDecode.m_sentPanel1._listInit = False
        self._Tab_AssetDecode.m_ReceivedPanel1._listInit = False
        self._Tab_RvnDecode.m_ReceivedPanel._listInit = False
        self._Tab_RvnDecode.m_sentPanel._listInit = False
        
        
        self.setupInputOutputTable()
        self.setupInputOutputAssetTable()
        
        
        self.setupVinVoutTable()
        
        self.Layout()
        #self._Tab_HexDecode = wxRaven_Ravencore_TxViewer_HEX_PanelLogic(parent, parentFrame, )
        #self._Tab_RvnDecode = None
        #self._Tab_AssetDecode = None
        #self._Tab_VinoutsDecode = None    
        
    
    
    def __SetupDynamicPanel__(self, _panelClass):
        _tabPanel = _panelClass(self, self.parent_frame, ) 
        _icon = self.parent_frame.RessourcesProvider.GetImage(_tabPanel.icon)
        self.m_auinotebook2.AddPage(_tabPanel, _tabPanel.view_name, bitmap = _icon)
        
        return _tabPanel
        '''
        self._Tab_HexDecode = wxRaven_Ravencore_TxViewer_HEX_PanelLogic(self, self.parentFrame, )   
        _icon = self.parent_frame.RessourcesProvider.GetImage(self._Tab_HexDecode.icon)
        self.m_auinotebook1.AddPage(_rvnUTXOPanel, "Wallet UTXO's", bitmap = _icon)
        self._allTabs["Wallet UTXO's"] = _rvnUTXOPanel
        
        '''
     
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
        
    
    
    
    
    
    
    
    
    def setupVinVoutTable(self):
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "txid"
        self._Tab_VinoutsDecodeDetails.m_listCtrlInputs.InsertColumn(0, info)
        #self._Tab_VinoutsDecodeDetails.m_listCtrOutputs.InsertColumn(0, info)

        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "vout"
        self._Tab_VinoutsDecodeDetails.m_listCtrlInputs.InsertColumn(1, info)
        
        
        
        
        
        
        
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "id"
        self._Tab_VinoutsDecodeDetails.m_listCtrOutputs.InsertColumn(0, info)
        #self._Tab_VinoutsDecodeDetails.m_listCtrOutputs.InsertColumn(0, info)

        info.Align = 0
        info.Text = "value"
        self._Tab_VinoutsDecodeDetails.m_listCtrOutputs.InsertColumn(1, info)
        
        
        info.Align = 0
        info.Text = "type"
        self._Tab_VinoutsDecodeDetails.m_listCtrOutputs.InsertColumn(2, info)
        
        
        info.Align = 0
        info.Text = "address"
        self._Tab_VinoutsDecodeDetails.m_listCtrOutputs.InsertColumn(3, info)
        
        info.Align = 0
        info.Text = "more"
        self._Tab_VinoutsDecodeDetails.m_listCtrOutputs.InsertColumn(4, info)
        
        #info.Align = wx.LIST_FORMAT_RIGHT
        #info.Text = "scriptSig"
        #self._Tab_VinoutsDecodeDetails.m_listCtrlInputs.InsertColumn(1, info)
        #self._Tab_VinoutsDecodeDetails.m_listCtrOutputs.InsertColumn(1, info)
        
        
        
        '''
        
        self.il = wx.ImageList(16, 16)
        
        self._Tab_VinoutsDecodeDetails._curColumnSort = 0
        
        self.allIcons['wallet'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('wallet') )
        
        self.allIcons['asset'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('asset') )
        self.allIcons['rvn'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('ravencoin') )
        
        self.allIcons['sort_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up') )
        self.allIcons['sort_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down') )
        self.allIcons['sort_up_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up_2') )
        self.allIcons['sort_down_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down_2') )
        
        self.allIcons['alphab_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_up') )
        self.allIcons['alphab_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_co') )
        
        '''
        self._Tab_VinoutsDecodeDetails.m_listCtrlInputs.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        self._Tab_VinoutsDecodeDetails.m_listCtrOutputs.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
    
    
    
    
    
    
    def setupInputOutputTable(self):
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "Address"
        self._Tab_RvnDecode.m_listCtrlInputs.InsertColumn(0, info)
        self._Tab_RvnDecode.m_listCtrOutputs.InsertColumn(0, info)

        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "Quantity"
        self._Tab_RvnDecode.m_listCtrlInputs.InsertColumn(1, info)
        self._Tab_RvnDecode.m_listCtrOutputs.InsertColumn(1, info)
        
        self.il = wx.ImageList(16, 16)
        
        self._Tab_RvnDecode._curColumnSort = 0
        
        self.allIcons['wallet'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('wallet') )
        
        self.allIcons['asset'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('asset') )
        self.allIcons['rvn'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('ravencoin') )
        
        self.allIcons['vin'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('vin_icon1') )
        self.allIcons['vout'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('vout_icon1') )
        
        
        self.allIcons['sort_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up') )
        self.allIcons['sort_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down') )
        self.allIcons['sort_up_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up_2') )
        self.allIcons['sort_down_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down_2') )
        
        self.allIcons['alphab_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_up') )
        self.allIcons['alphab_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_co') )
        
        
        self._Tab_RvnDecode.m_listCtrlInputs.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        self._Tab_RvnDecode.m_listCtrOutputs.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
    
    
    
    
    def setupInputOutputAssetTable(self):
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "Address"
        self._Tab_AssetDecode.m_listCtrlInputs1.InsertColumn(0, info)
        self._Tab_AssetDecode.m_listCtrOutputs1.InsertColumn(0, info)

        info.Text = "Asset"
        self._Tab_AssetDecode.m_listCtrlInputs1.InsertColumn(1, info)
        self._Tab_AssetDecode.m_listCtrOutputs1.InsertColumn(1, info)


        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "Quantity"
        self._Tab_AssetDecode.m_listCtrlInputs1.InsertColumn(2, info)
        self._Tab_AssetDecode.m_listCtrOutputs1.InsertColumn(2, info)
    
        
        self._Tab_AssetDecode.m_listCtrlInputs1.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        self._Tab_AssetDecode.m_listCtrOutputs1.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
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
        self._currentTxHEX = str(self._Tab_HexDecode.m_HEXText.GetValue())
        
        
        self.m_txIdText.SetValue("")
        #print("OnHexTextChanged")
        if self._currentTxHEX  != '':
            self._currentTxID = ''    
        
        self._INPUT_TREAT = False
        
        
        #self.UpdateView()
        self.RequestDecodeTx()
    
    
    def SetTxId(self, txid):
        self.m_txIdText.SetValue(txid)
        
    
    def OnTxIdChanged(self, evt):
        if self._INPUT_TREAT:
            return
        self._INPUT_TREAT = True
        print("OnTxIdChanged")
        self._currentTxID = str(self.m_txIdText.GetValue())
        
        
        self._Tab_HexDecode.m_HEXText.SetValue('')
        if self._currentTxID  != '':
            self._currentTxHEX = ''
            
        #self.m_AssetNameTxt.SetValue(self._currentName)
        #self.computeAssetFullName()
        self._INPUT_TREAT = False
    
    
        #self.UpdateView()
        self.RequestDecodeTx()
    
    
    
    
    def RequestDecodeTx(self):
        p = self.parent_frame.GetPlugin('Ravencore')
        
        if self._currentTxID != '' or  self._currentTxHEX != '':
            nj = Job_DecodeTx(p, self._currentTxID, self._currentTxHEX, self.UpdateView, safeMode=True)
            self.parent_frame.NewJob(nj)
            print("RequestDecodeTx")
            
            self._INPUT_TREAT = True
            self.ClearTx()
            self._INPUT_TREAT = False
    
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
        self.m_SizeText.SetValue('')
        #
        # clear lisrs
        #
        
        self._Tab_VinoutsDecode.m_VINsText.SetValue('')
        self._Tab_VinoutsDecode.m_VOUTsText.SetValue('')
        
        self._Tab_VinoutsDecodeDetails.m_staticText86.SetLabel(f'VINs :')
        self._Tab_VinoutsDecodeDetails.m_staticText861.SetLabel(f'VOUTs :')

    
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        
        self.ClearTx()
        #self.UpdateDataFromPluginDatas()
        self.UpdateFromDatas()
        self.Layout()
        #self.setupPanel()
    
    
    
    
    
    
    def ShowDecodeTx(self):
        #self.m_txDetailsPanel.Hide()
        #self.m_txDetailsAdvanced.Show()
        
        
        self._INPUT_TREAT = True
        
        
        self.m_txIdText.SetValue(self.LastDecode['txid'])
        self.m_hashText.SetValue(self.LastDecode['hash'])
        _size= '???'
        if  self.LastDecode.__contains__('size'):
            _size = str(self.LastDecode['size'])
        
        self.m_SizeText.SetValue(str(_size))
        #blockhash
        #blocktime
        #blockhash
        #confirmations
        
        
        #details
        #asset_details
        
        self._Tab_VinoutsDecode.m_VINsText.SetValue(str(self.LastDecode['vin']))
        self._Tab_VinoutsDecode.m_VOUTsText.SetValue(str(self.LastDecode['vout']))
        
        self.LoadTxVinVoutsTableDatas()
       
        print('ShowDecodeTx()')
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
        _size = '???'
        if  self.LastTx.__contains__('blocktime'):
            _time =  datetime.datetime.fromtimestamp(self.LastTx['blocktime']).strftime('%Y-%m-%d %H:%M:%S')
        
        
        if  self.LastTx.__contains__('fee'):
            _fee = str(self.LastTx['fee'].__abs__())
            
        if  self.LastTx.__contains__('confirmations'):
            _confs = str(self.LastTx['confirmations'].__abs__())
            
        if  self.LastTx.__contains__('size'):
            _size = str(self.LastTx['size'])
            
            
        self.m_timestampText.SetValue(_time)
        self.m_locktimeText.SetValue(_fee)
        self.m_ConfirmationsText.SetValue(_confs)
        self.m_SizeText.SetValue(_size)
        
        
        
        
        
        
        self.LoadTxDetailsTableDatas(self._Tab_RvnDecode.m_listCtrlInputs, self._Tab_RvnDecode.m_sentPanel, "send")
        self.LoadTxDetailsTableDatas(self._Tab_RvnDecode.m_listCtrOutputs, self._Tab_RvnDecode.m_ReceivedPanel, "receive")
        
        
        self.LoadTxDetailsAssetTableDatas(self._Tab_AssetDecode.m_listCtrlInputs1, self._Tab_AssetDecode.m_sentPanel1, "send")
        self.LoadTxDetailsAssetTableDatas(self._Tab_AssetDecode.m_listCtrOutputs1, self._Tab_AssetDecode.m_ReceivedPanel1, "receive")
        
        
        #blockhash
        #blocktime
        #blockhash
        #confirmations
        
        
        #details
        #asset_details
        
        self._Tab_HexDecode.m_HEXText.SetValue(self.LastTx['hex'])
        
        #hex
        
        self._INPUT_TREAT = False
    
    
    
    
    def UpdateFromDatas(self):
        
        p = self.parent_frame.GetPlugin('Ravencore')
        self.LastTx = p.getData('_last_tx_decoded')
        
        if self.LastTx != None:
            self.LastDecode = self.LastTx
            self.ShowTx()   
            self.ShowDecodeTx() 
            
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        if True:
        #try:
            
            ravencoin = self.parent_frame.getRvnRPC()
            
            #self.LastTx= None
            
            if self._currentTxID  != '':
                self.LastTx = ravencoin.utils.GetRawTransaction(self._currentTxID, inspect=True )
                print("GetTX")
                #print(self.LastTx)
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
                #print(self.LastDecode)
                
                if self.LastDecode != None:
                    self.ShowDecodeTx()
                    
                    '''
                    self.LastTx = ravencoin.utils.GetTransaction(self.LastDecode['txid'] )
                    if self.LastTx != None:
                        self.ShowTx()
                    '''
                    #self.LastTx = ravencoin.utils.GetTransaction(self.LastDecode['txid'] )
                    self.LastTx = ravencoin.utils.GetRawTransaction(self.LastDecode['txid'], inspect=True )
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
                    
    
    
    
    
    def LoadTxVinVoutsTableDatas(self):
        
        panelIn = self._Tab_VinoutsDecodeDetails.m_sentPanel
        panelOut = self._Tab_VinoutsDecodeDetails.m_ReceivedPanel
        
        listIn = self._Tab_VinoutsDecodeDetails.m_listCtrlInputs
        listOut = self._Tab_VinoutsDecodeDetails.m_listCtrOutputs
        
        listIn.Freeze()
        listOut.Freeze()
        
        #panelIn._listInit = False
        #panelOut._listInit = False
        
        
        #
        # List in
        #
        listIn.DeleteAllItems()
        
        
        panelIn.itemDataMap={}
        panelIn.cursor = 0
        
        for _vin in self.LastDecode['vin']:
            #print(_vin)
            
            if _vin.__contains__('txid'):
            
                index = listIn.InsertItem(listIn.GetItemCount(),str(_vin['txid']), self.allIcons['vin'] )
                listIn.SetItem(index,1, str(_vin['vout'].__abs__()))
                listIn.SetItemData(index, panelIn.cursor)
                
                panelIn.itemDataMap[panelIn.cursor] = ( str(_vin['txid'] ),int( _vin['vout'] ) )
                
                
            else:
                
                
                _text= ''
                if _vin.__contains__('coinbase'):
                    _text = "coinbase"
                
                index = listIn.InsertItem(listIn.GetItemCount(),str(_vin[_text]), self.allIcons['vin'] )
                listIn.SetItem(index,1, str(-1))
                listIn.SetItemData(index, panelIn.cursor)
                
                panelIn.itemDataMap[panelIn.cursor] = ( str(_vin[_text] ),int(-1 ) )    
                
                
                
                
                                                
            panelIn.cursor = panelIn.cursor+1
        
        listIn.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        listIn.SetColumnWidth(1, 100)      
        
        panelIn.list= listIn
        panelIn.allIcons = self.allIcons
        if not panelIn._listInit:
            listmix.ColumnSorterMixin.__init__(panelIn, 2)
            panelIn._listInit = True
            
        listmix.ColumnSorterMixin.SortListItems(panelIn, col=0, ascending=0)
        
        listIn.Thaw()
        #self.Layout()
        
        
        self._Tab_VinoutsDecodeDetails.m_staticText86.SetLabel(f'VINs : {panelIn.cursor} ')
        
        
        
        #
        # List Out
        #
        listOut.DeleteAllItems()
        
        
        panelOut.itemDataMap={}
        panelOut.cursor = 0
        
        for _vout in self.LastDecode['vout']:
            
            _icon = 'vout'
        
            if _vout['scriptPubKey']['type']=='transfer_asset':
                _icon = 'asset'
        
            
            index = listOut.InsertItem(listOut.GetItemCount(),str(_vout['n']), self.allIcons[_icon] )
            listOut.SetItem(index,1, str(_vout['value'] ) )
            listOut.SetItem(index,2, str(_vout['scriptPubKey']['type'] ) )
            
            _address = ""
            if _vout['scriptPubKey'].__contains__('addresses'):
                _address = _vout['scriptPubKey']['addresses']
            
            listOut.SetItem(index,3, str( _address) )
            
            _more = ''
            if _vout['scriptPubKey'].__contains__('asset'):
                _more = '' + str(_vout['scriptPubKey']['asset']['amount']) + ' ' + str(_vout['scriptPubKey']['asset']['name']) 
                
                
            listOut.SetItem(index,4, _more )    
                
            
            listOut.SetItemData(index, panelOut.cursor)
            
            panelOut.itemDataMap[panelOut.cursor] = ( int(_vout['n'] ),str( _vout['value'] ) ,  str(_vout['scriptPubKey']['type'] ),  str(_address ), _more    )
                                                
            panelOut.cursor = panelOut.cursor+1
        
        listOut.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        listOut.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        listOut.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        listOut.SetColumnWidth(3, wx.LIST_AUTOSIZE)      
        
        panelOut.list= listOut
        panelOut.allIcons = self.allIcons
        if not panelOut._listInit:
            listmix.ColumnSorterMixin.__init__(panelOut, 4)
            panelOut._listInit = True
            
        listmix.ColumnSorterMixin.SortListItems(panelOut, col=0, ascending=0)
        
        listOut.Thaw()
        
        
        self._Tab_VinoutsDecodeDetails.m_staticText861.SetLabel(f'VOUTs : {panelOut.cursor}')
        
        
        
        
        
        self.Layout()
        
        
        
        
        
        
        
        '''
        
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
        '''
    
    
    
            
    def LoadTxDetailsTableDatas(self, list, panel, category='send'):
        
        
        list.Freeze()
        panel.itemDataMap={}
        panel.cursor = 0
        
        
        list.DeleteAllItems()
        
        if self.LastTx.__contains__('details'):
        
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
            if not panel._listInit:
                listmix.ColumnSorterMixin.__init__(panel, 2)
                panel._listInit = True
            listmix.ColumnSorterMixin.SortListItems(panel, col=1, ascending=0)
        
        list.Thaw()
        self.Layout() 
    
    
    
    def LoadTxDetailsAssetTableDatas(self, list, panel, category='send'):
        
        
        list.Freeze()
        panel.itemDataMap={}
        panel.cursor = 0
        
        
        list.DeleteAllItems()
        
        if self.LastTx.__contains__('asset_details'):
        
            for _det in self.LastTx['asset_details']:
                if _det['category'] != category:
                    continue
                
                
                _dispAddress = str(_det['destination'])
                if _det.__contains__('address'):
                    _dispAddress = str(_det['address'])
                
                
                index = list.InsertItem(list.GetItemCount(), _dispAddress, self.allIcons['asset'] )
                list.SetItem(index,1, str(_det['asset_name']))
                list.SetItem(index,2, str(_det['amount'].__abs__()))
                list.SetItemData(index, panel.cursor)
                panel.itemDataMap[panel.cursor] = ( _dispAddress ,str(_det['asset_name']),str( _det['amount'].__abs__() ) )
                                                    
                panel.cursor = panel.cursor+1
            
            
            
            
            
            
                   
            list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
            list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
            list.SetColumnWidth(2, 150)      
            
            panel.list= list
            panel.allIcons = self.allIcons
            if not panel._listInit:
                listmix.ColumnSorterMixin.__init__(panel, 3)
                panel._listInit = True
            listmix.ColumnSorterMixin.SortListItems(panel, col=2, ascending=0)
        
        list.Thaw()
        self.Layout()    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
class  wxRaven_Ravencore_TxViewer_HEX_PanelLogic(wxRaven_Ravencore_TxViewer_HEX_Panel):
    
    
    view_base_name = "Decode Hexadecimal"
    view_name = "Decode Hexadecimal"
    parent_frame = None
    default_position = "main"
    icon = 'raw_datas_verified'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    def __init__(self,parent,  parentFrame, position = "main", viewName= "Decode Hexadecimal", isInternalPluginView=True):
        '''
        Constructor
        '''
        super().__init__(parent=parent)    
        self.parent_frame =  parentFrame
        
        
        
        
        
        
        
class  wxRaven_Ravencore_TxViewer_VINOUT_PanelLogic(wxRaven_Ravencore_TxViewer_VINOUT_Panel):
    
    
    view_base_name = "VINs/VOUTs Raw"
    view_name = "VINs/VOUTs Raw"
    parent_frame = None
    default_position = "main"
    icon = 'tx_vinout'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    def __init__(self,parent,  parentFrame, position = "main", viewName= "VINs/VOUTs", isInternalPluginView=True):
        '''
        Constructor
        '''
        super().__init__(parent=parent)    
        self.parent_frame =  parentFrame
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        
        
class  wxRaven_Ravencore_TxViewer_VINOUT_List_PanelLogic(wxRaven_Ravencore_TxViewer_VINOUT_List_Panel):
    
    
    view_base_name = "VINs/VOUTs"
    view_name = "VINs/VOUTs"
    parent_frame = None
    default_position = "main"
    icon = 'tx_vinout'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    def __init__(self,parent,  parentFrame, position = "main", viewName= "VINs/VOUTs Details", isInternalPluginView=True):
        '''
        Constructor
        '''
        super().__init__(parent=parent)    
        self.parent_frame =  parentFrame
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        
        
class  wxRaven_Ravencore_TxViewer_RVN_PanelLogic(wxRaven_Ravencore_TxViewer_RVN_Panel):
    
    
    view_base_name = "Transfer : RVN"
    view_name = "Transfer : RVN"
    parent_frame = None
    default_position = "main"
    icon = 'wallet_in_out'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    def __init__(self,parent,  parentFrame, position = "main", viewName= "Transfer : RVN", isInternalPluginView=True):
        '''
        Constructor
        '''
        super().__init__(parent=parent)    
        self.parent_frame =  parentFrame
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        
        
class  wxRaven_Ravencore_TxViewer_Asset_PanelLogic(wxRaven_Ravencore_TxViewer_Asset_Panel):
    
    
    view_base_name = "Transfer : Assets"
    view_name = "Transfer : Assets"
    parent_frame = None
    default_position = "main"
    icon = 'asset_trade'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    def __init__(self,parent,  parentFrame, position = "main", viewName= "Transfer : Assets", isInternalPluginView=True):
        '''
        Constructor
        '''
        super().__init__(parent=parent)    
        self.parent_frame =  parentFrame
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        
        
                                
        
        
        
        
        
 