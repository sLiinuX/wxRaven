'''
Created on 13 déc. 2021

@author: slinux
'''
import wx 
import inspect



from wxRavenGUI.view import *


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
    
    
    def RaiseMenuAndToolLog(self, message, type="error"):
        try:
            _source = str(inspect.stack()[1][0])
            self.parentframe.Log( message, source=str(_source), type=type)
        except Exception as e:
            print("RaiseMenuAndToolLog() " + str(e))  
    
        
    """
    
    Status bar
    
    """
    
    def setupStatusBar(self):
        self.parentframe.wxRavenStatusBarIcon=None
        
        self.parentframe.wxRavenStatusBar.SetFieldsCount( 3, [-3,150,32])
        self.parentframe.wxRavenStatusBar.SetStatusText("welcome to wxRaven", 0)
        self.parentframe.wxRavenStatusBar.Bind(wx.EVT_SIZE, self.OnSizeSB)
        
        
        
        self.parentframe.ConnexionManager.RegisterOnConnexionChanged(self.setStatusBarActiveNetwork)
    
    
    
    def OnSizeSB(self, event):
        rect = self.parentframe.wxRavenStatusBar.GetFieldRect(2)
        w, h = self.parentframe.wxRavenStatusBarIcon.Size
        xpad = (rect.width - w) / 2
        ypad = (rect.height - h) / 2
        self.parentframe.wxRavenStatusBarIcon.SetPosition((rect.x + xpad, rect.y + ypad))
        event.Skip() 
        
        
    
    def setStatusBarActiveNetwork(self, networkName=""):
        
        if networkName == '':
            networkName= self.parentframe.ConnexionManager.getCurrent()
        
        self.parentframe.wxRavenStatusBar.SetStatusText(networkName, 1)
        
        #print("test")
        
        """
        icon = wx.Bitmap( u"res/default_style/normal/mainnet.png", wx.BITMAP_TYPE_ANY )
        if networkName.__contains__("testnet"):
            icon = wx.Bitmap( u"res/default_style/normal/testnet.png", wx.BITMAP_TYPE_ANY )
        """
        
        icon = self.parentframe.ConnexionManager.getIcon(networkName)
        
        if self.parentframe.wxRavenStatusBarIcon != None:
            self.parentframe.wxRavenStatusBarIcon.Destroy()
            
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
    
    def OnContextMenu_ShowNetworkList(self, event):
        #print("showConnexionList!")
        self.refreshNetworkMenuItemList()
        self.showNetworkListMenu()
        
        
    
    def setupToolBar(self):
        self.parentframe.Bind( wx.EVT_TOOL, self.OnContextMenu_ShowNetworkList, id = self.parentframe.rpcConnexions_dropdown_button.GetId() )
    
    
    
    def showNetworkListMenu(self):
        mposx, mposy = wx.GetMousePosition()
        cposx, cposy = self.parentframe.ScreenToClient((mposx, mposy))
        self.parentframe.PopupMenu( self.parentframe.rpcConnexions_dropdown_menu, self.parentframe.ScreenToClient((mposx, mposy)) )
    
    def refreshNetworkMenuItemList(self):
        
        
        #print(self.rpcConnexions_dropdown_menu.GetMenuItemCount())
        if self.parentframe.rpcConnexions_dropdown_menu.GetMenuItemCount() > 0:
            
            for i in self.parentframe.rpcConnexions_dropdown_menu.GetMenuItems():
                self.parentframe.rpcConnexions_dropdown_menu.Delete(i)
            
        
        for text in self.parentframe.ConnexionManager.getAllConnexions() :
            
            #print(text)
            #item = self.rpcConnexions_dropdown_menu.Append(-1, text)
            item = self.parentframe.rpcConnexions_dropdown_menu.AppendRadioItem(-1, text)
             
            if text == self.parentframe.ConnexionManager.getCurrent():
                item.Check(True) 
            
            self.parentframe.Bind(wx.EVT_MENU, self.OnPopupNetworkItemSelected, item)
    
    
    
    
    def OnPopupNetworkItemSelected(self, event):
        item = self.parentframe.rpcConnexions_dropdown_menu.FindItemById(event.GetId())
        text = item.GetItemLabelText()
        self.parentframe.ConnexionManager.setCurrentConnexion(text)
    
    """
    
    MNenu bar
    
    """
    
    
    def purgeViewsListMenu(self):
        if self.parentframe.wxRavenMenuBar_Window_Views.GetMenuItemCount() > 0:
            
            for i in self.parentframe.wxRavenMenuBar_Window_Views.GetMenuItems():
                self.parentframe.wxRavenMenuBar_Window_Views.Delete(i) 
    
    def refreshViewsListMenu(self, args=[]):
        
        #allViews = self.parentframe.Views.all_views
        try:
            allViews = self.parentframe.Plugins.getAllActiveViews()
            
            self.purgeViewsListMenu()
            
            #print("allv"+str(allViews))
            
            
            
            for framedata in allViews:
                #framedata = allViews[frameName]
                
                #print("r="+str(framedata))
                
                title = framedata['title']
                icon = framedata['icon']
                name = framedata['name']
                
                #print(icon)
                
                item = self.parentframe.wxRavenMenuBar_Window_Views.Append(-1, name)
                if icon!=None:
                    item.SetBitmap(icon)
                    
                self.parentframe.Bind(wx.EVT_MENU, self.OnViewItemSelected, item)
        
                
            
            ## Add separator and classic menu
            
            self.parentframe.wxRavenMenuBar_Window_Views.AppendSeparator()
            
            itemShowAll = self.parentframe.wxRavenMenuBar_Window_Views.Append(-1, "Show All...")
            itemShowAll.SetBitmap(wx.Bitmap( u"res/default_style/normal/perspective_default.png", wx.BITMAP_TYPE_ANY ))
            self.parentframe.Bind(wx.EVT_MENU, self.OnViewShowAll, itemShowAll)
        
        
        
        
            itemCloseAll = self.parentframe.wxRavenMenuBar_Window_Views.Append(-1, "Close/Destroy All non visible...")
            itemCloseAll.SetBitmap(wx.Bitmap( u"res/default_style/normal/close_view.png", wx.BITMAP_TYPE_ANY ))
            
            self.parentframe.Bind(wx.EVT_MENU, self.OnViewDetroyNonVisible, itemCloseAll)
            
            
            
            self.parentframe.wxRavenMenuBar_Window_Views.AppendSeparator()
            
            itemOther = self.parentframe.wxRavenMenuBar_Window_Views.Append(-1, "Other...")
            self.parentframe.Bind(wx.EVT_MENU, self.OnViewItemOther, itemOther)
        except Exception as e:
            #print(" > refreshViewsListMenu " + str(e))
            self.RaiseMenuAndToolLog("Unable to refresh view list menu : "+ str(e), "error")
        
        
        #item.SetBitmap(icon)
    def OnViewItemOther(self, event):
        item = self.parentframe.wxRavenMenuBar_Window_Views.FindItemById(event.GetId())
        text = item.GetItemLabelText()
        self.RaiseMenuAndToolLog("Not implemented.", "msg")
        #print("to do, a dialog with a list of available views")    
    
    
    def OnViewShowAll(self, event):
        item = self.parentframe.wxRavenMenuBar_Window_Views.FindItemById(event.GetId())
        text = item.GetItemLabelText()
        
        #print("showall")
        
        self.parentframe.Views.ShowAllActiveViews()
        
        
    def OnViewDetroyNonVisible(self, event):
        item = self.parentframe.wxRavenMenuBar_Window_Views.FindItemById(event.GetId())
        text = item.GetItemLabelText()    
    
        #print("destroy all")
        self.parentframe.Views.DestroyAllNonVisible()
        
        
    
    def OnViewItemSelected(self, event):
        item = self.parentframe.wxRavenMenuBar_Window_Views.FindItemById(event.GetId())
        text = item.GetItemLabelText()
        #self.parentframe.ConnexionManager.setCurrentConnexion(text)
        
        wx.MessageBox("You selected the view '%s'" % text) 
        self.RaiseMenuAndToolLog("Not implemented.", "msg")
        
          
        viewInstance = self.parentframe.Plugins.GetViewNameInstance(text)
        #print("viewInstance="+str(viewInstance))
    
    
    
    
    def OnDeleteLastPerspectiveClick(self, evt):
        self.parentframe.PerspectiveManager.DeleteLastPerspective()
    
    def OnLoadLastPerspectiveClick(self, evt):
        self.parentframe.PerspectiveManager.LoadLastPerspective()
    
    
    
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
        aboutDial.Show(show=1)
        
    
    
    
    def setupMenuBar(self):
        
        
        index=self.parentframe.wxRavenMenuBar_Window.FindItem("Views")
        self.parentframe.wxRavenMenuBar_Window.FindItemById(index).SetBitmap(wx.Bitmap( u"res/default_style/normal/dialog_default.png", wx.BITMAP_TYPE_ANY ))
        
        
        #res\default_style\normal\main_tab.png
        index=self.parentframe.wxRavenMenuBar_Window.FindItem("Perspectives")
        self.parentframe.wxRavenMenuBar_Window.FindItemById(index).SetBitmap(wx.Bitmap( u"res/default_style/normal/perspective_default.png", wx.BITMAP_TYPE_ANY ))
        #res\default_style\normal\default_persp.png
        
        
        self.parentframe.Bind( wx.EVT_MENU, self.OnLoadLastPerspectiveClick, id = self.parentframe.wxRavenMenuBar_Window_Perspectives_LoadLast.GetId() )
        self.parentframe.Bind( wx.EVT_MENU, self.OnDeleteLastPerspectiveClick, id = self.parentframe.wxRavenMenuBar_Window_Perspectives_DeleteLast.GetId() )
        
        self.parentframe.Bind( wx.EVT_MENU, self.OnOpenWidgetInspector, id = self.parentframe.wxRavenMenuBar_Help_WidgetInspector.GetId() )
        
        
        
        self.parentframe.Bind( wx.EVT_MENU, self.OnAboutWxRaven, id = self.parentframe.wxRavenMenuBar_Help_About.GetId() )
        
    
    
    
    
    
    