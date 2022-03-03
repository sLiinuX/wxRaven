'''
Created on 10 déc. 2021

@author: slinux
'''
import wx
import wx.adv
import wx.aui
import os.path
from wx import *
import threading

from libs.wxRaven_Webservices import wxRaven_RPC_WebserviceClient
from libs.RVNpyRPC import *
from wxRavenGUI.view import *
from wxRavenGUI.application.core import *
from wxRavenGUI.application.core.wxRessourcesProvider import RessourcesProvider
from wxRavenGUI.application.wxcustom.CustomUserIO import UserAdvancedMessage
import sys


#
#
# Default Paths for LOCAL Profile
#
#
'''
ROOT_PATH = os.getcwd()
RES_PATH = os.getcwd() + "/res/"
CONFIG_PATH = os.getcwd() + "/config/"
PLUGIN_PATH = os.getcwd() + "/plugins/"
USERDATA_PATH = os.getcwd() + "/userdata/"
'''




class wxRavenAppMainFrame(wxRavenMainFrame):
    
    
    
    wxRavenStatusBarIcon = None
    wxRavenNetworkBarIcon = None
    
    
    mainApp =  None
    Logs = None
    
    Settings = None
    Views = None
    Plugins = None
    
    ConnexionManager = None
    RavencoinRPC = None
    
    PerspectiveManager = None
    MenusAndTool = None
    
    JobManager = None
    
    Ressources = None
    Paths = {}
    
    def __init__(self, _ProfilePath='', mainApp=None):
        
        self.logger = logging.getLogger('wxRaven')
        
        
        wxRavenMainFrame.__init__(self,None)
        self._isReady = False
        self._Closing = False
        self.mainApp = mainApp
        
        #splash.Show()
        
        _rootPath = os.getcwd()
        if _ProfilePath == '':
            _ProfilePath = os.getcwd()
        
        self.Paths = {'ROOT':_rootPath,
                      'RES' : _rootPath + "/res/",
                      'CONFIG' : _ProfilePath + "/config/",
                      'PLUGIN' : _rootPath + "/plugins/",
                      'USERDATA' : _ProfilePath + "/userdata/",
                      'PROFILE_ROOT' : _ProfilePath ,
            }
        #
        #
        #
        # TODO : look for all and replace with GetPath
        #    os.getcwd()
        #    userdata
        #    config
        
        
        # Setting manager will be used to load settings, both for app and plugin.
        self.Settings = SettingsManager(self, configpath=self.Paths['CONFIG'], pluginpath=self.Paths['PLUGIN'])
        self.RessourcesProvider = RessourcesProvider(self.GetPath('RES'), theme="default_style")
        
        
        
        
        
        
        icon = wx.EmptyIcon()
        #icon.CopyFromBitmap(wx.Bitmap( u"res/default_style/normal/ravencoin.png", wx.BITMAP_TYPE_ANY ))
        icon.CopyFromBitmap(self.RessourcesProvider.GetImage('wx_raven_64'))
        self.SetIcon(icon)
        self.RessourcesProvider.ApplyThemeOnPanel(self)
        
        
        
        
        
        
        
        # Managing views
        self.Views = ViewsManager(self, self.Settings.forceinprincipalauimanager)
        
        # Simple class to handle multiple RPC connexions
        self.ConnexionManager  =  RvnRPC_ConnectorManager(self)
        
        # Homemade work in progress API which intend to be END USER 
        # any basic data that requires multiple RPC call could finish in this
        self.RavencoinRPC  = RavenpyRPC(self.ConnexionManager.getCurrentConnexion(), userdataPath=self.Paths['USERDATA'])
        
        
        # Tools and menu management
        self.MenusAndTool = MenuAndToolBarManager(self)

        
        
        #Job Manager
        self.JobManager = JobManager(self)
        self.JobManager.StartJobManager()
        
        
        
        # Plugins management
        self.Plugins = pluginsManager(self.GetPath('PLUGIN'), self, loadPath=False)
        self.Plugins.SetSwConfiguration()
        self.Plugins.SetExclusionList()
           
        self.Plugins.Initialize()
        
        
        #self.demoBook()
        
        
        self.JobManager.RefreshSettings()
        
        #self.MenusAndTool.refreshViewsListMenu()
        #UserAdvancedMessage(self, str(self.Settings.resumeviewonstartup), 'info')

        self.PerspectiveManager = perspectiveManager(self, self.GetPath('CONFIG'), loadLastView=self.Settings.resumeviewonstartup)  
        
        
        
        
        #self.wxRavenMainBook.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)

        

        
        
        self.Log("wxRaven is ready !" )
        last_network = self.GetPluginSetting("General", 'last_network')
        self.ConnexionManager.setCurrentConnexion(last_network)
        self.initDialogOptions()
        
        
        #self._isReady = True
        
        
        #
        # Environement Variable for the Shells
        #
        #self.GetPlugin("RavenRPC").addLocalVarInShell(  self.Plugins.plugins, "Plugins")
        #self.GetPlugin("RavenRPC").addLocalVarInShell(  self.Views, "Views")
        self.addLocalVarInShell(  self, "wxRaven")
        #
        
        '''
        self.GetPlugin("RavenRPC").addLocalVarInShell(  self.ConnexionManager._wxRavenws, "wxRavenWebService")
        '''
        
        try:
            if self.GetPluginSetting('General', 'show_welcome'):
                self.logger.info(f'Welcome ON')
                self.Views.OpenView("Welcome", pluginname='', createIfNull=True)
            else:
                self.logger.info(f'Welcome OFF')
        
        except Exception as e:
            self.logger.info(f'Error Welcome : {e}')
        
        
        #
        # No wallet rpc webservice
        #
        #_wxRavenws = wxRaven_RPC_WebserviceClient()
        #self.GetPlugin("RavenRPC").addLocalVarInShell(  _wxRavenws, "_wxRavenws")
        #self.ConnexionManager.rpc_connectors['WEBSERVICE-MODE'] = _wxRavenws
        
        
        #self.wxRavenToolBook3.SetArtProvider(wx.aui.AuiSimpleTabArt())
       
        #splash.Close()
        '''
        if self.GetPluginSetting('General', 'show_disclaimer'):
            disclaimer = wxRavenDisclaimerDialogLogic(self)
            disclaimer.ShowModal()
        
        '''
         
        
    def makeColorPanel(self, color):
        p = wx.Panel(self, -1)
        win = wx.Panel()
        p.win = win
        def OnCPSize(evt, win=win):
            win.SetPosition((0,0))
            win.SetSize(evt.GetSize())
        p.Bind(wx.EVT_SIZE, OnCPSize)
        return p
        
        

    def SetReady(self,readyValue=True):
        self._isReady = readyValue
    
    
    #
    #Main App LOGS save management
    #
    
    
    def NewJob(self, job):
        self.JobManager.SubmitNewJob(job)
    
    def SetLogging(self, log=False, debug=False):
        self.logger.info(f'SetLogging L={log} D={debug}')
        if self.mainApp != None:
            _currentState = self.mainApp.logEnable
            
            if not _currentState and ( log or debug ):
                self.mainApp.setup_logging(self.GetPath('PROFILE_ROOT'), debug) 
            else:
                self.logger.info(f'logger already logging')
    
    
            if _currentState and  not log :
                self.mainApp.stop_logging()
                                   
    
        else:
            self.logger.error(f'no mainApp data')
    
    """
    
    RPC Stuff, maybe to remove later but it provide quck access to commands from childs
    
    """

    def RegisterOnConnexionChanged(self, callback):
        return self.ConnexionManager.RegisterOnConnexionChanged(callback)
    
    def UnregisterOnConnexionChanged(self, callback):
        return self.ConnexionManager.UnregisterOnConnexionChanged(callback)
    
    
    def GetPath(self, pathname):
        _res = self.Paths['ROOT']
        
        if self.Paths.__contains__(pathname):
            _res = self.Paths[pathname]
        return _res
    
    
    
    def GetPlugin(self, pname, loadIfNone = False):
        return self.Plugins.GetPlugin(pname, loadIfNone)
    
    def GetPluginData(self, pname, varname):
        p = self.Plugins.GetPlugin(pname, loadIfNone=False)
        if p != None:
            return p.getData(varname)
        
    def GetPluginSetting(self, pname, varname):
        p = self.Plugins.GetPlugin(pname, loadIfNone=False)
        if p != None:
            
            if p.PLUGIN_SETTINGS.__contains__(varname):
                return p.PLUGIN_SETTINGS[varname]
    
    
    def Log(self ,message , source="", timestamp=None, type="msg"):
        
        
        
        self.logger.info("APPLICATION BUILT-IN LOG :" + message)
        
        
        
        #self.GetPlugin("General").Log(message , source, timestamp, type)
        try:
            self.GetPlugin("General").Log(message , source, timestamp, type)
        except Exception as e:
            self.logger.error("APPLICATION BUILT-IN LOG : Log (wxRavenApp) :" + str(e))
    
    
    
    
    def ThreadedRequest(self, requestCallback, postCallback ):
        pass
    
        
    """    
    def Debug(self ,message ):
        try:
            self.GetPlugin("General").Log(message , "", None, "debug")
        except Exception as e:
            self.logger.info("Log (wxRavenApp) :" + str(e))
    
    """
    
    def addLocalVarInShell(self,_var, _name):
        if self.GetPlugin("RavenRPC")!=None:
            self.GetPlugin("RavenRPC").addLocalVarInShell(  _var, _name)
        else:
            self.Log('Plugin RavenRPC not detected, unable to add variable environment in shell', type='warning')
            self.logger.error("APPLICATION BUILT-IN LOG : Raven-RPC Plugin missing.")            
    
    #Get the highlevel queries
    def getRvnRPC(self, networkName=None):
        if networkName != None:
            self.RavencoinRPC  = RavenpyRPC(self.ConnexionManager.getConnexion(networkName), userdataPath=self.Paths['USERDATA'])
        else:
            self.RavencoinRPC  = RavenpyRPC(self.ConnexionManager.getCurrentConnexion(), userdataPath=self.Paths['USERDATA'])
            
            
        return self.RavencoinRPC  
    
    
    def setNetwork(self, networkName):  
        return self.ConnexionManager.setCurrentConnexion(networkName)
    
    #Get the rpc wrapper
    def getNetwork(self, networkName=None):  
        if  networkName == None:
            return self.ConnexionManager.getCurrentConnexion()
        else:
            return self.ConnexionManager.getConnexion(networkName)
    
    
    
    def isCurrentNetworkActive(self):
        return self.ConnexionManager.net_active
    
    
    
    
    
    
    """
    def OnConnexionChanged_T(self, networkName=""):    
        t=threading.Thread(target=self.OnConnexionChanged)
        t.start()    
    """
    
        
    def OnConnexionChanged(self, connexionName=""):
        if connexionName == '':
            connexionName= self.ConnexionManager.getCurrent()
        #wx.MessageBox("You selected the network '%s'" % connexionName)    
        
        _typeMessage = 'info'
        _Message = f"Network Changed for {connexionName}"
        _MessageDetails = ''
        _showCancel = False
        
        
        if connexionName == 'NO WALLET MODE' or connexionName == 'OFFLINE-MODE' or connexionName.__contains__('Relay'):
            _typeMessage = 'warning'
            _Message = f"Network Changed for {connexionName}.\nWarning : This connexion only provide limited features through a Third-Part server/service."
        else:
            
            if self.ConnexionManager.CheckConnexionStatus(connexionName):
                _typeMessage = 'success'
            
            
        if not self.ConnexionManager.CheckConnexionStatus(connexionName):
            _typeMessage = 'error'
            _Message = f"Connexion {connexionName} is not responding."
            
        UserAdvancedMessage(self,_Message, _typeMessage, _MessageDetails, _showCancel)
    
    
    def OnNewView(self, event):
        self.Views.ShowAddViewDialog()
    
    
    
    def OnPreferenceDialog(self, event):
        self.Settings.ShowSettingsDialog()
    
    
    """
    
    DEMO Purpose
    
    """

    def demoBook(self):
        icon = self.RessourcesProvider.GetImage('ravencoin') #wx.Bitmap( u"res/default_style/normal/mainnet-mini.png", wx.BITMAP_TYPE_ANY )
        for num in range(1, 5):
            page = wx.TextCtrl(self, -1, "This is page %d" % num ,
                               style=wx.TE_MULTILINE)
            self.wxRavenMainBook.AddPage(page, "Tab Number %d" % num, bitmap=icon)
            
        
    
    
    """
    
    GUI Functions to add, remove, update and resize graphics, also used from plugins
    
    """
        
    def Add(self, obj, nameFrame, position="mgr", icon=None):
        self.logger.info("Add()->"+position)
        self.Views.Add(obj, nameFrame, position, icon)
     
    
    def OnSize(self, event):

        self.Refresh()
        event.Skip() 
        
        
        
        
        
    """
    
    Default GUI Overwrite and customizations
    
    """
    
    
    def initDialogOptions(self):
        self.ConnexionManager.RegisterOnConnexionChanged(self.OnConnexionChanged)
        self.Layout()
        
    
    
    
 
    def ForceClose(self):    
        busy = wx.BusyInfo("One moment please, saving datas...")
        self.Plugins.CloseAllPlugin()
        self.Destroy()
        del busy
    
    
    
    def CloseSound(self):
        if hasattr(sys, 'getwindowsversion') : 
            _currentPath = os.getcwd()
            _intropath = _currentPath + f'/res/default_style/sounds/close.wav'
            try:
                #playsound(_intropath)
                intro = wx.adv.Sound(_intropath)
                intro.Play(wx.adv.SOUND_ASYNC)
            except Exception as e:
                pass
            
            
            
    def OnClose(self, event):
        self._Closing = True
        
        x = threading.Thread(target=self.CloseSound, daemon=True)
        x.start()
        
        
        busy = wx.BusyInfo("One moment please, saving datas...")
        
        
        self.JobManager.StopJobManager()
        
        self.ConnexionManager.SaveCurrentConnexion()
        self.Settings.SaveSettingsToFile()
        
        
        #self.logger.info( str(self.wxRavenMenuBar_Window_Perspectives.IsChecked(self.wxRavenMenuBar_Window_Perspectives_SaveOnClose.GetId())) )
        if self.wxRavenMenuBar_Window_Perspectives.IsChecked(self.wxRavenMenuBar_Window_Perspectives_SaveOnClose.GetId()):
            
            self.PerspectiveManager.SaveLastPerspective()
            self.Plugins.SaveAllPluginState()
            #self.logger.info( str(self.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.IsCheck()) )
            
        
        
        self.Plugins.CloseAllPlugin()
        self.Destroy()
        
        print(threading.enumerate())
        
        _allClosed = False
        _maxTime = 10
        _t = 0
        while not _allClosed:
            _t = _t+1
            _activeThreads = threading.enumerate()
            if len(_activeThreads) > 1:
                _allClosed = False
                print(f"[{_t}/{_maxTime}] Waiting for active thread : {_activeThreads}")
            else:
                _allClosed = True
            
            if not _allClosed   : 
                time.sleep(1)
            if _t >= _maxTime :
                print(f"[{_t}/{_maxTime}] Wait timeout.")
                break
        
        
        del busy
        self.mainApp.app.ExitMainLoop()
        
        #wx.GetApp().ExitMainLoop()
        
        
        #raise SystemExit
        #self.m_mgr.AddPane( wxRavenMainShellFrame(self).getShell() , aui.AuiPaneInfo() .Name( u"dsfsdf" ).Left() .Caption( u"SHEEEL" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 42,59 ) ).Layer( 1 ) )
        
        
        #she = wxRavenMainShellFrame(self.m_panel7)
        
        #self.m_mgr.AddPane( she.getShell(), aui.AuiPaneInfo() .Left() .Caption( u"RVN RPC Shell" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).MinSize( wx.Size( 500,500 ) ).CentrePane() )
        
        