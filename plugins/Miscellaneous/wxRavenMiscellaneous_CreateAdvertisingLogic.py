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

class wxRavenMiscellaneous_CreateAdvertisingWithLogic(wxRavenMiscellaneous_Advertising):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Create Advertising"
    view_name = "Create Advertising"
    parent_frame = None
    default_position = "dialog"
    icon = 'advertiser_icon'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent, parentFrame,  position = "dialog", viewName= "Create Advertising", isInternalPluginView=False, isInternalPanel=True, parentDataObj=None):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Create Advertising"
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
        
        self._startTime = 0
        self._stopTime = 0
        self._threadRunning = False
        self.allTx = []
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
    
    
    
    
    
    
    
    def SelectWinnerInList(self, allwins=False):
        winnerList = []
        
        isRandom= False#self.m_checkBox26.GetValue()
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
        
        '''
        myPlugin = self.parent_frame.GetPlugin("P2PMarket")
        p2p_market_change_address = myPlugin.PLUGIN_SETTINGS['p2p_market_change_address']
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
                UserAdvancedMessage(self.parent_frame, f"Airdrop Sent to {len(_allAddresses)} Addresses {_rdmText} !", "success", msgdetails=f'{_tx}', showCancel=False)
            else:
                UserAdvancedMessage(self.parent_frame, f"Airdrop Failed !", "error", msgdetails=f'{_tx}', showCancel=False)   
        #except Exception as e:
        #    self.parent_frame.Log(f"Unable Generate UTXO : {e}" , type="warning")
        
        
        return _tx
        '''
        
    
    def OnFileChanged(self, evt):
        self._airdropSOURCEaddress = []
        with open(self.m_filePicker1.GetPath()) as f:
            self._airdropSOURCEaddress = f.read().splitlines()
    
        self.m_listBox7.Clear()
        
        self.m_listBox7.AppendItems(self._airdropSOURCEaddress )
        self._currentUTXOcount = len(self._airdropSOURCEaddress)
        
        UserAdvancedMessage(self.parent_frame, f"List of {len(self._currentUTXOcount)} Addresses has been loaded.", 'info')
    
    def __CheckFeasibility__(self):
        _maxRequested = float(self._currentUTXOcount) *  float(self._currentAmount)
        
        print(f"__CheckFeasibility__ _maxRequested = {_maxRequested}  , av= {self._currentBalance}" )  
        if self._currentBalance>_maxRequested :
            return True
        return False
        
    
    
    def OnClickCreateUTXO(self, evt):
        print("OnClickCreateUTXO")  
        
        '''
        if not self.__CheckFeasibility__():
            UserError(self, "request exceeding balance, reduce UTXO count or amount.")
            return None 
        
        
        if UserQuestion(self, f"Do you confirm the Airdrop of {self._currentAmount} {self._currentAsset } to {self._currentUTXOcount} addresses ? \n"):
            #_result =  self.__GenerateUTXO__()
            _result = self.__GenerateAirdrop__()
            pass
        
        '''
    
    
    
    
    
    
    def __waitMemPool__(self, _cur=1):
        time.sleep(5)
        wx.CallAfter(self.ReportMemPoolFull, _cur)
        
    
    def __ThreadReport__(self, pos=0):
        wx.CallAfter(self.ReportProgress, pos)
    
    def __RocketDrop_Threaded__(self, evt=None):
        self._threadRunning  = True
        self._startTime = datetime.now()
        
        
        if True:
            #myPlugin = self.parent_frame.GetPlugin("P2PMarket")
            #p2p_market_change_address = myPlugin.PLUGIN_SETTINGS['p2p_market_change_address']
            
            """
            Updated change address settings
            """
            myPlugin = self.parent_frame.GetPlugin("General")
            p2p_market_change_address = myPlugin.GetFavoriteChangeAddress()
            
            
            
            
            ravencoin = self.parent_frame.getRvnRPC()
            _allAddresses = self.SelectWinnerInList()
        
            
            allTx = []
            
            _curStart = 0
            _step = 1000
            _curStop = _curStart + _step
            while  _curStart < len(_allAddresses):
                if _curStop > len(_allAddresses):
                    _curStop = len(_allAddresses)
                    
                    
                self.__ThreadReport__(_curStart)
                
                _packAddress = _allAddresses[_curStart:_curStop]
                _tx = None
                _txOk = False
                
                
                if self._currentAsset  == 'RVN':
                    pass
                    #_tx = ravencoin.wallet.sendSameRVN_Many( self._currentAmount, adresses=_allAddresses, pwd='', _changeAddress=p2p_market_change_address, _fund=False, _sign=True, _execute=False)
                   
                    #print(f"RVN  {_tx}") 
                else:
                    print(f" pack = {len(_packAddress)}")
                    _txOk,_tx = ravencoin.wallet.sendSameAsset_Many(  self._currentAsset, self._currentAmount, adresses=_packAddress, pwd='', _changeAddress=p2p_market_change_address, _fund=True, _sign=True, _execute=True)    
                    print(ravencoin.RPCconnexion.getmempoolinfo()['result'])
                    
                    #network.getmempoolinfo()
                    
                    #print(f"Asset  {_tx}") 
                    
                    
                  
                allTx.append([_txOk,_tx])
                
                
                _curStart = _curStart+_step
                _curStop = _curStop + _step
                
                
                _usage = ravencoin.network.GetMempoolUsage()
                if _usage > 60:
                    while _usage > 60:
                        time.sleep(10)
                        _usage = ravencoin.network.GetMempoolUsage()
                
                time.sleep(1)
                '''
                if ravencoin.RPCconnexion.getmempoolinfo()['result']['size'] == 3:
                    
                    while ravencoin.RPCconnexion.getmempoolinfo()['result']['size'] >=3:
                        #time.sleep(5)
                        self.__waitMemPool__(_curStart)
    
                '''
    
    
    
    
            self.allTx = allTx
    
        self._threadRunning  = False 
        self._stopTime = datetime.now()
        wx.CallAfter(self.ReportFinnish)
    
    
    def ReportFinnish(self, evt=None):
        
        self.ReportDone()
        allTx = self.allTx
        #print(f"ALL TX  {allTx}")     
        time_elapsed = self._stopTime  - self._startTime 
        #print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed)) 
        elapsedClean = f'Time elapsed : {time_elapsed}'
        _someOk = False 
        _allOk = True
        for _r in allTx:
            _ok = _r[0]
            if not _ok:
                _allOk = False    
            else:
                _someOk = True
                
                
                
                
        if _allOk:
            UserAdvancedMessage(self.parent_frame, f"Advertising Sent to {self._currentUTXOcount} Addresses! \n {elapsedClean}", "success", msgdetails=f'{allTx}', showCancel=False)
            #_res= ravencoin.wallet.CombineTransaction(allTx,_fund=True, _sign=True, _execute=True)
            #print(_res)
        
        else:
            
            
            if   _someOk:
                UserAdvancedMessage(self.parent_frame, f"Advertising Partially sent to {self._currentUTXOcount} Addresses ! \n {elapsedClean}", "warning", msgdetails=f'{allTx}', showCancel=False)
            
            
            else:
                UserAdvancedMessage(self.parent_frame, f"Advertising Failed ! \n {elapsedClean}", "error", msgdetails=f'{_allOk}', showCancel=False)
                  
    def ReportMemPoolFull(self,cursor=1, evt=None):  
        self.m_ProgressText.SetLabel(f" Waiting for mempool : {cursor} / {self._currentUTXOcount}...")  
    
    def ReportProgress(self, cursor=1, evt=None):
        self.m_gauge1.SetRange(self._currentUTXOcount)
        self.m_gauge1.SetValue(cursor)
        self.m_ProgressText.SetLabel(f" {cursor} / {self._currentUTXOcount}")
        self.Layout()
    
    def ReportDone(self, evt=None):
        self.m_gauge1.SetRange(100)
        self.m_gauge1.SetValue(100)
        self.m_ProgressText.SetLabel(f" 100% Complete !")
        self.Layout()
    
        
    def OnRocketDropClicked(self, evt):
        print("OnRocketDropClicked")  
        
        
        _needSplitter = False
        
        #self._currentUTXOcount = len(self._airdropSOURCEaddress)
        
        
        
        if self._currentUTXOcount > 1000:
            #self._currentUTXOcount = 5000
            UserAdvancedMessage(self.parent_frame, f"Advertising exceeding 1000 address must be splitted and timed", 'info')
    
        
        
        
        if not self.__CheckFeasibility__():
            UserError(self, "request exceeding balance, reduce UTXO count or amount.")
            return None 
        
        
        if UserQuestion(self, f"Do you confirm the {self._currentUTXOcount} Airdrop of {self._currentAmount} {self._currentAsset } ? \n"):
            #_result =  self.__GenerateUTXO__()
            #_result = self.__GenerateAirdrop__(False)
            
            
            
            self._threadRunning  = True
            t=threading.Thread(target=self.__RocketDrop_Threaded__, args=(self.__RocketDrop_Threaded__,))
            t.start()
            
            self.m_RocketDrop.Enable(False)
            
            
            '''
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
                _txOk = False
                if self._currentAsset  == 'RVN':
                    pass
                    #_tx = ravencoin.wallet.sendSameRVN_Many( self._currentAmount, adresses=_allAddresses, pwd='', _changeAddress=p2p_market_change_address, _fund=False, _sign=True, _execute=False)
                   
                    #print(f"RVN  {_tx}") 
                else:
                    
                    _txOk,_tx = ravencoin.wallet.sendSameAsset_Many(  self._currentAsset, self._currentAmount, adresses=_packAddress, pwd='', _changeAddress=p2p_market_change_address, _fund=True, _sign=True, _execute=True)    
                    print(ravencoin.RPCconnexion.getmempoolinfo()['result'])
                    
                    #network.getmempoolinfo()
                    
                    #print(f"Asset  {_tx}") 
                    
                    
                  
                allTx.append([_txOk,_tx])
                
                
                _curStart = _curStart+_step
                _curStop = _curStop + _step
                
               ''' 
            
            
            
        '''    
        print(f"ALL TX  {allTx}")     
         
        _someOk = False 
        _allOk = True
        for _r in allTx:
            _ok = _r[0]
            if not _ok:
                _allOk = False    
            else:
                _someOk = True
                
                
                
                
        if _allOk:
            UserAdvancedMessage(self.parent_frame, f"Advertising Sent to {len(self._currentUTXOcount)} Addresses !", "success", msgdetails=f'{_allOk}', showCancel=False)
            #_res= ravencoin.wallet.CombineTransaction(allTx,_fund=True, _sign=True, _execute=True)
            #print(_res)
        
        else:
            
            
            if   _someOk:
                UserAdvancedMessage(self.parent_frame, f"Advertising Partially sent to {len(self._currentUTXOcount)} Addresses !", "warning", msgdetails=f'{_allOk}', showCancel=False)
            
            
            else:
                UserAdvancedMessage(self.parent_frame, f"Advertising Failed !", "error", msgdetails=f'{_allOk}', showCancel=False)
                  
        '''
        
    def LockPanel(self, locking): 
        print('pannel locked to avoid user modifications')
        
        if    locking:
            self.Enable(enable=False)
        else:
            self.Enable(enable=True)    
        
    def setupPanel(self):
        
        if self.parent_frame.getNetworkType() != 'RPC':
            _err = f"This view is not available with your current connexion {self.parent_frame.getNetworkType()}"
            #UserAdvancedMessage(parentf, message, type, msgdetails, showCancel)
            wx.CallAfter(UserError, self.parent_frame, _err)
            #UserError(self, )
            raise ConnectionError
        
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
            self.parent_frame.Log("Unable to load datas" , type="warning")
                    
            
            