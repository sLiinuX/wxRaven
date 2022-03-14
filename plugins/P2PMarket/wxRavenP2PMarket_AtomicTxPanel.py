'''
Created on 10 janv. 2022

@author: slinux
'''
import threading
import time 

from .wxRavenP2PMarketDesign import * 
from wxRavenGUI.application.wxcustom import *

#from libs.RVNpyRPC._P2PmarketPlace import 

from libs.RVNpyRPC._P2PmarketPlace import RavencoinP2PMarketPlaceAd, _P2PMARKET_ID_




import os
import time
from datetime import datetime

class wxRavenP2PMarket_AdAtomiSwapWithLogic_DONOTUSEANYMORE(wxRavenAtomicSwapPanel_NoDetails):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "New Atomic Swap"
    view_name = "New Atomic Swap"
    parent_frame = None
    default_position = "dialog"
    icon = 'p2p_icon_new'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent, parentFrame,  position = "dialog", viewName= "New Atomic Swap", isInternalPluginView=False, isInternalPanel=False , parentDataObj=None):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "New Atomic Swap"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parent
        self.parentDataObj = parentDataObj
        
        self.isInternalPluginView = isInternalPluginView
        self.isInternalPanel = isInternalPanel
        
        self.m_assetTradePanel.Hide()
        self._newAdObject = RavencoinP2PMarketPlaceAd()
        self._newAdObject._adType=0
        self._newAdObject._adTxType=0
        self._newAdObject._adAssetQt=1
        self._newAdObject._adPrice=200
        
        
        self.SizerObj= None
        #isInternalPanel= True
        if isInternalPanel:
            
            print("Internal Panel")
            #self.m_GenerateSwapTx.Hide()
            #self.m_txDatas.Hide()
            self.m_panelTxType.Hide()
            #self.m_detailsPanel.Hide()
            #self.m_staticline18.Hide()
            #self.m_staticline19.Hide()
            #self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
            #w, h = self.GetSize()
            #w = h
            #panel.SetSize(w, h)
            
            #self.Fit()
            #self.Sizer = wx.BoxSizer( wx.VERTICAL )
            #self.Sizer .Add( self._Panel, 1, wx.ALL|wx.EXPAND, 5 )
            
        self.setupPanel()
        
        self.Layout()
        
        
        
        
        
    def setupPanel(self):
        ravencoin = self.parent_frame.getRvnRPC()
        
        
        self.m_AdAssetChoice.Clear()
        #self.m_AdAssetChoice_Receive.Clear()
        
        
        _allAdmins= ravencoin.asset.GetAllMyAssets()
        _allNotAdmins= ravencoin.asset.GetAllMyAssets(_excludeAdmin=True)
        #print(_allAdmins)
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        
        for key in _allAdmins:
            
            self.m_AdAssetChoice.Append(key)
        
    def OnOrderCountChange(self, evt):
        self._newAdObject._adOrders =  self.m_orderCount.GetValue()
        print(f"OnOrderCountChange  {self._newAdObject._adOrders}")
        self.UpdateParentPanelObject()
        
    def OnAssetChanged(self, evt):
        self._newAdObject._adAsset = self.m_AdAssetChoice.GetString(self.m_AdAssetChoice.GetCurrentSelection())
        print(f"OnAssetChanged  {self._newAdObject._adAsset}")
        self.UpdateParentPanelObject()
    
    def OnWantedAssetChanged(self, evt):
        self._newAdObject._adPriceAsset= self.m_WantedAssetText.GetValue()
        print(f"OnWantedAssetChanged  {self._newAdObject._adPriceAsset}")
        self.UpdateParentPanelObject()
    
    def OnQuantityChanged(self, evt):
        self._newAdObject._adAssetQt = self.m_AdAssetQt.GetValue()
        print(f"OnQuantityChanged  {self._newAdObject._adAssetQt}")
        self.UpdateParentPanelObject()
        
    def OnPriceChanged(self, evt):
        self._newAdObject._adPrice = self.m_AdAssetPrice.GetValue()   
        print(f"OnPriceChanged  {self._newAdObject._adPrice}")
        self.UpdateParentPanelObject()
        
    def UpdateParentPanelObject(self):
        if self.isInternalPanel:
            if self.parentDataObj != None:
                print(f"UpdateParentPanelObject  {self.parentDataObj}")
                self.parentDataObj._newAdObject._adPrice = self._newAdObject._adPrice
                self.parentDataObj._newAdObject._adAssetQt = self._newAdObject._adAssetQt
                self.parentDataObj._newAdObject._adPriceAsset = self._newAdObject._adPriceAsset
                self.parentDataObj._newAdObject._adAsset = self._newAdObject._adAsset
                self.parentDataObj._newAdObject._adOrders = self._newAdObject._adOrders
        #obj
        
    def OnSwapTypeChanged(self, evt, forceId=-1):
        
        
        _newTypeId = self.m_AtomicSwapType.GetCurrentSelection()
        _newTypeStr =  self.m_AtomicSwapType.GetString(_newTypeId)
        
        if forceId!=-1:
            _newTypeStr =  self.m_AtomicSwapType.GetString(forceId)
            _newTypeId = forceId
        
        print(f"{_newTypeId}  {_newTypeStr}")
        
        
        self._newAdObject._adType=_newTypeId
        
        #
        #if trade
        if _newTypeId == 2:
            self.m_assetTradePanel.Show()
            self.m_assetSellPanel.Show()
            self.m_staticText712.SetLabel("Quantity :")
            self._newAdObject._adPriceAsset= self.m_WantedAssetText.GetValue()
            
            self.m_bitmap21.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('asset_out') )
            self.m_bitmap212.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('asset_in') )
        #
        #else    
        else:
            
            if _newTypeId == 0:
                self.m_assetTradePanel.Hide()
                self.m_assetSellPanel.Show()
            elif _newTypeId == 1:
                self.m_assetSellPanel.Hide()
                self.m_assetTradePanel.Show()
            
            self.m_staticText712.SetLabel("Price :")
            self._newAdObject._adPriceAsset='RVN'
    
        self.Layout()
        
        try:
            self.parent.ResizeDialog()
        except Exception as e:
            pass
        
    
    
    
    def OnGenerateAtomicSwap(self, evt):
        #
        # Todo all checks
        #
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
                #self.m_txDatas.SetValue(str(self._newAdObject._adTxDatas))
                
                UserInfo(self, str(self._newAdObject._adTxDatas) )
            else:
                UserError(self, "Error, cannot create atomic swap.")
    
    
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        
        self.UpdateDataFromPluginDatas()
        self.Layout()
        self.setupPanel()
            
            
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        
        try:
       
            #myPluginData = self.parent_frame.GetPluginData("Tutorial","myPluginData2")
            #myPluginSetting =  self.parent_frame.GetPluginSetting("Tutorial","booleansetting")#SavePanelSettings GetPluginSetting
            #
            #Update your panel
            #       
            
            
            #textToPrint = " booleansetting = " + str(myPluginSetting)
            #textToPrint = textToPrint + "\n\n myPluginData2 = " + str(myPluginData)
             
            #self.m_staticText2.SetLabel(str(textToPrint)) 
            pass
             
                
        except Exception as e:
            self.parent_frame.Log("Unable to load p2p Market datas" , type="warning")
                    
            
            