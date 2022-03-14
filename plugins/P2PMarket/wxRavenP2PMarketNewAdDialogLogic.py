'''
Created on 8 janv. 2022

@author: slinux
'''

#from .wxRavenTutorialPluginDesign import *

import threading
import time 

from .wxRavenP2PMarketDesign import * 
from wxRavenGUI.application.wxcustom import *

from libs.RVNpyRPC._P2PmarketPlace import RavencoinP2PMarketPlaceAd, _P2PMARKET_ID_


from .wxRavenCreateAtomicSwapLogic import *
#from .wxRavenP2PMarket_AtomicTxPanel import *
from .wxRavenP2PMarket_RawTxPanel import * 

import os
import time
from datetime import datetime

import logging


class wxRavenP2PMarket_NewAdWithLogic(wxRavenP2PMarket_NewAdDialog):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "New P2P Market Ad"
    view_name = "New P2P Market Ad"
    parent_frame = None
    default_position = "dialog"
    icon = 'p2p_icon_new'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent, parentFrame,  position = "dialog", viewName= "New P2P Market Ad", isInternalPluginView=True):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "New P2P Market Ad"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parent
        
        self.logger = logging.getLogger('wxRaven')
        
        self.m_toggleAssistant.SetBitmap(parentFrame.RessourcesProvider.GetImage('wizard_ico'))
        self.m_toggleRawTxDatas.SetBitmap(parentFrame.RessourcesProvider.GetImage('raw_datas'))
        
        
        self._useWizard = True
        self._timestamp = round(time.time() * 1000) 
        self._filegenerated = False
    
        self._validChanel = False
    
        
        self._MethodsPanelList = {}
        
        self.TxMethodPanelSizer = None
        #
        #
        # Wizard default datas
        #
        self._newAdObject = RavencoinP2PMarketPlaceAd()
        self._newAdObject._adType=0
        self._newAdObject._adTxType=0
        self._newAdObject._adOrders=1
        self._newAdObject._adAssetQt=1
        self._newAdObject.m_AdAssetPrice='rvn'
        self._newAdObject._adPrice=200
        
        self._forceManual = False
        self.savepath = self.parent_frame.Paths['USERDATA'] + 'p2pmarket/'
        #
        #
        #
        
        
        '''
        self._MethodsPanelList = {0:wxRavenP2PMarket_NewAtomiSwapWithLogic,
                                  1:wxRavenP2PMarket_NewAtomiSwapWithLogic,
                                  2:wxRavenP2PMarket_NewAtomiSwapWithLogic}
        '''
        #_defaultAtomicSwapPanel = self.__LoadMethodPanel__(wxRavenP2PMarket_AdAtomiSwapWithLogic, True)
        _defaultAtomicSwapPanel = self.__LoadMethodPanel__(wxRavenP2PMarket_NewAtomiSwapWithLogic, True)
        
        _RawAtomicSwapPanel =  self.__LoadMethodPanel__(wxRavenP2PMarket_RawAtomiSwapWithLogic, False)
        
        self._MethodsPanelList = {0:_defaultAtomicSwapPanel ,
                                  1:None ,
                                  2: _RawAtomicSwapPanel}
        
        self.setupPanel()
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        #if not isInternalPluginView:
        #    parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
        self.Layout()
        self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
        
        self.parent.ResizeDialog()
    
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        #self.waitApplicationReady()
    
    
    def OnWizardButtonToggle(self, evt):
        self._useWizard = self.m_toggleAssistant.GetValue()
        
        if self._useWizard:
            self.m_assistantPanel.Show()
            self.m_AdFileIPFSHash.Enable(enable=False)
            self.m_PreviewAdBt.Show()
            if self._filegenerated:
                self.m_GeneraeteAdBt.Enable(True)
            else:
                self.m_GeneraeteAdBt.Enable(False)
            
        else:
            self.m_assistantPanel.Hide()
            self.m_AdFileIPFSHash.Enable(enable=True)
            self.m_PreviewAdBt.Hide()
            #self.m_staticline18.Hide()
            #self.m_txDatas.Hide()
            self.m_GeneraeteAdBt.Enable(True)
        #self.SetSizerAndFit(sizer, deleteOld=True)
        self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
        #self.Layout()
        self.parent.ResizeDialog()
        
        
    
    
    
    
        
    def OnGenerateButtonClick(self, evt):
        
        _userCheck = UserQuestion(self, "Once publish you cannot modify the Ad anymore, continue ?")
            
        if _userCheck:
            
            ravencoin = self.parent_frame.getRvnRPC()
            
            myPlugin = self.parent_frame.GetPlugin('P2PMarket')
            p2p_channel_asset_target_address = myPlugin.PLUGIN_SETTINGS['p2p_channel_asset_target_address']
            p2p_market_change_address = myPlugin.PLUGIN_SETTINGS['p2p_market_change_address']
            
            
            _hashFile = self.m_AdFileIPFSHash.GetValue()
            
            _fakeResult = {'result':None , 'error': {'code':-1, 'message': f"Unknown error, please check logs."}}
        
            
            try:
                _fakeResult = ravencoin.p2pmarket.PublishNewP2PAd(self._newAdObject._adP2PChannelAsset, p2p_channel_asset_target_address, _hashFile, p2p_market_change_address, expiration=200000000 )
            
                
                #UserInfo(self, "Your asset is on the P2P Marketplace !")
            
            
            except Exception as e:
                self.parent_frame.Log("Unable to load publish p2p Market ad." , type="error")
                _fakeResult = {'result':None , 'error': {'code':-1, 'message': e}}
        
            ReportRPCResult(self.parent_frame, _fakeResult, "success", "Your asset is on the P2P Marketplace !", "Unable to publish your ad.", False)
        
    
    def OnPreviewAdButtonClick(self, evt):
        
        self.OnAdTypeChanged(None)
        self.OnTitleChanged(None)
        #self.OnAssetChanged(None)
        self.OnTxMethodChanged(None)
        #self.OnQuantityChanged(None)
        #self.OnPriceChanged(None)
        self.OnLinkChanged(None)
        self.OnDescriptionChanged(None)
        self.OnP2PChannelChanged(None)
        self.OnKeywordChanged(None)
        
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        ravencoin = self.parent_frame.getRvnRPC()
        
        _hasvalidTx = False
        _hasTx = False
        print(self._newAdObject)
        
        
        _fakeResult = {'result':None , 'error': {'code':-1, 'message': f"Unknown error, please check logs."}}
        
        if self._newAdObject.isEmptyTxData():
            _doCreateSwap = False
            
            _doCreateSwap = UserQuestion(self, "The atomic swap transaction is not yet created, create it now ?")
            
            
            if _doCreateSwap :
                self._newAdObject = ravencoin.p2pmarket.CreateAtomicSwapTransaction(self._newAdObject)
                self.logger.info(f"CreateAtomicSwapTransaction DONE = {self._newAdObject._adTxDatas}")
        
        
        
        
        
        if self._newAdObject.isEmptyTxData():
            self.m_P2PmethodErrorText.SetLabel("Error : No Atomicswap datas tx generated !")   
            
            self.m_bitmap38.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('error_tsk'))
            
            #self.m_atomicTransactionUserFeedback.SetLabel("Error : No Atomicswap datas tx generated")
        else:
            self.m_P2PmethodErrorText.SetLabel("P2P Method : Atomicswap datas found !") 
            self.m_bitmap38.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('passed'))
            self.LockAllMethodPanel(True)
            self.SetManualPanelValue(self._newAdObject._adTxDatas)
            
            self.logger.info(f"P2P Method : Atomicswap datas found , verifying TX")
            
            _hasTx=True
            try:
                _valid, _data = myPlugin.DecodeTx(self._newAdObject._adTxDatas[0])
                if _valid:
                    _hasvalidTx = True
            except Exception as e:
                self.logger.error(f"P2P Method : error in TX")
                _hasvalidTx = False
        
        
        self.Layout()
        self.m_assistantPanel.Layout()
        
        
        
        _hash = None
        
        if _hasTx and _hasvalidTx:
            pass
        
        
        
        
            _filtetosave = self.savepath + 'p2p_market_order' + str(self._timestamp) + '.json'   
            f = open(_filtetosave, "w")
            f.write(str(self._newAdObject.JSON()))
            f.close()     
        
            #
            #ALL GOOD
            #self.m_atomicTransactionUserFeedback.SetLabel(self._newAdObject._adTxDatas)
        
            
            ipfsPlugins = self.parent_frame.GetPlugin('IPFS')
            
            _hash = None
            
            if ipfsPlugins != None:
                
                try:
                    _hash = ipfsPlugins.UploadJSONToIPFS_RPC(str(self._newAdObject.JSON()))
                except Exception as e:
                    self.parent_frame.Log("Unable to load upload p2p Market json datas to IPFS." , type="error")
                
                if _hash!=None:
                    self.m_AdFileIPFSHash.SetValue(str(_hash))
            
            
            
                
            if _hash == None:
                
                
                #UserInfo(self, f"No IPFS Plugin or an error occured, filed has been saved in {_filtetosave} for manual upload.")
                UserAdvancedMessage(self.parent_frame, f"No IPFS Plugin or an error occured, filed has been saved in {_filtetosave} for manual upload.", "info", msgdetails=_filtetosave, showCancel=False)
            
            
            
        else:
            #UserError(self, f"An error occured while creating the atomic swap, please retry.")
            UserAdvancedMessage(self.parent_frame, f"An error occured while creating the atomic swap, please retry.", "error", msgdetails='', showCancel=False)
            self.m_toggleRawTxDatas.SetValue(True)
            self.SwitchMethodPanel(manual=True)
        
            
        
        
        if _hash != None :
                self.m_GeneraeteAdBt.Enable(True)
                #UserInfo(self, f"Ad created, ready for upload.") 
                UserAdvancedMessage(self.parent_frame, f"Ad created, ready for upload.", "info", msgdetails='', showCancel=False)
            
        #else:
        #    self.parent_frame.Log("Unable to load upload p2p Market json datas to IPFS." , type="error")        
                   
            
        self.logger.info(self._newAdObject.JSON())
        #self._newAdObject._adAsset = 
        
        
        
        
        
    
    
    def OnAdTypeChanged(self, evt):
        self._newAdObject._adType = self.m_radioBox1.GetSelection()
        
        self.OnTxMethodChanged(evt)
    
    def OnTitleChanged(self, evt):
        self._newAdObject._adTitle = self.m_AdTitle.GetValue()
    
    """
    def OnAssetChanged(self, evt):
        self._newAdObject._adAsset = self.m_AdAssetChoice.GetString(self.m_AdAssetChoice.GetCurrentSelection())
    """
    
    
    def OnToggleRawTxData(self, evt):
        self.OnTxMethodChanged(evt)
    
    def OnCreateUTXODialogClicked(self, evt):
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        myPlugin.CreateNewUTXO()
    
    
    def OnTxMethodChanged(self, evt):
        _str = self.m_txMethod.GetString(self.m_txMethod.GetCurrentSelection())
        self.logger.info(_str)
        self._newAdObject._adTxType = _P2PMARKET_ID_[_str]
        
        _forceManual = self.m_toggleRawTxDatas.GetValue()
        self._forceManual = _forceManual
        self.SwitchMethodPanel(manual=_forceManual)
        
    
    def LockAllMethodPanel(self, locking):
        for panKey in self._MethodsPanelList:
            
            pan = self._MethodsPanelList[panKey]
            self.logger.info(f'found {panKey} {pan}')
            if pan != None:
                self.logger.info(f'locking {panKey}')
                try:
                    pan.LockPanel(locking)
                except Exception as e:
                    pass
        
    
    
    def SetManualPanelValue(self, val):
        _manualPanel = self._MethodsPanelList[2]
        if _manualPanel != None:
            _manualPanel.m_rawDatasText.SetValue(str(val))
    
    
    
    def SwitchMethodPanel(self,manual=False):
        self.logger.info(f"SwitchMethodPanel {manual}")
        
        _type = self._newAdObject._adTxType
        _adtype = self._newAdObject._adType
        
        if self._MethodsPanelList == {}:
            return
        
        if manual == True:
            _type = 2
            
            
        for panKey in self._MethodsPanelList:
            
            pan = self._MethodsPanelList[panKey]
            self.logger.info(f'found {panKey} {pan}')
            if pan != None:
                self.logger.info(f'hiding {panKey}')
                pan.Hide()
        
        self.logger.info(_type)
        _toShow = self._MethodsPanelList[_type]
        
        if _toShow != None:
            _toShow.Show()
            self.logger.info(f"onswapchangedforce = {_adtype}")
            _toShow.OnSwapTypeChanged(evt=None ,forceId=_adtype)
            
            
            #w, h = _toShow.GetSize()
            #w = h
            #_toShow.SetSize(w, 150)
            #self.m_txMethodPanel.SetSize(w, 150)
            self.Layout()
            #panel.SetSize(w, h)
            
            
            #_toShow.SetSizerAndFit(self.TxMethodPanelSizer,deleteOld=False)
            #self.m_txMethodPanel.SetSizerAndFit(self.TxMethodPanelSizer,deleteOld=False)
        
        #self.m_txMethodPanel.SetSizerAndFit(self.TxMethodPanelSizer)
        
        
    """    
    def OnQuantityChanged(self, evt):
        self._newAdObject._adAssetQt = self.m_AdAssetQt.GetValue()
        
    def OnPriceChanged(self, evt):
        self._newAdObject._adPrice = self.m_AdAssetPrice.GetValue()
    """
    def OnLinkChanged(self, evt):
        self._newAdObject._adExternalLink = self.m_AdLink.GetValue()
    
    def OnDescriptionChanged(self, evt):
        self._newAdObject._adDescription = self.m_AdDescription.GetValue()
        
    def OnKeywordChanged(self, evt):
        self._newAdObject._adKeywords = self.m_AdKeyword.GetValue()
    
    
    
    
    
    def __checkChannel__(self):
        self._validChanel = False
        try:
            myPlugin = self.parent_frame.GetPlugin('P2PMarket')
            ravencoin = myPlugin.__getNetwork__()
            #balanceChanel = ravencoin.asset.GetBalance(self._newAdObject._adP2PChannelAsset)
            
            self._validChanel = ravencoin.p2pmarket.CheckP2PAnnouncerAccount(self._newAdObject._adAddress, self._newAdObject._adP2PChannelAsset, setupIfNotReady=False , password="")
            
            #if balanceChanel > 0.2:
            #    self._validChanel = True
            
        except Exception as e:
            self.parent_frame.Log("Unable to load Chanel '{self._newAdObject._adP2PChannelAsset}' balance" , type="warning")
         
         
         
        if self._validChanel:
            self.m_bitmap16.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('passed')) 
        else:
            
            
            self.m_bitmap16.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('warning_2'))    
        
        
        self.Layout()    
        return self._validChanel
        
    
    
    
    def OnP2PChannelChanged(self, evt):
        _str = self.m_AdP2PChannelChoice.GetString(self.m_AdP2PChannelChoice.GetCurrentSelection())
        self._newAdObject._adP2PChannelAsset = _str
        
        self.__checkChannel__()
        
        
        
        
        
        

    def __LoadMethodPanel__(self, panel, show=False):
        
        if self.TxMethodPanelSizer == None:
            self.TxMethodPanelSizer = wx.BoxSizer( wx.VERTICAL )
            
            
        _newPanel = panel(self.m_txMethodPanel, self.parent_frame, isInternalPluginView=True, isInternalPanel=True, parentDataObj=self) 
        self.TxMethodPanelSizer.Add( _newPanel, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        
        if show:
            self.SwitchMethodPanel(False)
        
        
        
        self.m_txMethodPanel.SetSizerAndFit(self.TxMethodPanelSizer)
            
        
        self.Layout()
        return _newPanel

    def setupPanel(self):
        
        '''
        self._MethodsPanelListClasses = {0:wxRavenP2PMarket_NewAtomiSwapWithLogic,
                                  1:wxRavenP2PMarket_NewAtomiSwapWithLogic,
                                  2:wxRavenP2PMarket_NewAtomiSwapWithLogic}
        '''
        
        
        
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        ravencoin = myPlugin.__getNetwork__()
        
        
        
        if not ravencoin.test_rpc_status():
            UserError(self.parent_frame, "You must have an active connexion !")
        
        
        
        #self.m_AdAssetChoice.Clear()
        self.m_AdP2PChannelChoice.Clear()
        
        '''
        _allAdmins= ravencoin.asset.GetAllMyAssets()
        '''
        _allNotAdmins= ravencoin.asset.GetAllMyAssets(_excludeAdmin=True)
        
        
        #self.logger.info(_allAdmins)
        defaultChannel = myPlugin.PLUGIN_SETTINGS['p2p_channel_asset_default']
        
        AnnouncerAddress = myPlugin.PLUGIN_SETTINGS['p2p_channel_asset_target_address']
        self._newAdObject._adAddress = AnnouncerAddress
        '''
        for key in _allAdmins:
            
            self.m_AdAssetChoice.Append(key)
        '''

        for key in _allNotAdmins:    
            self.m_AdP2PChannelChoice.Append(key)
    
        
        _dc = self.m_AdP2PChannelChoice.FindString(defaultChannel)
        if _dc != wx.NOT_FOUND:
            self.m_AdP2PChannelChoice.SetSelection(_dc)
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.UpdateView,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
    
            
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
                    
            
            
            
            