'''
Created on 13 janv. 2022

@author: slinux
'''

import wx
from libs import RavencoinP2PMarketPlaceAd

from wxRavenGUI.application.wxcustom import *



class MarketPlaceAdRightclickPopupMenu(object):
    '''
    classdocs
    '''


    def __init__(self, parentBinding, parentFrame, adData:RavencoinP2PMarketPlaceAd):
        '''
        Constructor
        '''
        self._menu = wx.Menu()
        
        self.popupIDS = {}
        self.popupMAP = {}
        
        
        
        #self._ipfsgateway_providers = parentFrame.GetPluginSetting("Ravencore","ipfsgateway_providers")
        #self._ipfsgateway_default = parentFrame.GetPluginSetting("Ravencore","ipfsgateway_default")
        
        self.parentBinding = parentBinding
        self.parent_frame = parentFrame
        
        
        self._data= adData
        self._hasTx = False
        self._TxCount = 0
        
        if not adData.isEmptyTxData():
            self._hasTx =  True
            self._TxCount = len(adData._adTxDatas)
        else:
            self._hasTx =  False
            
            
            
        
        self.createMenu()
        
        
    
    
   
        
    def createMenu(self):   
        self.__createItemsIds__()
        self.__createMenuItems__()
        
        
        
    
    
    def __createItemsIds__(self):
        if not self.popupIDS.__contains__("popupID1"):
            
            pptext = "popupID"
            ppcount = 1
            
            if self._data._adTxDatas!= None:
                for p in self._data._adTxDatas:
                    popupID = wx.NewId()
                    _pp = pptext + str(ppcount)
                    self.popupIDS[_pp] = popupID
                    self.popupMAP[popupID] = p
                    self.parentBinding.Bind(wx.EVT_MENU, self.OnOpenOrder, id=popupID)
                    ppcount= ppcount+1
                    
                    if ppcount > 10: 
                        break
                
                
                
    
    def __createMenuItems__(self):
        
        # make a menu
        #menu = wx.Menu()
        self._menu = wx.Menu()
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        
        
        
        # Preview
        nid = wx.NewId()
        self._preview = self._menu.Append(nid, "Open Ad Details" )
        self._preview.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('ressource_picture'))
        self.parentBinding.Bind(wx.EVT_MENU, self.openAdDetails, id=nid)
        
        
        self._menu.AppendSeparator()
        
        
        nid = wx.NewId()
        self._search = self._menu.Append(nid, "Inspect Asset In Ravencore" )
        self._search.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('search_asset'))
        self.parentBinding.Bind(wx.EVT_MENU, self.inspectAsset, id=nid)
        
        
        self._menu.AppendSeparator()
        
        #Add Bkmrk
        #
        nid = wx.NewId()
        self._addBk = self._menu.Append(nid, "Add/Remove Address in blacklist", '',  wx.ITEM_NORMAL)
        self._addBk.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('blacklist'))
        self.parentBinding.Bind(wx.EVT_MENU, self.addInBlacklist, id=nid)
        
        
        #self._addBk.Check( myPlugin.isBlackList(self._data._adAddress) )
        
        
        #Navigate
        #ITEM_CHECK
        nid = wx.NewId()
        self._addTr = self._menu.Append(nid, "Add/Remove Address in Trusted Peers" , '',  wx.ITEM_NORMAL)
        self._addTr.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('trusted_peer'))
        self.parentBinding.Bind(wx.EVT_MENU, self.addPeerInTrusted, id=nid)
        
        
        
        #self._addBk.Check( myPlugin.isTrusted(self._data._adAddress) )
        
        
        #
        #
        #
        
        
        
        self._menu.AppendSeparator()
        
        
        
        #
        #
        #
        
        
        #webresources16
        _tx_menu = wx.Menu()
        _tx_menu_item = self._menu.AppendSubMenu(_tx_menu, "Available Order(s)")
        _tx_menu_item.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('raw_datas'))
        
        
        pptext = "popupID" 
        ppcount = 1
        
        if self._hasTx :
        
            for p in self._data._adTxDatas:
                pptext = "popupID"
                _pp = pptext + str(ppcount)
                _i = _tx_menu.Append(self.popupIDS[_pp], f"Order {p}")
                _i.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('raw_datas'))
                ppcount= ppcount+1
                
                if ppcount > 10: 
                        break
                
        else:
            _tx_menu_item.Enable(False)
        
        """
        # Preview
        nid = wx.NewId()
        _preview = self._menu.Append(nid, "Preview" )
        _preview.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('ressource_picture'))
        self.parentBinding.Bind(wx.EVT_MENU, self.previewIPFS, id=nid)
        
        
        
        # Copy Hash
        nid = wx.NewId()
        _copyHash = self._menu.Append(nid, "Copy Hash" )
        _copyHash.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('copy_clipboard'))
        self.parentBinding.Bind(wx.EVT_MENU, self.copyHash, id=nid)
        
        
        
        # Open items
        nid = wx.NewId()
        _opendefaultipfs = self._menu.Append(nid, "Open IPFS" )
        _opendefaultipfs.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('raven_ipfs'))
        self.parentBinding.Bind(wx.EVT_MENU, self.openDefaultIPFS, id=nid)
        
        
        
        #webresources16
        _ipfs_menu = wx.Menu()
        _ipfs_menu_item = self._menu.AppendSubMenu(_ipfs_menu, "Open IPFS with...")
        _ipfs_menu_item.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('webresources16'))
    
        pptext = "popupID" 
        ppcount = 1
        
        for p in self._ipfsgateway_providers:
            pptext = "popupID"
            _pp = pptext + str(ppcount)
            _i = _ipfs_menu.Append(self.popupIDS[_pp], p)
            _i.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('webresources16'))
            ppcount= ppcount+1
            
        
        
        #_hasIpfs =  _data['has_ipfs']
        
        
        if not self._hasIpfs:
            _ipfs_menu_item.Enable(False)
            _opendefaultipfs.Enable(False)
            _copyHash.Enable(False)
            _preview.Enable(False)
        #menu.Append(self.popupID2, "Iterate Selected")
        #menu.Append(self.popupID3, "ClearAll and repopulate")
        #menu.Append(self.popupID4, "DeleteAllItems")
        #menu.Append(self.popupID5, "GetItem")
        #menu.Append(self.popupID6, "Edit")
        """
        
        
        
        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.parentBinding.PopupMenu(self._menu)
        self._menu.Destroy()   
    
    
    def OnOpenOrder(self, event):
        #self.log.WriteText("Popup one\n")
        #print("FindItem:", self.m_listCtrl1.FindItem(-1, "Roxette"))
        #print("FindItemData:", self.m_listCtrl1.FindItemData(-1, 11))
        
        _data= self._data
        print(str(self.popupMAP[event.GetId()]))
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        
        
        
        #
        # CHANGED
        #
        
        #myPlugin.ShowTxInfos(self._data._adTxDatas[self.popupMAP[event.GetId()]], openIfnotExist=True)
        
        myPlugin.ShowAdInfos(_data, self.popupMAP[event.GetId()] , openIfnotExist=True)
        
        
        
        
        
        #if self._hasTx:
        #    self.parent_frame.GetPlugin("Ravencore").OpenIPFSinWebBrowser(_data, str(self.popupMAP[event.GetId()]))
        
        
    def inspectAsset(self, event):
        myPlugin = self.parent_frame.GetPlugin('Ravencore')
        
        _assetInspect = self._data._adAsset
        
        if self._data._adType in range(1,2):
            _assetInspect = self._data._adPriceAsset
        
        if myPlugin!= None:
            myPlugin.OnSearchRequested_T( keyword=_assetInspect, limit=50, onlyMain=False, openViewAfter=True)
            
    
    
    def addInBlacklist(self, event):
        #itemData = self._data
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        
        
        if not myPlugin.isBlackList(self._data._adAddress):
            
           
            myPlugin.AddAddressInBlacklist(self._data._adAddress)
            print('AddAddressInBlacklist')
        else:
            myPlugin.RemoveAddressFromBlacklist(self._data._adAddress)
            print('RemoveAddressFromBlacklist')
        
        """
        _navItem = itemData['name']
        #print(itemData['type'])
        
        
        
        if itemData['type'] != 'MAINASSET':
            
            dlg = wx.MessageDialog(self.parentBinding, 'The Asset you selected is not a main asset, add main asset in bookmark instead ?',
                               'Confirmation',
                               wx.YES_NO | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
            res=dlg.ShowModal()
            dlg.Destroy()
            
            if res==wx.ID_YES or res==wx.YES:
            
                _navItem = itemData['parent'] 
            
            
        self.parent_frame.GetPlugin("Ravencore").AddAssetInBookmark(str(_navItem))
        
        
        dlg = wx.MessageDialog(self.parentBinding, 'Asset added in the Bookmark with Success !',
                               'Confirmation',
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()
        """
    
    
    def addPeerInTrusted(self, event):
        
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        
        
        print('addPeerInTrusted')
        if not myPlugin.isTrusted(self._data._adAddress):
            
            
            _alias = RequestUserTextInput(self.parentBinding, "Enter an alias for this address", "Enter an alias")
            
            
            if _alias != "":
                myPlugin.AddAddressInTrusted(self._data._adAddress,_alias )
            
                print('added')
        else:
            myPlugin.RemoveAddressFromTrusted(self._data._adAddress)
            print('removed')
    
    
    
    def openAdDetails(self, event):
        
        print('openAdDetails')
        print(self._data._adTitle)
        
        myPlugin = self.parent_frame.GetPlugin('P2PMarket')
        #adData:RavencoinP2PMarketPlaceAd
        myPlugin.OpenAdDetails(self._data)
        #ShowTxInfos
        #if self._hasIpfs :
        #    _url = self._ipfsgateway_default  + self._data['ipfs_hash']
        #    self.parent_frame.GetPlugin("Ravencore").previewIPFS(_url)

    
    
    
    
    
    def copyHash(self, event):
        if self._hasIpfs :
            _data= self._data
            self.parent_frame.GetPlugin("Ravencore").CopyClip(_data)
  
        
    
    def openDefaultIPFS(self, event): 
        if self._hasIpfs :
            _data= self._data
            self.parent_frame.GetPlugin("Ravencore").OpenIPFSinWebBrowser(_data)
           

        
    def getMenu(self):
        return self._menu