'''
Created on 26 déc. 2021

@author: slinux
'''

from .wxRavenRavencoreDesign import wxRavenRavencoreSettingPanel_Search, wxRavenRavencoreSettingPanel_IPFS

from wxRavenGUI.application.pluginsframework import PluginSettingsPanelObject

import wx

from libs import AssetType
from libs.RVNpyRPC import _asset as assetLib
from plugins.Ravencore.wxRavenRavencoreDesign import wxRavenRavencoreSettingPanel_Bookmarks


class wxRavencore_GeneralSettings_WithLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenRavencoreSettingPanel_Search(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
        _Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
        
        
        
        self._Panel.searchopt_strictmode.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        self._Panel.searchopt_maxresults.Bind( wx.EVT_TEXT, self.OnChanged )
        self._Panel.searchopt_onlymain.Bind( wx.EVT_CHECKBOX, self.OnChanged )
        
        
        self._Panel.searchopt_onlymain.Bind( wx.EVT_CHECKBOX, self.toggleAssetTypeList )
    
        self.Layout()
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        #_newValueForBoolSetting = self._Panel.booleansetting.IsChecked()
        strictname = self._Panel.searchopt_strictmode.GetValue()
        assetsearchlimit = self._Panel.searchopt_maxresults.GetValue()
        mainOnly = self._Panel.searchopt_onlymain.IsChecked()
        
        listType = []
        if mainOnly:
            _res = self._Panel.m_assetTypeList.GetCheckedStrings()
            
            for i in _res:
                listType.append(i)
            
            
            
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        
        
        myPlugin.PLUGIN_SETTINGS["assetsearchlimit"] = assetsearchlimit
        myPlugin.PLUGIN_SETTINGS["strictname"] = strictname
        myPlugin.PLUGIN_SETTINGS["filtertype"] = mainOnly
        myPlugin.PLUGIN_SETTINGS["filtertypelist"] = listType   
        
        print(listType)
        
          
        """
        strictname = self.searchopt_strictmode.GetValue()
        assetsearchlimit = self.searchopt_maxresults.GetValue()
        mainOnly = self.searchopt_onlymain.GetValue()
        
        """
        #now its up to the dev to chose how to take this information
        #in our demo lets do simple and just change the  booleansetting in PLUGIN_SETTINGS
        
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin.PLUGIN_SETTINGS['booleansetting'] = _newValueForBoolSetting
    
        #print("SavePanelSettings" + str(_newValueForBoolSetting))
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        assetsearchlimit = myPlugin.PLUGIN_SETTINGS["assetsearchlimit"]
        strictname =  myPlugin.PLUGIN_SETTINGS["strictname"] 
        mainOnly =  myPlugin.PLUGIN_SETTINGS["filtertype"]
        
        #print(assetsearchlimit)
        #print(strictname)
        #print(mainOnly)
        
        
        #print(self.parent_frame.GetPlugin("Ravencore") )
        self._Panel.searchopt_strictmode.SetValue(strictname)
        self._Panel.searchopt_maxresults.SetValue(str(assetsearchlimit))
        self._Panel.searchopt_onlymain.SetValue(mainOnly)
        
        print("LoadPanelSettings")
        self.initListAssetType()
        
        


    def toggleAssetTypeList(self, evt):
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        mainOnly =  self._Panel.searchopt_onlymain.IsChecked()
        filtertypelist =  myPlugin.PLUGIN_SETTINGS["filtertypelist"]
        
        if mainOnly:
            self._Panel.m_assetTypeList.Enable(True)
            print("CHECKED ITEMS")
            print(filtertypelist)
            
            self._Panel.m_assetTypeList.SetCheckedStrings(filtertypelist)
        else:
            self._Panel.m_assetTypeList.SetCheckedStrings([])
            self._Panel.m_assetTypeList.Enable(False)



    def initListAssetType(self):
        _assetTypeList = [ ]
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        
        
        for key in assetLib._ASSET_KEYCHAR_:
            _assetTypeList.append(key)
            
            
        self._Panel.m_assetTypeList.InsertItems( _assetTypeList, 0)
        
        self.toggleAssetTypeList(None)
        
            #InsertItems(self, items, pos)










class wxRavencore_IPFSSettings_WithLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenRavencoreSettingPanel_IPFS(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
        _Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
        
        
        
        
        _Panel.Bind( wx.EVT_BUTTON, self.OnAddProvider,id = _Panel.ipfs_provider_addbt.GetId()  )
        _Panel.Bind( wx.EVT_BUTTON, self.OnRemoveProvider,id = _Panel.ipfs_provider_rembt.GetId()  )
        _Panel.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp,id = _Panel.ipfs_provider_upbt.GetId()  )
        
        
        """
        _Panel.ipfs_provider_addbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        #_Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        _Panel.ipfs_provider_rembt.Bind( wx.EVT_BUTTON, self.OnRemoveProvider )
        
        
        _Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp )
        """
    
    
    
    
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        #_newValueForBoolSetting = self._Panel.booleansetting.IsChecked()
        
        allProviders = []
        
        for i in range(0, self._Panel.ipfs_provider_list.Count):
            allProviders.append(self._Panel.ipfs_provider_list.GetString(i)) 
        
        
        default =    allProviders[0] 
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]    = default
        myPlugin.PLUGIN_SETTINGS["ipfsgateway_providers"]  = allProviders
        print(allProviders)
        print(default)
        
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        ipfsgateway_default = myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]
        ipfsgateway_providers =  myPlugin.PLUGIN_SETTINGS["ipfsgateway_providers"] 
        
        #for i in ipfsgateway_providers:
        self._Panel.ipfs_provider_list.InsertItems(ipfsgateway_providers, 0)
        
        #print("LoadPanelSettings")     
        
        
        self._Panel.Layout()
        
        
    def OnAddProvider(self, evt):    
        
        newp  = self._Panel.ipfs_text_area.GetValue()
        self._Panel.ipfs_provider_list.InsertItems([newp], self._Panel.ipfs_provider_list.Count)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnRemoveProvider(self, evt):    
        x = self._Panel.ipfs_provider_list.GetSelection()
        self._Panel.ipfs_provider_list.Delete(x)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnMoveProviderUp(self, evt): 
        x = self._Panel.ipfs_provider_list.GetSelection()
        #self._Panel.ipfs_provider_list.SetFirstItem(x)
        #print(x)
        
        _itemTopromote = self._Panel.ipfs_provider_list.GetString(x)
        self._Panel.ipfs_provider_list.Delete(x)
        
        self._Panel.ipfs_provider_list.InsertItems([_itemTopromote], 0)
        
        self._settingsHasChanged = True
        self._Panel.Layout()
        







class wxRavencore_BookmarksSettings_WithLogic(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _Panel = wxRavenRavencoreSettingPanel_Bookmarks(parent)
        PluginSettingsPanelObject.__init__(self,_Panel, parentFrame, pluginName)
    
        _Panel.SetBackgroundColour( wx.Colour( 217, 228, 255 ) )
        
        
        
        
        _Panel.Bind( wx.EVT_BUTTON, self.OnAddProvider,id = _Panel.bookmark_addbt.GetId()  )
        _Panel.Bind( wx.EVT_BUTTON, self.OnRemoveProvider,id = _Panel.bookmark_rembt.GetId()  )
        #_Panel.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp,id = _Panel.ipfs_provider_upbt.GetId()  )
        
        
        """
        _Panel.ipfs_provider_addbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        #_Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnChanged )
        _Panel.ipfs_provider_rembt.Bind( wx.EVT_BUTTON, self.OnRemoveProvider )
        
        
        _Panel.ipfs_provider_upbt.Bind( wx.EVT_BUTTON, self.OnMoveProviderUp )
        """
    
    
    
    
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        #_newValueForBoolSetting = self._Panel.booleansetting.IsChecked()
        
        allProviders = []
        
        for i in range(0, self._Panel.bookmark_list.Count):
            allProviders.append(self._Panel.bookmark_list.GetString(i)) 
        
        
        #default =    allProviders[0] 
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]    = default
        myPlugin.PLUGIN_SETTINGS["bookmark_list"]  = allProviders
        #print(allProviders)
        #print(default)
        
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        #ipfsgateway_default = myPlugin.PLUGIN_SETTINGS["ipfsgateway_default"]
        bookmark_list_s =  myPlugin.PLUGIN_SETTINGS["bookmark_list"] 
        
        #for i in ipfsgateway_providers:
        self._Panel.bookmark_list.InsertItems(bookmark_list_s, 0)
        
        #print("LoadPanelSettings")     
        
        
        self._Panel.Layout()
        
        
    def OnAddProvider(self, evt):    
        
        newp  = self._Panel.bookmark_text_area.GetValue()
        self._Panel.bookmark_list.InsertItems([newp], self._Panel.bookmark_list.Count)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnRemoveProvider(self, evt):    
        x = self._Panel.bookmark_list.GetSelection()
        self._Panel.bookmark_list.Delete(x)
        self._settingsHasChanged = True
        self._Panel.Layout()
        
        
    def OnMoveProviderUp(self, evt): 
        x = self._Panel.bookmark_list.GetSelection()
        #self._Panel.ipfs_provider_list.SetFirstItem(x)
        #print(x)
        
        _itemTopromote = self._Panel.bookmark_list.GetString(x)
        self._Panel.bookmark_list.Delete(x)
        
        self._Panel.bookmark_list.InsertItems([_itemTopromote], 0)
        
        self._settingsHasChanged = True
        self._Panel.Layout()
                