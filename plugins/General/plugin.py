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

from .wxRavenWelcomePanel import wxRavenWelcomeTabLogic


#import libs.wxRaven_Flask_WebserviceClient
from libs.wxRaven_Webservices.wxRaven_Flask_Webservice import wxRaven_Flask_WebserviceClient

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
                    
                    
                ]
        
        
        
        self.PLUGIN_SETTINGS = {
                'showerror' : ['error','message', 'warning', 'infos'],
                'defaultviewarea':'main',
                'last_network':'mainnet_localhost',
                'disable_plugins' :[],
                'quick_links' :[],
                'debug_out' :'stderr',
                'show_disclaimer':True,
                'show_welcome':True,
                'purge_on_close':True,
                'save_on_close':True,
                
                
                'favorite_send_addresses':{},
                'favorite_receive_addresses':{},
                'favorite_change_addresses':{},
                
                
                'webservices_relays':{'wxRaven_Relay1':'wx:wx@18.221.126.115:9090'},
            }
        
        
        
        
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
        self.setData("_cursor",0)
        self.setData("_errorPushed",False)
        
        self.Init_Webservices_Relays()
        
        
        
        #self.LoadPluginFrames()
    
    
    
    
    
    
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
    
    
    
    
    
    
    def Init_Webservices_Relays(self):
        allCons = self.PLUGIN_SETTINGS['webservices_relays']
        
        
        for conName in allCons:
                #pass
                data = allCons[conName]

                _creds = data.split("@")
                _loginPwd = _creds[0].split(":")
                _hostPort = _creds[1].split(":")
                
                #newCon = Ravencoin(username=_loginPwd[0], password=_loginPwd[1],host=_hostPort[0],port=_hostPort[1])
                newCon = wxRaven_Flask_WebserviceClient(ip=_hostPort[0], port=_hostPort[1])
                
                self.parentFrame.ConnexionManager.rpc_connectors[conName] = newCon
    
    
    '''
    Quick wins
    '''
    
    
    
    
    
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
    
    
    
    
    
    
    
    
        
    '''
    
    Plugin Triggers for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
    '''
  
        
    def OnNetworkChanged_T(self, networkName=""):    
        if not self.parentFrame._isReady:
            return
        
        t=threading.Thread(target=self.OnNetworkChanged)
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
        