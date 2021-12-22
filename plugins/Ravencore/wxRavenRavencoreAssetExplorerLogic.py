'''
Created on 20 déc. 2021

@author: slinux
'''

from .wxRavenRavencoreDesign import *

from wxRavenGUI.application.wxcustom.CustomLoading import *
import webbrowser


class RavencoreAssetExplorer(wxRavenAssetExplorer):
    '''
    classdocs
    '''

    view_base_name = "Asset Search"
    view_name = "Asset Search"
    parent_frame = None
    default_position = "main"
    icon = 'ravencoin'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, position = "main", viewName= "Asset Search", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "AssetExplorer"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.allIcons = {}
        
        
        
        #
        #
        #
        self.searchOptionsPanel.Hide()
        self._filterPanelVisible = False
        
        self._loadingPanel = None
        
        self.popupIDS = {}
        self.popupMAP = {}
        
        
        self._datacache = {}
        
        #self.LoadSearchOptions()
        
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
    
        
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.m_listCtrl1)
        #self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown, self.m_listCtrl1)
        self.m_listCtrl1.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OnRightClick)
        # for wxGTK
        self.m_listCtrl1.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)
        
        
        
        self.setupTableview()
    
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetListCtrl(self):
        return self.m_listCtrl1
    
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetSortImages(self):
        return (self.allIcons['sort_down'], self.allIcons['sort_up'])
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self):
        
        self.UpdateDataFromPluginDatas()
        self.Layout()
        
        
    
    
    #    
    #
    # Options load and change
    #
    #
    def LoadSearchOptions(self):
        assetSearchLimit = self.parent_frame.GetPluginSetting("Ravencore","assetSearchLimit") 
        strictName = self.parent_frame.GetPluginSetting("Ravencore","strictName") 
        mainOnly = self.parent_frame.GetPluginSetting("Ravencore","onlyMainAsset") 
        
        #print(assetSearchLimit)
        #print(strictName)
        #print(mainOnly)
        
        
        #print(self.parent_frame.GetPlugin("Ravencore") )
        self.searchopt_strictmode.SetValue(strictName)
        self.searchopt_maxresults.SetValue(assetSearchLimit)
        self.searchopt_onlymain.SetValue(mainOnly)
        
        
    
    def SearchOptionsChanged(self, evt):
        strictName = self.searchopt_strictmode.GetValue()
        assetSearchLimit = self.searchopt_maxresults.GetValue()
        mainOnly = self.searchopt_onlymain.GetValue()
        
        print("options saved !")
        
        _p = self.parent_frame.GetPlugin("Ravencore")
        
        _p.PLUGIN_SETTINGS['assetSearchLimit'] = assetSearchLimit
        _p.PLUGIN_SETTINGS['strictName'] = strictName
        _p.PLUGIN_SETTINGS['onlyMainAsset'] = mainOnly
        
        
        self.infoMessage("Filter preferences saved !", wx.ICON_INFORMATION)
        
        
        
    
    def ToggleFilterPanel(self, event):
        
        
        
        if self._filterPanelVisible:
            self.searchOptionsPanel.Hide()
        else:
            self.searchOptionsPanel.Show()
            self.LoadSearchOptions()
        
        self._filterPanelVisible = not self._filterPanelVisible
        
        self.Layout()
    
    
    
    
    
    
    
        
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        
        #filterSearch = self.m_searchCtrl1.GetValue()
        self.ShowLoading()
        
        
        self.m_listCtrl1.Freeze()
        self.ClearResults()
        self._datacache = {}
        
        mainOnly = self.parent_frame.GetPluginSetting("Ravencore","onlyMainAsset") 
        result = self.parent_frame.GetPluginData("Ravencore","_AssetSearchResult") 


        excludeChars = ['#', '/']


        _cursor = 0
        if result != None:
            for _assetName in result:
                
                
                
                
                
                _assetDatas = result[_assetName]
                
                
                _skipAsset = False
                
                
                if mainOnly:
                    for _char in excludeChars:
                        if _assetDatas['name'].__contains__(_char):
                            _skipAsset = True
                            continue
                
                #print(_assetDatas)
                if not _skipAsset:
                    index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),_assetDatas['name'], self.allIcons['asset'] )
                    self.m_listCtrl1.SetItem(index,1, 'n/a')
                    self.m_listCtrl1.SetItem(index,2, str(_assetDatas['amount']))
                    
                    #self.m_listCtrl1.SetItem(index,3, str(_assetDatas['block_height']))
                    self.m_listCtrl1.SetItem(index,3, str(_assetDatas['datetime']))
                    
                    _variousText = ""
                    if _assetDatas['has_ipfs'] == 1:
                        _variousText = "[IPFS] "
                        
                    if _assetDatas['reissuable'] == 1:
                        _variousText = _variousText + "[R] "
                        
                    self.m_listCtrl1.SetItem(index,4, str(_variousText))    
                        
                    self.m_listCtrl1.SetItemData(index, _cursor)
                    self._datacache[_cursor] = _assetDatas
                    _cursor= _cursor + 1
        
        #self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        
        self.m_listCtrl1.SetColumnWidth(0, 275)
        self.m_listCtrl1.SetColumnWidth(1, 100)
        self.m_listCtrl1.SetColumnWidth(2, 100)
        self.m_listCtrl1.SetColumnWidth(3, 175)
        self.m_listCtrl1.SetColumnWidth(4, 150)
        
        #self.m_listCtrl1.itemDataMap = self._datacache
        #listmix.ColumnSorterMixin.__init__(self.m_listCtrl1, 3)
              
        self.HideLoading()
        
        
        
        self.infoMessage(""+ str(_cursor) + " Result(s) found.", wx.ICON_INFORMATION)
        
        self.m_listCtrl1.Thaw()
        self.SetAutoLayout(True)
        self.Layout()
            
    
    
    #
    #Asset Explorer Logic
    #
            
    def setupTableview(self):
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "Asset Name"
        self.m_listCtrl1.InsertColumn(0, info)

        info.Align = 0#wx.LIST_FORMAT_RIGHT
        info.Text = "TX Volume"
        self.m_listCtrl1.InsertColumn(1, info)

        info.Align = 0
        info.Text = "Supply"
        self.m_listCtrl1.InsertColumn(2, info)
        
        info.Align = 0
        info.Text = "Created"
        self.m_listCtrl1.InsertColumn(3, info)
        
        info.Align = 0
        info.Text = "Various"
        self.m_listCtrl1.InsertColumn(4, info)
        
        
        
        """
        
        self.m_listCtrl1.SetColumnWidth(0, 350)
        self.m_listCtrl1.SetColumnWidth(1, 100)
        self.m_listCtrl1.SetColumnWidth(2, 100)
        self.m_listCtrl1.SetColumnWidth(3, 100)
        self.m_listCtrl1.SetColumnWidth(4, 100)
        """
        
        self.il = wx.ImageList(16, 16)
        

        
        
        self.allIcons['asset'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('asset_ravencoin-blue') )
        self.allIcons['info'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('info_obj') )
        
        self.allIcons['sort_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up') )
        self.allIcons['sort_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down') )
        
        
        
        
        
        self.m_listCtrl1.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        
        
    def ClearResults(self):
        self.m_listCtrl1.DeleteAllItems()
        
    
    
    
    
    def infoMessage(self, msg, type=wx.ICON_INFORMATION):
        self.resultControl.ShowMessage(msg, type)
            
        self.m_timer1.Start(3000)
        #OnTimerTick
    
    
    
    def OnTimerTick(self, evt):
        self.m_timer1.Stop()
        self.resultControl.Dismiss()
        #print("Tick")
        

        
    def OnSearch(self, evt):
        
        filterSearch = self.m_searchCtrl1.GetValue()
        
        
        assetSearchLimit = self.parent_frame.GetPluginSetting("Ravencore","assetSearchLimit") 
        
        strictName = self.parent_frame.GetPluginSetting("Ravencore","strictName") 
        
        mainOnly = self.parent_frame.GetPluginSetting("Ravencore","onlyMainAsset") 
        
        if strictName==False and not filterSearch.__contains__("*"):
            
            filterSearch = filterSearch + "*"

        #result = self.SearchAsset(filterSearch, assetSearchLimit)
        #self.m_listCtrl1.Freeze()
        
        #
        # Asynch Search
        #
        self.ClearResults()
        self.parent_frame.GetPlugin("Ravencore").OnSearchRequested_T(filterSearch, assetSearchLimit,mainOnly )
        
        
        
        
        
        
        if assetSearchLimit > 100:
            self.infoMessage("Search in progress, it can be longer with current search limit.", wx.ICON_WARNING)
            
        
        
        #
        #
        #
        #Animation 
        self.ShowLoading()
        
        
        self.Layout()
    
    
    def ShowLoading(self):
        
        #print('LOADER ON !')
        
        if self._loadingPanel  == None:
            self._loadingPanel =  wxBackgroundWorkerAnimation(self.m_listCtrl1)
        
        
        self._loadingPanel.Show(show=True)
        
        #self._loadingPanel.Popup()
        self.Layout()
        
    def HideLoading(self):
        if self._loadingPanel  != None:
            self._loadingPanel.Hide()
            self.Layout()
    
        #print('LOADER OFF !')
        
    def SearchAsset(self, keyword, _limit=50):
        _AssetSearchResult = {}
        #try:
                    
        _AssetSearchResult = self.parent_frame.getRvnRPC().asset.SearchAsset(keyword,_limit )    

        #except Exception as e:
        #    self.parent_frame.Log("Unable to search assets '"+keyword+"'" , type="warning")
        
        return _AssetSearchResult
        
    
    
    def getColumnText(self, index, col):
        item = self.m_listCtrl1.GetItem(index, col)
        return item.GetText()
    
    def OnItemSelected(self, event):
        ##print(event.GetItem().GetTextColour())
        self._currentItem = event.Index
        
        
        
        print(self._currentItem)
        print(self.m_listCtrl1.GetItemText(self._currentItem))
        print(self.getColumnText(self._currentItem, 1))
        #print(self._currentItem)
        """
        self.log.WriteText("OnItemSelected: %s, %s, %s, %s\n" %
                           (self.currentItem,
                            self.list.GetItemText(self.currentItem),
                            self.getColumnText(self.currentItem, 1),
                            self.getColumnText(self.currentItem, 2)))
        """
        
        event.Skip()
        
    
    def OnRightClick(self, event):
        #self.log.WriteText("OnRightClick %s\n" % self.list.GetItemText(self.currentItem))
        
        _ipfsgateway_providers = self.parent_frame.GetPluginSetting("Ravencore","ipfsgateway_providers")
        _ipfsgateway_default = self.parent_frame.GetPluginSetting("Ravencore","ipfsgateway_default")
        
        
        #'has_ipfs'
        #ipfs_hash
        _data= self._datacache[self._currentItem]
        _hasIpfs =  _data['has_ipfs']
        
        
        
        # only do this part the first time so the events are only bound once
        if not self.popupIDS.__contains__("popupID1"):
            
            pptext = "popupID"
            ppcount = 1
            
            
            for p in _ipfsgateway_providers:
                popupID = wx.NewId()
                _pp = pptext + str(ppcount)
                self.popupIDS[_pp] = popupID
                self.popupMAP[popupID] = p
                self.Bind(wx.EVT_MENU, self.OnPopupOne, id=popupID)
                ppcount= ppcount+1
            
            

            
        # make a menu
        menu = wx.Menu()
        
        
        # add some items
        nid = wx.NewId()
        _opendefaultipfs = menu.Append(nid, "Open IPFS" )
        _opendefaultipfs.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('raven_ipfs'))
        self.Bind(wx.EVT_MENU, self.openDefaultIPFS, id=nid)
        
        #webresources16
        _ipfs_menu = wx.Menu()
        _ipfs_menu_item = menu.AppendSubMenu(_ipfs_menu, "Open IPFS with...")
        _ipfs_menu_item.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('webresources16'))
        
        pptext = "popupID" 
        ppcount = 1
        
        for p in _ipfsgateway_providers:
            pptext = "popupID"
            _pp = pptext + str(ppcount)
            _i = _ipfs_menu.Append(self.popupIDS[_pp], p)
            _i.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('webresources16'))
            ppcount= ppcount+1
            

        if not _hasIpfs:
            _ipfs_menu_item.Enable(False)
            _opendefaultipfs.Enable(False)
        #menu.Append(self.popupID2, "Iterate Selected")
        #menu.Append(self.popupID3, "ClearAll and repopulate")
        #menu.Append(self.popupID4, "DeleteAllItems")
        #menu.Append(self.popupID5, "GetItem")
        #menu.Append(self.popupID6, "Edit")

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()   
    
    
    
    def openDefaultIPFS(self, event):    
        
        _ipfsgateway_default = self.parent_frame.GetPluginSetting("Ravencore","ipfsgateway_default")
        
        
        
        _data= self._datacache[self._currentItem]
        print(_data['has_ipfs'])
        
        if _data['has_ipfs']:
            _url = _ipfsgateway_default  +_data['ipfs_hash']
            webbrowser.open(_url)
            
            
            
    def OnPopupOne(self, event):
        #self.log.WriteText("Popup one\n")
        #print("FindItem:", self.m_listCtrl1.FindItem(-1, "Roxette"))
        #print("FindItemData:", self.m_listCtrl1.FindItemData(-1, 11))
        
        
        
        #
        #ipfsgateway_providers
        #
        #print(event)
        #print(event.GetId())
        #print(event.GetText())
        #print()
        #self.popupMAP[popupID] 
        #index = animals.index('dog')
        
        
        _data= self._datacache[self._currentItem]
        print(_data['has_ipfs'])
        
        if _data['has_ipfs']:
            _url = str(self.popupMAP[event.GetId()])  +_data['ipfs_hash']
            webbrowser.open(_url)
            #webbrowser.open('https://cloudflare-ipfs.com/ipfs/'+_data['ipfs_hash'])
            
        pass
            
