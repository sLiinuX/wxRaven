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



import logging
import os
import time
from datetime import datetime

class wxRavenP2PMarket_ViewTexInfosDialog( wxRavenDecodeTxPanel):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "View TX Infos"
    view_name = "View TX Infos"
    parent_frame = None
    default_position = "dialog"
    icon = 'inspect_swap'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parent, parentFrame,  position = "dialog", viewName= "View TX Infos", isInternalPluginView=False, isInternalPanel=True, parentDataObj=None):
        '''
        Constructor
        '''
        
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        
        self.logger = logging.getLogger('wxRaven')
        
        self.view_base_name = "View TX Infos"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parent
        self.parentDataObj = parentDataObj
        
        self.isInternalPluginView = isInternalPluginView
        self.isInternalPanel = isInternalPanel
        
        #self.m_assetTradePanel.Hide()
        self._newAdObject = RavencoinP2PMarketPlaceAd()
        self._loading = False
        self.m_buttonPrevious.Enable(False)
        self.m_buttonNext.Enable(False)
        #self._newAdObject._adOrders=1
        #self._newAdObject._adType=0
        #self._newAdObject._adTxType=0
        #self._newAdObject._adAssetQt=1
        #self._newAdObject._adPrice=200
        #self._newAdObject._adTxDatas = {}
        
        self._orderCursor=0
        
        
        self.SizerObj= None
        #isInternalPanel= True
        if isInternalPanel:
            pass
            #self.m_GenerateSwapTx.Hide()
            #self.m_txDatas.Hide()
            #self.m_panelTxType.Hide()
            
            #self.Sizer = wx.BoxSizer( wx.VERTICAL )
            #self.Sizer .Add( self._Panel, 1, wx.ALL|wx.EXPAND, 5 )
        #if not isInternalPluginView:
        #    parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
        
        self.setupPanel()
        self.m_TXDetailsPanel.Hide()
        self.Layout()
        self.parent.ResizeDialog()    
        
        
    def OnCloseParent(self, evt=None):
        self.parent.Close()    
        
    def OnClose(self, evt=None):    
        self.logger.info("ViewTxPanel OnClose()")
        self.parent_frame.Views.__unregisterDialog__(self.view_name)
        #
        self.Destroy()
        
        
    def setupPanel(self):
        #ravencoin = self.parent_frame.getRvnRPC()
        pass
    
    
    def __checkOrdersCount__(self):
        
        print(f"c= {self._orderCursor}, max= {len(self._newAdObject._adTxDatas)}")
        
        print(type(self._newAdObject._adTxDatas))
        print(self._newAdObject._adTxDatas)
        if len(self._newAdObject._adTxDatas) >1:
            
            
            if self._orderCursor > 0:
                self.m_buttonPrevious.Enable(True)
            else:
                self.m_buttonPrevious.Enable(False)
            
            
            if self._orderCursor >= len(self._newAdObject._adTxDatas)-1:
                self.m_buttonNext.Enable(False)
            else:
                self.m_buttonNext.Enable(True)
            
            self.m_staticText186.SetLabel(f"ORDER : {self._orderCursor +1}/{len(self._newAdObject._adTxDatas)}")
            
            
        else:
            self.m_buttonPrevious.Enable(False)
            self.m_buttonNext.Enable(False)
            self.m_staticText186.SetLabel("ORDER : 1/1")
    
        if str(type(self._newAdObject._adTxDatas))!= "<class 'dict'>":
            self.m_buttonNext.Enable(False)
            self.m_buttonPrevious.Enable(False)
    
    
        
    def SetRaw(self, raw, cursor=0):
        self.m_SignedPartialText.SetValue(raw)  
        self._orderCursor=cursor 
        self.OnRawDataChanged(None)
        self.m_staticText186.SetLabel("ORDER : 1/?")
        
        
        self.__checkOrdersCount__()
        
        
        self.Layout()
    
    
    
    def SetAd(self, ad:RavencoinP2PMarketPlaceAd, cursor=0):
        #self.m_SignedPartialText.SetValue(raw)  
        self._loading = True
        self._newAdObject.Load_JSON(ad.JSON())
        
        self._orderCursor= cursor
        
        
        print(f'Received AD : {ad._adTxDatas}')
        print(f'Received AD : {type(ad._adTxDatas)}')
        
        print(f'_newAdObject AD : {self._newAdObject._adTxDatas}')
        print(f'_newAdObject AD : {type(self._newAdObject._adTxDatas)}')
        
        if self._newAdObject != None:
            self.SetRaw(self._newAdObject._adTxDatas[cursor], cursor)
        else:
            self.SetRaw('')
        #self.OnRawDataChanged(None)
        #self.m_staticText186.SetValue("ORDER : 1/?")
        #self.__checkOrdersCount__()
        #self.Layout()
        self._loading = False
    
    def OnPreviousOrder(self, evt):
        self._loading = True
        self._orderCursor = self._orderCursor-1
        self.m_SignedPartialText.SetValue(self._newAdObject._adTxDatas[self._orderCursor]) 
        self.OnRawDataChanged(None) 
        self.__checkOrdersCount__()
        self.Layout()
        self._loading = False
    
    def OnNextOrder(self, evt):
        self._loading = True
        self._orderCursor = self._orderCursor+1
        self.m_SignedPartialText.SetValue(self._newAdObject._adTxDatas[self._orderCursor]) 
        self.OnRawDataChanged(None) 
        self.__checkOrdersCount__()
        self.Layout()
        self._loading = False
    
        
    def OnCompleteTx(self, evt):
        
        
        if UserQuestion(self, "Complete this transaction ?"):
            #_result = self._data.complete_order()
            ravencoin = self.parent_frame.getRvnRPC()
            
            _result = None
            
            try:
                swaptocomplete=self.m_SignedPartialText.GetValue()
                _result= ravencoin.atomicswap.CompleteSwap(swaptocomplete)
                
            except Exception as e:
                self.parent_frame.Log("Unable to complete tx :" + str(e) , type="warning")
            
            
            
            
            self.parent.Close()
            ReportRPCResult(self.parent_frame, _result, "success", "Transaction complete !", "Unable to complete the transaction.", False)
            '''
            if _result != None:

                #UserAdvancedMessage(self.parent_frame, f"List of {len(self._currentUTXOcount)} Addresses has been loaded.", 'info')
                UserInfo(self, str(_result))
                self.m_completeButton.Enable(False)
            else:
                UserError(self, "Error : Unable to complete the transaction : "+ str(_result))
     
            '''
    
    
    def OnRawDataInputChanged(self, evt=None):
        if self._loading:
            return None
        
        print("OnRawDataInputChanged")
        self._newAdObject = RavencoinP2PMarketPlaceAd()
        self._newAdObject._adTxDatas[0] = self.m_SignedPartialText.GetValue() 
        self._orderCursor=0  
        self.OnRawDataChanged(None)
        self.__checkOrdersCount__()
        self.Layout()
        
        
    def OnRawDataChanged(self, evt=None):
        #self._newAdObject._adTxDatas = self.m_SignedPartialText.GetValue()   
        
        self.logger.info(f"OnRawDataChanged  {self._newAdObject._adTxDatas}")
        self.logger.info(f"self._orderCursor  {self._orderCursor}")
        
        
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        self.m_completeButton.Enable(False)
        self.m_completeButton.Show(False)
        
        _invalidIcon = self.parent_frame.RessourcesProvider.GetImage('raw_datas_invalid')
        _validIcon = self.parent_frame.RessourcesProvider.GetImage('raw_datas_verified')
        _validTxIcon = self.parent_frame.RessourcesProvider.GetImage('passed_3')
        _errTxIcon = self.parent_frame.RessourcesProvider.GetImage('error_tsk')
        
        self.m_bitmapUTXO.SetBitmap(_invalidIcon)
        self.m_bitmapPartial.SetBitmap(_invalidIcon)
        self.m_bitmapStatus.SetBitmap(_errTxIcon)
        
        if self._newAdObject._adTxDatas == "":
            self.m_ErrorMsgPanel.Show()
            self.m_TXDetailsPanel.Hide()
            self.m_ErrorDetails.SetLabel("Empty TX")
        else:
            _valid=False
            _data =None
            if str(type(self._newAdObject._adTxDatas))== "<class 'dict'>":
                _valid, _data = myPlugin.DecodeTx(self._newAdObject._adTxDatas[self._orderCursor])
            
            else:
                _valid, _data = myPlugin.DecodeTx(self._newAdObject._adTxDatas)
            
            
            
            if not _valid:
                self.m_ErrorMsgPanel.Show()
                self.m_TXDetailsPanel.Hide()
                self.m_ErrorDetails.SetLabel(_data)
            else:
                
                self.m_completeButton.Enable(True)
                self.m_completeButton.Show(True)
                self.logger.info("Valid !!")
                
                self.m_ErrorMsgPanel.Hide()
                self.m_TXDetailsPanel.Show()
                
                
                self.m_bitmapUTXO.SetBitmap(_validIcon)
                self.m_bitmapPartial.SetBitmap(_validIcon)
                
                
                self.m_bitmapStatus.SetBitmap(_validTxIcon)
                
                self._data = _data
                self.logger.info(f"Data =  {_data}")
                
                self.m_mineText.SetValue(_data.destination)
                
                self.m_StatusText.SetValue('VALID')
                self.m_TypeText.SetValue(_data.type)
                self.m_AssetText.SetValue(_data.asset())
                self.m_QuantityText.SetValue(str(_data.quantity()))
                self.m_UTXOText.SetValue(_data.utxo)
                
                
                #self.m_PriceText.SetValue(str(_data.destination))
                
                if _data.type == "buy":
                    self.m_PriceText.SetValue("{:.8g} RVN".format(_data.total_price()))
                    self.m_bitmap721.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('asset_in'))
                    if _data.own:
                        self.m_TypeText.SetValue("Buy - You want to purchase.")
                    else:
                        self.m_TypeText.SetValue("Sale - You want to sell to a buyer.")
                
                elif _data.type == "sell":
                    self.m_PriceText.SetValue("{:.8g} RVN".format(_data.total_price()))
                    self.m_bitmap721.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('asset_out'))
                    if _data.own:
                        self.m_TypeText.SetValue("Sell - You want to sell.")
                    else:
                        self.m_TypeText.SetValue("Purchase - You want to buy someone's sale.")
                
                elif _data.type == "trade":
                    #self.spnUpdateUnitPrice.setSuffix(" {}/{}".format(swap.out_type.upper(), swap.in_type.upper()) )
                    self.m_PriceText.SetValue("{:.8g} {}".format(_data.total_price(), _data.in_type.upper()))
                    self.m_bitmap721.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('asset_trade'))
                    if _data.own:
                        self.m_TypeText.SetValue("Trade - You want to trade assets of your own, for different assets.")
                    else:
                        self.m_TypeText.SetValue("Exchange - You want to exchange assets with another party.")
                #m_spinCtrl7
                #self.m_mineText.SetValue(_data.destination)
                
                
                
                
            '''
        try:
            _res = myPlugin.DecodeTx(self._newAdObject._adTxDatas)
            
            self.logger.info(_res)
            
        except Exception as e:
            self.parent_frame.Log("Unable to load tx datas" , type="warning")
        
        '''
        
        self.Layout()
        self.parent.ResizeDialog()
    
                
        #obj
        
    
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        
        self.UpdateDataFromPluginDatas()
        
        self.Layout()
        self.setupPanel()
        self.parent.ResizeDialog()
            
            
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        
        try:
       
            #myPluginData = self.parent_frame.GetPluginData("Tutorial","myPluginData2")
            #myPluginSetting =  self.parent_frame.GetPluginSetting("Tutorial","booleansetting")#SavePanelSettings GetPluginSetting
            #
            #Update your panel
            #       
            
            
            #textToself.logger.info = " booleansetting = " + str(myPluginSetting)
            #textToPrint = textToPrint + "\n\n myPluginData2 = " + str(myPluginData)
             
            #self.m_staticText2.SetLabel(str(textToPrint)) 
            pass
             
                
        except Exception as e:
            self.parent_frame.Log("Unable to load p2p Market datas" , type="warning")
                    
            
            