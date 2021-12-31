'''
Created on 24 déc. 2021

@author: slinux
'''


from .wxRavenRavencoreDesign import *

from wxRavenGUI.application.wxcustom.CustomLoading import *
import webbrowser

from .wxRavenRavencoreHTMLviewer import *
from libs.RVNpyRPC import _asset as assetLib
from libs.RVNpyRPC import AssetTreeObj

try:
    import pyperclip
except ImportError:
    from libs import pyperclip
    
    
from wxRavenGUI.application.wxcustom.CustomTreeView import wxRavenTreeView


from .wxRavenRavencoreAssetOverviewLogic import wxRavenAssetOverviewPanel


"""

Simple object to handle the tree + some add informations

"""
class RavencoreAssetLibrary(object):
    
    libraryName = ""
    
    
    def __init__(self, libraryName, assetTree:AssetTreeObj):
        
        self.libraryName =  libraryName
        self.assetTree =  assetTree






class RavencoreAssetNavigator(wxRavenAssetNavigator):
    '''
    classdocs
    '''

    view_base_name = "Asset Navigator"
    view_name = "Asset Navigator"
    parent_frame = None
    default_position = "main"
    icon = 'asset_navigation'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    #asset_library_list =[]
    

    def __init__(self, parentFrame, startin="My Assets", position = "main", viewName= "Asset Navigator", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Asset Navigator"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.allIcons = {}
        
        
        self.navigatorToolboxPanel.Hide()
        self.treeExplorerToolboxPanel.Hide()
        
        self._toolbarsVisible= False
        
        
        self.Layout()
        
        self._loadingPanel  = None
        
        
        self._tempDisplayPanel = None #wxRavenAssetOverviewPanel
        
        #self.asset_library_list = []
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
    
        self.initBookmarkList()
        
        
        self.Bind(wx.EVT_CHOICE, self.EvtChoiceChangeLib, self.bookmarkChoiceList)
        
        
        self.__initPluginSettingsOptions__()
        
        _icons = {
            'person':parentFrame.RessourcesProvider.GetImage('person')  ,
            'wallet': parentFrame.RessourcesProvider.GetImage('wallet'),
            'asset': parentFrame.RessourcesProvider.GetImage('asset'),
            'asset_virtual': parentFrame.RessourcesProvider.GetImage('asset_virtual'),
            'asset_admin': parentFrame.RessourcesProvider.GetImage('asset_admin'),
            
            
            #console_view.png
            }
        
        self.wxTree = wxRavenTreeView(self.assetTreeView, _icons, _fillTreeCallback=None, _onChangeCallback=self.onChangeTest)
        
    
    def __initPluginSettingsOptions__(self):
        _p = self.parent_frame.GetPlugin("Ravencore")
        _useCache = _p.PLUGIN_SETTINGS['navigation_use_cache'] 
        tree_display_regroupby_main = _p.PLUGIN_SETTINGS['tree_display_regroupby_main'] 
        tree_display_virtual_sort = _p.PLUGIN_SETTINGS['tree_display_virtual_sort'] 
        
        if _useCache:
            self.m_useCacheButton.SetState(32)
            
        if tree_display_regroupby_main:
            self.m_TreeDisplayOption_OrganizeByMainAsset.SetState(32)
            
        if tree_display_virtual_sort:
            self.m_TreeDisplayOption_ReorganizeSubCat.SetState(32)
    
    
    
    def OnToggleBookmarkToolbar(self, event):
        if self._toolbarsVisible:
            self.navigatorToolboxPanel.Hide()
            self.treeExplorerToolboxPanel.Hide()
            self._toolbarsVisible= False
        else:
            self.navigatorToolboxPanel.Show()
            self.treeExplorerToolboxPanel.Show()
            self._toolbarsVisible= True
        
        self.Layout()

    def onChangeTest(self,evt):    
        toplabel = self.wxTree._currentText 
        self.m_staticText2.SetLabel(toplabel) 
        
        if self._tempDisplayPanel == None:
            self._tempDisplayPanel = wxRavenAssetOverviewPanel(self.AssetDetailsContainerPanel, self.parent_frame)
            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(self._tempDisplayPanel , 1, wx.EXPAND|wx.ALL, 0)
            self.AssetDetailsContainerPanel.SetSizer(sizer)
        
            self._tempDisplayPanel.Show()
            
            
            
        self._tempDisplayPanel.DisplayAsset(self.wxTree._currentData)
            #wxRavenAssetOverviewPanel
        self.checkToolbars()
        self.Layout()
    
    
    
    
    def checkToolbars(self):
        
        
        #self.m_auiToolBar3.EnableTool(self.m_CreateNewAssetButton.GetId(), True) 
        
        
        #
        # Admin asset, allow creation
        #
        if self.wxTree._currentText == None:
            self.m_auiToolBar3.EnableTool(self.m_CreateNewAssetButton.GetId(), False) 
            
        elif self.wxTree._currentText.__contains__('!') or self.wxTree._currentText== "Wallet":
            #self.m_CreateNewAssetButton.Enable(True)
            self.m_auiToolBar3.EnableTool(self.m_CreateNewAssetButton.GetId(), True) 
        else:
            #self.m_CreateNewAssetButton.Enable(False)
            self.m_auiToolBar3.EnableTool(self.m_CreateNewAssetButton.GetId(), False) 
    
    
        _cdata = self.wxTree._currentData
        if _cdata!=None:
            self.m_auiToolBar3.EnableTool(self.m_OpenAssetIpfsButton.GetId(), True) 
            self.m_auiToolBar3.EnableTool(self.m_shareAssetButton.GetId(), True) 
            
        else:
            self.m_auiToolBar3.EnableTool(self.m_OpenAssetIpfsButton.GetId(), False) 
            self.m_auiToolBar3.EnableTool(self.m_shareAssetButton.GetId(), False)    
             
        self.Layout()    
    
    def OnSaveBookmarkList(self, evt):
        
        _listOfLibs = self.parent_frame.GetPluginData("Ravencore","_AssetLibraryList")  
        
        _bookmarkList = []
        
        for _lib in _listOfLibs:
            _bookmarkList.append(_lib) 
            
            
        _p = self.parent_frame.GetPlugin("Ravencore")
        
        _p.PLUGIN_SETTINGS['bookmark_list'] = _bookmarkList
        
        #self.parentFrame.Settings.SaveSettingsToFile()
        
    def OnRemoveBookmarkListItem(self, evt):
        _curLibData = self.parent_frame.GetPluginData("Ravencore","_CurrentLibrary")
        
        
        if _curLibData == "My Asset":
            return
        
        dlg = wx.MessageDialog(self,"Remove '"+_curLibData+"' from the bookmark list ?",
                               'Confirm deletion',
                               wx.YES_NO | wx.ICON_QUESTION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        res = dlg.ShowModal()
        dlg.Destroy()
        
        
        if res == wx.ID_YES:
            _p = self.parent_frame.GetPlugin("Ravencore")
            _bkmrk = _p.PLUGIN_SETTINGS['bookmark_list']
            
            _bkmrk.remove(_curLibData)
            _p.PLUGIN_SETTINGS['bookmark_list'] = _bkmrk
            
            _p.setData("_CurrentLibrary",_bkmrk[0])
            
            self.RefreshLibList()
    
    
    def OnAddBookmarkListItem(self, evt):
        dlg = wx.TextEntryDialog(
                self, 'Please enter the ASSET Name to add in Bookmark',
                'Add an Asset to Bookmark', '...')

        dlg.SetValue("MYASSETNAME")

        if dlg.ShowModal() == wx.ID_OK:
            #self.log.WriteText('You entered: %s\n' % dlg.GetValue())
            
            
            _p = self.parent_frame.GetPlugin("Ravencore")
            _bkmrk = _p.PLUGIN_SETTINGS['bookmark_list']
            
            if not _bkmrk.__contains__(dlg.GetValue()):
            
                _bkmrk.append(dlg.GetValue())
                _p.PLUGIN_SETTINGS['bookmark_list'] = _bkmrk
                
                _listOfLibs = self.parent_frame.GetPluginData("Ravencore","_AssetLibraryList")   
                
                _listOfLibs[dlg.GetValue()] = None
                
                self.RefreshLibList()

        dlg.Destroy()
    
    
    
    def OnUseCacheToggle(self, evt):
        _currentButtonState =self.m_useCacheButton.GetState()
        print(_currentButtonState)
        _p = self.parent_frame.GetPlugin("Ravencore")
        
        
        if _currentButtonState in [32 ,34 ]:
            
            _p.PLUGIN_SETTINGS['navigation_use_cache'] = True
            
        else:
            _p.PLUGIN_SETTINGS['navigation_use_cache'] = False
    
    
    
    def OnTreeDisplayOptionsChanged(self, evt):
        _organizeByMainAssetButtonState =self.m_TreeDisplayOption_OrganizeByMainAsset.GetState()
        _virtualReorganizationButtonState =self.m_TreeDisplayOption_ReorganizeSubCat.GetState()
    
        _p = self.parent_frame.GetPlugin("Ravencore")
        
        if _organizeByMainAssetButtonState in [32 ,34 ]:
            _p.PLUGIN_SETTINGS['tree_display_regroupby_main'] = True
        else:
            _p.PLUGIN_SETTINGS['tree_display_regroupby_main'] = False
    
        if _virtualReorganizationButtonState in [32 ,34 ]:
            _p.PLUGIN_SETTINGS['tree_display_virtual_sort'] = True
        else:
            _p.PLUGIN_SETTINGS['tree_display_virtual_sort'] = False
            
        print(_virtualReorganizationButtonState)
            
            
    
    def OnOpenCurrentAssetIPFS(self, evt):
        _cdata = self.wxTree._currentData
        
        
        if _cdata!=None:
            self.parent_frame.GetPlugin("Ravencore").OpenIPFSinWebBrowser(_cdata)
    
    
    
    
    def OnShareCurrentAssetIPFS(self, evt):
        _cdata = self.wxTree._currentData
         
        if _cdata!=None:
            #self.parent_frame.GetPlugin("Ravencore").OpenIPFSinWebBrowser(_cdata)
            self.parent_frame.GetPlugin("Ravencore").CopyClip(_cdata)
    
    
    
    
    
    
    def OnCreateNewAsset(self, evt):
        
        #OpenAssetIssuer
        
        _p = self.parent_frame.GetPlugin("Ravencore")
        _p.OpenAssetIssuer(self.wxTree._currentText)
    
    
    
    
    def OnResetTreeDisplay(self, evt):
        _curLibData = self.parent_frame.GetPluginData("Ravencore","_CurrentLibrary")   
        _listOfLibs = self.parent_frame.GetPluginData("Ravencore","_AssetLibraryList")   
        
        _listOfLibs[_curLibData] = None
        _p = self.parent_frame.GetPlugin("Ravencore")
        _p.setData("_AssetLibraryList", _listOfLibs)
        _p.OnNavigateRequested_T(_curLibData)
        
        self.ShowLoading()
    
    
    
    def NaviguateAsset(self, assetName):
        
        if self.bookmarkChoiceList.FindString(assetName) ==  wx.NOT_FOUND:
            pass
        
        else:
            self.bookmarkChoiceList.SetSelection(self.bookmarkChoiceList.FindString(assetName))
            
            
    
    
    def EvtChoiceChangeLib(self, event):
        #self.log.WriteText('EvtChoice: %s\n' % event.GetString())
        
        
        _libname = event.GetString()
        #print("SET "+ _libname)
        #self.ch.Append("A new item")
        _p = self.parent_frame.GetPlugin("Ravencore")
        
        _p.setData("_CurrentLibrary", _libname)
        _p.OnNavigateRequested_T(_libname)
        
        self.ShowLoading()
        #if event.GetString() == 'one':
        #    self.log.WriteText('Well done!\n')
    
    
    
    def RefreshLibList(self):
        self.initBookmarkList()
        
        
        _curLibLocal = self.bookmarkChoiceList.GetString(self.bookmarkChoiceList.GetCurrentSelection())
        _curLibData = self.parent_frame.GetPluginData("Ravencore","_CurrentLibrary")   
        
        print("_curLibLocal "+ _curLibLocal)
        print("_curLibData "+ _curLibData)
        
        if _curLibData != _curLibLocal:
            pass
            self.NaviguateAsset(_curLibData)
        
    
    
    
    
    
    
    
    
    
    
    def ShowLoading(self):
        
        #print('LOADER ON !')
        
        if self._loadingPanel  == None:
            self._loadingPanel =  wxBackgroundWorkerAnimation(self)
        
        
        self._loadingPanel.Show(show=True)
        self.bookmarkChoiceList.Enable(False)
        #self._loadingPanel.Popup()
        self.Layout()
        
    def HideLoading(self):
        if self._loadingPanel  != None:
            self._loadingPanel.Hide()
            self.Layout()
            
        self.bookmarkChoiceList.Enable(True)
    
    
    def initBookmarkList(self):
        
        
        #_walletAssetTree = None
        #myLib = RavencoreAssetLibrary("My Assets", _walletAssetTree)
        
        _listOfLibs = self.parent_frame.GetPluginData("Ravencore","_AssetLibraryList")   
        _x = 0
        if _listOfLibs != None:
            
            for _l in _listOfLibs:
                #print(_l)
                lTree = _listOfLibs[_l]
                
                if self.bookmarkChoiceList.FindString(_l) ==  wx.NOT_FOUND:
                    self.bookmarkChoiceList.Append(_l)
                #if lTree!= None:
                #    self.bookmarkChoiceList.Append(_l)
                #   _x = _x+1
                    
                    
        #print(_listOfLibs)            
        #print(_x)
        self.Layout()
        
        
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self):
        
        self.UpdateDataFromPluginDatas()

        self.RefreshLibList()
        self.checkToolbars()
        self.Layout()   
        
        
        
    def UpdateDataFromPluginDatas(self):
        self.ShowLoading()
        
        
        _curLib = self.bookmarkChoiceList.GetString(self.bookmarkChoiceList.GetCurrentSelection())
        
        _listOfLibs = self.parent_frame.GetPluginData("Ravencore","_AssetLibraryList")   
        
        
        if _listOfLibs.__contains__(_curLib):
            #print("data does not contains the current lib")
            _libToLoad = _listOfLibs[_curLib]
            if _libToLoad != None:
                self.LoadFromRoot(_libToLoad)
        else:
            
            print("data does not contains the current lib")
        
        
        
        
        self.HideLoading()
        
        
    
    
    def LoadTree(self, parentTreeObj,libObj):   
        _dummyData = {} 
        
        _icon  = "asset"
        if libObj._isVirtual:
            _icon = "asset_virtual"
            
        if libObj._isAdmin:
            _icon = "asset_admin"
        
        _newChild = self.wxTree.addItem(parentTreeObj, libObj.name, libObj.datas,_icon)
        
        for _c in libObj.childs:
            self.LoadTree(_newChild, _c)
        
        
    def LoadFromRoot(self, libObj:AssetTreeObj):
        
        
        self.wxTree._tree.Freeze()
        
        self.wxTree._tree.DeleteAllItems()
        
        _dummyData = {}
        _icon = "asset"
        if libObj.name == "My Assets" or libObj.name == "Wallet":
            #_icon = "wallet"
            _icon = "asset_admin"
            
            
        _root = self.wxTree.addItem(None, libObj.name, libObj.datas, _icon)
        self._root = _root
        
        for _c in libObj.childs:
            self.LoadTree(_root, _c)
        #_app = self.wxTree.addItem(_root, "Application", _dummyData, "app")
        self.wxTree._tree.Thaw()
        