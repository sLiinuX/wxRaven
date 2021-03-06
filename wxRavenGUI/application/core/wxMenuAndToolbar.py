'''
Created on 13 déc. 2021

@author: slinux
'''
import wx 
import inspect

import threading
import time 
import wx.aui  as aui
import logging

import webbrowser


from wxRavenGUI.view import *
from libs.RVNComunity import __RVN_COMMUNITY_TOPICS_MAPPING__

from wxRavenGUI.application.wxcustom import *


class MenuAndToolBarManager(object):
    '''
    classdocs
    '''

    parentframe = None
    
    
    
    def __init__(self, parentframe):
        '''
        Constructor
        '''
        self.parentframe = parentframe
        
        self.setupMenuBar()
        self.setupToolBar()
        self.setupStatusBar()
        
        self.logger = logging.getLogger('wxRaven')
        
        self._aboutDialog = None
        
        
        self._pluginsToolbars = {}
        
        
        self.popupIDS = {}
        self.popupMAP = {}
        self.popupCount= 1
    
        self.statusBarErrorPushed = False
    
    
    
        self.waitApplicationReady()
        
    
    
    
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.__PostReadyLoader__,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parentframe._isReady:
            time.sleep(1)
            
        wx.CallAfter(callback, ()) 
    
    
    
    def __PostReadyLoader__(self, evt=None):
        self.logger.info("__PostReadyLoader__")
        self.InitPluginsShortcutToolbars()
        self.refreshPerspectiveListMenu()
        
        self.RefreshLinksListMenu()
        
    
    
    
    def RaiseMenuAndToolLog(self, message, type="error"):
        try:
            _source = str(inspect.stack()[1][0])
            self.parentframe.Log( message, source=str(_source), type=type)
        except Exception as e:
            self.logger.error("RaiseMenuAndToolLog() " + str(e))  
    
    
    
    
        
    """
    
    Status bar
    
    """
    
    
    def PopStatusBarErrorMessage(self, evt=None):
        if self.statusBarErrorPushed :
            print('pop')
            self.parentframe.wxRavenStatusBar.PopStatusText(  0)
            self.statusBarErrorPushed =False
            
            
            if self.parentframe.wxRavenStatusBarLeftIcon != None:
                try:
                    self.parentframe.wxRavenStatusBarLeftIcon.Destroy()
                except Exception as e:
                    pass
    
    def PushStatusBarErrorMessage(self, evt=None):
        
        if not self.statusBarErrorPushed :
            print('push')
            self.parentframe.wxRavenStatusBar.PushStatusText( "--   Some Errors occured, check the console log.", 0)
            self.statusBarErrorPushed =True
            
            if self.parentframe.wxRavenStatusBarLeftIcon != None:
                try:
                    self.parentframe.wxRavenStatusBarLeftIcon.Destroy()
                except Exception as e:
                    pass
            _icon =self.parentframe.RessourcesProvider.GetImage('warning_2')
            self.parentframe.wxRavenStatusBarLeftIcon = wx.StaticBitmap(self.parentframe.wxRavenStatusBar, -1, _icon, (16, 16))
            
            try:
                rect = self.parentframe.wxRavenStatusBar.GetFieldRect(0)
                w, h = self.parentframe.wxRavenStatusBarLeftIcon.Size
                xpad = (rect.width - w) / 2
                ypad = (rect.height - h) / 2
                self.parentframe.wxRavenStatusBarLeftIcon.SetPosition((rect.x, rect.y + ypad))
            except Exception as e:
                pass
            
            
        #self.parentFrame.wxRavenStatusBar.PushStatusText( "Some Errors occured, check the console log.", 1)
    
     
    
    
    
    def setupStatusBar(self):
        self.parentframe.wxRavenStatusBarIcon=None
        self.parentframe.wxRavenStatusBarLeftIcon=None
        
        self.parentframe.wxRavenStatusBar.SetFieldsCount( 3, [-3,250,32])
        self.parentframe.wxRavenStatusBar.SetStatusText("welcome to wxRaven", 0)
        self.parentframe.wxRavenStatusBar.Bind(wx.EVT_SIZE, self.OnSizeSB)
        
        
        
        self.parentframe.ConnexionManager.RegisterOnConnexionChanged(self.setStatusBarActiveNetwork)
    
    
    
    
    
    
    
    
    def OnSizeSB(self, event):
        try:
            rect = self.parentframe.wxRavenStatusBar.GetFieldRect(2)
            w, h = self.parentframe.wxRavenStatusBarIcon.Size
            xpad = (rect.width - w) / 2
            ypad = (rect.height - h) / 2
            self.parentframe.wxRavenStatusBarIcon.SetPosition((rect.x + xpad, rect.y + ypad))
             
        except Exception as e:
            pass
        
        
        try:
            rect = self.parentframe.wxRavenStatusBar.GetFieldRect(0)
            w, h = self.parentframe.wxRavenStatusBarLeftIcon.Size
            xpad = (rect.width - w) / 2
            ypad = (rect.height - h) / 2
            self.parentframe.wxRavenStatusBarLeftIcon.SetPosition((rect.x, rect.y + ypad))
             
        except Exception as e:
            pass
        event.Skip()
    
    
    def __StatusBar_DetroyIcons__(self):
        if self.parentframe.wxRavenStatusBarIcon != None:
            try:
                self.parentframe.wxRavenStatusBarIcon.Destroy()
            except Exception as e:
                pass   
            
         
         
        if self.parentframe.wxRavenStatusBarLeftIcon != None:
            try:
                self.parentframe.wxRavenStatusBarLeftIcon.Destroy()
            except Exception as e:
                pass
    
    def setStatusBarActiveNetwork(self, networkName=""):
        
        if networkName == '':
            networkName= self.parentframe.ConnexionManager.getCurrent()
        
        #_type = 'RPC'
        _type = self.parentframe.ConnexionManager.getConnexionType(networkName)
        
        
        _textBar = f'[{_type}] : {networkName}'
        
        self.parentframe.wxRavenStatusBar.SetStatusText(_textBar, 1)
        
        #self.logger.info("test")
        
        """
        icon = wx.Bitmap( u"res/default_style/normal/mainnet.png", wx.BITMAP_TYPE_ANY )
        if networkName.__contains__("testnet"):
            icon = wx.Bitmap( u"res/default_style/normal/testnet.png", wx.BITMAP_TYPE_ANY )
        """
        
        icon = self.parentframe.ConnexionManager.getIcon(networkName)
        
        self.__StatusBar_DetroyIcons__()
           
        #toolbar as well    
        self.parentframe.wxRavenNetworkBarIcon = icon
        self.parentframe.rpcConnexions_dropdown_button.SetBitmap(icon)
        #self.parentframe.rpcConnexions_dropdown_button.Layout()
        
        
        self.parentframe.wxRavenStatusBarIcon = wx.StaticBitmap(self.parentframe.wxRavenStatusBar, -1, icon, (16, 16))
        
        rect = self.parentframe.wxRavenStatusBar.GetFieldRect(2)
        w, h = self.parentframe.wxRavenStatusBarIcon.Size
        xpad = (rect.width - w) / 2
        ypad = (rect.height - h) / 2
        self.parentframe.wxRavenStatusBarIcon.SetPosition((rect.x + xpad, rect.y + ypad))
        
        
        self.parentframe.m_auiToolBar2.Layout()
        self.parentframe.Layout()
        
    """
    
    Tool bar
    
    """
    
    
    def RefreshToolbar(self, evt=None):
        self.logger.info('RefreshToolbar')
        self.RefreshConsoleToogleButtonState()
        self.RefreshViewShortcutButtonState()
        
        self.parentframe.m_auiToolBar2.Realize()
        self.parentframe.m_auiViewsShortcutToolbar.Realize()
        
        #self.parentframe.Views.UpdateGUIManager()
    
    def OnContextMenu_ShowNetworkList(self, event):
        #self.logger.info("showConnexionList!")
        self.refreshNetworkMenuItemList()
        self.showNetworkListMenu()
        
        
    
    def getToggleConsoleLogStateIsChecked(self):
        res=False
        #self.logger.info(self.parentframe.m_showConsoleLog.GetState())
        if self.parentframe.m_auiToolBar2.GetToolToggled(self.parentframe.m_showConsoleLog.GetId()):
        #if self.parentframe.m_showConsoleLog.GetState() in [32 ,34 ] :
            res=True
        return res    
    
    
    def RefreshViewShortcutButtonState(self, evt=None):
        #_disp = self.parentframe.m_auiToolBar2.GetToolToggled(self.parentframe.m_showViewShortcutToolbar.GetId())
        _pan = self.parentframe.m_mgr.GetPane('ViewsShortcutToolbar')
        _disp = _pan.IsShown()
        if _disp:
            self.parentframe.m_auiToolBar2.ToggleTool(self.parentframe.m_showViewShortcutToolbar.GetId(), True)
        else:
            self.parentframe.m_auiToolBar2.ToggleTool(self.parentframe.m_showViewShortcutToolbar.GetId(), False)
    
    
    
    
    def RefreshConsoleToogleButtonState(self, evt=None):
        vmgr = self.parentframe.Views 
        
        if vmgr.isViewVisible('Error Log Console'):
            #self.parentframe.GetPlugin('General').PopStatusBarErrorMessage()
            self.PopStatusBarErrorMessage()
            #self.logger.info("Error Log Console visible")
            cs = self.parentframe.m_showConsoleLog.GetState()
            #self.parentframe.m_showConsoleLog.SetState(34)
            self.parentframe.m_auiToolBar2.ToggleTool(self.parentframe.m_showConsoleLog.GetId(), True)
            self.parentframe.Views.UpdateView("Error Log Console")
            
            
            
            
        else:
            #self.logger.info("Error Log Console NOT visible")
            #self.parentframe.m_showConsoleLog.SetState(2)
            self.parentframe.m_auiToolBar2.ToggleTool(self.parentframe.m_showConsoleLog.GetId(), False)
            #ts = 34
    
    
    
    def OnToggleConsoleLog(self, event):
        
        self.logger.info('OnToggleConsoleLog')
        if self.getToggleConsoleLogStateIsChecked():
            self.parentframe.Views.OpenView("Error Log Console", "General", True)    
        else:
            self.parentframe.Views.HideView("Error Log Console")
    
    
    
    
    def setupToolBar(self):
        
        #
        #
        #  main Toolbar : connexion, add and switch view 
        #
        #
        
        self.parentframe.Bind( wx.EVT_TOOL, self.OnContextMenu_ShowNetworkList, id = self.parentframe.rpcConnexions_dropdown_button.GetId() )
        self.parentframe.Bind( aui.EVT_AUITOOLBAR_TOOL_DROPDOWN, self.OnContextMenu_ShowNetworkList, id = self.parentframe.rpcConnexions_dropdown_button.GetId() )
        
         
        self.parentframe.RessourcesProvider.ApplyThemeOnPanel(self.parentframe.m_auiToolBar2)
        
        
        self.parentframe.Bind( wx.EVT_TOOL,self.OnToggleConsoleLog ,id = self.parentframe.m_showConsoleLog.GetId()  )
        
        self.PopupViewMenu = wx.Menu()
        self.parentframe.Bind( wx.EVT_TOOL,self.OnShowCurrentOpenViews ,id = self.parentframe.m_ShowOpenViewList.GetId()  )
        self.parentframe.Bind( aui.EVT_AUITOOLBAR_TOOL_DROPDOWN,self.OnShowCurrentOpenViews ,id = self.parentframe.m_ShowOpenViewList.GetId()  )
        
        
        self.parentframe.Bind( wx.EVT_TOOL,self.OnShowNewViewDialog ,id = self.parentframe.m_showNewViewDialog.GetId()  )
        
        self.parentframe.Bind( wx.EVT_TOOL,self.OnToggleViewShortcutToolbar ,id = self.parentframe.m_showViewShortcutToolbar.GetId()  )
        
        #
        #
        #
        # ShortcutToolbar
        #
        #
        #
        #
        
        
        self.parentframe.Bind( wx.EVT_TOOL,self.OnShowAboutDialogClicked ,id = self.parentframe.m_showAboutDialogToolbt.GetId()  )
        self.parentframe.Bind( wx.EVT_TOOL,self.OnShowSettingsDialogClicked ,id = self.parentframe.m_showSettingsDialogToolbt.GetId()  )
        
        
        self._pluginsToolbars = {}
        
        self.PluginsViewsMenuShortcuts = wx.Menu() 
        #self.parentframe.m_auiViewsShortcutToolbar.Bind( wx.EVT_RIGHT_DOWN, self.OnToolbarRightClick)
        self.parentframe.Bind( wx.EVT_TOOL,self.OnToolbarRightClick ,id = self.parentframe.m_showToolbarListToolbt.GetId()  )
        
        #self._pluginsToolbars['Application'] = self.parentframe.m_auiViewsShortcutToolbar
        
        
        
        self.parentframe.m_auiToolBar2.Realize()
        self.parentframe.m_auiViewsShortcutToolbar.Realize()
    
    def OnToggleViewShortcutToolbar(self, evt):
        _disp = self.parentframe.m_auiToolBar2.GetToolToggled(self.parentframe.m_showViewShortcutToolbar.GetId())
        #self.logger.info(_disp)
        
        _pan = self.parentframe.m_mgr.GetPane('ViewsShortcutToolbar')
        
        if _disp:
            _pan.Show()
        else:
            self.parentframe.m_mgr.ClosePane(_pan)
        
        
        
        _settingsShortcut = self.parentframe.GetPluginSetting('General', 'quick_links')    
            
        for _tb in self._pluginsToolbars:
            _pan = self.parentframe.m_mgr.GetPane(f'{_tb}_Toolbar')
            
            if _disp and _settingsShortcut.__contains__(_tb):
                _pan.Show()
                #self.parentframe.m_mgr.MaximizePane(_pan)
            else:
                self.parentframe.m_mgr.ClosePane(_pan)
            
        
        #self.parentframe.Views.UpdateGUIManager()
        self.parentframe.Views.__refreshGUI_Job__()
    
    def OnShowNewViewDialog(self,evt):
        self.parentframe.Views.ShowAddViewDialog()
    
    def OnShowCurrentOpenViews(self, evt):
        mposx, mposy = wx.GetMousePosition()
        cposx, cposy = self.parentframe.ScreenToClient((mposx, mposy))
        self.parentframe.PopupMenu(self.PopupViewMenu, self.parentframe.ScreenToClient((mposx, mposy)) )
    
    
    def OnToolbarRightClick(self, evt):
        mposx, mposy = wx.GetMousePosition()
        cposx, cposy = self.parentframe.ScreenToClient((mposx, mposy))
        self.parentframe.PopupMenu(self.PluginsViewsMenuShortcuts, self.parentframe.ScreenToClient((mposx, mposy)) )
    
    
    def showNetworkListMenu(self):
        mposx, mposy = wx.GetMousePosition()
        cposx, cposy = self.parentframe.ScreenToClient((mposx, mposy))
        self.parentframe.PopupMenu( self.parentframe.rpcConnexions_dropdown_menu, self.parentframe.ScreenToClient((mposx, mposy)) )
    
    def refreshNetworkMenuItemList(self):
        
        
        #self.logger.info(self.rpcConnexions_dropdown_menu.GetMenuItemCount())
        if self.parentframe.rpcConnexions_dropdown_menu.GetMenuItemCount() > 0:
            
            for i in self.parentframe.rpcConnexions_dropdown_menu.GetMenuItems():
                self.parentframe.rpcConnexions_dropdown_menu.Delete(i)
            
        
        for text in self.parentframe.ConnexionManager.getAllConnexions() :
            
            #self.logger.info(text)
            #item = self.rpcConnexions_dropdown_menu.Append(-1, text)
            item = self.parentframe.rpcConnexions_dropdown_menu.AppendRadioItem(-1, text)
             
            if text == self.parentframe.ConnexionManager.getCurrent():
                item.Check(True) 
            
            self.parentframe.Bind(wx.EVT_MENU, self.OnPopupNetworkItemSelected, item)
    
    
    
    
    def OnPopupNetworkItemSelected(self, event):
        item = self.parentframe.rpcConnexions_dropdown_menu.FindItemById(event.GetId())
        text = item.GetItemLabelText()
        self.parentframe.ConnexionManager.setCurrentConnexion(text)
    
    
    
    #
    #
    #
    #    Shortcut toolbar
    #
    #
    
    def InitPluginsShortcutToolbars(self, evt=None):
        self.__Load__Plugins__Toolbars__()
        #self.parentframe.Views.UpdateGUIManager()
        self.parentframe.Views.__refreshGUI_Job__()
    
    def OnShowAboutDialogClicked(self, evt):
        self.OnAboutWxRaven(evt)
    
    
    def OnShowSettingsDialogClicked(self, evt):
        self.parentframe.OnPreferenceDialog(evt)
    
    
    def __Load__Plugins__Toolbars__(self):
        #pass
        _allViews = self.parentframe.Plugins.getAllAvailableViews()
        _allPlugins = self.parentframe.Plugins.getAllAvailablePlugins()
        
        _settingsShortcut = self.parentframe.GetPluginSetting('General', 'quick_links')
        
        #self._pluginsToolbars['wxRaven'] = self.parentframe.m_auiViewsShortcutToolbar
        #self._pluginsToolbars[str(self.parentframe.m_auiViewsShortcutToolbar.GetId())] = self.parentframe.m_auiViewsShortcutToolbar
        #item = self.PluginsViewsMenuShortcuts.AppendCheckItem(-1, 'wxRaven', f'Show/Hide wxRaven toolbar')   
        #self.PluginsViewsMenuShortcuts.Check(item.GetId(), _settingsShortcut.__contains__('wxRaven'))
        
        
        for _plugin in _allPlugins :
            #_pinstance = 
            
            #
            # Create a toolbar for the plugin
            #
            _pluginToolbar = aui.AuiToolBar( self.parentframe, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, aui.AUI_TB_HORZ_LAYOUT ) 
            
        
            
            m_staticText5 = wx.StaticText( _pluginToolbar, wx.ID_ANY, f"{_plugin} ", wx.DefaultPosition, wx.DefaultSize, 0 )
            m_staticText5.Wrap( -1 )
            m_staticText5.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
            _pluginToolbar.AddControl( m_staticText5 )
        
            
            _pluginsViews = self.parentframe.Plugins.getAvailablePluginsViews(_plugin)

            
            for _view in _pluginsViews:
                
                _viewname = _view['viewid']
                _viewicon = _view['icon']
                
                if _view.__contains__('toolbar_shortcut'):
                    show = _view['toolbar_shortcut']
                    if not show :
                        continue
                    
                
                _pluginToolbarViewbt = _pluginToolbar.AddTool( wx.ID_ANY, f"{_viewname}", _viewicon , wx.NullBitmap, wx.ITEM_NORMAL,f"{_viewname}", f"{_viewname}", None ) 
                
                self.parentframe.Bind( wx.EVT_MENU, self.OnPluginToolbarItemClick, id = _pluginToolbarViewbt.GetId() )
                self._pluginsToolbars[str(_pluginToolbarViewbt.GetId())] = _pluginToolbarViewbt
        
        
        
            _pluginToolbar.Realize()
            self._pluginsToolbars[str(_pluginToolbar.GetId())] = _pluginToolbar
            self._pluginsToolbars[_plugin] = _pluginToolbar
            self.parentframe.m_mgr.AddPane( _pluginToolbar, aui.AuiPaneInfo().Name( f"{_plugin}_Toolbar" ).Top().Caption( f"{_plugin}" ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Layer( 10 ).ToolbarPane() )
            
            
            self.__showPluginToolbar__(_plugin, _settingsShortcut.__contains__(_plugin))
            
            
            
            
            #
            # Add the plugin in list name
            #
            item = self.PluginsViewsMenuShortcuts.AppendCheckItem(-1, _plugin, f'Show/Hide {_plugin} toolbar')
            
            self.PluginsViewsMenuShortcuts.Check(item.GetId(), _settingsShortcut.__contains__(_plugin))
            
            self._pluginsToolbars[str(item.GetId())] = item
            
            self.parentframe.Bind(wx.EVT_MENU, self.OnToggleViewShortcut, item)
        
            #self.logger.info(self._pluginsToolbars)
        #for _views in _allViews:
        #    pass
        #    item = self.PluginsViewsMenuShortcuts.AppendRadioItem(-1, _views['name'])
        #    self.parentframe.Bind(wx.EVT_MENU, self.OnToggleViewShortcut, item)
        
        
        
        """
        item = self.parentframe.rpcConnexions_dropdown_menu.AppendRadioItem(-1, text)
             
            if text == self.parentframe.ConnexionManager.getCurrent():
                item.Check(True) 
            
            self.parentframe.Bind(wx.EVT_MENU, self.OnPopupNetworkItemSelected, item)
        
        
        """
    def __getToolbarItem__(self, id):
        _item = None 
        if self._pluginsToolbars.__contains__(id):
            _item = self._pluginsToolbars[id]
        return _item
    
    
    def __showPluginToolbar__(self, pluginname, show=True):
        _pan = self.parentframe.m_mgr.GetPane(pluginname+'_Toolbar')
        
        if show:
            _pan.Show()
        else:
            self.parentframe.m_mgr.ClosePane(_pan)
        # _tb = self.__getToolbarItem__(pluginname)
        
    
    
    
    def OnToggleViewShortcut(self, evt):
        #
        # MENU
        #
        
        #self.logger.info(f"{evt}")
        #self.logger.info(f"OnToggleViewShortcut STRING {evt.GetString()}")
        #self.logger.info(f"OnToggleViewShortcut ID {evt.GetId()}")
        
        
        _item = self.__getToolbarItem__(str(evt.GetId()))
        
        _settingsShortcut = self.parentframe.GetPluginSetting('General', 'quick_links')
        
        
        
        if _item != None:
            pass
            _label = _item.GetItemLabel()
            
            if _item.IsChecked():
                if not _settingsShortcut.__contains__(_label):
                    #_settingsShortcut.remove(_label) 
                    _settingsShortcut.append(_label) 
                self.__showPluginToolbar__(_label)
            else:
                if _settingsShortcut.__contains__(_label):
                    _settingsShortcut.remove(_label) 
                    
                self.__showPluginToolbar__(_label, False)
            
            #self.logger.info(_label)
        #evt.GetMenuId()
        
        _p = self.parentframe.GetPlugin('General')
        _p.PLUGIN_SETTINGS['quick_links'] = _settingsShortcut
        #self.parentframe.Views.UpdateGUIManager()
        self.parentframe.Views.__refreshGUI_Job__()
    
    def OnPluginToolbarItemClick(self, evt):
        #
        #
        # Toolbar
        #
        #self.logger.info(f"{evt}")
        #self.logger.info(f"OnPluginToolbarItemClick ID {evt.GetId()}")
        #self.logger.info(f"OnPluginToolbarItemClick STR {evt.GetString()}")
        
        
        
        _item = self.__getToolbarItem__(str(evt.GetId()))
        if _item != None:
            pass
            _label = _item.GetLabel()
            self.logger.info(_label)
            
            self.parentframe.Views.OpenView(_label, createIfNull=True)
        #_tb = self._pluginsToolbars[evt.GetId()]
        #_tb.FindTool( toolId)
    
    """
    
    MNenu bar
    
    """
    
    
    def __ProceedLinkMenuTopic__(self, topicname, topicDatas,_topicIcon ):
        
        #print(f'__ProceedLinkMenuTopic__ : {topicname} {topicDatas}')
        
        _topic_menu = wx.Menu()
        _topic_menu_item = self.parentframe.wxRavenMenuBar_Links.AppendSubMenu(_topic_menu, topicname)
        
        
        
        #_topicIcon = self.parentframe.RessourcesProvider.GetTopicImage('webresources16')
        
        
        _topic_menu_item.SetBitmap(_topicIcon)
        pptext = f"popupID" 
        
        ppcount = self.popupCount
        for _key in topicDatas:
            _url = topicDatas[_key]
            
            popupID = wx.NewId()
            _pp = pptext + str(ppcount)
            self.popupIDS[_pp] = popupID
            self.popupMAP[popupID] = _url
            self.parentframe.Bind(wx.EVT_MENU, self.OnLinkMenuItemClicked, id=popupID)
            
            _i = _topic_menu.Append(self.popupIDS[_pp], f"{_key}")
            if _i != None:
                _i.SetBitmap(self.parentframe.RessourcesProvider.GetImage('browser'))
                #ppcount= ppcount+1
            
            
            ppcount= ppcount+1
        
        self.popupCount = ppcount
   
    def OnLinkMenuItemClicked(self, evt):
        #_data= self._data
        _url=str(self.popupMAP[evt.GetId()])
        gplugin = self.parentframe.GetPlugin('General')
        gplugin.OpenUrl(_url)
        #OpenUrl
        
    
    def RefreshLinksListMenu(self):
        _list = {}
        #if True:
        try:
            from libs.RVNComunity import __RVN_COMMUNITY_DEFAULT_LINKS__
            _list = __RVN_COMMUNITY_DEFAULT_LINKS__
            _icons = __RVN_COMMUNITY_TOPICS_MAPPING__
            
            for _topic in _list:
                
                _topicIcon = self.parentframe.RessourcesProvider.GetTopicImage(_icons[_topic])
                
                self.__ProceedLinkMenuTopic__(_topic, _list[_topic], _topicIcon)
            
            
        except Exception as e:
            #self.logger.info(" > refreshViewsListMenu " + str(e))
            self.RaiseMenuAndToolLog("Unable to refresh Links list menu : "+ str(e), "error")
    
    
    def purgePerspectiveListMenu(self):
        self.purgeViewsListMenu(self.parentframe.wxRavenMenuBar_Window_Perspectives_OpenPerspectives)
    
    
    def purgeViewsListMenu(self , menuObject=None):
        if menuObject==None:
            menuObject = self.parentframe.wxRavenMenuBar_Window_Views
            
        if menuObject.GetMenuItemCount() > 0:
            
            for i in menuObject.GetMenuItems():
                menuObject.Delete(i) 
    
    
    
    
    def refreshPerspectiveListMenu(self, args=[]):
        
        self.logger.info('refreshPerspectiveListMenu')
        
        self.purgePerspectiveListMenu()
        try:
            
            _allPersp = self.parentframe.PerspectiveManager.GetPerspectiveList()
            
            menuObject =   self.parentframe.wxRavenMenuBar_Window_Perspectives_OpenPerspectives
            for p in _allPersp:
                item = menuObject.Append(-1, p)
                item.SetBitmap(self.parentframe.RessourcesProvider.GetImage('perspective_default'))
                
                
                self.parentframe.Bind(wx.EVT_MENU, self.OnPerspectiveItemSelected, item)
                
                
            
        except Exception as e:
            #self.logger.info(" > refreshViewsListMenu " + str(e))
            self.RaiseMenuAndToolLog("Unable to refresh perspective list menu : "+ str(e), "error")
    
    
    
    def refreshViewsListMenu(self, args=[]):
        self.refreshViewsListMenu_Param( self.parentframe.wxRavenMenuBar_Window_Views)
        #self.PopupViewMenu = wx.Menu()
        self.refreshViewsListMenu_Param( self.PopupViewMenu)
        self.logger.info('refreshViewsListMenu')
       
    
    
    def refreshViewsListMenu_Param(self, menuObject=None):
        
        #allViews = self.parentframe.Views.all_views
        
        if menuObject == None:
            menuObject = self.parentframe.wxRavenMenuBar_Window_Views
        
        
        try:
            allViews = self.parentframe.Plugins.getAllActiveViews()
            
            self.purgeViewsListMenu(menuObject)
            
            #self.logger.info("allv"+str(allViews))
            
            
            
            for framedata in allViews:
                #framedata = allViews[frameName]
                
                #self.logger.info("r="+str(framedata))
                
                title = framedata['title']
                icon = framedata['icon']
                name = framedata['name']
                
                #self.logger.info(icon)
                
                #item = self.parentframe.wxRavenMenuBar_Window_Views.Append(-1, name)
                item = menuObject.Append(-1, name)
                
                if icon!=None:
                    item.SetBitmap(icon)
                    
                self.parentframe.Bind(wx.EVT_MENU, self.OnViewItemSelected, item)
        
                
            
            ## Add separator and classic menu
            
            menuObject.AppendSeparator()
            
            itemShowAll = menuObject.Append(-1, "Show All...")
            
            #self.parentframe.RessourcesProvider.GetImage('perspective_default')
            itemShowAll.SetBitmap(self.parentframe.RessourcesProvider.GetImage('perspective_default'))
            self.parentframe.Bind(wx.EVT_MENU, self.OnViewShowAll, itemShowAll)
        
        
        
            #self.parentframe.RessourcesProvider.GetImage('close_view')
            itemCloseAll = menuObject.Append(-1, "Close/Destroy All non visible...")
            itemCloseAll.SetBitmap(self.parentframe.RessourcesProvider.GetImage('close_view'))
            
            self.parentframe.Bind(wx.EVT_MENU, self.OnViewDetroyNonVisible, itemCloseAll)
            
            
            
            menuObject.AppendSeparator()
            
            itemOther = menuObject.Append(-1, "Other...")
            self.parentframe.Bind(wx.EVT_MENU, self.OnViewItemOther, itemOther)
        except Exception as e:
            #self.logger.info(" > refreshViewsListMenu " + str(e))
            self.RaiseMenuAndToolLog("Unable to refresh view list menu : "+ str(e), "error")
        
        
        #item.SetBitmap(icon)
    def OnViewItemOther(self, event):
        item = self.parentframe.wxRavenMenuBar_Window_Views.FindItemById(event.GetId())
        if item == None:
            item = self.PopupViewMenu.FindItemById(event.GetId())
        text = item.GetItemLabelText()
        self.RaiseMenuAndToolLog("Not implemented.", "msg")
        #self.logger.info("to do, a dialog with a list of available views")    
    
    
    def OnViewShowAll(self, event):
        
        item = self.parentframe.wxRavenMenuBar_Window_Views.FindItemById(event.GetId())
        if item == None:
            item = self.PopupViewMenu.FindItemById(event.GetId())
        text = item.GetItemLabelText()
        
        #self.logger.info("showall")
        
        self.parentframe.Views.ShowAllActiveViews()
        
        
    def OnViewDetroyNonVisible(self, event):
        item = self.parentframe.wxRavenMenuBar_Window_Views.FindItemById(event.GetId())
        if item == None:
            item = self.PopupViewMenu.FindItemById(event.GetId())
        text = item.GetItemLabelText()    
    
        #self.logger.info("destroy all")
        self.parentframe.Views.DestroyAllNonVisible()
        
    
    
    
    def OnPerspectiveItemSelected(self, event): 
        item = self.parentframe.wxRavenMenuBar_Window_Perspectives_OpenPerspectives.FindItemById(event.GetId())
        
        text = item.GetItemLabelText()
        self.parentframe.PerspectiveManager.LoadUserPerspective(text)
          
    
    def OnViewItemSelected(self, event):
        item = self.parentframe.wxRavenMenuBar_Window_Views.FindItemById(event.GetId())
        if item == None:
            item = self.PopupViewMenu.FindItemById(event.GetId())
        text = item.GetItemLabelText()
        #self.parentframe.ConnexionManager.setCurrentConnexion(text)
        
        #wx.MessageBox("You selected the view '%s'" % text) 
        #self.RaiseMenuAndToolLog("Not implemented.", "msg")
        
          
        #viewInstance = self.parentframe.Plugins.GetViewNameInstance(text)
        #self.parentframe.m_mgr.GetPane(text).Show()
        #self.parentframe.Views.UpdateGUIManager()
        
        self.parentframe.Views.OpenView(text)
        
        #self.logger.info("viewInstance="+str(viewInstance))
    
    
    
    
    def OnDeleteLastPerspectiveClick(self, evt):
        self.parentframe.PerspectiveManager.DeleteLastPerspective()
    
    def OnLoadLastPerspectiveClick(self, evt):
        self.parentframe.PerspectiveManager.LoadLastPerspective()
        
    def OnSavePerspectiveAsClick(self, evt):
        self.parentframe.PerspectiveManager.SaveCurrentPerspective()
        self.refreshPerspectiveListMenu()
    
    
    
    
    
    def OnOpenWidgetInspector(self, evt):
        # Activate the widget inspection tool, giving it a widget to preselect
        # in the tree.  Use either the one under the cursor, if any, or this
        # frame.
        from wx.lib.inspection import InspectionTool
        wnd = wx.FindWindowAtPointer()
        if not wnd:
            wnd = self
        InspectionTool().Show(wnd, True)
    
    
    def OnAboutWxRaven(self, evt):
        
        
        aboutDial = wxRavenAbout(self.parentframe)
        from wxRavenGUI.version import __VERSION__, __BUILD_ID__
        
        versionDetails = aboutDial.m_textCtrl2.GetValue()
        versionDetails = versionDetails.replace("<VERSION>", __VERSION__)
        versionDetails = versionDetails.replace("<BUILD_ID>", __BUILD_ID__)
        aboutDial.m_textCtrl2.SetValue(versionDetails)
        aboutDial.Show(show=1)
        
        aboutDial.Bind(wx.EVT_CLOSE, self.OnCloseAbout )
        self._aboutDialog = aboutDial
    
    
    def OnCloseAbout(self, evt):
        if self._aboutDialog !=None:
            self._aboutDialog.Destroy()
            self._aboutDialog = None
    
    
    def OnSupportClicked(self, evt):
        _inviteToken = 'e4tNn3C3N3'
        webbrowser.open('https://discord.gg/'+_inviteToken)
        
        
    def OnQuickUnlockClicked(self, evt):
        _p = self.parentframe.GetPlugin('Ravencore')
        if _p != None:
            _p.QuickWalletUnlockRequest()
        
    def OnAboutConnexionClicked(self,evt):
        #print('yyy')
        _p = self.parentframe.GetPlugin('General')
        if _p != None:
            _p.OpenAboutConnexion()
            
    def OnOpenRelaySessionTokenManagementClicked(self,evt):
        #print('yyy')
        _p = self.parentframe.GetPlugin('General')
        if _p != None:
            _p.OpenRelaySessionTokenManagement()        
    
    
    
    def OnPrivateUserSessionTokenRequestClicked(self,evt):
        #print('yyy')
        
        if UserQuestion(self.parentframe, "Request a private token for webservice ?"):
            _p = self.parentframe.GetPlugin('General')
            _eK, eV = _p.GetUserTokenSettings()
            
            if _eK == True and eV!=None:
                UserAdvancedMessage(self.parentframe, 'A Private Session Token has been detected in your settings, it will be erased.', 'warning', f'{eV}')
            
            
            if _p != None:
                njob = self.parentframe.JobManager.CreateJob('General', 'Job_CreatePrivateWsTokenRemoteJob_ClientRequest' , 'plugins.Webservices.jobs.RemoteJobs_CreatePrivateToken' , _jobparams={}, _localJob=True)
                self.parentframe.NewJob( njob)
                
                
                #Job_CreatePrivateWsTokenRemoteJob_ClientRequest
            #_p.OpenRelaySessionTokenManagement()               
            
    
    def setupMenuBar(self):
        
        
        index=self.parentframe.wxRavenMenuBar_Window.FindItem("Views")
        #self.parentframe.RessourcesProvider.GetImage('dialog_default')
        self.parentframe.wxRavenMenuBar_Window.FindItemById(index).SetBitmap(self.parentframe.RessourcesProvider.GetImage('dialog_default'))
        
        
        #res\default_style\normal\main_tab.png
        index=self.parentframe.wxRavenMenuBar_Window.FindItem("Perspectives")
        self.parentframe.wxRavenMenuBar_Window.FindItemById(index).SetBitmap( self.parentframe.RessourcesProvider.GetImage('perspective_default'))
        #res\default_style\normal\default_persp.png
        
        
        
        self.parentframe.Bind( wx.EVT_MENU, self.OnLoadLastPerspectiveClick, id = self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLast.GetId() )
        self.parentframe.Bind( wx.EVT_MENU, self.OnDeleteLastPerspectiveClick, id = self.parentframe.wxRavenMenuBar_Window_Perspectives_DeleteLast.GetId() )
        self.parentframe.Bind( wx.EVT_MENU, self.OnSavePerspectiveAsClick, id = self.parentframe.wxRavenMenuBar_Window_Perspectives_SavePerspAs.GetId() )
        
        
        
        
        self.parentframe.Bind( wx.EVT_MENU, self.OnOpenWidgetInspector, id = self.parentframe.wxRavenMenuBar_Help_WidgetInspector.GetId() )
        
        
        
        self.parentframe.Bind( wx.EVT_MENU, self.OnAboutWxRaven, id = self.parentframe.wxRavenMenuBar_Help_About.GetId() )
        
        self.parentframe.Bind( wx.EVT_MENU, self.OnSupportClicked, id = self.parentframe.wxRavenMenuBar_Help_Support.GetId() )
        
    
        self.parentframe.Bind( wx.EVT_MENU, self.OnQuickUnlockClicked, id = self.parentframe.wxRavenMenuBar_Wallet_Unlock.GetId() )
        
        
        
        self.parentframe.Bind( wx.EVT_MENU, self.OnAboutConnexionClicked, id = self.parentframe.wxRavenMenuBar_Connexion_About.GetId() )
        self.parentframe.Bind( wx.EVT_MENU, self.OnOpenRelaySessionTokenManagementClicked, id = self.parentframe.wxRavenMenuBar_Connexion_Relay_SessionInfos.GetId() )
        self.parentframe.Bind( wx.EVT_MENU, self.OnPrivateUserSessionTokenRequestClicked, id = self.parentframe.wxRavenMenuBar_Connexion_Relay_RequestPrivateToken.GetId() )
        
    
        
        index=self.parentframe.wxRavenMenuBar_Connexion.FindItem("wxRaven Relay")
        #self.parentframe.RessourcesProvider.GetImage('dialog_default')
        self.parentframe.wxRavenMenuBar_Connexion.FindItemById(index).SetBitmap(self.parentframe.RessourcesProvider.GetImage('connexion_speed_2'))
        
    
        
    
    