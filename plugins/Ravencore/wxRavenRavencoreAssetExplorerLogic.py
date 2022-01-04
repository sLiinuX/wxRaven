'''
Created on 20 déc. 2021

@author: slinux
'''


from .wxRavenRavencoreDesign import *

from wxRavenGUI.application.wxcustom.CustomLoading import *
import webbrowser

from .wxRavenRavencoreHTMLviewer import *
from libs.RVNpyRPC import _asset as assetLib
from libs.RVNpyRPC._asset import AssetType

try:
    import pyperclip
except ImportError:
    from libs import pyperclip
    
    
import wx.lib.mixins.listctrl as listmix 




from .wxRavenRavencoreAssetRightClickPopupMenu import RavencoreAssetRightclickPopupMenu


class RavencoreAssetExplorer(wxRavenAssetExplorer, listmix.ColumnSorterMixin):
    '''
    classdocs
    '''

    view_base_name = "Asset Search"
    view_name = "Asset Search"
    parent_frame = None
    default_position = "main"
    icon = 'search_ravencoin'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    #self.RessourcesProvider.GetImage('asset_navigation')
    
    
    

    def __init__(self, parentFrame, position = "main", viewName= "Asset Search", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Asset Search"
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
        self._pwin  = None
        
        self._datacache = {}
        
        #self.LoadSearchOptions()
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        
        
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
        return (self.allIcons['sort_down_2'], self.allIcons['sort_up_2'])
            
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
        assetsearchlimit = self.parent_frame.GetPluginSetting("Ravencore","assetsearchlimit") 
        strictname = self.parent_frame.GetPluginSetting("Ravencore","strictname") 
        mainOnly = self.parent_frame.GetPluginSetting("Ravencore","filtertype") 
        
        #print(assetsearchlimit)
        #print(strictname)
        #print(mainOnly)
        
        
        #print(self.parent_frame.GetPlugin("Ravencore") )
        self.searchopt_strictmode.SetValue(strictname)
        self.searchopt_maxresults.SetValue(assetsearchlimit)
        self.searchopt_onlymain.SetValue(mainOnly)
    
    
    
    
    
    def filtertypeDialog(self, _plugin):
        _assetTypeList = [ ]
        
        for key in assetLib._ASSET_KEYCHAR_:
            _assetTypeList.append(key)
            
            
        
        dlg = wx.MultiChoiceDialog( self,
                                   "Select Asset Type(s) :",
                                   "Filter...", _assetTypeList)
    
        if (dlg.ShowModal() == wx.ID_OK):
            _plugin.PLUGIN_SETTINGS['filtertype'] = True
            
            selections = dlg.GetSelections()
            strings = [_assetTypeList[x] for x in selections]
            
            _plugin.PLUGIN_SETTINGS['filtertypelist'] = strings
            
            print("save:")
            print(strings )
            
            
        else:
            _plugin.PLUGIN_SETTINGS['filtertype'] = False
            
        return strings   
            
    
        
    def SearchAssetTypeChanged(self):
        #strictname = self.searchopt_strictmode.GetValue()
        #assetsearchlimit = self.searchopt_maxresults.GetValue()
        _p = self.parent_frame.GetPlugin("Ravencore")
        mainOnly_OLD = _p.PLUGIN_SETTINGS['filtertype']        
        mainOnly = self.searchopt_onlymain.GetValue()  
        
        if mainOnly != mainOnly_OLD:
            if mainOnly:
                self.filtertypeDialog(_p)
            else:
                _p.PLUGIN_SETTINGS['filtertype'] = False
          
    
    def SearchOptionsChanged(self, evt):
        strictname = self.searchopt_strictmode.GetValue()
        assetsearchlimit = self.searchopt_maxresults.GetValue()
        mainOnly = self.searchopt_onlymain.GetValue()
        
        print("options saved !")
        
        _p = self.parent_frame.GetPlugin("Ravencore")
        
        _p.PLUGIN_SETTINGS['assetsearchlimit'] = assetsearchlimit
        _p.PLUGIN_SETTINGS['strictname'] = strictname
        
        #
        self.SearchAssetTypeChanged()
        #
        
        
        _p.PLUGIN_SETTINGS['filtertype'] = mainOnly
        
        
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
        
        mainOnly = self.parent_frame.GetPluginSetting("Ravencore","filtertype") 
        result = self.parent_frame.GetPluginData("Ravencore","_AssetSearchResult") 
        
        _filteronTypes = self.parent_frame.GetPluginSetting("Ravencore","filtertypelist") 
        #_plugin.PLUGIN_SETTINGS['filtertypeDetails'] = strings


        excludeChars = ['#', '/']
        
        
        self.itemDataMap = {}

        _cursor = 0
        if result != None:
            for _assetName in result:
                
                
                
                
                
                _assetDatas = result[_assetName]
                
                
                _skipAsset = False
                
                
                if mainOnly:
                    
                    _currentType = str(_assetDatas['type'].value)
                    
                    #print("Filtering type :" + str(_filteronTypes))
                    if _filteronTypes != None:
                    
                        if _currentType not in _filteronTypes:
                            _skipAsset = True
                            continue
                    
                    #for _char in excludeChars:
                    #    if _assetDatas['name'].__contains__(_char):
                    #        _skipAsset = True
                    #        continue
                
                
                
                
                
                
                
                #print(_assetDatas)
                if not _skipAsset:
                    index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),_assetDatas['name'], self.allIcons['asset'] )
                    self.m_listCtrl1.SetItem(index,1, str(_assetDatas['type'].value))
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
                    self.itemDataMap[_cursor] = (str(_assetDatas['name']), str(_assetDatas['type']), float(_assetDatas['amount']), str(_assetDatas['datetime']) ,str(_variousText))
                    
                    
                    _cursor= _cursor + 1
        
        #self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        
        self.m_listCtrl1.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.m_listCtrl1.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.m_listCtrl1.SetColumnWidth(2, 150)
        self.m_listCtrl1.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.m_listCtrl1.SetColumnWidth(4, wx.LIST_AUTOSIZE)
        
        #self.m_listCtrl1.itemDataMap = self._datacache
        listmix.ColumnSorterMixin.__init__(self, 5)
              
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
        info.Text = "Asset Type"
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
        self.allIcons['sort_up_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up_2') )
        self.allIcons['sort_down_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down_2') )
        
        self.allIcons['alphab_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_up') )
        self.allIcons['alphab_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_co') )
        
        
        
        
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
        
        
        assetsearchlimit = self.parent_frame.GetPluginSetting("Ravencore","assetsearchlimit") 
        
        strictname = self.parent_frame.GetPluginSetting("Ravencore","strictname") 
        
        filtertypelist = self.parent_frame.GetPluginSetting("Ravencore","filtertypelist") 
        filtertype = self.parent_frame.GetPluginSetting("Ravencore","filtertype") 
        
        mainOnly = False
        
        if filtertype:
            if filtertypelist == ["MAINASSET"]:
                mainOnly = True 
            
            
        
        if strictname==False and not filterSearch.__contains__("*"):
            
            filterSearch = filterSearch + "*"

        #result = self.SearchAsset(filterSearch, assetsearchlimit)
        #self.m_listCtrl1.Freeze()
        
        #
        # Asynch Search
        #
        self.ClearResults()
        self.parent_frame.GetPlugin("Ravencore").OnSearchRequested_T(filterSearch, assetsearchlimit,mainOnly )
        
        
        
        
        
        
        if int(assetsearchlimit) > 100:
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
        
        
        itemData = self._datacache[self._currentItem]
        self._currentItemData = itemData
        _hasIpfs =  itemData['has_ipfs']
        
        
        #asset_new_qrcode
        if _hasIpfs:
            _ipfsgateway_default = self.parent_frame.GetPluginSetting("Ravencore","ipfsgateway_default")
            _url = _ipfsgateway_default  +itemData['ipfs_hash']
            
            self._currentItemURl = _url   
            self._currentItemHash = itemData['ipfs_hash']
            
            
            #if self._pwin != None:
                #self._pwin.wv.LoadURL(self._currentItemURl)
                #self._pwin.wv.LoadURL(self._currentItemURl)
                #self._pwin.LoadAssetUrl(self._currentItemURl)
            #    if self._pwin.IsShown() :
            #        self.previewIPFS(event)
                
        #print(self._currentItem)
        #print(self.m_listCtrl1.GetItemText(self._currentItem))
        #print(self.getColumnText(self._currentItem, 1))
        
        
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
        
        menuAsset = RavencoreAssetRightclickPopupMenu(self, self.parent_frame, _data)
        """
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
        
        
        
        #Add Bkmrk
        #
        nid = wx.NewId()
        _addBk = menu.Append(nid, "Add in Bookmarks" )
        _addBk.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('addbkmrk_co'))
        self.Bind(wx.EVT_MENU, self.addInBkmrk, id=nid)
        
        
        
        #Navigate
        #
        nid = wx.NewId()
        _Navigate = menu.Append(nid, "Navigate" )
        _Navigate.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('hierarchicalLayout'))
        self.Bind(wx.EVT_MENU, self.navigateAsset, id=nid)
        
        # Preview
        nid = wx.NewId()
        _preview = menu.Append(nid, "Preview" )
        _preview.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('ressource_picture'))
        self.Bind(wx.EVT_MENU, self.previewIPFS, id=nid)
        
        
        
        # Copy Hash
        nid = wx.NewId()
        _copyHash = menu.Append(nid, "Copy Hash" )
        _copyHash.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('copy_clipboard'))
        self.Bind(wx.EVT_MENU, self.copyHash, id=nid)
        
        
        
        # Open items
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
            _copyHash.Enable(False)
            _preview.Enable(False)
        #menu.Append(self.popupID2, "Iterate Selected")
        #menu.Append(self.popupID3, "ClearAll and repopulate")
        #menu.Append(self.popupID4, "DeleteAllItems")
        #menu.Append(self.popupID5, "GetItem")
        #menu.Append(self.popupID6, "Edit")

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()  
        
        
        """ 
    
    
    def addInBkmrk(self, event):
        itemData = self._datacache[self._currentItem]
        
        _navItem = itemData['name']
        #print(itemData['type'])
        
        
        
        if itemData['type'] != AssetType.MAINASSET:
            
            dlg = wx.MessageDialog(self, 'The Asset you selected is not a main asset, add main asset in bookmark instead ?',
                               'Confirmation',
                               wx.YES_NO | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
            res=dlg.ShowModal()
            dlg.Destroy()
            
            if res==wx.ID_YES or res==wx.YES:
            
                _navItem = itemData['parent'] 
            
            
        self.parent_frame.GetPlugin("Ravencore").AddAssetInBookmark(str(_navItem))
        
        
        dlg = wx.MessageDialog(self, 'Asset added in the Bookmark with Success !',
                               'Confirmation',
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()
        
    
    def navigateAsset(self, event):
        itemData = self._datacache[self._currentItem]
        
        _navItem = itemData['name']
        #print(itemData['type'])
        if itemData['type'] != AssetType.MAINASSET:
            _navItem = itemData['parent'] 
            
            
        self.parent_frame.GetPlugin("Ravencore").NaviguateAsset(str(_navItem))
    
    
    def previewIPFS(self, event):
        #wx.Log.SetActiveTarget(wx.LogStderr())
        self.parent_frame.GetPlugin("Ravencore").previewIPFS(self._currentItemURl)
        """
        if self._pwin == None:
            self._pwin = RavencoreHTMLViewer(self.parent_frame, self._currentItemURl, 'mgr')
        
        
        self._pwin.wv.LoadURL(self._currentItemURl)
        self.parent_frame.m_mgr.GetPane("Asset Preview").Show()
        self.parent_frame.Views.UpdateGUIManager()
        """
        
        #self._pwin.LoadAssetUrl(self._currentItemURl)
    
    
    def copyHash(self, event):
        #print(self._currentItem)
        #print(self.m_listCtrl1.GetItemText(self._currentItem))
        #print(self.getColumnText(self._currentItem, 1))
        _data= self._datacache[self._currentItem]
        self.parent_frame.GetPlugin("Ravencore").CopyClip(_data)
        """
        itemData = self._datacache[self._currentItem]
        print(itemData['ipfs_hash'])
        pyperclip.copy(itemData['ipfs_hash'])
        
        self.infoMessage("IPFS Hash copied to the clipboard", wx.ICON_INFORMATION)
        """    
        
    
    def openDefaultIPFS(self, event): 
        _data= self._datacache[self._currentItem]
        if _data['has_ipfs']:
            self.parent_frame.GetPlugin("Ravencore").OpenIPFSinWebBrowser(_data)
           
        """
        _ipfsgateway_default = self.parent_frame.GetPluginSetting("Ravencore","ipfsgateway_default")
        
        
        
        
        print(_data['has_ipfs'])
        
        if _data['has_ipfs']:
            _url = _ipfsgateway_default  +_data['ipfs_hash']
            webbrowser.open(_url)
        """    
            
            
    def OnPopupOne(self, event):
        #self.log.WriteText("Popup one\n")
        #print("FindItem:", self.m_listCtrl1.FindItem(-1, "Roxette"))
        #print("FindItemData:", self.m_listCtrl1.FindItemData(-1, 11))
        
        _data= self._datacache[self._currentItem]
        if _data['has_ipfs']:
            self.parent_frame.GetPlugin("Ravencore").OpenIPFSinWebBrowser(_data, str(self.popupMAP[event.GetId()]))
        
        """
        _data= self._datacache[self._currentItem]
        print(_data['has_ipfs'])
        
        if _data['has_ipfs']:
            _url = str(self.popupMAP[event.GetId()])  +_data['ipfs_hash']
            webbrowser.open(_url)
            #webbrowser.open('https://cloudflare-ipfs.com/ipfs/'+_data['ipfs_hash'])
            
        pass
    
        """
            
