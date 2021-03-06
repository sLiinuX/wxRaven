'''
Created on 10 déc. 2021

@author: slinux
'''

from wxRavenGUI.application.pluginsframework import *
import threading
from datetime import datetime
import inspect

import re
from .wxRavenDebugConsoleLogic import *
from .wxRavenErrorLogConsoleLogic import *
from .wxNotebookToolbox import *
from .pluginSettings import *
from .wxRaven_JobManager_ConsoleLogic import *

from .wxRavenWelcomePanel import wxRavenWelcomeTabLogic
from .wxRaven_WebBrowser import *

#import libs.wxRaven_Flask_WebserviceClient
from libs.wxRaven_Webservices.wxRaven_Flask_Webservice import wxRaven_Flask_WebserviceClient



from wxRavenGUI.application.core.jobs import *

from .wxRaven_General_AboutConnexionLogic import wxRaven_General_AboutConnexion_Logic
from .wxRaven_General_RelaySessionTokenManagementLogic import wxRaven_General_RelaySessionTokenManagement_Logic
from .wxRaven_General_TxStandbyLogic import wxRaven_General_TxStandby_Logic


class wxRavenPlugin(PluginObject):
    
    
    
    
    def __init__(self, parentFrame, position="mgr"):
        PluginObject.__init__(self, parentFrame, position=position)
        
        
        self.PLUGIN_NAME = "General"
        #self.PLUGIN_ICON = wx.Bitmap( u"res/default_style/normal/dialog_default.png", wx.BITMAP_TYPE_ANY )
        self.PLUGIN_ICON = self.RessourcesProvider.GetImage('dialog_default')
        
        self.PLUGINS_VIEWS= [ 
                    {
                     'viewid':'Error Log Console', 
                     'name':'Error Log Console', 
                     'title':'Error Log Console', 
                     'position':'mgr', 
                     'icon':  self.RessourcesProvider.GetImage('error_console'), 
                     'class': RavenErrorLogConsole ,
                     'default':True,
                     'multipleViewAllowed':False
                     },
                    
                     {
                     'viewid':'Job Manager Console', 
                     'name':'Job Manager Console', 
                     'title':'Job Manager Console', 
                     'position':'mgr', 
                     'icon':  self.RessourcesProvider.GetImage('pview'), 
                     'class': wxRaven_JobManager_Console_Logic ,
                     'default':True,
                     'multipleViewAllowed':False
                     },
                    
                    {
                     'viewid':'Debug', 
                     'name':'Debug', 
                     'title':'Debug', 
                     'position':'mgr', 
                     'icon':  self.RessourcesProvider.GetImage('debug_exc'), 
                     'class': wxRavenDebugConsole ,
                     'default':False,
                     'multipleViewAllowed':False
                     },
                    
                    
                    {
                     'viewid':'Notebook Toolbox', 
                     'name':'Notebook Toolbox', 
                     'title':'Notebook Toolbox', 
                     'position':'mgr', 
                     'icon':   self.RessourcesProvider.GetImage('tab_view') , 
                     'class': RavenNotebookToolbox ,
                     'default':False,
                     'multipleViewAllowed':True,
                     'isArea':True
                     
                     },
                    
                    
                    
                     {
                     'viewid':'Welcome', 
                     'name':'Welcome', 
                     'title':'Welcome', 
                     'position':'main', 
                     'icon':   self.RessourcesProvider.GetImage('welcome16') , 
                     'class': wxRavenWelcomeTabLogic ,
                     'default':True,
                     'multipleViewAllowed':False,
                     'isArea':False,
                     
                     },
                     
                     
                     {
                     'viewid':'WebBrowser', 
                     'name':'WebBrowser', 
                     'title':'WebBrowser', 
                     'position':'main', 
                     'icon':   self.RessourcesProvider.GetImage('internal_browser') , 
                     'class': wxRaven_WebBrowserLogic ,
                     'default':False,
                     'multipleViewAllowed':True,
                     'isArea':False,
                     
                     },
                     
                     
                     
                     {
                     'viewid':'About Connexions', 
                     'name':'About Connexions', 
                     'title':'About Connexions', 
                     'position':'dialog', 
                     'icon':   self.RessourcesProvider.GetImage('connexion_speed') , 
                     'class': wxRaven_General_AboutConnexion_Logic ,
                     'default':False,
                     'multipleViewAllowed':False,
                     'isArea':False,
                     'toolbar_shortcut': False,
                     'hidden_view': True,
                     'skip_save': True,
                     
                     },
                     
                      {
                     'viewid':'Relay Session Token Management', 
                     'name':'Relay Session Token Management', 
                     'title':'Relay Session Token Management', 
                     'position':'dialog', 
                     'icon':   self.RessourcesProvider.GetImage('help_view') , 
                     'class': wxRaven_General_RelaySessionTokenManagement_Logic ,
                     'default':False,
                     'multipleViewAllowed':False,
                     'isArea':False,
                     'toolbar_shortcut': False,
                     'hidden_view': True,
                     'skip_save': True,
                     
                     },
                      
                       {
                     'viewid':'Transaction Standby Dialog', 
                     'name':'Transaction Standby Dialog', 
                     'title':'Transaction Standby Dialog', 
                     'position':'dialog', 
                     'icon':   self.RessourcesProvider.GetImage('credit_card') , 
                     'class': wxRaven_General_TxStandby_Logic ,
                     'default':False,
                     'multipleViewAllowed':False,
                     'isArea':False,
                     'toolbar_shortcut': False,
                     'hidden_view': True,
                     'skip_save': True,
                     
                     },
                    
                    
                ]
        
        
        
        self.PLUGIN_SETTINGS = {
                'showerror' : ['error','message', 'warning', 'infos'],
                'defaultviewarea':'main',
                'last_network':'mainnet_localhost',
                'disable_plugins' :[],
                'quick_links' :[],
                'show_disclaimer':True,
                'show_welcome':True,
                'purge_on_close':True,
                'save_on_close':True,
                'max_running_jobs':5,
                'log_mode':True,
                'debug_mode':False,
                
                'open_url_with_webbrowser':None,
                
                'sw_configuration':'wxRaven : Developer/Server Edition',
                
                
                'favorite_send_addresses':{},
                'favorite_receive_addresses':{},
                'favorite_change_addresses':{},
                
                
                'webservices_relays':{
                    'wxRaven_Relay1_HTTPS':'https://wxraven.link/relay/'
                    },
                
                'use_remote_jobs':True,
                'authorize_remote_jobs':False,
                
                'relay_user_session_token':True,
                'relay_private_session_key':False,
                'relay_private_session_key_value':'',
                
            }
        
        
        
        #'relay_use_tokens':True,
        #        'relay_private_tokens':'',
        
        
        '''
        #NOT REGISTERED AS NO USAGE REMOTE
        self.registerJob(Job_DisplayRejectJob)
        self.registerJob(Job_RefreshGUI)
        self.registerJob(Job_RemoteJob)
        
        '''
        
        
        
        
        """
        
        
        Settings pannel tree, using the objhect PluginSettingsTreeObject
        
        
        """
        self.PLUGIN_SETTINGS_GUI = []
        
        """
        _prefIcon = wx.Bitmap( u"res/default_style/normal/wizard-prefs.png", wx.BITMAP_TYPE_ANY )
        _viewIcon = wx.Bitmap( u"res/default_style/normal/perspective_default.png", wx.BITMAP_TYPE_ANY )
        _conIcon = wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY )
        _appIcon = wx.Bitmap( u"res/default_style/normal/frame_default.png", wx.BITMAP_TYPE_ANY )
        """
        
        _prefIcon = self.RessourcesProvider.GetImage('wizard-prefs')
        _viewIcon = self.RessourcesProvider.GetImage('perspective_default')
        _conIcon = self.RessourcesProvider.GetImage('network')
        _relays = self.RessourcesProvider.GetImage('connexion_share_1')
        _appIcon = self.RessourcesProvider.GetImage('frame_default')
        _pluginsIcon = self.RessourcesProvider.GetImage('install-handler')
        _walletIcon = self.RessourcesProvider.GetImage('wallet')
        
        

        self.PLUGIN_SETTINGS_GUI.clear()
        
        
        _applicationPannel = PluginSettingsTreeObject("Application", _appIcon, classPanel=wxRavenApplicationSettingPanel, _childs=None)
        

        _generalPannel = PluginSettingsTreeObject("General", _prefIcon, classPanel=wxRavenGeneralSettingPanel, _childs=None)
        #_viewPannel = PluginSettingsTreeObject("Views", _viewIcon, classPanel=None, _childs=None)
        _connexionPannel = PluginSettingsTreeObject("Connexions", _conIcon, classPanel=wxRavenConexionsSettingPanel, _childs=None)
        
        _relaysPannel = PluginSettingsTreeObject("Relays", _relays, classPanel=wxRavenConnexionRelaysSettings_SettingLogic, _childs=None)
        
        
        _pluginsPannel = PluginSettingsTreeObject("Plugins", _pluginsIcon, classPanel=wxRavenPluginsSettingPanel, _childs=None)
        
        
        _WalletPannel = PluginSettingsTreeObject("Wallet", _walletIcon, classPanel=wxRaven_General_WalletSettingsLogic, _childs=None)
        
        
        
        
        _applicationPannel._childs.append(_generalPannel)
        #_applicationPannel._childs.append(_viewPannel)
        _applicationPannel._childs.append(_connexionPannel)
        _applicationPannel._childs.append(_relaysPannel)
        _applicationPannel._childs.append(_WalletPannel)
        _applicationPannel._childs.append(_pluginsPannel)
        
        
        self.PLUGIN_SETTINGS_GUI.append(_applicationPannel)
        
        #self.PLUGIN_SETTINGS_GUI.append(_generalPannel)
        #self.PLUGIN_SETTINGS_GUI.append(_viewPannel)
        #self.PLUGIN_SETTINGS_GUI.append(_connexionPannel)
        
        
        
        
        """
        _prefIcon = self.RessourcesProvider.GetImage('wizard-prefs')
        _generalPannel = PluginSettingsTreeObject("General", _prefIcon, classPanel=None, _childs=None)
        self.PLUGIN_SETTINGS_GUI.append(_generalPannel)
       
        """
        
        
        

        self.ALLOW_MULTIPLE_VIEWS_INSTANCE = True
        
        
        self.parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        
        self.setData("allLogs", {})
        self.setData("_RejectedJobList",[])
        self.setData("_cursor",0)
        self.setData("_errorPushed",False)
        
        #self.Init_Webservices_Relays()
        
        
        
        #self.LoadPluginFrames()
        
        self.waitApplicationReady()
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.__applicationReady__,),  daemon=True)
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parentFrame._isReady:
            time.sleep(1)
            
        wx.CallAfter(callback, ()) 
        
        
        #self.initializeAssetManagerBackgroundService()
    
    
    def __applicationReady__(self, evt=None):
        self.Init_Webservices_Relays()
    
    
    
    
    
    '''
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
                
                
            #print(key) 
            #print(self.PLUGIN_SETTINGS[key])
    
    '''
    
    
    
    
    def Init_Webservices_Relays(self):
        allCons = self.PLUGIN_SETTINGS['webservices_relays']
        
        
        for conName in allCons:
                #pass
                data = allCons[conName]
                self.logger.info(f" {conName} Relay detected !")
                
                
                _host = data
                _port = 9090
                
                if data.__contains__('@'):
                    _creds = data.split("@")
                    _loginPwd = _creds[0].split(":")
                    _hostPort = _creds[1].split(":")
                    _host=_hostPort[0]
                    _port=_hostPort[1]
                if data.__contains__('http'):
                    _host = data
                    _port = 9090
                
                #newCon = Ravencoin(username=_loginPwd[0], password=_loginPwd[1],host=_hostPort[0],port=_hostPort[1])
                newCon = wxRaven_Flask_WebserviceClient(ip=_host, port=_port)
                
                _useToken =  self.PLUGIN_SETTINGS['relay_user_session_token']
                relay_private_session_key = self.PLUGIN_SETTINGS["relay_private_session_key"]
                relay_private_session_key_value = self.PLUGIN_SETTINGS["relay_private_session_key_value"]
                
                try:
                    if _useToken:
                        if not relay_private_session_key:
                            newCon.__RequestSessionToken__()
                        else:
                            newCon.__SetSessionToken__(relay_private_session_key_value)
                except Exception as e:
                    self.logger.warning('unable to get a token from webservice')
                self.parentFrame.ConnexionManager.rpc_connectors[conName] = newCon
    
    
    '''
    Quick wins
    '''
    
    
    def OpenUrl(self, _url):
        
        _inWebBrowser=False
        if self.PLUGIN_SETTINGS['open_url_with_webbrowser'] == None :
            _inWebBrowser = UserQuestion(self.parentFrame, "Open the url in external webbrowser ?\nInternal Webview require to install some aditionals components and may not be compatible with all websites.")   
            
            
            
        if _inWebBrowser:
            rvcoreplugin = self.parentFrame.GetPlugin('Ravencore')
            rvcoreplugin.OpeninWebBrowser(_url)
            
        else:
            self.OpenInternalUrl(_url)
            pass
    
    
    def OpenInternalUrl(self, ItemURL):
        #wx.Log.SetActiveTarget(wx.LogStderr())
        
        #_PreviewWindow = self.getData("_PreviewWindow")
        _newView = self.LoadView(self.SearchPluginView("WebBrowser"), "main",)
        _newView.OpenUrl(ItemURL)
        
    
    
    
    
    
    def OpenTxStandbyDialog(self, jobInstance=None, jobDatas=None):
        _v= self.parentFrame.Views.OpenView("Transaction Standby Dialog", createIfNull=True)
        _d = self.parentFrame.Views.SearchDialog("Transaction Standby Dialog")
        self.setData('_lastTxDialog', _d)
        
        if jobInstance != None:
            jobInstance._txDialog = _d
            
        if jobDatas != None:
            _d._Panel.__SetDatas__(jobDatas)
            
        #print(_v)
        #print(_d)
        return _d
    
    def OpenAboutConnexion(self):
        #wx.Log.SetActiveTarget(wx.LogStderr())
        #_PreviewWindow = self.getData("_PreviewWindow")
        #_newView = self.LoadView(self.SearchPluginView("About Connexion"), "dialog",)
        #_newView = self.parentFrame.Views.OpenView("About Connexion", "General", True)
        self.parentFrame.Views.OpenView("About Connexions", createIfNull=True)
        '''
        if isinstance(_newView, dict):
            _newView = self.parentFrame.Views.SearchDialog("About Connexion")
        print(_newView)
        _newView.Show()
        '''
    
    
    def OpenRelaySessionTokenManagement(self):
        #wx.Log.SetActiveTarget(wx.LogStderr())
        #_PreviewWindow = self.getData("_PreviewWindow")
        #_newView = self.LoadView(self.SearchPluginView("About Connexion"), "dialog",)
        #_newView = self.parentFrame.Views.OpenView("About Connexion", "General", True)
        self.parentFrame.Views.OpenView("Relay Session Token Management", createIfNull=True)
    
    
    
    def GetFavoriteAddress(self, favorite_key, network):
        
        if network == '':
            network = self.parentFrame.ConnexionManager.getCurrent()
        
        _res=''
        if self.PLUGIN_SETTINGS[favorite_key].__contains__(network):
            _res = self.PLUGIN_SETTINGS[favorite_key][network]
        return _res
    
    
    
    
    def GetFavoriteSendAddress(self, network=''):
        return self.GetFavoriteAddress('favorite_send_addresses', network)
    
    def GetFavoriteReceiveAddress(self, network=''):
        return self.GetFavoriteAddress('favorite_receive_addresses', network)
    
    def GetFavoriteChangeAddress(self, network=''):
        return self.GetFavoriteAddress('favorite_change_addresses', network)
    
    
    def SetUserTokenSettingsAndEnableOption(self, key):
        self.PLUGIN_SETTINGS["relay_private_session_key"] = True
        self.PLUGIN_SETTINGS["relay_private_session_key_value"] = key
        
        for _c in self.parentFrame.ConnexionManager.getAllConnexions():
            if self.parentFrame.getNetworkType(_c) == "WS-RPC":
                self.parentFrame.ConnexionManager.rpc_connectors[_c].__SetSessionToken__(key)
        
        #if self.w
    
    
    def GetUserTokenSettings(self):
        return self.PLUGIN_SETTINGS["relay_private_session_key"], self.PLUGIN_SETTINGS["relay_private_session_key_value"]
    
    
        
    '''
    
    Plugin Triggers for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
    '''
  
  

  
  
        
    def OnNetworkChanged_T(self, networkName=""):    
        if not self.parentFrame._isReady:
            return
        
        t=threading.Thread(target=self.OnNetworkChanged, daemon=True)
        t.start()
        
        
    def OnNetworkChanged(self):
        
        self.Log("Network Changed !")
        
        """
        self.setData("globalBalance", 0.0)
        self.setData("allAccountsDatas", [])
        self.setData("globalAssetBalance", [])
        self.setData("allAddresses", [])
        """
    
    
    
    def PopStatusBarErrorMessage(self, evt=None):
        pass
        '''
        if self.getData("_errorPushed") :
            print('pop')
            self.parentFrame.wxRavenStatusBar.PopStatusText(  0)
            self.setData("_errorPushed",False)
        '''
    
    def PushStatusBarErrorMessage(self, evt=None):
        self.parentFrame.MenusAndTool.PushStatusBarErrorMessage()
        #self.parentFrame.Views.PopStatusBarErrorMessage()
        '''
        if not self.getData("_errorPushed") :
            print('push')
            self.parentFrame.wxRavenStatusBar.PushStatusText( "Some Errors occured, check the console log.", 0)
            self.setData("_errorPushed",True)
        #self.parentFrame.wxRavenStatusBar.PushStatusText( "Some Errors occured, check the console log.", 1)
        '''
            
        
    def Log(self, message , source="", timestamp=None, type="info"):
        
        
        existingLogs = self.getData("allLogs")
        _cursor = self.getData("_cursor")
        
        if timestamp == None:
            now = datetime.now()
            timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
         
        #print(str(inspect.stack()[0][0].f_code.co_name))
        #print(str(inspect.stack()[1][0].f_code.co_name))
        #print(str(inspect.stack()[2][0].f_code.co_name))
        
        #print(str(inspect.stack()[0][0]))
        #print(str(inspect.stack()[1][0]))
        #print(str(inspect.stack()[2][0]))
        #print(message)
        
        
        '''
        _match = re.search(r'(.+)(<Fault.+)', message)
        if _match:
            message = _match.group(1) + ' Feature not available in Webservice / No Wallet Mode.'
        '''
        
        if source == "":
            source = str(inspect.stack()[1][0])
         
        if type=="error":
            wx.CallAfter(self.PushStatusBarErrorMessage, ())
             
         
        newLogLine = [type,str(message), source, timestamp]
        existingLogs[_cursor] = newLogLine
        self.setData("allLogs", existingLogs)
        
        _cursor = _cursor+1
        self.setData("_cursor", _cursor)
        wx.CallAfter(self.UpdateActiveViews, ())
        