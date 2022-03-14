'''
Created on 24 févr. 2022

@author: slinux
'''


import wx 


from wxRavenGUI.application.wxcustom import *



class wxRavenRavencore_UTXOManager_TxHistoryRightClickMenuLogic(object):
    '''
    classdocs
    '''


    def __init__(self, parentBinding, parentFrame, txData={}):
        '''
        Constructor
        '''
        self._menu = wx.Menu()
        
        self.popupIDS = {}
        self.popupMAP = {}
        
        
        self.parentBinding = parentBinding
        self.parent_frame = parentFrame
        
        
        self._data= txData
        #self._Locked = assetData['locked']
        #self._dataNone = False

        self.__createItemsIds__()
        self.createMenu()
        
        
    
    def __createItemsIds__(self):
        if not self.popupIDS.__contains__("popupID1"):
            
            pptext = "popupID"
            ppcount = 1
            
            if self._data.__contains__('addresses_in'):
                for p in self._data['addresses_in']:
                    popupID = wx.NewId()
                    _pp = pptext + str(ppcount)
                    self.popupIDS[_pp] = popupID
                    self.popupMAP[popupID] = p
                    self.parentBinding.Bind(wx.EVT_MENU, self.OnJoinAddressSelected, id=popupID)
                    ppcount= ppcount+1
                    
                    
            if self._data.__contains__('addresses_out'):
                for p in self._data['addresses_out']:
                    popupID = wx.NewId()
                    _pp = pptext + str(ppcount)
                    self.popupIDS[_pp] = popupID
                    self.popupMAP[popupID] = p
                    self.parentBinding.Bind(wx.EVT_MENU, self.OnJoinAddressSelected, id=popupID)
                    ppcount= ppcount+1        
            
   
        
    def createMenu(self):   
        #self.__createItemsIds__()
        self.__createMenuItems__()
        
        
        
        
    def __createMenuItems__(self):
        
        # make a menu
        #menu = wx.Menu()
        self._menu = wx.Menu()
        
        
        #Navigate
        #
        nid = wx.NewId()
        _Navigate = self._menu.Append(nid, "View Tx" )
        _Navigate.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('inspect_file'))
        self.parentBinding.Bind(wx.EVT_MENU, self.menuItemAction_ShowTx, id=nid)
        
        #
        # Manipulate Addresses
        #
        pptext = "popupID" 
        ppcount = 1
        
        
        if self._data.__contains__('addresses_in'):
            
            _tx_menu = wx.Menu()
            _tx_menu_item = self._menu.AppendSubMenu(_tx_menu, "Sender Addresse(s)")
            _tx_menu_item.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('mail_send'))
            
            
            for _addresses in self._data['addresses_in']:
                pptext = "popupID"
                _pp = pptext + str(ppcount)
                
                _menuLabel = f"+ {_addresses}"
                if self._data['addresses_in_details'].__contains__(_addresses):
                    _details = self._data['addresses_in_details'][_addresses]
                    
                    _dAmount = _details['amount']
                    _dAsset = _details['asset']
                    
                    
                    _menuLabel = f"+ {_addresses} [{_dAmount} {_dAsset}]"
                
                
                
                _i = _tx_menu.Append(self.popupIDS[_pp], f"{_menuLabel}")
                if _i != None:
                    _i.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('mail_icon'))
                    ppcount= ppcount+1
            
            if ppcount == 0:
                _tx_menu_item.Enable(False)
            

        
        
        
        if self._data.__contains__('addresses_out'):
            
            _tx_menu = wx.Menu()
            _tx_menu_item = self._menu.AppendSubMenu(_tx_menu, "Receiver Addresse(s)")
            _tx_menu_item.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('mail_in_green'))
            
            for _addresses in self._data['addresses_out']:
                pptext = "popupID"
                _pp = pptext + str(ppcount)
                
                
                _menuLabel = f"+ {_addresses}"
                #print(f'menulabel = {_menuLabel} ')
                if self._data['addresses_out_details'].__contains__(_addresses):
                    _details = self._data['addresses_out_details'][_addresses]
                    
                    #print(f'_details = {_details} ')
                    
                    _dAmount = _details['amount']
                    _dAsset = _details['asset']
                    
                    
                    _menuLabel = f"+ {_addresses} [{_dAmount} {_dAsset}]"
                
                
                _i = _tx_menu.Append(self.popupIDS[_pp], f"{_menuLabel}")
                if _i != None:
                    _i.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('mail_icon'))
                    ppcount= ppcount+1
            
            if ppcount == 0:
                _tx_menu_item.Enable(False)

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.parentBinding.PopupMenu(self._menu)
        self._menu.Destroy()       
    
    
    
    
    def OnJoinAddressSelected(self, event):
        #self.log.WriteText("Popup one\n")
        #print("FindItem:", self.m_listCtrl1.FindItem(-1, "Roxette"))
        #print("FindItemData:", self.m_listCtrl1.FindItemData(-1, 11))
        
        _data= self._data
        print(str(self.popupMAP[event.GetId()]))
        self.parentBinding.UpdateParentAddressSearch(str(self.popupMAP[event.GetId()]))
    
    
    
        
        
    def menuItemAction_ShowTx(self, event):
        _data= self._data
        
        
        myplugin = self.parent_frame.GetPlugin('Ravencore')
        myplugin.ShowTxInfos(_data['txid'])