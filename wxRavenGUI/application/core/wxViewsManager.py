'''
Created on 13 déc. 2021

@author: slinux
'''


import inspect
from wxRavenGUI.view import wxRavenAddView

import wx
import wx.aui

class ViewsManager(object):
    '''
    classdocs
    '''
    parentframe = None
    
    
    all_areas = {}
    #all_views = {}
    #viewsChangeCallbacks=[]
    
    
    force_mgr = False
    

    def __init__(self, parentframe, forceInPrincipalAuiManager=False):
        '''
        Constructor
        '''
        self.parentframe = parentframe
        self.force_mgr = forceInPrincipalAuiManager
    
        self.InitViewManager()
    
    
    def InitViewManager(self):
        
        
        self.AddArea('main', self.parentframe.wxRavenMainBook)
        self.AddArea('toolbox1', self.parentframe.wxRavenToolBook1)
        self.AddArea('toolbox2', self.parentframe.wxRavenToolBook2)
        self.AddArea('toolbox3', self.parentframe.wxRavenToolBook3)
        self.AddArea('mgr', self.parentframe.m_mgr)
    
        
        self.parentframe.wxRavenToolBook1.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)
        self.parentframe.wxRavenToolBook2.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)
        self.parentframe.wxRavenToolBook3.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)
        self.parentframe.wxRavenMainBook.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)


    def OnPageClose( self, event ):
        objNotebook = event.GetEventObject()
        index = event.GetSelection()
        page = objNotebook.GetPage(index)
        label = objNotebook.GetPageText(index)
        #print("view instance to delete !")
        self.parentframe.Plugins.DeleteViewInstance(label)
        wx.CallAfter(self.parentframe.MenusAndTool.refreshViewsListMenu, ())
        event.Skip()   
   
        
    def AddArea(self, frameName, Obj):
        self.all_areas[frameName] = Obj
        #self.AddView(frameName, Obj)
        
    def GetAllAreas(self):
        return self.all_areas
    
    
    def GetArea(self, areaName):
        result = None 
        
        if self.all_areas.__contains__(areaName):
            result = self.all_areas[areaName]
            
        return result
    
    def Add(self, obj, nameFrame, position="main", icon=None):
        
        if self.all_areas.__contains__(position):
            targetPosition= self.all_areas[position]
            
            if self.force_mgr:
                position = "mgr"
            
  
            if position == "main":
                self.AddInMainbook(obj, nameFrame, icon=icon) 
                
            if position == "mgr":
                self.AddInMainFrame(obj, nameFrame, icon=icon)
             
                
            if position.__contains__("toolbox") or position.__contains__("Notebook Toolbox") :
                #print("Position !!!")
                self.AddInNotebook(obj, nameFrame, targetPosition, icon=icon)
            
            
            
            self.RaiseViewLog("New View ["+nameFrame+"] has been added in '"+position+"'", "info")    
            #self.AddView(nameFrame, obj, icon)    
        else:
            self.RaiseViewLog("["+nameFrame+"] : Invalid position '"+position+"'", "error")  
            
            
            
    
    def ShowAllActiveViews(self):
        
        ### TODO , what if not in mgr, like all toolbox and stuff.
        all_panes = self.parentframe.m_mgr.GetAllPanes()
        for ii in range(len(all_panes)):
            if not all_panes[ii].IsToolbar():
                #print(all_panes[ii])
                capt = all_panes[ii].caption
                na = all_panes[ii].name
                all_panes[ii].Show()    
                #print(capt)
                #print(na)
                
                
    
    
        self.UpdateGUIManager()
    
    
    def DestroyAllNonVisible(self):
        
        ### TODO , what if not in mgr, like all toolbox and stuff.
        ### Update 1 : toolbox partially fixed since notebook destroy view on closing page
        ###
        ### a ton of things to fix ? still ?
        ###
        all_panes = self.parentframe.m_mgr.GetAllPanes()
        
        todelete = []
        
        for ii in range(len(all_panes)):
            if not all_panes[ii].IsToolbar():
                #print(all_panes[ii])
                #capt = all_panes[ii].caption
                #na = all_panes[ii].name
                #all_panes[ii].Show()    
                #print(capt)
                #print(na)
                if not all_panes[ii].IsShown():
                    capt = all_panes[ii].caption
                    na = all_panes[ii].name
                    #print(capt)
                    #print(na)
                    
                    
                    self.parentframe.Plugins.DeleteViewInstance(na)
                    
                    all_panes[ii].DestroyOnClose(True)
                    todelete.append(all_panes[ii])
        
        
        for td in todelete:
            self.parentframe.m_mgr.ClosePane(td)
            self.RaiseViewLog("["+str(td)+"] has been destroyed.", "info")  
                      
                
    
        wx.CallAfter(self.parentframe.MenusAndTool.refreshViewsListMenu, ())
        self.UpdateGUIManager()
        
    
                
                
    def UpdateGUIManager(self):
        

        self.parentframe.m_mgr.Update()
        self.parentframe.Layout()
        #self.parentframe.Centre( wx.BOTH )   
        
                    
    """           
             
    def RegisterOnViewsChanged(self, callback):
    
        if not self.viewsChangeCallbacks.__contains__(callback):
            self.viewsChangeCallbacks.append(callback)
    
    
    
    def UnregisterOnViewsChanged(self, callback):

        if self.viewsChangeCallbacks.__contains__(callback):
            self.viewsChangeCallbacks.remove(callback)
            
            
            
          
    def SafeCallbackLoop(self, connexionName):
        
        
        for c in self.networkChangeCallbacks:
            try:
                c(connexionName)
            except Exception as e:
                #print(e)
                self.RaiseViewError()
                
          
                
    """  
    
    
    
    def RaiseViewLog(self, message, type="error"):
        try:
            _source = str(inspect.stack()[1][0])
            self.parentframe.Log( message, source=str(_source), type=type)
        except Exception as e:
            print("RaiseViewError() " + str(e))  
    
    
    
    
              
                            
    """
    
    Low Level Functions to place elements in Dialog
    
    """       
    
    def getFrameTitleAndName(self, obj, nameFrame):
        
        
        view_name = nameFrame
        view_base_name = view_name
        
        try:
            view_base_name = obj.view_base_name
        except Exception as e:
            pass
            #print(e)    
        #view_base_name = getattr(obj, "view_base_name")  
        
        if view_base_name == None:
            view_base_name = view_name
            
            
        return view_name, view_base_name
             
        
    def AddInMainFrame(self, obj, nameFrame, icon=None):
        
        
        t, n = self.getFrameTitleAndName(obj, nameFrame)
        title = ""+t+" ("+ n +")" 
        if icon==None:
            icon = wx.Bitmap( u"res/default_style/normal/view_default_frame.png", wx.BITMAP_TYPE_ANY )
        
        #print("Add Frame :" + nameFrame)
        #self.parentframe.m_mgr.AddPane( obj, wx.aui.AuiPaneInfo() .Bottom() .Icon(icon) .Name( nameFrame ) .Caption( u"> "+title+"" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
        self.parentframe.m_mgr.AddPane( obj, wx.aui.AuiPaneInfo() .Bottom() .Icon(icon)  .Name( nameFrame ) .Caption( u"> "+title+"" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
        self.parentframe.m_mgr.GetPane(nameFrame).Icon(icon)
        #self.AddView(nameFrame, obj, icon=icon)
        self.UpdateGUIManager()
        
       
    def AddInMainbook(self, obj, nameFrame, icon=None):
        


  
        self.AddInNotebook(obj, nameFrame, self.parentframe.wxRavenMainBook, icon=icon)
        #self.AddView(nameFrame, obj, icon)
        
        
    def AddInNotebook(self, obj, nameFrame, notebook, icon=None):
        
        t, n = self.getFrameTitleAndName(obj, nameFrame)
        title = ""+t+" ("+ n +")"
        
        #print(title)
        if icon==None:
            icon = wx.Bitmap( u"res/default_style/normal/mainnet-mini.png", wx.BITMAP_TYPE_ANY )
        
        
        #print(str(type(notebook)))
        if str(type(notebook)).__contains__("wx._aui.AuiNotebook"):
            notebook.AddPage(obj, t, bitmap = icon)
            #print("notebook.AddPage()")
        elif str(type(notebook)).__contains__("RavenNotebookToolbox"):
            notebook.AddPage(obj, t, icon)
            #print("notebook.AddPage()")
        
        elif str(type(notebook)).__contains__("wx._core.Notebook"): 
            self.RaiseViewLog("Unable to addview '"+ nameFrame+"' not supported type target : " + str(type(notebook)) , "warning")  
            
        else: 
            self.RaiseViewLog("Unable to addview '"+ nameFrame+"' unknown type : " + str(type(notebook)) , "error")
        #self.AddView(nameFrame, obj, icon)
        self.UpdateGUIManager()
        
        
        
        
        
        
    
    
    
    def ShowAddViewDialog(self):
        nViewDialog = RavenAddViewDialog(self.parentframe)
        nViewDialog.Show()    
        
        
        
        
        
        
        
        
        
        
class RavenAddViewDialog(wxRavenAddView):
    
    parentframe = None
    
    imagesListReference = {}
    
    
    
    _selected_plugin = ""
    _selected_view = {}
    
    _target = "mgr"
    
    def __init__(self, parentFrame):
        super().__init__(parentFrame)
        self.parentframe = parentFrame
        
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(wx.Bitmap( u"res/default_style/normal/new_view.png", wx.BITMAP_TYPE_ANY ))
        self.SetIcon(icon)
        
        self._selected_plugin = ""
        self._selected_view = {}
        
        self.openButton.Enable(False)
        
        self.imagesListReference = {}
        
        self.SetupTreeView()
        
        self.FillAreaList()
        self.FillTree()
    
    
    
    
    
    
    
    def SetupTreeView(self):
        
        
        
        
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        
        
        
        
        fldridx     = il.Add(wx.Bitmap( u"res/default_style/normal/packagefolder_obj.gif", wx.BITMAP_TYPE_ANY ))
        fldrOpenidx     = il.Add(wx.Bitmap( u"res/default_style/normal/packagefolder_obj.gif", wx.BITMAP_TYPE_ANY ))
        viewIdx     = il.Add(wx.Bitmap( u"res/default_style/normal/view_default_frame.png", wx.BITMAP_TYPE_ANY ))
        
        
        self.imagesListReference['folder'] = fldridx
        self.imagesListReference['folderOpen'] = fldrOpenidx
        self.imagesListReference['view'] = viewIdx
        

        self.m_treeCtrl1.SetImageList(il)
        self.il = il
        
        
        self.root = self.m_treeCtrl1.AddRoot("Views")
        #self.rootb = self.m_treeCtrl1.AddRoot("Viewds")
        self.m_treeCtrl1.SetItemData(self.root, None)
        self.m_treeCtrl1.SetItemImage(self.root, self.imagesListReference['folder'], wx.TreeItemIcon_Normal)
        self.m_treeCtrl1.SetItemImage(self.root, self.imagesListReference['folderOpen'], wx.TreeItemIcon_Expanded)
        
    
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.m_treeCtrl1)
        
    
    
    
    def FillAreaList(self):
        
        #m_choice1
        
        
        for _areas in self.parentframe.Views.GetAllAreas():
            self.m_choice1.Append(_areas)
            
            
        default = self.m_choice1.FindString("mgr")
        self.m_choice1.SetSelection(default)
        
        self._target = "mgr"
        self.Bind(wx.EVT_CHOICE, self.EvtChoice, self.m_choice1)
        
        
    def EvtChoice(self, event):
        
        self._target = event.GetString()
        
    
    def FillTree(self):
        
        #DeleteAllItems()
        for _plugin in self.parentframe.Plugins.plugins:
            _pluginInstance = self.parentframe.GetPlugin(_plugin)
            
            
            child = self.m_treeCtrl1.AppendItem(self.root, _plugin)
            self.m_treeCtrl1.SetItemData(child, None)
            self.m_treeCtrl1.SetItemImage(child, self.imagesListReference['folder'], wx.TreeItemIcon_Normal)
            self.m_treeCtrl1.SetItemImage(child, self.imagesListReference['folderOpen'], wx.TreeItemIcon_Expanded)
    
            
            
            
            for _views in _pluginInstance.PLUGINS_VIEWS:
                _viewName = _views['name']
                _viewIcon = _views['icon']
                
                _viewClass = _views['class']
                
                iconName = 'view'
                
                if not self.imagesListReference.__contains__(_viewName):
                    _viewIconIdx     = self.il.Add(_viewIcon)
                    self.imagesListReference[_viewName] = _viewIconIdx
                    iconName = _viewName
                
                
                
                last = self.m_treeCtrl1.AppendItem(child, _viewName)
                self.m_treeCtrl1.SetItemData(last, _views)
                self.m_treeCtrl1.SetItemImage(last, self.imagesListReference[_viewName], wx.TreeItemIcon_Normal)
                self.m_treeCtrl1.SetItemImage(last, self.imagesListReference[_viewName], wx.TreeItemIcon_Selected)
            
    
    
    
    def OnSelChanged(self, event):
        self.item = event.GetItem()
        
        
       
        
        #print(self.item)
        self.openButton.Enable(False)
        if self.item:
            
            _itemData = self.m_treeCtrl1.GetItemData(self.item)
            
            if _itemData != None: 
             
                self.openButton.Enable(True)
                itemtext = self.m_treeCtrl1.GetItemText(self.item)
                
                
                parentPluginItem = self.m_treeCtrl1.GetItemParent( self.item)
                pluginName = self.m_treeCtrl1.GetItemText(parentPluginItem)
                
                self._selected_plugin = pluginName
                self._selected_view = _itemData
                
                #print(itemtext)
                #print(_itemData)
                
            #items = self.tree.GetSelections()
            #print(map(self.tree.GetItemText, items))
        event.Skip()
        
        
        
        
    def OnCancel(self, event):
        self.Close(force=True)
        
        
    def OnOpen(self, event):   
        #print("OnOpen")
   
        if self._selected_plugin != "" and self._selected_view != None:
            self.parentframe.GetPlugin(self._selected_plugin).LoadView(self._selected_view, self._target)
            wx.CallAfter(self.parentframe.MenusAndTool.refreshViewsListMenu, ())
            self.Close(force=True)
        
        
        
        
        
        
        
        
        
        
        
        
        