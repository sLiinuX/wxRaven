'''
Created on 20 janv. 2022

@author: slinux
'''

import wx 


from wxRavenGUI.application.wxcustom import *

class RavencoreUTXORightclickPopupMenu(object):
    '''
    classdocs
    '''


    def __init__(self, parentBinding, parentFrame, assetData={}):
        '''
        Constructor
        '''
        self._menu = wx.Menu()
        
        self.popupIDS = {}
        self.popupMAP = {}
        
        
        self.parentBinding = parentBinding
        self.parent_frame = parentFrame
        
        
        self._data= assetData
        self._Locked = assetData['locked']
        #self._dataNone = False
        
        
        
        
        self.createMenu()
        
        
    
    
   
        
    def createMenu(self):   
        #self.__createItemsIds__()
        self.__createMenuItems__()
        
        
        
    
    '''
    def __createItemsIds__(self):
        if not self.popupIDS.__contains__("popupID1"):
            
            pptext = "popupID"
            ppcount = 1
            
            
            for p in self._ipfsgateway_providers:
                popupID = wx.NewId()
                _pp = pptext + str(ppcount)
                self.popupIDS[_pp] = popupID
                self.popupMAP[popupID] = p
                self.parentBinding.Bind(wx.EVT_MENU, self.OnOpenIPFSWithGateway, id=popupID)
                ppcount= ppcount+1
                
                
    '''        
    
    def __createMenuItems__(self):
        
        # make a menu
        #menu = wx.Menu()
        self._menu = wx.Menu()
        
        
        #Lock
        #
        if not self._Locked:
            nid = wx.NewId()
            _addBk = self._menu.Append(nid, "Lock" )
            _addBk.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('lock_icon'))
            self.parentBinding.Bind(wx.EVT_MENU, self.menuItemAction_Lock, id=nid)
        else:
            nid = wx.NewId()
            _addBk = self._menu.Append(nid, "Unlock" )
            _addBk.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('unlock'))
            self.parentBinding.Bind(wx.EVT_MENU, self.menuItemAction_Unlock, id=nid)
        
        
        #Navigate
        #
        nid = wx.NewId()
        _Navigate = self._menu.Append(nid, "View Tx" )
        _Navigate.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('inspect_file'))
        self.parentBinding.Bind(wx.EVT_MENU, self.menuItemAction_ShowTx, id=nid)
        
        

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.parentBinding.PopupMenu(self._menu)
        self._menu.Destroy()   
    
    
    def menuItemAction_Lock(self, event):
        _data= self._data
        ravencoin = self.parent_frame.getRvnRPC()
        
        #UserInfo(self.parentBinding, "Lock succes")
        if not ravencoin.wallet.LockUTXO([{'txid':_data['txid'], 'vout':_data['vout']}]):
            UserError(self.parentBinding, "Unable to lock UTXO !")
        
        wx.CallAfter(self.forceRefreshUtxo,())  
    
    def menuItemAction_Unlock(self, event):
        _data= self._data
        ravencoin = self.parent_frame.getRvnRPC()
        
        #UserInfo(self.parentBinding, "Lock succes")
        if not ravencoin.wallet.UnlockUTXO([{'txid':_data['txid'], 'vout':_data['vout']}]):
            UserError(self.parentBinding, "Unable to lock UTXO !")
    
        wx.CallAfter(self.forceRefreshUtxo,())
    
    
        
    def forceRefreshUtxo(self, evt=None):
        myplugin = self.parent_frame.GetPlugin('Ravencore') 
        #wx.CallAfter(self.parentBinding.UpdateView, ())  
        myplugin.OnUTXORequested_T(self.parentBinding.UpdateView)
        
            
    def menuItemAction_ShowTx(self, event):
        _data= self._data
        
        
        myplugin = self.parent_frame.GetPlugin('Ravencore')
        myplugin.ShowTxInfos(_data['txid'])
    
    
    '''
    def OnOpenIPFSWithGateway(self, event):
        #self.log.WriteText("Popup one\n")
        #print("FindItem:", self.m_listCtrl1.FindItem(-1, "Roxette"))
        #print("FindItemData:", self.m_listCtrl1.FindItemData(-1, 11))
        
        _data= self._data
        if _data['has_ipfs']:
            self.parent_frame.GetPlugin("Ravencore").OpenIPFSinWebBrowser(_data, str(self.popupMAP[event.GetId()]))
        
    '''    
    
    '''
    
    def addInBkmrk(self, event):
        itemData = self._data
        
        _navItem = itemData['name']
        #print(itemData['type'])
        
        
        
        if itemData['type'] != AssetType.MAINASSET:
            
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
    
    '''
            
            
    '''
    def navigateAsset(self, event):
        
        if not self._dataNone:
        
            itemData = self._data
            
            _navItem = itemData['name']
            if itemData['type'] != AssetType.MAINASSET:
                _navItem = itemData['parent'] 
            
            
        self.parent_frame.GetPlugin("Ravencore").NaviguateAsset(str(_navItem))
    
    
    
    def previewIPFS(self, event):
        if self._hasIpfs :
            _url = self._ipfsgateway_default  + self._data['ipfs_hash']
            self.parent_frame.GetPlugin("Ravencore").previewIPFS(_url)

    
    
    def copyHash(self, event):
        if self._hasIpfs :
            _data= self._data
            self.parent_frame.GetPlugin("Ravencore").CopyClip(_data)
  
        
    
    def openDefaultIPFS(self, event): 
        if self._hasIpfs :
            _data= self._data
            self.parent_frame.GetPlugin("Ravencore").OpenIPFSinWebBrowser(_data)
           
    '''
        
    def getMenu(self):
        return self._menu
        