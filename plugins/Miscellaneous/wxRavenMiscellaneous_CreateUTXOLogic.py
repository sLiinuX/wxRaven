'''
Created on 10 févr. 2022

@author: slinux
'''


import threading
import time 

from .wxRavenMiscellaneousDesign import * 
from wxRavenGUI.application.wxcustom import *

#from libs.RVNpyRPC._P2PmarketPlace import 





import os
import time
from datetime import datetime

class wxRavenMiscellaneous_CreateUTXOWithLogic(wxRavenMiscellaneous_CreateUTXO):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Create UTXO"
    view_name = "Create UTXO"
    parent_frame = None
    default_position = "dialog"
    icon = 'new_utxo'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent, parentFrame,  position = "dialog", viewName= "Create UTXO", isInternalPluginView=False, isInternalPanel=True, parentDataObj=None):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Create UTXO"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parent
        self.parentDataObj = parentDataObj
        
        self.isInternalPluginView = isInternalPluginView
        self.isInternalPanel = isInternalPanel
        
        
        
        self._currentAsset = 'RVN'
        self._currentAmount = 1
        self._currentUTXOcount = 1
        self._currentBalance = 0.0
        
        
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
    
    
    
    
    
    
    def __GenerateUTXO__(self):
        print("__GenerateUTXO__")  
        #myPlugin = self.parent_frame.GetPlugin("P2PMarket")
        #p2p_market_change_address = myPlugin.PLUGIN_SETTINGS['p2p_market_change_address']
        myPlugin = self.parent_frame.GetPlugin("General")
        p2p_market_change_address = myPlugin.GetFavoriteChangeAddress()
        
        #p2p_market_swap_address= myPlugin.PLUGIN_SETTINGS['p2p_market_swap_address']
        
        self._currentAsset 
        _fakeResult = {'result':None , 'error': {'code':-1, 'message': f"Unknown error, please check logs."}}
        
        _tx=None
        #if True:
        try:
            ravencoin = self.parent_frame.getRvnRPC()
            
            _allAddresses = ravencoin.wallet.GenerateAdress(int(self._currentUTXOcount ))
            print(f"__GenerateUTXO__ : {_allAddresses}") 
            
            
            if self._currentAsset  == 'RVN':
                _txOk, _tx = ravencoin.wallet.sendSameRVN_Many( self._currentAmount, adresses=_allAddresses, pwd='', _changeAddress=p2p_market_change_address, _fund=True, _sign=True, _execute=True)
               
                print(f"RVN  {_tx}") 
            else:
                
                _txOk, _tx = ravencoin.wallet.sendSameAsset_Many(  self._currentAsset, self._currentAmount, adresses=_allAddresses, pwd='', _changeAddress=p2p_market_change_address, _fund=True, _sign=True, _execute=True)
                
                print(f"Asset  {_tx}") 
                
            
            _fakeResult = {'result':_tx , 'error':None}
            if not _txOk:
                _fakeResult['error'] = {'code':-1, 'message': f"{_tx}"}
                
                
                
            
            #UserInfo(self, _tx)
                
        except Exception as e:
            self.parent_frame.Log(f"Unable Generate UTXO : {e}" , type="warning")
            _fakeResult = {'result':None , 'error': {'code':-1, 'message': e}}
        
        
        
        ReportRPCResult(self.parent_frame, _fakeResult, "success", "UTXO's created !", "Unable Generate UTXO's.", False)
            
        return _tx
    
    
    
    
    
    def __CheckFeasibility__(self):
        _maxRequested = float(self._currentUTXOcount) *  float(self._currentAmount)
        
        print(f"__CheckFeasibility__ _maxRequested = {_maxRequested}  , av= {self._currentBalance}" )  
        if self._currentBalance>_maxRequested :
            return True
        return False
        
    
    
    def OnClickCreateUTXO(self, evt):
        print("OnClickCreateUTXO")  
        
        
        if not self.__CheckFeasibility__():
            UserError(self, "request exceeding balance, reduce UTXO count or amount.")
            return None 
        
        
        if UserQuestion(self, f"Do you confirm the creation of  {self._currentUTXOcount} ? \nA new address for each UTXO will be created."):
            _result =  self.__GenerateUTXO__()
        
        
          
        
        
    def LockPanel(self, locking): 
        print('pannel locked to avoid user modifications')
        
        if    locking:
            self.Enable(enable=False)
        else:
            self.Enable(enable=True)    
        
    def setupPanel(self):
        ravencoin = self.parent_frame.getRvnRPC()
        
        
        self.m_AssetChoice.Clear()
        
        
        #_allAdmins= ravencoin.asset.GetAllMyAssets()
        _allNotAdmins= ravencoin.asset.GetAllMyAssets(_excludeAdmin=True)
        #print(_allAdmins)
        #myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        self.m_AssetChoice.Append('RVN')
        for key in _allNotAdmins:
            
            self.m_AssetChoice.Append(key)
            
    
    
    
    def checkAssetBalance(self, assetName):
        ravencoin = self.parent_frame.getRvnRPC()
        _bal = 0.0
        try:
            if assetName != 'RVN':
                _bal = ravencoin.asset.GetBalance(assetName)
                print(f"checkAssetBalance  {_bal}")
            else:
                #_bal = ravencoin.asset.GetBalance(assetName)
                _bal = ravencoin.wallet.GetBalance()
                #print(f"checkAssetBalance ASS  {_bal}") 
                print(f"checkAssetBalance RVN  {_bal}") 
        except Exception as e:
            self.parent_frame.Log("Unable Check Asset Balance" , type="warning")
        return _bal
    
    def OnAssetChanged(self, evt):
        self._currentAsset =  self.m_AssetChoice.GetString(self.m_AssetChoice.GetCurrentSelection())
        print(f"OnAssetChanged  {self._currentAsset}")   
        
        self._currentBalance=self.checkAssetBalance(self._currentAsset)
        self.m_availableText.SetLabel(str(self._currentBalance))   
        self.Layout() 
    
    
    def OnAmountChanged(self, evt):
        self._currentAmount = self.m_AssetAmount.GetValue()
        print(f"OnAmountChanged  {self._currentAmount}")
    
    def OnUTXOChanged(self, evt):
        self._currentUTXOcount = self.m_UTXOcount.GetValue()
        print(f"OnUTXOChanged  {self._currentUTXOcount}")    
                
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
            self.parent_frame.Log("Unable to load utxos" , type="warning")
                    
            