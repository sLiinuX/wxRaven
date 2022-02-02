'''
Created on 31 janv. 2022

@author: slinux
'''


import threading
import time 

#from .wxRavenP2PMarketDesign import * 
from wxRavenGUI.application.wxcustom import *

from .wxRavenP2PMarketDesign import wxRavenP2PMarket_AdDetails, wxRavenP2PMarket_AdDetails_Splitter

#from plugins.Ravencore.wxRavenRavencoreDesign import wxRavenHTMLViewer
from libs import RavencoinP2PMarketPlaceAd


class wxRavenP2PMarket_AdDetailsLogic(wxRavenP2PMarket_AdDetails_Splitter):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Ad Details"
    view_name = "Ad Details"
    parent_frame = None
    default_position = "main"
    icon = 'inspect_file'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame,  position = "main", viewName= "Ad Details", isInternalPluginView=False, isInternalPanel=False, parentDataObj=None):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Ad Details"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parentFrame
        
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self.m_topPanel)
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self.m_detailTabPanel)
        
        self.isInternalPluginView = isInternalPluginView
        self.isInternalPanel = isInternalPanel
        self.parentDataObj = parentDataObj
        self.allIcons = {}
        
        
        self.currentAd = None
        self.websiteTab = None
        self.AssetTab = None
        
        
        '''
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
        
        
        #self.setupPanel()
        #self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
        #self.Fit()
        
        #self.Layout()
        
        
        
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
    
    
    def OnOpenTxClicked(self, evt):
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        #adData:RavencoinP2PMarketPlaceAd
        myPlugin.ShowAdInfos(self.currentAd)    
    
    
    def LoadAd(self, adData:RavencoinP2PMarketPlaceAd):  
        
        
        self.m_TitleText.SetLabel(adData._adTitle )
        self.m_DescriptionText.SetLabel(adData._adDescription)
        
        print(f'Loading url : {adData._adExternalLink}')
        self.m_websiteText.SetLabel(adData._adExternalLink)
        if adData._adExternalLink == '':
            self.m_websiteText.SetLabel('{N/A}')
        
        
        
        self.currentAd = adData
        self.websiteTab.LoadURL(adData._adExternalLink)
        
        
        
        
        _assetPreviewDatas = ''
        if self.currentAd.GetType() == "Sell":
            _assetPreviewDatas = self.currentAd._adAsset
        elif self.currentAd.GetType() == "Buy":
            _assetPreviewDatas = self.currentAd._adPriceAsset
        elif  self.currentAd.GetType() == "Trade":
            _assetPreviewDatas = self.currentAd._adPriceAsset
        
        print(f'Loading _assetPreviewDatas : {adData}')
        print(f'Loading _assetPreviewDatas : {_assetPreviewDatas}')
        
        
        self.m_assetText.SetLabel(_assetPreviewDatas + ' - [IPFS : N/A]')
        
        ravencoin = self.parent_frame.getRvnRPC()
        #ravencoin.asset.
        try:
            _assetData = ravencoin.asset.GetAssetData({'name':_assetPreviewDatas})
            if  _assetData['has_ipfs']:
                _hash =  _assetData['ipfs_hash']
                
                
                myIpfsPlugin = self.parent_frame.GetPlugin('Ravencore')
                _baseUrl = myIpfsPlugin.PLUGIN_SETTINGS['ipfsgateway_default']
                
                self.m_assetText.SetLabel(_assetPreviewDatas + f' - [IPFS : {_hash}]')
                
                
                url= _baseUrl + _hash
                self.AssetTab.LoadURL(url)
                
            
        except Exception as e:
            self.parent_frame.Log(f"Unable to load ipfs asset datas : {e}" , type="warning")
        #self.AssetTab = adData.
        
        
        self.Layout() 
        
        
    def setupPanel(self):
            
    
        #wxRavenHTMLViewer(parent)
         
        
        #self.AssetTab = wxRavenHTMLViewer(self.m_detailTabPanel ) 
        self.AssetTab = wxRavenWebview.GetWebView(self.m_detailTabPanel)
        _icon = self.parent_frame.RessourcesProvider.GetImage('asset')
        self.m_auinotebook1.AddPage(self.AssetTab, 'Asset Preview', bitmap = _icon)
        
        
        #self.websiteTab = wxRavenHTMLViewer(self.m_detailTabPanel ) 
        self.websiteTab = wxRavenWebview.GetWebView(self.m_detailTabPanel)
        _icon = self.parent_frame.RessourcesProvider.GetImage('browser')
        self.m_auinotebook1.AddPage(self.websiteTab, 'Website', bitmap = _icon)
        print('pannel ok')
        self.Layout()
        
        
        
        