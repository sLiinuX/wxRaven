'''
Created on 18 déc. 2021

@author: slinux



This file contains the main class to define the plugin
Each plugin must have a plugin.py file which declare a class wxRavenPlugin(PluginObject)


'''


#import the class form above level, it contains predefined functions to overwrite.
#from plugins.pluginObjectTemplate import * 
from wxRavenGUI.application.pluginsframework import *
#import the design of your plugin made in FormBuilder
from .wxRavenRavencoreAssetExplorerLogic import *
#import the logic of your plugin (inherit design class with logic)
from .wxRavenRavencoreDesign import *

from .pluginSettings import *



#import the plugin setting panels, from another file to be more simple
#from .pluginSettings import MyTutorialSettingPanel_WithLogic
import json

#used for long datas requests
import threading
from .wxRavenRavencoreAssetNavigatorLogic import *

from .wxRavenRavencoreAssetIssuerLogic import *


try:
    import pyperclip
except ImportError:
    from libs import pyperclip
    
    

class wxRavenPlugin(PluginObject):
    '''
    classdocs
    '''


    def __init__(self, parentFrame, position="mgr"):
        
        
        #Call the parent class with ParentFrame and Position
        #This object is the plugin instance and will manage all views internally.
        PluginObject.__init__(self, parentFrame, position=position)
        
        
        #
        #ParentFrame is used to refer to the main app
        #Position is used to refer to the defaut position views are open.
        #
        
        
        
        #Define your plugin meta-datas :
        #
        # Name : Name of the plugin, It match the Plugin Folder name (not verified in other cases)
        # Icon
        # Views : All the views that contains the plugin
        
       
        self.PLUGIN_NAME = "Ravencore"
        self.PLUGIN_ICON = self.RessourcesProvider.GetImage('ravencoin') #wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
        
        
        
        
        #
        #    View Object declare all the 'Views' that can be instanciated
        #    {
        #             'viewid':                  a unique id for the view
        #             'name':                    a name for the view
        #             'title':                   a title id for the view
        #             'position':, 
        #             'icon':
        #             'class': 
        #             'default':                 Boolean to determine if the view is open by default at startup
        #             'multipleViewAllowed':     Boolean to determine if the view allow multiple instance of it 
        #}
        #        
        
        
        self.PLUGINS_VIEWS= [ 
                    
                    
                    {
                     'viewid':'Asset Search', 
                     'name':'Asset Search', 
                     'title':'Asset Search', 
                     'position':position, 
                     'icon':self.RessourcesProvider.GetImage('search_ravencoin'), 
                     'class': RavencoreAssetExplorer ,
                     'default':False,
                     'multipleViewAllowed':True
                     } ,
                    
                    
                    {
                     'viewid':'Asset Navigator', 
                     'name':'Asset Navigator', 
                     'title':'Asset Navigator', 
                     'position':position, 
                     'icon':self.RessourcesProvider.GetImage('asset_navigation'), 
                     'class': RavencoreAssetNavigator ,
                     'default':False,
                     'multipleViewAllowed':True
                     } ,
                    
                    
                    
                    
                    {
                     'viewid':'Asset Issuer', 
                     'name':'Asset Issuer', 
                     'title':'Asset Issuer', 
                     'position':position, 
                     'icon':self.RessourcesProvider.GetImage('asset_new'), 
                     'class': RavencoreAssetIssuerDialog ,
                     'default':False,
                     'multipleViewAllowed':False
                     }
                    
        
                    
                ]
        
        """
        
        ,
                    
                    
                    
                    
                    {
                     'viewid':'Asset Issuer', 
                     'name':'Asset Issuer', 
                     'title':'Asset Issuer', 
                     'position':position, 
                     'icon':self.RessourcesProvider.GetImage('asset'), 
                     'class': RavencoreAssetIssuerDialog ,
                     'default':False,
                     'multipleViewAllowed':False
                     }
        
        
        """
        
        #
        #    Setting Object declare all the 'default settings' 
        #    Once the plugin loaded for the first time, those settings will be saved
        #    in the config.ini file in a dedicated section when app close.
        #
        #    On next plugin load, if the config file contains plugins settings
        #    those will be overwritten in the _LoadPluginSettings() function
        #    
        #    you need to declare your own function as later in the file to CAST datas 
        #    that come from the ConfigParser in String only
        #
        #    {
        #             'key':                 value
        #    }
        #        
        
        
        self.PLUGIN_SETTINGS = {
                'assetsearchlimit' : 50,
                'strictname' : False,
                'filtertype' : False,
                'filtertypelist' : [],
                'ipfsgateway_default' : 'https://ravencoinipfs-gateway.com/ipfs/',
                'ipfsgateway_providers':['https://ravencoinipfs-gateway.com/ipfs/','https://gateway.ravenclause.com/ipfs/', 'https://cloudflare-ipfs.com/ipfs/'],
                
                'bookmark_list':['My Assets'],
                'navigation_use_cache' : True,
                'tree_display_regroupby_main':False,
                'tree_display_virtual_sort':False,
            
            
            }
        
        
        
        
        #
        # Lets put some setting pannels from pluginsetting file (to define as well)
        #
        """
        self.PLUGIN_SETTINGS_GUI = []
        
        _prefIcon = self.RessourcesProvider.GetImage('wizard-prefs')
        _MyTutorialSettingPanel_WithLogic = PluginSettingsTreeObject("Tutorial", _prefIcon, classPanel=MyTutorialSettingPanel_WithLogic, _childs=None)
        self.PLUGIN_SETTINGS_GUI.append(_MyTutorialSettingPanel_WithLogic)

        """
        self.PLUGIN_SETTINGS_GUI.clear()
        
        
        _Icon = self.RessourcesProvider.GetImage('ravencoin')
        _generalPannel = PluginSettingsTreeObject("Ravencore", _Icon, classPanel=wxRavencore_GeneralSettings_WithLogic, _childs=None)
        
        
        
        
        _Icon = self.RessourcesProvider.GetImage('bookmarks_view')
        _bmrkPannel = PluginSettingsTreeObject("Bookmarks", _Icon, classPanel=wxRavencore_BookmarksSettings_WithLogic, _childs=None)
        
        
        _Icon = self.RessourcesProvider.GetImage('raven_ipfs')
        _ipfsPannel = PluginSettingsTreeObject("IPFS Gateway", _Icon, classPanel=wxRavencore_IPFSSettings_WithLogic, _childs=None)
        
        #wxRavencore_IPFSSettings_WithLogic
        
        
        _generalPannel._childs.append(_ipfsPannel)
        _generalPannel._childs.append(_bmrkPannel)
        
        
        self.PLUGIN_SETTINGS_GUI.append(_generalPannel)
        #self.PLUGIN_SETTINGS_GUI.append(_bmrkPannel)
        
        
        #
        # Datas : In order to avoid each view to individually request the same data through RPC,
        #         the plugin can contains Global vars / datas shared to the views
        #         it also allow to request those big datas through thread and call update after
        #
        #self.setData("myPluginData", {})
        #self.setData("myPluginData2", False)
        self.setData("_LastSearch", "")
        self.setData("_AssetSearchResult", {})
        
        
        self.setData("_AssetLibraryList", {'My Assets':None})
        self.setData("_CurrentLibrary", 'My Assets')
        
        
        
        
        
        #
        # Plugin can Register on callbacks like Connexion change in this case, it will start a thread to get datas
        #
        self.parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        
        
        #
        # Finally, this last line is MANDATORY to load the default views.
        #
        #self.LoadPluginFrames()
        
    
    
    
    
    """
    
    Plugins setting management
    
    Note, this method must be overwritten on plugins that use settings since
    config parser only use STRING values.
    
    
    """
    
    def _LoadPluginSettings(self):
        _recordedSettings = self.parentFrame.Settings._GetPluginSettings(self.PLUGIN_NAME)
        
        
        for key in _recordedSettings:
            
            
            #
            # _recordedSettings[key] Return string only, do your own mapping for complex datastructure
            #
            self.PLUGIN_SETTINGS[key] = _recordedSettings[key]

            _str  = _recordedSettings[key]
            try:
                convertedData = json.loads(_str.replace('\'','"'))
                self.PLUGIN_SETTINGS[key] = convertedData
                
            except Exception as e:
                #print("NOT json data :" + str(e))
                pass
            
            if _str == "True":
                self.PLUGIN_SETTINGS[key] = True
            elif _str == "False":
                self.PLUGIN_SETTINGS[key] = False
            
        
        self.__create__libcache__()    
        
        

                
    
    def __create__libcache__(self):
        
        _AssetLibraryList = {}
        
        _bkmrk = self.PLUGIN_SETTINGS['bookmark_list']
        
        for _bookmark in _bkmrk:
            _AssetLibraryList[_bookmark] = None
        
        self.setData("_AssetLibraryList", _AssetLibraryList)
    
    
        
    '''
    
    Plugin Triggers / Callbacks for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
     
    '''
        
    def OnSearchRequested_T(self, keyword="", limit=50, onlyMain=False):    
        t=threading.Thread(target=self.OnUpdatePluginDatas_SEARCH, args=(keyword,limit, onlyMain))
        t.start()        
        
    def OnNetworkChanged_T(self, networkName=""):    
        #t=threading.Thread(target=self.OnUpdatePluginDatas)
        #t.start()
        pass
        
        
    def OnUpdatePluginDatas_SEARCH(self, keyword="", limit=50, onlyMain=False):
        
        #self.setData("myPluginData", {})
        #self.setData("myPluginData2", False)
        _AssetSearchResult = {}
        #try:
        try:
        #if True:    
            keyword = keyword.upper()

        
            _lastSearch = self.getData("_LastSearch")
            
            if _lastSearch == keyword:
                wx.CallAfter(self.UpdateActiveViews, ())
                return
            if keyword == "":
                keyword =  self.getData("_LastSearch")
  
            _SkipChars = []
            if onlyMain:
                _SkipChars = ['#', "/", '$']
            
            
            _AssetSearchResult = self.parentFrame.getRvnRPC().asset.SearchAsset(AssetName=keyword,limit=limit,datetime=True, skipChars=_SkipChars ) 
            #myPluginData = self.parentFrame.ConnexionManager.getAllConnexions()
            #myPluginData2 = self.parentFrame.ConnexionManager.getCurrent()
            
            
            self.setData("_AssetSearchResult", _AssetSearchResult)
            self.setData("_LastSearch", keyword)
               
            #self.setData("myPluginData2", myPluginData2)

            #When datas are loaded, add a call after to trigger plugins view update
            wx.CallAfter(self.UpdateActiveViews, ())
            
        except Exception as e:
            self.RaisePluginLog( "Unable to search asset :"+ str(e), type="error")
    
    
    
    
    
    def OnNavigateRequested_T(self, library=""):    
        self.setData("_CurrentLibrary", library)
        t=threading.Thread(target=self.OnUpdatePluginDatas_NAVIGATE, args=(library,))
        t.start() 
    
    def OnUpdatePluginDatas_NAVIGATE(self, library=""):
        
        
        if library == "":
            library = "My Assets"
            
            
        _resultData = None 
        
        _allLibs = self.getData("_AssetLibraryList")
        
        
        navigation_use_cache = self.PLUGIN_SETTINGS['navigation_use_cache']
        
        _virtualReorganizationButtonState = self.PLUGIN_SETTINGS['tree_display_virtual_sort']
        _organizeByMainAssetButtonState  = self.PLUGIN_SETTINGS['tree_display_regroupby_main']
        
        if navigation_use_cache:
            if _allLibs.__contains__(library):
                if _allLibs[library] != None:
                    wx.CallAfter(self.UpdateActiveViews, ())
                    return
        
        
        
        
        if library == "My Assets":
            _resultData = self.parentFrame.getRvnRPC().asset.ExploreWalletAsset(OrganizeByMainAsset=_organizeByMainAssetButtonState)
            _allLibs[library] = _resultData
           
        else:
            _resultData = self.parentFrame.getRvnRPC().asset.ExploreAsset(library, _limit=99999, _skipchars=[])
            
            
            if _virtualReorganizationButtonState:
                #print("EXPERIMENTAL =  TRY TO REORGANIZE DATAS")
                _resultData.Reorganize_Series(regularExp="^#[a-zA-Z0-9]+" , minOccurence=1)
                #print(_resultData)
            
            _allLibs[library] = _resultData
        
        
        
        
        self.setData("_AssetLibraryList", _allLibs)
        #self.setData("_CurrentLibrary", library)
        
        wx.CallAfter(self.UpdateActiveViews, ())
        
        #self.RaisePluginLog( "Unable to explore asset '"+keyword+"' :"+ str(e), type="error")
    
    
    
    def AddAssetInBookmark(self, assetName):
        currentBk = self.PLUGIN_SETTINGS['bookmark_list']
        if not currentBk.__contains__(assetName):
            currentBk.append(assetName)
            
            
            _allLibs = self.getData("_AssetLibraryList")
            _allLibs[assetName] = None
            self.setData("_AssetLibraryList", _allLibs)
            
        self.PLUGIN_SETTINGS['bookmark_list'] = currentBk
        wx.CallAfter(self.UpdateActiveViews, ())
        
    
    
    def NaviguateAsset(self, assetName):
        print("Plugin navigation requested:"+str(assetName))
        
        self.OnNavigateRequested_T(assetName)
        
        
        vcount = 0
        _views = []
        
        _navViewDatas = {}
        
        for r in self.VIEWS_INSTANCES:
            rView = r['instance']
            vName = r['viewid']
            

            if vName == "Asset Navigator":
                rView.ShowLoading()
                vcount = vcount+1
                _views.append(rView)
                
        if vcount ==0:
            _newView = self.LoadView(self.SearchPluginView("Asset Navigator"), "main")
            _newView.ShowLoading()
        #_allLibs = self.getData("_AssetLibraryList")
        
    
    
    def previewIPFS(self, ItemURL, openNew=False):
        #wx.Log.SetActiveTarget(wx.LogStderr())
        
        _PreviewWindow = self.getData("_PreviewWindow")
        
        
        if _PreviewWindow == None or openNew:
            _PreviewWindow = RavencoreHTMLViewer(self.parentFrame, ItemURL, 'mgr')
            self.setData("_PreviewWindow", _PreviewWindow)
        
        else:
            _PreviewWindow.wv.LoadURL(ItemURL)
            
            
        self.parentFrame.Views.ShowParentInManager(_PreviewWindow)
        #self.parent_frame.Views.OpenView("Simple Wallet", pluginname='', createIfNull=True)
    
        #self.parent_frame.m_mgr.GetPane("Asset Preview").Show()
        #self.parent_frame.Views.UpdateGUIManager()    
        
    
    def OpenIPFSinWebBrowser(self, _data, provider=""):
        
        print(_data)
        
        _ipfsgateway_default = self.parentFrame.GetPluginSetting("Ravencore","ipfsgateway_default")
        
        _gateway = provider
        if provider == "":
            _gateway = _ipfsgateway_default
        
        #_data= self._datacache[self._currentItem]
        print(_data['has_ipfs'])
        
        if _data['has_ipfs']:
            _url = _gateway  +_data['ipfs_hash']
            webbrowser.open(_url)
            
            
            
    def CopyClip(self, _data):
        #itemData = self._datacache[self._currentItem]
        
        print(_data)
        if _data['has_ipfs']:
            pyperclip.copy(_data['ipfs_hash'])
        
        #self.infoMessage("IPFS Hash copied to the clipboard", wx.ICON_INFORMATION)
    
    
    
    def OpenAssetIssuer(self, rootAsset=""):
        _newView = self.LoadView(self.SearchPluginView("Asset Issuer"), "main")
        
        if rootAsset !="":
            print(">root setup requested")
            _newView.setupRoot(rootAsset)
        #_popupDialog = RavencoreAssetIssuerDialog(self.parentFrame)
    
    