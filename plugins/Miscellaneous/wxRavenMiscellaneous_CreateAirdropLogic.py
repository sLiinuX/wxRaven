'''
Created on 17 janv. 2022

@author: slinux
'''


import threading
import time 

from .wxRavenMiscellaneousDesign import * 
from wxRavenGUI.application.wxcustom import *

#from libs.RVNpyRPC._P2PmarketPlace import 


import random


import os
import time
from datetime import datetime

class wxRavenMiscellaneous_CreateAirdropWithLogic(wxRavenMiscellaneous_Airdrop):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Create Airdrop"
    view_name = "Create Airdrop"
    parent_frame = None
    default_position = "dialog"
    icon = 'airdrop_icon'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent, parentFrame,  position = "dialog", viewName= "Create Airdrop", isInternalPluginView=False, isInternalPanel=True, parentDataObj=None):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Create Airdrop"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parent
        self.parentDataObj = parentDataObj
        
        self.isInternalPluginView = isInternalPluginView
        self.isInternalPanel = isInternalPanel
        
        self._airdropSOURCEaddress = []
        
        self._currentAsset = 'RVN'
        self._currentAmount = 1
        self._currentUTXOcount = 1
        self._currentBalance = 0.0
        
        self._airdropSOURCEaddress = []
        
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
    
    
        self.m_AssetAmount.Bind( wx.EVT_TEXT, self.OnAmountChanged )
        self.m_UTXOcount.Bind( wx.EVT_SPINCTRL, self.OnUTXOChanged )
    
    
    
    def SelectWinnerInList(self, allwins=False):
        winnerList = []
        
        isRandom= self.m_checkBox26.GetValue()
        if int(self._currentUTXOcount ) >= len(self._airdropSOURCEaddress):
            print('More winners than address, full list win !')
            winnerList = self._airdropSOURCEaddress
        else:
            if isRandom:
                winnerList = random.sample(self._airdropSOURCEaddress,int(self._currentUTXOcount))#random.choices(list, k=self._currentUTXOcount)
            else:
                winnerList = self._airdropSOURCEaddress[:(self._currentUTXOcount)]
                
        if allwins:
            winnerList = self._airdropSOURCEaddress
                
        print(f"winners = {winnerList} ")    
        return winnerList    
    
    
    def __GenerateAirdrop__(self, allListWin=False):
        print("__GenerateUTXO__")  
        
        """
        Updated change address settings
        """
        myPlugin = self.parent_frame.GetPlugin("General")
        p2p_market_change_address = myPlugin.GetFavoriteChangeAddress()
        #p2p_market_swap_address= myPlugin.PLUGIN_SETTINGS['p2p_market_swap_address']
        
        #self._currentAsset 
        
        _tx=None
        if True:
        #try:
            ravencoin = self.parent_frame.getRvnRPC()
            _allAddresses = self.SelectWinnerInList(allListWin)
            
            #_allAddresses = ravencoin.wallet.GenerateAdress(int(self._currentUTXOcount ))
            print(f"__GenerateUTXO__ : {_allAddresses}") 
                        
            if self._currentAsset  == 'RVN':
                _ok,_tx = ravencoin.wallet.sendSameRVN_Many( self._currentAmount, adresses=_allAddresses, pwd='', _changeAddress=p2p_market_change_address, _fund=True, _sign=True, _execute=True)
               
                print(f"RVN  Airdrop {_ok} : {_tx}") 
            else:
                
                _ok,_tx = ravencoin.wallet.sendSameAsset_Many(  self._currentAsset, self._currentAmount, adresses=_allAddresses, pwd='', _changeAddress=p2p_market_change_address, _fund=True, _sign=True, _execute=True)
                
                print(f"Asset Airdrop {_ok} : {_tx}") 
                
            
            if _ok:
                isRandom= self.m_checkBox26.GetValue()
                _rdmText=''
                if isRandom:
                    _rdmText='Radomly selected'
                #UserInfo(self, f"TX = {_tx}  \n Winners : {len(_allAddresses)} ")
                UserAdvancedMessage(self.parent_frame, f"Airdrop Sent to {len(_allAddresses)} Addresses {_rdmText} !", "success", msgdetails=f'Tx = {_tx} \nWinner List = {_allAddresses}', showCancel=False)
            else:
                UserAdvancedMessage(self.parent_frame, f"Airdrop Failed !", "error", msgdetails=f'Tx = {_tx}\nWinner List = {_allAddresses}', showCancel=False)   
        #except Exception as e:
        #    self.parent_frame.Log(f"Unable Generate UTXO : {e}" , type="warning")
        
        
        return _tx
        
    
    def OnFileChanged(self, evt):
        self._airdropSOURCEaddress = []
        with open(self.m_filePicker1.GetPath()) as f:
            self._airdropSOURCEaddress = f.read().splitlines()
    
        self.m_listBox7.Clear()
        
        self.m_listBox7.AppendItems(self._airdropSOURCEaddress )
    
    def __CheckFeasibility__(self):
        _maxRequested = float(self._currentUTXOcount) *  float(self._currentAmount)
        
        print(f"__CheckFeasibility__ _maxRequested = {_maxRequested}  , av= {self._currentBalance}" )  
        if self._currentBalance>=_maxRequested :
            return True
        return False
        
    
    
    def OnClickCreateUTXO(self, evt):
        print("OnClickCreateUTXO")  
        
        
        if not self.__CheckFeasibility__():
            UserError(self, "request exceeding balance, reduce UTXO count or amount.")
            return None 
        
        
        if UserQuestion(self, f"Do you confirm the Airdrop of {self._currentAmount} {self._currentAsset } to {self._currentUTXOcount} addresses ? \n"):
            #_result =  self.__GenerateUTXO__()
            _result = self.__GenerateAirdrop__()
            pass
        
        
    def OnRocketDropClicked(self, evt):
        print("OnRocketDropClicked")  
        
        pass
        """
        _needSplitter = False
        
        self._currentUTXOcount = len(self._airdropSOURCEaddress)
        if self._currentUTXOcount > 5000:
            self._currentUTXOcount = 5000
        
        
        
        if not self.__CheckFeasibility__():
            UserError(self, "request exceeding balance, reduce UTXO count or amount.")
            return None 
        
        
        if UserQuestion(self, f"Do you confirm the {self._currentUTXOcount} Airdrop of {self._currentAmount} {self._currentAsset } ? \n"):
            #_result =  self.__GenerateUTXO__()
            #_result = self.__GenerateAirdrop__(False)
            
            
            
            myPlugin = self.parent_frame.GetPlugin("P2PMarket")
            p2p_market_change_address = myPlugin.PLUGIN_SETTINGS['p2p_market_change_address']
            ravencoin = self.parent_frame.getRvnRPC()
            _allAddresses = self.SelectWinnerInList()
        
            
            allTx = []
            
            _curStart = 0
            _step = 1000
            _curStop = _curStart + _step
            while  _curStart < len(_allAddresses):
                if _curStop > len(_allAddresses):
                    _curStop = len(_allAddresses)
                
                _packAddress = _allAddresses[_curStart:_curStop]
                _tx = None
                
                if self._currentAsset  == 'RVN':
                    pass
                    #_tx = ravencoin.wallet.sendSameRVN_Many( self._currentAmount, adresses=_allAddresses, pwd='', _changeAddress=p2p_market_change_address, _fund=False, _sign=True, _execute=False)
                   
                    #print(f"RVN  {_tx}") 
                else:
                    
                    _tx = ravencoin.wallet.sendSameAsset_Many(  self._currentAsset, self._currentAmount, adresses=_packAddress, pwd='', _changeAddress=p2p_market_change_address, _fund=True, _sign=True, _execute=True)    
                    #print(f"Asset  {_tx}") 
                    
                    
                  
                allTx.append(_tx)
                
                
                _curStart = _curStart+_step
                _curStop = _curStop + _step
                
                
            
        print(f"ALL TX  {allTx}")     
            
            #_res= ravencoin.wallet.CombineTransaction(allTx,_fund=True, _sign=True, _execute=True)
            #print(_res)
            
        """    
              
        
        
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
            self.parent_frame.Log("Unable to load p2p Market datas" , type="warning")
                    
            
            