'''
Created on 18 déc. 2021

@author: slinux



This file contains the main class to define the plugin
Each plugin must have a plugin.py file which declare a class wxRavenPlugin(PluginObject)


'''

import webbrowser
#import the class form above level, it contains predefined functions to overwrite.
#from plugins.pluginObjectTemplate import * 
from wxRavenGUI.application.pluginsframework import *
#import the design of your plugin made in FormBuilder
from .wxRavenRavencoreAssetExplorerLogic import *
#import the logic of your plugin (inherit design class with logic)
from .wxRavenRavencoreDesign import *
#from .wxRavenRavencore_NetworkInfosLogic import *
from .pluginSettings import *
from .wxRavenRavencore_TransactionsViewer_Logic import * 
from .wxRavenRavencore_UTXOManagerLogic import *
from .wxRaven_Ravencore_AssetOwnerExporterLogic import * 

from .wxRavenRavencore_AddressViewer_Logic import * 

#import the plugin setting panels, from another file to be more simple
#from .pluginSettings import MyTutorialSettingPanel_WithLogic
import json

#used for long datas requests
import threading
from .wxRavenRavencoreAssetNavigatorLogic import *

from .wxRavenRavencoreAssetIssuerLogic import *
from wxRavenGUI.application.wxcustom import *
from plugins.Ravencore.jobs import *
'''
from plugins.Ravencore.jobs.AddressViewer_AddressUTXOJob import Job_AddressUTXO
from plugins.Ravencore.jobs.AssetNavigator_AssetOwnerJob import Job_AssetNavigator_AssetOwner
from plugins.Ravencore.jobs.AssetNavigator_NavigateAssetJob import Job_AssetNavigator_Explore
from plugins.Ravencore.jobs.AssetSearch_SeachJob import Job_AssetNavigator_Search
from plugins.Ravencore.jobs.TransactionViewer_DecodeJob import Job_DecodeTx
from plugins.Ravencore.jobs.UTXOManager_TransactionHistory import Job_WalletHistory
from plugins.Ravencore.jobs.UTXOManager_WalletUTXOJob import Job_WalletUTXO
'''
try:
    import pyperclip
except ImportError:
    from libs import pyperclip
    
    
from datetime import datetime


import inspect
from .jobs import *


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
        
        _iconOwnerlist = self.RessourcesProvider.GetImage('ownerlist')
        
        
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
                     'multipleViewAllowed':False,
                     'skip_save': True,
                     }, 
                    
                    
                    {
                     'viewid':'Wallet', 
                     'name':'Wallet', 
                     'title':'Wallet', 
                     'position':'main', 
                     'icon':self.RessourcesProvider.GetImage('wallet'), 
                     'class': wxRavenRavencore_UTXOManagerLogic ,
                     'default':False,
                     'multipleViewAllowed':True,
                     
                     }, 
                    
                    
                    
                    {
                     'viewid':'Transactions Viewer', 
                     'name':'Transactions Viewer', 
                     'title':'Transactions Viewer', 
                     'position':'main', 
                     'icon':self.RessourcesProvider.GetImage('inspect_file'), 
                     'class': wxRavenP2PMarket_RavencoreTxViewerWithLogic ,
                     'default':False,
                     'multipleViewAllowed':True,
                     'skip_save': True,
                     }, 
                    
                    
                    
                    {
                     'viewid':'Address Viewer', 
                     'name':'Address Viewer', 
                     'title':'Address Viewer', 
                     'position':'main', 
                     'icon':self.RessourcesProvider.GetImage('inspect_address'), 
                     'class': wxRaven_Ravencore_AddressViewerLogic ,
                     'default':False,
                     'multipleViewAllowed':True,
                     
                     }, 
                    
                    {
                     'viewid':'Asset Owner Exporter', 
                     'name':'Asset Owner Exporter', 
                     'title':'Asset Owner Exporter', 
                     'position':'dialog', 
                     'icon':_iconOwnerlist, 
                     'class': wxRaven_Ravencore_AssetOwnerExporterLogic ,
                     'default':False,
                     'multipleViewAllowed':False,
                     'skip_save': True,
                     'toolbar_shortcut': False,
                     'hidden_view': True,
                     },
        
                    
                ]
        
        """
         {
                     'viewid':"Network Infos", 
                     'name':"Network Infos", 
                     'title':"Network Infos", 
                     'position':position, 
                     'icon':self.RessourcesProvider.GetImage('connexion_speed_2'), 
                     'class': wxRavenRavencore_NetInfosLogic ,
                     'default':False,
                     'multipleViewAllowed':False, 
                     'toolbar_shortcut': False
                     },
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
                'ipfsgateway_default' : 'https://wxraven.link/ipfs/',
                'ipfsgateway_providers':['https://wxraven.link/ipfs/','https://wxraven.link/ipfs2/','https://ipfs.cryptide.ca/ipfs/','https://gateway.ravenclause.com/ipfs/', 'https://cloudflare-ipfs.com/ipfs/', 'https://ravencoinipfs-gateway.com/ipfs/'],
                
                'bookmark_list':['My Assets'],
                'navigation_use_cache' : True,
                'tree_display_regroupby_main':False,
                'tree_display_virtual_sort':False,
            
            
            }
        
        
        
        
        
        
        
        self.registerJob(Job_AddressInspectionAdvanced)
        self.registerJob(Job_AddressInspection)
        
        self.registerJob(Job_AddressUTXO)
        self.registerJob(Job_AssetNavigator_AssetOwner)
        self.registerJob(Job_AssetNavigator_Explore)
        self.registerJob(Job_AssetNavigator_Search)
        self.registerJob(Job_DecodeTx)
        self.registerJob(Job_WalletHistory)
        self.registerJob(Job_WalletUTXO)
        
        
        
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
        
        self.setData('_AssetOwnerList', {})
        
        
        self.setData("_AssetLibraryList", {'My Assets':None})
        self.setData("_CurrentLibrary", 'My Assets')
        
        self.setData("_AllUTXOs", {'RVN':[], 'ASSETS':[]})
        self.setData("_AllUTXOs_running", False)
        
        self.setData("_tx_history", {}) 
        self.setData("_tx_history_category", '') 
        self.setData("_tx_history_start", None) 
        self.setData("_tx_history_stop", None) 
        self.setData("_tx_history_address_filter", []) 
        
        
        self.setData("_utxo_manager_views_addons_callbacks", []) 
        
        
        self.setData("_last_tx_decoded", None) 
        
        self.setData("_address_viewer_running", False) 
        self.setData("_address_viewer_current_address_text", '') 
        
        self.setData("_address_viewer_advanced_mode", False) 
        self.setData("_address_viewer_check_inputs", False) 
        self.setData("_address_viewer_check_iterations", 1) 
        
        self.setData("_address_viewer_datas_utxo", {}) 
        self.setData("_address_viewer_datas_tx_history", {}) 
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
        
    def OnSearchRequested_T(self, keyword="", limit=50, onlyMain=False, callback=None, openViewAfter=False):    
        #t=threading.Thread(target=self.OnUpdatePluginDatas_SEARCH, args=(keyword,limit, onlyMain))
        #t.start()     
        
        #Job_AssetNavigator_Explore
        
        j = Job_AssetNavigator_Search(self, keyword=keyword,limit=limit,onlyMain=onlyMain, viewCallback=callback, safeMode=True)
        self.parentFrame.NewJob(j)
        
        if openViewAfter:
            _newView = self.parentFrame.Views.OpenView("Asset Search", "Ravencore", True)
            print(_newView)
            if _newView != None:
                self.parentFrame.Views.OpenView("Asset Search", "Ravencore", False)
                #_vi = self.parentFrame.Views.SearchViewInstance("Asset Search")
                #_vi['instance'].Show()
                #self.parentFrame.Views.
           
        
    def OnNetworkChanged_T(self, networkName=""):    
        #t=threading.Thread(target=self.OnUpdatePluginDatas)
        #t.start()
        #wx.CallAfter(self.UpdateActiveViews, ())
        #pass
        if not self.parentFrame._isReady:
            return None 
        
        
        #self.OnUTXORequested_T()
        
        
    def OnUpdatePluginDatas_SEARCH(self, keyword="", limit=50, onlyMain=False):
        print('OnUpdatePluginDatas_SEARCH === SHOULD BE REPLACED')
        #self.setData("myPluginData", {})
        #self.setData("myPluginData2", False)
        '''
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
    
        '''
    
    
    
    def OnNavigateRequested_T(self, lib="", callback=None):    
        self.setData("_CurrentLibrary", lib)
        #t=threading.Thread(target=self.OnUpdatePluginDatas_NAVIGATE, args=(library,))
        #t.start() 
        j = Job_AssetNavigator_Explore(self,library=lib, viewCallback=callback, safeMode=True)
        self.parentFrame.NewJob(j)
    
    def OnUpdatePluginDatas_NAVIGATE(self, library=""):
        print('OnUpdatePluginDatas_HISTORY === SHOULD BE REPLACED')
        '''
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
        '''
    
    
    
    
    
    
    
    
    
    
    
    def OnHISTORYRequested_T(self,callback=None):
        self.setData("_tx_history", {})
        #t=threading.Thread(target=self.OnUpdatePluginDatas_HISTORY, args=())
        #t.start()  
        j = Job_WalletHistory(self, viewCallback=callback, safeMode=True)
        self.parentFrame.NewJob(j)
    
    def OnUpdatePluginDatas_HISTORY(self, library=""):
        print('OnUpdatePluginDatas_HISTORY === SHOULD BE REPLACED')
        #print('OnUpdatePluginDatas_HISTORY')
        
        '''
        ravencoin = self.parentFrame.getRvnRPC()
        _DatasHistory = { }
        #if True:
        #if True:
        try:
            
            
            _categorie = self.getData("_tx_history_category") 
            _start_date = self.getData("_tx_history_start") 
            _stop_date = self.getData("_tx_history_stop") 
            _filter_addresses = self.getData("_tx_history_address_filter") 

            _DatasHistory = ravencoin.wallet.GetWalletTransactionList(categorie=_categorie, filter_addresses=_filter_addresses, start_date=_start_date, stop_date=_stop_date)
            
            #_ListAsset = ravencoin.asset.GetAssetUnspentList(assetname='', _fullDatas=True, _includeLocked=True)
            #_DatasUtxo['ASSETS'] = _ListAsset
            
            #print(f"_DatasUtxo {_DatasUtxo['ASSETS']}")
            wx.CallAfter(self.UpdateActiveViews, ())

        except Exception as e:
            self.RaisePluginLog( "Unable to update UTXO List : "+ str(e), type="error")
    
        
        self.setData("_tx_history", _DatasHistory)
        #print(f"SAVEDATA ")
    
        '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def OnUTXORequested_T(self, callback=None):
        self.setData("_AllUTXOs", {'RVN':[], 'ASSETS':[]})
        #t=threading.Thread(target=self.OnUpdatePluginDatas_UTXO, args=())
        #t.start() 
        
        j = Job_WalletUTXO(self, viewCallback=callback, safeMode=True)
        self.parentFrame.NewJob(j)
        
    
    def OnUpdatePluginDatas_UTXO(self, library=""):
        pass
        print('OnUpdatePluginDatas_UTXO === SHOULD BE REPLACED')
        '''
        if self.getData("_AllUTXOs_running")==True:
            return 
        
        
        self.setData("_AllUTXOs_running", True)
        print('OnUpdatePluginDatas_UTXO')
        
        
        ravencoin = self.parentFrame.getRvnRPC()
        _DatasUtxo = {'RVN':[],'ASSETS':[] }
        #if True:
        try:
            _listRaw = ravencoin.wallet.GetUnspentList(_OnlySpendable=True, _ExlcudeAddresses=[],_IncludeOnlyAddresses=[], _fullDatas=True , _includeLocked=True)
            _DatasUtxo = self.getData('_AllUTXOs')
            _DatasUtxo['RVN'] = _listRaw
            
            
            _ListAsset = ravencoin.asset.GetAssetUnspentList(assetname='', _fullDatas=True, _includeLocked=True)
            _DatasUtxo['ASSETS'] = _ListAsset
            
            #print(f"_DatasUtxo {_DatasUtxo['ASSETS']}")
            wx.CallAfter(self.UpdateActiveViews, ())
    
    
        
    
        except Exception as e:
            self.RaisePluginLog( "Unable to update UTXO List : "+ str(e), type="error")
    
        self.setData("_AllUTXOs_running", False)
        self.setData("_AllUTXOs", _DatasUtxo)
        #print(f"SAVEDATA ")
        '''
        
     
     
     
     
     
     
     
    #
    #
    #AddressScan
    #    
    #
        
        
        
    def OnAddressScanRequest_T(self):
        print(str(inspect.stack()[0][0].f_code.co_name))
        print(str(inspect.stack()[1][0].f_code.co_name))
        #print(str(inspect.stack()[2][0].f_code.co_name))
        print('OnAddressScanRequest_T === SHOULD BE REPLACED')
        #self.OnAddressUTXORequested_T()
        #self.OnAddressHISTORYRequested_T()
        
    
    
    
        
    def OnAddressUTXORequested_T(self, callback=None):   
        self.setData("_address_viewer_datas_utxo", {'RVN':[],'ASSETS':[] }) 
        
        
        j = Job_AddressUTXO(self, viewCallback=callback, safeMode=True)
        self.parentFrame.NewJob(j)
        #t=threading.Thread(target=self.OnUpdatePluginAddressDatas_UTXO, args=())
        #t.start() 
    
    
    #
    # Replaced by a JOB
    #
    def OnUpdatePluginAddressDatas_UTXO(self, library=""):
        pass
        print('OnUpdatePluginAddressDatas_UTXO === SHOULD BE REPLACED')
        '''
        _add = self.getData('_address_viewer_current_address_text') 
        print(f'OnUpdatePluginAddressDatas_UTXO {_add}')
        
        
        ravencoin = self.parentFrame.getRvnRPC()
        _DatasUtxo = {'RVN':[],'ASSETS':[] }
        if True:
        #try:
            
            if _add == "":
                return
            
            _addressList = _add.split(',')
            
            
            
            _listRaw = ravencoin.directories.GetAddressUnspentList( _addressList, asset="RVN", _excludeAsset='')
            _DatasUtxo = self.getData('_address_viewer_datas_utxo')
            _DatasUtxo['RVN'] = _listRaw
            
            
            _ListAsset = ravencoin.directories.GetAddressUnspentList(_addressList, asset='*', _excludeAsset='RVN')
            _DatasUtxo['ASSETS'] = _ListAsset
            
            #print(f"_DatasUtxo {_DatasUtxo['ASSETS']}")
            wx.CallAfter(self.UpdateActiveViews, ())
    
    
        
    
        #except Exception as e:
        #    self.RaisePluginLog( "Unable to update address UTXO List : "+ str(e), type="error")
    
        
        self.setData("_address_viewer_datas_utxo", _DatasUtxo)
        '''
        
        
        
        
        
        
        
    
    
    
    
    
    def OnAddressHISTORYRequested_T(self, callback=None):
        
        self.setData("_address_viewer_datas_tx_history", {})
        j = Job_AddressInspection(self, viewCallback=callback, safeMode=True)
        self.parentFrame.NewJob(j)
        #self.setData("_address_viewer_datas_tx_history", {})
        #t=threading.Thread(target=self.OnUpdatePluginAddressDatas_HISTORY, args=())
        #t.start() 
    
    
    #
    # Replaced by a JOB
    #
    def OnUpdatePluginAddressDatas_HISTORY(self, library=""):
        pass
        print('OnUpdatePluginAddressDatas_UTXO === SHOULD BE REPLACED')
        
        
        '''
        
        
        if self.getData("_address_viewer_running") ==True:
            return 
        print('OnUpdatePluginDatas_HISTORY')
        
        _add = self.getData('_address_viewer_current_address_text') 
        ravencoin = self.parentFrame.getRvnRPC()
        _DatasHistory = []
        
        self.setData("_address_viewer_running", True) 
        
        #if True:
        if True:
        #try:
            
            if _add == "":
                return
            
            _addressList = _add.split(',')
            #_categorie = self.getData("_tx_history_category") 
            #_start_date = self.getData("_tx_history_start") 
            #_stop_date = self.getData("_tx_history_stop") 
            #_filter_addresses = self.getData("_tx_history_address_filter") 

            _DatasHistoryList = ravencoin.directories.GetAddressTransactionList(_addressList, _fullScan=False)
            _cursor = 0
            _max = len(_DatasHistoryList)
            
            for _item in _DatasHistoryList:
                #print(f"Inspecting Transactions ({_cursor} / {_max}0")
                
                _txInspected = ravencoin.utils.GetAndScanRawTransaction(_item, _addressList)
                _DatasHistory.append(_txInspected)
            
                _cursor = _cursor+1
               
            
            #print(_DatasHistory)
            #_ListAsset = ravencoin.asset.GetAssetUnspentList(assetname='', _fullDatas=True, _includeLocked=True)
            #_DatasUtxo['ASSETS'] = _ListAsset
            
            #print(f"_DatasUtxo {_DatasUtxo['ASSETS']}")
            #wx.CallAfter(self.UpdateActiveViews, ())

        #except Exception as e:
        #    self.RaisePluginLog( "Unable to update address transaction history List : "+ str(e), type="error")
    
        self.setData("_address_viewer_running", False)
        self.setData("_address_viewer_datas_tx_history", _DatasHistory)
    
        '''
    
    
    
    
    
        
        
        
    #
    # Views caller and quickwin
    #
    
    
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
    def OpeninWebBrowser(self, _url):
        webbrowser.open(_url)    
    
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
            self.OpeninWebBrowser(_url)
            
            
            
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
    
    
    
    def ExportAssetOwnerList(self, assetSearch):
        
        _newView = self.parentFrame.Views.OpenView("Asset Owner Exporter", "Ravencore", True)
        
        #if txdatas !="":
        if True:
            _v=self.parentFrame.Views.SearchDialog("Asset Owner Exporter")
            
            if _v!=None:
                print(f">ExportAssetOwnerList requested {assetSearch}")
                _v._Panel.SetAssetAndStart(assetSearch)
    
    
    
    def ShowTxInfos(self, txdatas="", openIfnotExist=True):
        
        #_newView = self.parentFrame.Views.OpenView("Transactions Viewer", "Ravencore", openIfnotExist)
        _newView = self.LoadView(self.SearchPluginView("Transactions Viewer"), "main")
        
        if txdatas!="":
            _newView.SetTxId(txdatas)
            
            
            
            
            
    def GetUTXOManager(self, open=True):
        _newView = self.parentFrame.Views.OpenView("Wallet", "Ravencore", open)
        print(_newView)
        if _newView == None:
            _vi = self.parentFrame.Views.SearchViewInstance("Wallet")
            return _vi['instance']
        return _newView['instance']
    
    
    
    def CheckIPFSGateway(self):
        pass
    
    def QuickWalletUnlockRequest(self):
        
        
        ravencoin = self.parentFrame.getRvnRPC()
        pwd=RequestUserWalletPassword(self.parentFrame)
        if pwd != None:
            res=ravencoin.wallet.__check_unlock__(_passphrase=pwd, timeout=30)
            #UserAdvancedMessage(parentf, message, type, msgdetails, showCancel)
        
            ReportRPCResult(self.parentFrame, res )
    
    
    
    