'''
Created on 10 déc. 2021

@author: slinux
'''
import wx
import wx.aui
import os.path
from wx import *
import threading


from libs.RVNpyRPC import *
from wxRavenGUI.view import *
from wxRavenGUI.application.core import *
from wxRavenGUI.application.core.wxRessourcesProvider import RessourcesProvider


ROOT_PATH = os.getcwd()
RES_PATH = os.getcwd() + "/res/"
CONFIG_PATH = os.getcwd() + "/config/"
PLUGIN_PATH = os.getcwd() + "/plugins/"
USERDATA_PATH = os.getcwd() + "/userdata/"





class wxRavenAppMainFrame(wxRavenMainFrame):
    
    
    
    wxRavenStatusBarIcon = None
    wxRavenNetworkBarIcon = None
    
    
    
    Logs = None
    
    Settings = None
    Views = None
    Plugins = None
    
    ConnexionManager = None
    RavencoinRPC = None
    
    PerspectiveManager = None
    MenusAndTool = None
    
    Ressources = None
    Paths = {}
    
    def __init__(self):
        
        self.logger = logging.getLogger('wxRaven')
        
        
        wxRavenMainFrame.__init__(self,None)
        self._isReady = False
        
        #splash.Show()
        
        self.Paths = {'ROOT':os.getcwd(),
                      'RES' : os.getcwd() + "/res/",
                      'CONFIG' : os.getcwd() + "/config/",
                      'PLUGIN' : os.getcwd() + "/plugins/",
                      'USERDATA' : os.getcwd() + "/userdata/",
            }
        
        
        
        # Setting manager will be used to load settings, both for app and plugin.
        self.Settings = SettingsManager(self)
        self.RessourcesProvider = RessourcesProvider(RES_PATH, theme="default_style")
        
        
        
        icon = wx.EmptyIcon()
        #icon.CopyFromBitmap(wx.Bitmap( u"res/default_style/normal/ravencoin.png", wx.BITMAP_TYPE_ANY ))
        icon.CopyFromBitmap(self.RessourcesProvider.GetImage('ravencoin'))
        self.SetIcon(icon)
        self.RessourcesProvider.ApplyThemeOnPanel(self)
        
        
        
        
        
        
        
        # Managing views
        self.Views = ViewsManager(self, self.Settings.forceinprincipalauimanager)
        
        # Simple class to handle multiple RPC connexions
        self.ConnexionManager  =  RvnRPC_ConnectorManager(self)
        
        # Homemade work in progress API which intend to be END USER 
        # any basic data that requires multiple RPC call could finish in this
        self.RavencoinRPC  = RavenpyRPC(self.ConnexionManager.getCurrentConnexion())
        
        
        # Tools and menu management
        self.MenusAndTool = MenuAndToolBarManager(self)

        
        # Plugins management
        self.Plugins = pluginsManager(PLUGIN_PATH, self, loadPath=False)
        self.Plugins.SetExclusionList()
           
        self.Plugins.Initialize()
        
        
        #self.demoBook()
        
        
        
        #self.MenusAndTool.refreshViewsListMenu()
        

        self.PerspectiveManager = perspectiveManager(self, CONFIG_PATH, loadLastView=self.Settings.resumeviewonstartup)  
        
        
        
        
        #self.wxRavenMainBook.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)

        

        
        
        self.Log("wxRaven is ready !" )
        last_network = self.GetPluginSetting("General", 'last_network')
        self.ConnexionManager.setCurrentConnexion(last_network)
        self.initDialogOptions()
        
        
        self._isReady = True
        #
        # Environement Variable for the Shells
        #
        #self.GetPlugin("RavenRPC").addLocalVarInShell(  self.Plugins.plugins, "Plugins")
        #self.GetPlugin("RavenRPC").addLocalVarInShell(  self.Views, "Views")
        self.GetPlugin("RavenRPC").addLocalVarInShell(  self, "wxRaven")
        
        
        self.Views.OpenView("Welcome", pluginname='', createIfNull=True)
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
            _res = self.Paths['ROOT']
    
    
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
    
    """    
    def Debug(self ,message ):
        try:
            self.GetPlugin("General").Log(message , "", None, "debug")
        except Exception as e:
            self.logger.info("Log (wxRavenApp) :" + str(e))
    
    """
    
    
    
    #Get the highlevel queries
    def getRvnRPC(self, networkName=None):
        if networkName != None:
            self.RavencoinRPC  = RavenpyRPC(self.ConnexionManager.getConnexion(networkName))
        else:
            self.RavencoinRPC  = RavenpyRPC(self.ConnexionManager.getCurrentConnexion())
            
            
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
        wx.MessageBox("You selected the network '%s'" % connexionName)    
    
    
    
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
        
    def OnClose(self, event):
        
        
        busy = wx.BusyInfo("One moment please, saving datas...")
        
        self.ConnexionManager.SaveCurrentConnexion()
        self.Settings.SaveSettingsToFile()
        
        
        #self.logger.info( str(self.wxRavenMenuBar_Window_Perspectives.IsChecked(self.wxRavenMenuBar_Window_Perspectives_SaveOnClose.GetId())) )
        if self.wxRavenMenuBar_Window_Perspectives.IsChecked(self.wxRavenMenuBar_Window_Perspectives_SaveOnClose.GetId()):
            
            self.PerspectiveManager.SaveLastPerspective()
            self.Plugins.SaveAllPluginState()
            #self.logger.info( str(self.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.IsCheck()) )
            
        
        
        self.Plugins.CloseAllPlugin()
        
        self.Destroy()
        
        del busy
        
        #wx.GetApp().ExitMainLoop()
        
        
        #raise SystemExit
        #self.m_mgr.AddPane( wxRavenMainShellFrame(self).getShell() , aui.AuiPaneInfo() .Name( u"dsfsdf" ).Left() .Caption( u"SHEEEL" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 42,59 ) ).Layer( 1 ) )
        
        
        #she = wxRavenMainShellFrame(self.m_panel7)
        
        #self.m_mgr.AddPane( she.getShell(), aui.AuiPaneInfo() .Left() .Caption( u"RVN RPC Shell" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).MinSize( wx.Size( 500,500 ) ).CentrePane() )
        
        