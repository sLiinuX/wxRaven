'''
Created on 10 déc. 2021

@author: slinux
'''
import wx
import wx.aui
import os.path
from wx import *
import threading


#from wxRavenGUI.application import *
from libs.RVNpyRPC import *
from wxRavenGUI.application.core.rpcConnectorManager import *


from wxRavenGUI.view import *
from wxRavenGUI.application.wxcomponents import *

"""
from wxRavenGUI.application.wxPluginsManager import *
from wxRavenGUI.application.wxcomponents.wxPerspectiveManager import *
from wxRavenGUI.application.wxcomponents.wxViewsManager import *
from wxRavenGUI.application.wxcomponents.wxSettingsManager import *
from wxRavenGUI.application.wxcomponents.wxMenuAndToolbar import *
"""

CONFIG_PATH = os.getcwd() + "/config/"
PLUGIN_PATH = os.getcwd() + "/plugins/"






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
    
    
    def __init__(self):
        
        
        wxRavenMainFrame.__init__(self,None)
        
        
        #splash.Show()
        
        
        
        
        
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap( u"res/default_style/normal/mainnet-mini.png", wx.BITMAP_TYPE_ANY ))
        self.SetIcon(icon)
        
        
        
        
        
        
        self.Settings = SettingsManager(self)
        
        
        
        
        
        self.Views = ViewsManager(self)
        
        self.ConnexionManager  =  RvnRPC_ConnectorManager(self)
        self.RavencoinRPC  = RavenpyRPC(self.ConnexionManager.getCurrentConnexion())
        
        
        
        
        
        
        
        self.MenusAndTool = MenuAndToolBarManager(self)
        
        
        
        self.Plugins = pluginsManager(PLUGIN_PATH, self, loadPath=False)   
        self.Plugins.Initialize()
        
        
        self.demoBook()
        
        
        
        #self.MenusAndTool.refreshViewsListMenu()
        
        
        
        
        
        

        self.PerspectiveManager = perspectiveManager(self, CONFIG_PATH, loadLastView=self.Settings.resumeViewOnStartup)  
        
        
        
        
        #self.wxRavenMainBook.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)

        

        
        
        self.Log("wxRaven is ready !" )
        
        self.ConnexionManager.setCurrentConnexion("testnet_localhost")
        self.initDialogOptions()
        
        
        
        #self.wxRavenToolBook3.SetArtProvider(wx.aui.AuiSimpleTabArt())
       
        #splash.Close()
        
        
        
        
    """    
    def OnPageClose( self, event ):
        objNotebook = event.GetEventObject()
        index = event.GetSelection()
        page = objNotebook.GetPage(index)
        label = objNotebook.GetPageText(index)
        print("view instance to delete !")
        self.Plugins.DeleteViewInstance(label)
        wx.CallAfter(self.MenusAndTool.refreshViewsListMenu, ())
        event.Skip()   
        
    """    
        
        
         
        
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
    
    def NewViewDialog(self):
        
        #print("NewViewDialog")
        nViewDialog = RavenAddViewDialog(self)
        nViewDialog.Show()
    
    def RegisterOnConnexionChanged(self, callback):
        return self.ConnexionManager.RegisterOnConnexionChanged(callback)
    
    def UnregisterOnConnexionChanged(self, callback):
        return self.ConnexionManager.UnregisterOnConnexionChanged(callback)
    
    
    
    def GetPlugin(self, pname, loadIfNone = False):
        return self.Plugins.GetPlugin(pname, loadIfNone)
    
    def GetPluginData(self, pname, varname):
        p = self.Plugins.GetPlugin(pname, loadIfNone=False)
        if p != None:
            return p.getData(varname)
    
    
    def Log(self ,message , source="", timestamp=None, type="msg"):
        
        #print("LOG :" + message)
        #self.GetPlugin("General").Log(message , source, timestamp, type)
        
        try:
            self.GetPlugin("General").Log(message , source, timestamp, type)
        except Exception as e:
            print("Log (wxRavenApp) :" + str(e))
        
    
    
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
        self.NewViewDialog()
    
    """
    
    DEMO Purpose
    
    """

    def demoBook(self):
        icon = wx.Bitmap( u"res/default_style/normal/mainnet-mini.png", wx.BITMAP_TYPE_ANY )
        for num in range(1, 5):
            page = wx.TextCtrl(self, -1, "This is page %d" % num ,
                               style=wx.TE_MULTILINE)
            self.wxRavenMainBook.AddPage(page, "Tab Number %d" % num, bitmap=icon)
            
        
    
    
    """
    
    GUI Functions to add, remove, update and resize graphics, also used from plugins
    
    """
        
    def Add(self, obj, nameFrame, position="mgr", icon=None):
        print("Add()->"+position)
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
        
    
    
    
 
        

        
    def OnClose(self, event):
        
        #print( str(self.wxRavenMenuBar_Window_Perspectives.IsChecked(self.wxRavenMenuBar_Window_Perspectives_SaveOnClose.GetId())) )
        if self.wxRavenMenuBar_Window_Perspectives.IsChecked(self.wxRavenMenuBar_Window_Perspectives_SaveOnClose.GetId()):
            self.PerspectiveManager.SaveLastPerspective()
            self.Plugins.SaveAllPluginState()
            #print( str(self.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.IsCheck()) )
            self.Settings.SaveSettingsToFile()
        
        
        self.Destroy()
        event.Skip() 
        #self.m_mgr.AddPane( wxRavenMainShellFrame(self).getShell() , aui.AuiPaneInfo() .Name( u"dsfsdf" ).Left() .Caption( u"SHEEEL" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.Size( 42,59 ) ).Layer( 1 ) )
        
        
        #she = wxRavenMainShellFrame(self.m_panel7)
        
        #self.m_mgr.AddPane( she.getShell(), aui.AuiPaneInfo() .Left() .Caption( u"RVN RPC Shell" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).MinSize( wx.Size( 500,500 ) ).CentrePane() )
        
        