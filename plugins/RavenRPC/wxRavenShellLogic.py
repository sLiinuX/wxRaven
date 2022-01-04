'''
Created on 13 déc. 2021

@author: slinux
'''

import wx.aui
#from wxRavenGUI.view import wxRavenDesign
from .wxRavenShellDesign import *
import wx.py as py
import threading
import time

class shellMainPanel(wxRavenShellPanel):
    '''
    classdocs
    '''
    view_base_name = "RavenRPC Shell"
    view_name = "RavenRPC Shell"
    parent_frame = None
    default_position = "toolbox1"
    
    
    icon = 'shell' #wx.Bitmap( u"res/default_style/normal/shell.png", wx.BITMAP_TYPE_ANY )
    

    def __init__(self, parentFrame, position = "toolbox1", viewName= "Shell"):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        #parentFrame.m_mgr.AddPane( self, wx.aui.AuiPaneInfo() .Left() .Caption( u"wxRavenFrame" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
        
        """
        parentFrame.m_mgr.AddPane( self, wx.aui.AuiPaneInfo() .Bottom() .Caption( u"> Shell" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
        parentFrame.m_mgr.Update()
        parentFrame.Centre( wx.BOTH )
        """
        self.view_base_name = "Shell"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        
        self.simpleShell()
        
        parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
        #parentFrame.AddInMainFrame(self, "Shell" )
        #parentFrame.AddInNotebook(self, "Shell",parentFrame.wxRavenMainBook )
        #parentFrame.AddInNotebook(self, "Shell",parentFrame.wxRavenToolBook1 , self.icon)

        #parentFrame.AddInNotebook(self, "Shell",parentFrame.wxRavenToolBook2 )
        #self.refreshMenuItemList()
        #self.Bind(wx.EVT_MENU, self.wxRavenShellPanelOnContextMenu, self.rpcConnexions_dropdown_button)
        
    def UpdateView(self):
        pass
    
    
    
    

    
    
    
    
    
    
    def simpleShell(self):
        
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
          
        _locals = {"dev": "this is a test"} 
        _networkName = self.parent_frame.ConnexionManager.getCurrent()
        #_icon = self.parent_frame.GetPluginData("RavenRPC", "_icon")

        
        
        startupText = """PyRPC Basic Shell for wxRaven - Active Network : %NETWORKNAME%
        
 - rpc([OptionalName]).<command>()        RPC Raw Commands
 - api([OptionalName]).<command>()        Ravencoin API Commands

"""
        
        startupText = startupText.replace("%NETWORKNAME%", _networkName)
        
        _locals['rpc']  = self.parent_frame.getNetwork
        _locals['api']  = self.parent_frame.getRvnRPC
        
        _locals['wxRaven']  = self.parent_frame
        
        try:
            _addinLocals = self.parent_frame.GetPlugin("RavenRPC").getAddinsLocals()
            startupText = startupText + "- All additionals : ["
            for _loc in _addinLocals:
                _locals[_loc]  = _addinLocals[_loc]
                startupText = startupText+ " "+ _loc + ", "
            startupText = startupText + "]\n"    
        except Exception as e:
            
            print(str(e))
            pass
        #advShell = py.crust.Crust(self , intro=startupText , locals = _locals)
        
        
        
        self.wxRavenShell = py.shell.Shell(self ,-1, introText=startupText, locals = _locals)
        bSizer1.Add( self.wxRavenShell, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
    


    

class shellAdvancedPanel(wxRavenAdvancedShellPanel):
    '''
    classdocs
    '''
    view_base_name = "RavenRPC Advanced Shell"
    view_name = "RavenRPC Advanced Shell"
    default_position = "toolbox1"
    
    
    icon = 'shell' # wx.Bitmap( u"res/default_style/normal/shell.png", wx.BITMAP_TYPE_ANY )
    
    
    
    
    _autowsitchNetwork = False
    

    def __init__(self, parentFrame, position = "toolbox1", viewName= "Shell"):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        #parentFrame.m_mgr.AddPane( self, wx.aui.AuiPaneInfo() .Left() .Caption( u"wxRavenFrame" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
        
        """
        parentFrame.m_mgr.AddPane( self, wx.aui.AuiPaneInfo() .Bottom() .Caption( u"> Shell" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
        parentFrame.m_mgr.Update()
        parentFrame.Centre( wx.BOTH )
        """
        self.view_base_name = "Shell"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        
        
        
        self._autowsitchNetwork=False
        self._currentLocalNetworkName= self.parent_frame.ConnexionManager.getCurrent()
        self._currentLocalNetworkIcon=  self.parent_frame.ConnexionManager.getIcon()
        
        self.helpCommandPannel = None
        
        parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))        
        
        #self.defaultShell()
        self.waitApplicationReady()
        
        
        
        #Replaced by the main plugin data management
        #self.parent_frame.ConnexionManager.RegisterOnConnexionChanged(self.setStatusBarActiveNetwork)
        
        
    
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.defaultShell,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ())
    
    
    
    
    
    def defaultShell(self, evt=None):
        
        
         
        
        
        _locals = {"dev": "this is a test"}
        _icon = self.icon
        _networkName = ""
        
        if self.getAutoSwitchStateIsChecked() :
            
            _networkName = self.parent_frame.GetPluginData("RavenRPC", "current_connexion")
            _icon = self.parent_frame.GetPluginData("RavenRPC", "_icon")
            #_locals['network']  = self.parent_frame.getNetwork(_networkName)
        else:
            _networkName = self._currentLocalNetworkName
            _icon = self._currentLocalNetworkIcon
        
        
        
        startupText = """PyRPC Advanced Shell for wxRaven - Active Network : %NETWORKNAME%
        
 - network.<command>()         execute RPC Raw Commands
 - ravencoin.<command>()         execute Ravencoin API Commands
         
 - rpc([OptionalName]).<command>()         RPC Raw Commands
 - api([OptionalName]).<command>()         Ravencoin API Commands
         
        """
        
 
        
        startupText = startupText.replace("%NETWORKNAME%", _networkName)
        
        _locals['network']  = self.parent_frame.getNetwork(_networkName)
        _locals['ravencoin']  = self.parent_frame.getRvnRPC(_networkName)
        
        _locals['rpc']  = self.parent_frame.getNetwork
        _locals['api']  = self.parent_frame.getRvnRPC
        
        _locals['wxRaven']  = self.parent_frame
        
        
        try:
            _addinLocals = self.parent_frame.GetPlugin("RavenRPC").getAddinsLocals()
            startupText = startupText + "- All additionals from plugins : ["
            for _loc in _addinLocals:
                _locals[_loc]  = _addinLocals[_loc]
                startupText = startupText+ " "+ _loc + ", "
            startupText = startupText + "]\n" 
            
        except Exception as e:
            print(str(e))
            
            
        
        advShell = py.crust.Crust(self , intro=startupText , locals = _locals)
        #advShell = py.crust.CrustFrame(self ,  locals = _locals)
        #advShell.ToggleTools()
        _titlePage = "PyRPC Shell (" + _networkName + ")"
        
        
        #self.wxRavenShell = py.shell.Shell(self ,-1, introText=startupText)   
        self.wxRavenAdvancedShellPanelNotebook.AddPage(advShell, _titlePage, bitmap = _icon)
    
    
    
    def OnContextMenu_ShowNetworkList(self, evt):
        self.refreshNetworkMenuItemList()
        self.showNetworkListMenu()
    
 
    def showNetworkListMenu(self):
        mposx, mposy = wx.GetMousePosition()
        cposx, cposy = self.parent_frame.ScreenToClient((mposx, mposy))
        self.parent_frame.PopupMenu( self.rpcConnexions_dropdown_menu, self.parent_frame.ScreenToClient((mposx, mposy)) )
    
    
    
    
    def cleanNetworkList(self):
        for i in self.rpcConnexions_dropdown_menu.GetMenuItems():
            self.rpcConnexions_dropdown_menu.Delete(i)
    
    def refreshNetworkMenuItemList(self):
        
        if self.rpcConnexions_dropdown_menu.GetMenuItemCount() > 0:
            self.cleanNetworkList()
        
        
        try:
            
            for text in self.parent_frame.GetPluginData("RavenRPC","all_connexion") :
                    item = self.rpcConnexions_dropdown_menu.AppendRadioItem(-1, text)
                    
                    
                    if self.getAutoSwitchStateIsChecked() :
                        if text == self.parent_frame.GetPluginData("RavenRPC","current_connexion"):
                            item.Check(True) 
                    else:
                        if text == self._currentLocalNetworkName:
                            item.Check(True) 
                    
                    
                    self.parent_frame.Bind(wx.EVT_MENU, self.OnPopupNetworkItemSelected, item)        
        
        
        except Exception as e:
            self.parent_frame.Log("Unable to load the network list" , type="warning")
            #print("refreshNetworkMenuItemList() " + str(e))  
            pass
        #if self.getAutoSwitchStateIsChecked() :
 
        #else:
            
    
    
    
    def OnPopupNetworkItemSelected(self, event):
        item = self.rpcConnexions_dropdown_menu.FindItemById(event.GetId())
        text = item.GetItemLabelText()
        
        
        
        #print(self.rpcConnexions_autoswitch.GetState())
        if self.getAutoSwitchStateIsChecked() :
            self.parent_frame.ConnexionManager.setCurrentConnexion(text)
        else:    
            self._currentLocalNetworkName = text
            self._currentLocalNetworkIcon= self.parent_frame.ConnexionManager.getIcon(self._currentLocalNetworkName)
            self.setStatusBarActiveNetwork()
            #Todo = change local icon !
    
    
    
    def UpdateView(self):
        self.setStatusBarActiveNetwork("")
        self.refreshNetworkMenuItemList()
        
        
    
    def setStatusBarActiveNetwork(self, networkName=''):
        
        
        #if autottogle we read plugin data, else local panel
        if self.getAutoSwitchStateIsChecked() :
            
            #networkName= self.parent_frame.ConnexionManager.getCurrent()
            networkName = self.parent_frame.GetPluginData("RavenRPC", "current_connexion")
            #icon = self.parent_frame.ConnexionManager.getIcon(networkName)
            icon = self.parent_frame.GetPluginData("RavenRPC", "_icon")
            self.rpcConnexions_dropdown_button.SetBitmap(icon)
        
        else:
            #networkName = self._currentLocalNetworkName
            #icon = self.ConnexionManager.getIcon(networkName)
            self.rpcConnexions_dropdown_button.SetBitmap(self._currentLocalNetworkIcon)


        self.Layout()
    
    def OnAutoswitchChanged(self, event):
        
        #print("swtichedauto " + str(self.getAutoSwitchStateIsChecked()))
        self.setStatusBarActiveNetwork("")
        self._autowsitchNetwork = self.getAutoSwitchStateIsChecked()
        
        
    def getAutoSwitchStateIsChecked(self):
        res=False
        if self.rpcConnexions_autoswitch.GetState() in [32 ,34 ] :
            res=True
        return res
    
    def OnNewTerminal(self, event):
        self.defaultShell()
    
    def OnCloseTerminal(self, event):
        cp = self.wxRavenAdvancedShellPanelNotebook.GetCurrentPage()
        cpi = self.wxRavenAdvancedShellPanelNotebook.GetPageIndex(cp)
        
        self.wxRavenAdvancedShellPanelNotebook.DeletePage(cpi)
    
    
    
    def OnRPCHelp(self, event):
        
        
        if self.helpCommandPannel == None:
            
            #print("None")
            
            newHelpPanel = ShellDocumentationHelper(self.parent_frame, position="wxRavenAdvancedShellPanelNotebook")
            #self.wxRavenAdvancedShellPanelNotebook.AddPage(newHelpPanel, "RPC Command List", bitmap = newHelpPanel.icon)
            _panIcon =  self.parent_frame.RessourcesProvider.GetImage(newHelpPanel.icon)
            
            self.wxRavenAdvancedShellPanelNotebook.AddPage(newHelpPanel, "RPC Command List", bitmap = _panIcon)
            
           
            
            self.helpCommandPannel = newHelpPanel
            #self.helpCommandPannel.FillHelpDocumentationTreebook()
        else:
            #self.helpCommandPannel.FillHelpDocumentationTreebook()
            print("already")
            pass



class ShellDocumentationHelper(wxRavenShellDocumentation):
    '''
    classdocs
    '''
    view_base_name = "RPC Documentation Helper"
    view_name = "RPC Documentation Helper"
    default_position = "main"
    
    
    icon = 'bookmarks_view' #wx.Bitmap( u"res/default_style/normal/bookmarks_view.png", wx.BITMAP_TYPE_ANY )
    
    

    def __init__(self, parentFrame, position = "main", viewName= "RPC Documentation Helper"):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        #parentFrame.m_mgr.AddPane( self, wx.aui.AuiPaneInfo() .Left() .Caption( u"wxRavenFrame" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
        
        """
        parentFrame.m_mgr.AddPane( self, wx.aui.AuiPaneInfo() .Bottom() .Caption( u"> Shell" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
        parentFrame.m_mgr.Update()
        parentFrame.Centre( wx.BOTH )
        """
        self.view_base_name = "RPC Documentation Helper"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        
        self._cursor = 0
        
        #self.helpCommandPannel.FillHelpDocumentationTreebook()
        
        #parentFrame.Add(self, self.view_name ,position, self.icon)  
        
        if position != "wxRavenAdvancedShellPanelNotebook":
            parentFrame.Add(self, self.view_name ,position, self.parent_frame.RessourcesProvider.GetImage(self.icon))
        
        self.SetupTreebook() 
        self.FillHelpDocumentationTreebook()
        
        self.Show()
    
    """
    def LoadHelpDocumentation_T(self, networkName=""):    
        t=threading.Thread(target=self.LoadHelpDocumentation)
        t.start()
    
    def LoadHelpDocumentation(self):
        pass    
    """
    
    def OnSearch(self, evt):
        self.FillHelpDocumentationTreebook()
        #self.search.GetValue()
    
    
    def SetupTreebook(self):
        self.il = wx.ImageList(16, 16)
        self.defaultIcon = self.il.Add(self.parent_frame.RessourcesProvider.GetImage(self.icon))
        self.m_customControl2.AssignImageList(self.il)
    
    
    def UpdateView(self):
        pass
    
    def CleanTree(self):
        while self._cursor>0:
            #print(self._cursor)
            self.m_customControl2.DeletePage(self._cursor-1)
            self._cursor = self._cursor-1
    
    def FillHelpDocumentationTreebook(self):
        
        
        #
        # To put a trry and retry
        #
        
        self.m_customControl2.Freeze()
        #self.m_customControl2.Thaw()
        self.CleanTree()
        self._cursor = 0
        
        
        filterSearch = self.m_searchCtrl1.GetValue()
        
        if len(filterSearch) < 2 :
            filterSearch=""
        
        #print(filterSearch)
        try:
            #self.GetPlugin("General").Log(message , source, timestamp, type)
            _CmdList= self.parent_frame.GetPluginData("RavenRPC","_CmdList")
            
            #print("Fill")
            
            for _cmd in _CmdList:
                
                #print(_cmd)
                
                
                if filterSearch != "" and not _cmd.__contains__(filterSearch):
                    continue
                
                _commandeHelperPanel = ShellCommandDescriberPanel(self.m_customControl2, _CmdList[_cmd])
                self.m_customControl2.AddPage(_commandeHelperPanel, _cmd, imageId=self.defaultIcon)
                
                self._cursor = self._cursor +1
        
        except Exception as e:
            #print("FillHelpDocumentationTreebook  :" + str(e))
            self.parent_frame.Log("Unable to load the commands list" , type="warning")
        
        self.m_customControl2.Thaw()
        self.Layout()



class ShellCommandDescriberPanel(wxRavenShellCommandDescriber):
    
    def __init__(self, parent, desc):
        wxRavenShellCommandDescriber.__init__(self, parent)
        self.cmdHelper.SetValue(desc)

