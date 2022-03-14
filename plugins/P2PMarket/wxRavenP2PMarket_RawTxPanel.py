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
import ast



import os
import time
from datetime import datetime

class wxRavenP2PMarket_RawAtomiSwapWithLogic(wxRavenRawTxPanel):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "RAW Atomic Swap"
    view_name = "RAW Atomic Swap"
    parent_frame = None
    default_position = "dialog"
    icon = 'p2p_icon_new'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent, parentFrame,  position = "dialog", viewName= "RAW Atomic Swap", isInternalPluginView=False, isInternalPanel=True, parentDataObj=None):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "RAW Atomic Swap"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parent
        self.parentDataObj = parentDataObj
        
        self.isInternalPluginView = isInternalPluginView
        self.isInternalPanel = isInternalPanel
        
        #self.m_assetTradePanel.Hide()
        self._newAdObject = RavencoinP2PMarketPlaceAd()
        self._newAdObject._adType=0
        self._newAdObject._adTxType=0
        self._newAdObject._adAssetQt=1
        self._newAdObject._adPrice=200
        
        
        self.SizerObj= None
        #isInternalPanel= True
        if isInternalPanel:
            pass
            #self.m_GenerateSwapTx.Hide()
            #self.m_txDatas.Hide()
            #self.m_panelTxType.Hide()
            
            #self.Sizer = wx.BoxSizer( wx.VERTICAL )
            #self.Sizer .Add( self._Panel, 1, wx.ALL|wx.EXPAND, 5 )
            
        self.setupPanel()
        
        self.Layout()
        
        
        
    def LockPanel(self, locking): 
        print('pannel locked to avoid user modifications')
        
        if    locking:
            self.Enable(enable=False)
        else:
            self.Enable(enable=True)    
        
    def setupPanel(self):
        #ravencoin = self.parent_frame.getRvnRPC()
        pass
        
        #self.m_AdAssetChoice.Clear()
        #self.m_AdAssetChoice_Receive.Clear()
        
        
        #_allAdmins= ravencoin.asset.GetAllMyAssets()
        #_allNotAdmins= ravencoin.asset.GetAllMyAssets(_excludeAdmin=True)
        #print(_allAdmins)
        #myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        
        #for key in _allAdmins:
            
        #    self.m_AdAssetChoice.Append(key)
    '''    
    def OnOrderCountChange(self, evt):
        self._newAdObject._adOrders =  self.m_orderCount.GetValue()
        print(f"OnOrderCountChange  {self._newAdObject._adOrders}")
        
    def OnAssetChanged(self, evt):
        self._newAdObject._adAsset = self.m_AdAssetChoice.GetString(self.m_AdAssetChoice.GetCurrentSelection())
        print(f"OnAssetChanged  {self._newAdObject._adAsset}")
    
    def OnWantedAssetChanged(self, evt):
        self._newAdObject._adPriceAsset= self.m_WantedAssetText.GetValue()
        print(f"OnWantedAssetChanged  {self._newAdObject._adPriceAsset}")
    
    def OnQuantityChanged(self, evt):
        self._newAdObject._adAssetQt = self.m_AdAssetQt.GetValue()
        print(f"OnQuantityChanged  {self._newAdObject._adAssetQt}")
        
    def OnPriceChanged(self, evt):
        self._newAdObject._adPrice = self.m_AdAssetPrice.GetValue()   
        print(f"OnPriceChanged  {self._newAdObject._adPrice}")
    '''
    
    def OnRawDataChanged(self, evt):
        
        _inputRawText=self.m_rawDatasText.GetValue() 
        jsonData = {}
        try:
            jsonData = ast.literal_eval(_inputRawText)
        except Exception as e:
            print(e) 
        self._newAdObject._adTxDatas = jsonData
        
        
        
        if self._newAdObject._adTxDatas == '':
            self._newAdObject._adTxDatas = {}
        print(f"OnRawDataChanged  {type(self._newAdObject._adTxDatas)}")
        print(f"OnRawDataChanged  {self._newAdObject._adTxDatas}")
        self.UpdateParentPanelObject()
        
    def UpdateParentPanelObject(self):
        if self.isInternalPanel:
            if self.parentDataObj != None:
            #self.parent._newAdObject._adPrice = self._newAdObject._adPrice
            #self.parent._newAdObject._adAssetQt = self._newAdObject._adAssetQt
            #self.parent._newAdObject._adPriceAsset = self._newAdObject._adPriceAsset
            #self.parent._newAdObject._adAsset = self._newAdObject._adAsset
            #self.parent._newAdObject._adOrders = self._newAdObject._adOrders
                self.parentDataObj._newAdObject._adTxDatas = self._newAdObject._adTxDatas
                
                
        #obj
        
    def OnSwapTypeChanged(self, evt, forceId=-1):
        pass
        
    
    
    
    def OnGenerateAtomicSwap(self, evt):
        pass
    
    
            
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
                    
            
            