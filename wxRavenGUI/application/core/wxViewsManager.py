'''
Created on 13 déc. 2021

@author: slinux
'''


import inspect
from wxRavenGUI.view import wxRavenAddView

from wxRavenGUI.application.wxcustom.CustomDialog import wxRavenCustomDialog

import wx
import wx.aui

import logging

class ViewsManager(object):
    '''
    classdocs
    '''
    parentframe = None
    
    dialogs = {}
    all_areas = {}
    #all_views = {}
    #viewsChangeCallbacks=[]
    
    
    force_mgr = False
    

    def __init__(self, parentframe, forceinprincipalauimanager=False):
        '''
        Constructor
        '''
        self.parentframe = parentframe
        self.force_mgr = forceinprincipalauimanager
    
        self.nViewDialog = None
        
        self.dialogs = {}
        self.logger = logging.getLogger('wxRaven')
        self.InitViewManager()
        
        parentframe.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnAuiPaneActivated )
        parentframe.Bind( wx.aui.EVT_AUI_PANE_ACTIVATED, self.OnAuiPaneActivated )
        parentframe.Bind( wx.aui.EVT_AUI_PANE_CLOSE, self.OnAuiPaneClose )
        #parentframe.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnAuiPaneClose )
        #parentframe.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnAuiNotebookPageClose )
        
    
    
    
    #
    #
    #    Event management (for GUI refresh)
    #
    #
    #    
        
    def OnAuiNotebookPageClose(self, evt):
        self.logger.info("OnAuiPaneClose in view man ")
        self.OnPageClose(evt)
        
        wx.CallAfter(self.parentframe.MenusAndTool.refreshViewsListMenu, ())
        #wx.CallAfter(self.parentframe.MenusAndTool.RefreshToolbar, ())
    
    
       
    def OnAuiPaneClose(self, evt):
        self.logger.info("OnAuiPaneClose in view man ")
        wx.CallAfter(self.parentframe.MenusAndTool.refreshViewsListMenu, ())
        wx.CallAfter(self.parentframe.MenusAndTool.RefreshToolbar, ())
        
        
        
    def OnAuiPaneActivated(self, evt):
        self.logger.info("OnAuiPaneActivated in view man") 
        wx.CallAfter(self.parentframe.MenusAndTool.refreshViewsListMenu, ())    
        wx.CallAfter(self.parentframe.MenusAndTool.RefreshToolbar, ())      
        
    
    
    
    
    
        
        
    def OnPageClose( self, event ):
        self.logger.info("OnPageClose")
        objNotebook = event.GetEventObject()
        index = event.GetSelection()
        page = objNotebook.GetPage(index)
        label = objNotebook.GetPageText(index)
        self.logger.info("view instance to delete !")
        
        
        _v = self.parentframe.Plugins.GetViewNameInstance(label)
        
        
        
        
        if _v != None:
            self.logger.info('instance found, close it')
            self.parentframe.Plugins.DeleteViewInstance(label)
            
            _closed=False
            try:
                _v['instance'].Close()
                #_closed=True
            except Exception as e:
                self.logger.error("_v['instance'].Close() " + str(e)) 
            if not _closed:
                try:
                    _v['instance'].OnClose(None)
                    #_closed=True
                except Exception as e:
                    self.logger.error("_v['instance'].OnClose() " + str(e)) 
                
            if not _closed:
                try:
                    _v['instance'].safeClose(None)
                    #_closed=True
                except Exception as e:
                    #pass
                    self.logger.error("_v['instance'].SafeClose() " + str(e))
        
        
        wx.CallAfter(self.parentframe.MenusAndTool.refreshViewsListMenu, ())
        event.Skip()       
        
        
    #SearchViewPanelInManager   
        
        
        
        
    #
    #
    #    Init and creation of the view manager
    #
    #
    #
        
    
    
    def InitViewManager(self):
        
        
        self.AddArea('main', self.parentframe.wxRavenMainBook)
       
        self.AddArea('mgr', self.parentframe.m_mgr)
    
        
        self.parentframe.wxRavenToolBook1.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)
        self.parentframe.wxRavenToolBook2.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)
        self.parentframe.wxRavenToolBook3.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)
        self.parentframe.wxRavenMainBook.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)
        
        
        self.parentframe.RessourcesProvider.ApplyThemeOnPanel(self.parentframe.wxRavenToolBook1)
        self.parentframe.RessourcesProvider.ApplyThemeOnPanel(self.parentframe.wxRavenToolBook2)
        self.parentframe.RessourcesProvider.ApplyThemeOnPanel(self.parentframe.wxRavenToolBook3)
        self.parentframe.RessourcesProvider.ApplyThemeOnPanel(self.parentframe.wxRavenMainBook)
        
        
        if not self.force_mgr:
            self.AddArea('toolbox1', self.parentframe.wxRavenToolBook1)
            self.AddArea('toolbox2', self.parentframe.wxRavenToolBook2)
            self.AddArea('toolbox3', self.parentframe.wxRavenToolBook3)
        
        else:
            self.parentframe.m_mgr.GetPane("toolbox1").DestroyOnClose(True)
            self.parentframe.m_mgr.GetPane("toolbox2").DestroyOnClose(True)
            self.parentframe.m_mgr.GetPane("toolbox3").DestroyOnClose(True)
            #pa = self.parentframe.m_mgr.GetPane("Toolbox1")
            #self.parentframe.m_mgr.ClosePane(pa)
            self.parentframe.m_mgr.ClosePane(self.parentframe.m_mgr.GetPane("toolbox1"))
            self.parentframe.m_mgr.ClosePane(self.parentframe.m_mgr.GetPane("toolbox2"))
            self.parentframe.m_mgr.ClosePane(self.parentframe.m_mgr.GetPane("toolbox3"))
            self.UpdateGUIManager()

    
    
    
    
    
    
    
    
    
    
    
   
        
    def AddArea(self, frameName, Obj):
        self.all_areas[frameName] = Obj
        self.logger.info(f"Add Area {frameName}")
        #self.AddView(frameName, Obj)
        
    def GetAllAreas(self):
        return self.all_areas
    
    
    def GetArea(self, areaName):
        result = None 
        
        if self.all_areas.__contains__(areaName):
            result = self.all_areas[areaName]
            
        return result
    
    
    def Add(self, obj, nameFrame, position="main", icon=None):
        self.logger.info("Add")
        
        if position=="dialog":
            self.logger.info("FORCE Dialog !")
            self.AddDialog(obj, nameFrame, position, icon)
        
        if self.all_areas.__contains__(position):
            targetPosition= self.all_areas[position]
            
            if self.force_mgr:
                position = "main"
                self.logger.info("FORCE MAIN !")
            else:
                self.logger.info(f"position received = {position}")
                
                
            
  
            if position == "main":
                self.AddInMainbook(obj, nameFrame, icon=icon) 
                
            if position == "mgr":
                self.AddInMainFrame(obj, nameFrame, icon=icon)
             
                
            if position.__contains__("toolbox") or position.__contains__("Notebook Toolbox") :
                #self.logger.info("Position !!!")
                self.AddInNotebook(obj, nameFrame, targetPosition, icon=icon)
            
            
            
            self.RaiseViewLog("New View ["+nameFrame+"] has been added in '"+position+"'", "info")    
            #self.AddView(nameFrame, obj, icon)    
        else:
            self.RaiseViewLog("["+nameFrame+"] : Invalid position '"+position+"'", "error")  
            
    
    
    
    def SearchDialog(self, dname):
        _d=None
        
        for d in self.dialogs:
            if d == dname:
                _d = self.dialogs[d]
                break
            
        return _d
            
    
    def __registerDialog__(self, dname, dinst):
        self.dialogs[dname] = dinst
    
    def __unregisterDialog__(self, dname):
        self.dialogs[dname] = None
            
    
    def AddDialog(self,_view, nameFrame="", position="dialog", icon=None):
        
        self.logger.info(_view)
        if nameFrame == "":
            nameFrame = _view[0]['name']
            
        if icon == None:
            icon = _view[0]['icon']

       
        
        _newDialog = wxRavenCustomDialog(self.parentframe, _view[0], title=nameFrame, icon=icon)
        self.__registerDialog__(nameFrame, _newDialog)
        _newDialog.Show()
        #_newDialog.ShowModal()
        
        #self.__unregisterDialog__(nameFrame, _newDialog)
    
    
            
    
    def ShowAllActiveViews(self):
        
        ### TODO , what if not in mgr, like all toolbox and stuff.
        all_panes = self.parentframe.m_mgr.GetAllPanes()
        for ii in range(len(all_panes)):
            if not all_panes[ii].IsToolbar():
                #self.logger.info(all_panes[ii])
                capt = all_panes[ii].caption
                na = all_panes[ii].name
                all_panes[ii].Show()    
                #self.logger.info(capt)
                #self.logger.info(na)
                
                
    
    
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
                #self.logger.info(all_panes[ii])
                #capt = all_panes[ii].caption
                #na = all_panes[ii].name
                #all_panes[ii].Show()    
                #self.logger.info(capt)
                #self.logger.info(na)
                if not all_panes[ii].IsShown():
                    capt = all_panes[ii].caption
                    na = all_panes[ii].name
                    self.logger.info(f"Hidden dialog found : {capt} - {na}")
                    #self.logger.info(na)
                    
                    
                    self.parentframe.Plugins.DeleteViewInstance(na)
                    
                    all_panes[ii].DestroyOnClose(True)
                    todelete.append(all_panes[ii])
        
        
        for td in todelete:
            self.logger.info(f"removing {td}")
            self.parentframe.m_mgr.ClosePane(td)
            self.RaiseViewLog("["+str(td)+"] has been destroyed.", "info")  
                      
                
    
        wx.CallAfter(self.parentframe.MenusAndTool.refreshViewsListMenu, ())
        self.UpdateGUIManager()
        
    
                
                
    def UpdateGUIManager(self):
        
        self.parentframe.m_mgr.GetPane("wxRavenToolBar").window.Realize()
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
                #self.logger.info(e)
                self.RaiseViewError()
                
          
                
    """  
    
    
    
    def RaiseViewLog(self, message, type="error"):
        try:
            _source = str(inspect.stack()[1][0])
            self.parentframe.Log( message, source=str(_source), type=type)
        except Exception as e:
            self.logger.error("RaiseViewError() " + str(e))  
    
    
    
    
    
    def HideParentInManager(self, instanceParent):
        
        all_panes = self.parentframe.m_mgr.GetAllPanes()
        for ii in range(len(all_panes)):
            if not all_panes[ii].IsToolbar():
                #self.logger.info(all_panes[ii].name)
                #self.logger.info(all_panes[ii].caption)
                
                if all_panes[ii].window == instanceParent:
                    all_panes[ii].Hide()
                
        self.UpdateGUIManager()
    
    
    
    def ShowParentInManager(self, instanceParent):
        
        all_panes = self.parentframe.m_mgr.GetAllPanes()
        for ii in range(len(all_panes)):
            if not all_panes[ii].IsToolbar():
                #self.logger.info(all_panes[ii].name)
                #self.logger.info(all_panes[ii].caption)
                
                if all_panes[ii].window == instanceParent:
                    all_panes[ii].Show(True)
                
        self.UpdateGUIManager()
    
    
    
    
    def SearchViewInstance(self, viewname):
        _v = None 
        
        for _p in self.parentframe.Plugins.plugins:
            #self.logger.info(f"scanning {_p}")
            _plugin = self.parentframe.GetPlugin(_p)
            _v = _plugin.GetViewAttrDetails(viewname, attr="name")
            
            if _v == None:
                _v = _plugin.GetViewAttrDetails(viewname, attr="viewid")
            
            if _v != None:
                #self.logger.info("found!")
                break
        
        return _v
    
    
    
    def SearchViewPanelInManager(self, viewname):
        _panel = None 
        
        all_panes = self.parentframe.m_mgr.GetAllPanes()
        for ii in range(len(all_panes)):
            
            n = all_panes[ii].name
            c = all_panes[ii].caption
                      
            if viewname == c or viewname == n:
                _panel = all_panes[ii]
                break
            
        return _panel
    
    
    
    def UpdateView(self, viewname):
        
        _panelFound = self.SearchViewInstance(viewname)
        _visible = False
        
        if _panelFound !=None:
            _panelFound['instance'].UpdateView()
            
    
    
    
    def isViewVisible(self, viewname):
        #self.logger.info(f"isViewVisible {viewname}")
        _panelFound = self.SearchViewPanelInManager(viewname)
        
        if _panelFound == None:
            _panelIns = self.SearchViewInstance(viewname)
            if _panelIns != None :
                _panelFound = _panelIns['instance']
        
        _visible = False
        
        #self.logger.info(_panelFound)
        
        if _panelFound !=None:
            
            try:
                if _panelFound.window.IsShownOnScreen():
                    _visible = True
                #self.logger.info(f"IsShownOnScreen {_visible}")
            except Exception as e:
                pass
            
            try:
                if _panelFound.IsShownOnScreen():
                    _visible = True
                #self.logger.info(f"IsShownOnScreen {_visible}")
            except Exception as e:
                pass
            
            try:
                if _panelFound.IsShown():
                    _visible = True
                #self.logger.info(f"IsShown {_visible}")
            except Exception as e:
                pass
            
        return _visible   
    
    
    def HideView(self, viewName, pluginname=""):
        _v = None 
        _v = self.SearchViewInstance(viewName)
        
        if _v != None:
            
            
            if _v['position'] == 'mgr':
                self.parentframe.m_mgr.GetPane(_v['name']).Hide()
            
            
            elif _v['position'] == 'main':
                #RemovePage
                pass
            
            elif _v['position'] == 'toolbox1':
                self.parentframe.m_mgr.GetPane(_v['name']).Hide()
                _parent = self.GetArea(_v['position'])
                self.HideParentInManager(_parent)
                
                
            else:
                self.parentframe.m_mgr.GetPane(_v['name']).Hide()
                _parent = self.GetArea(_v['position'])
                self.HideParentInManager(_parent)
                
                _parentArea = self.GetArea(_v['position'])
                if _parentArea != None :
                    self.HideParentInManager(_parentArea)
                
                
                
        self.UpdateGUIManager()
    
    
    def RenameView(self):
        pass
    
    
    
    #
    #
    #Best and cleanest way to call a view
    #   
    def OpenView(self, viewName, pluginname="", createIfNull=False):
        
        
        _defaultArea = self.parentframe.GetPluginSetting("General", 'defaultviewarea')
        
        _v = None 
        _isDialog = False
        
        if pluginname == "":
            
            _v = self.SearchViewInstance(viewName)
            """
            for _p in self.parentframe.Plugins.plugins:
                #self.logger.info(f"scanning {_p}")
                _plugin = self.parentframe.GetPlugin(_p)
                _v = _plugin.GetViewAttrDetails(viewName, attr="name")
                if _v != None:
                    #self.logger.info("found!")
                    break
            """
        
        else:
            _plugin = self.parentframe.GetPlugin(pluginname)
            _v = _plugin.GetViewAttrDetails(viewName, attr="name")
            
            if _v == None:
                _v = _plugin.GetViewAttrDetails(viewName, attr="viewid")
        
        
            if _v== None:
                _v = self.SearchDialog(viewName)
        
                _isDialog = True
        
        
        
        
        if _v != None :
            #self.logger.info(_v)
        
        
            
            
            if  not _isDialog :
                
                
                if self.force_mgr:
                    position = "main"
                    _v['position']= 'main'
                    self.logger.info("FORCE MAIN !")
                    
                  
                    
                if _v['position'] == 'mgr':
                    self.logger.info(f"{_v['position']} will be managed dynamically with Manager")
                    self.parentframe.m_mgr.GetPane(_v['name']).Show(True)
                    self.UpdateGUIManager()
                
                elif _v['position'] == 'main':
                    self.logger.info(f"{_v['position']} will be managed dynamically with MainNotebook")
                    self.SetCurrentView_Notebook(viewName, self.parentframe.wxRavenMainBook)
                
                elif _v['position'] == 'toolbox1':
                    self.logger.info(f"{_v['position']} will be managed dynamically with Toolbox")
                    
                    _parent = self.GetArea(_v['position'])
                    #self.parentframe.m_mgr.GetPane("Toolbox1").Show(True)
                    self.SetCurrentView_Notebook(viewName, _parent)
                    
                    self.ShowParentInManager(_parent)
                    
                
                else:
                    self.logger.info(f"{_v['position']} will be managed dynamically with getParent")
                    
                    self.SetCurrentView_Notebook(viewName, _v['instance'].GetParent())   
                    self.ShowParentInManager(_v['instance'].GetParent())
                    
                    _parentArea = self.GetArea(_v['position'])
                    if _parentArea != None :
                        self.ShowParentInManager(_parentArea)
                
                
                
        else:
            
            if createIfNull:
                
                
                
                _viewObj = None
                if pluginname == "":
                    
                    for _p in self.parentframe.Plugins.plugins:
                        #self.logger.info(f"scanning {_p}")
                        _plugin = self.parentframe.GetPlugin(_p)
                        _viewObj = _plugin.SearchPluginView(viewName)
                        if _viewObj != None:
                        #self.logger.info("found!")
                            pluginname = _p
                            break
                
                else:
                    _plugin = self.parentframe.GetPlugin(pluginname)
                    _viewObj = _plugin.SearchPluginView(viewName)
                    
                    
                if _viewObj != None:
                    
                    if _viewObj['position'] == 'dialog':
                        self.AddDialog((_viewObj,))
                    else:    
                        _plugin = self.parentframe.GetPlugin(pluginname)
                        _plugin.LoadView(_viewObj, _defaultArea)
                
                
                _v = _viewObj
                
                
                
                
                
                """
                cp = self.parentframe.wxRavenMainBook.GetCurrentPage()
                cpi = self.parentframe.wxRavenMainBook.GetPageIndex(cp)
                cpText = self.parentframe.wxRavenMainBook.GetPageText( cpi)
                self.logger.info(f"current mainbook page {cp}   {cpText}")
                
                
                for _x in range(0, self.parentframe.wxRavenMainBook.GetPageCount()-1):
                    _xname = self.parentframe.wxRavenMainBook.GetPageText(_x)
                    self.logger.info(f"current mainbook page {_x}   {_xname}")
                    
                    if _xname == viewName:
                        self.parentframe.wxRavenMainBook.SetSelection(_x)
                        self.logger.info(f"selecting {_x}")
                        
                """
            
            
            
                
    
        return _v
    
    
    
    
    
    
    def SetCurrentView_Notebook(self, viewname, notebook):
        cp = notebook.GetCurrentPage()
        cpi = notebook.GetPageIndex(cp)
        cpText = notebook.GetPageText( cpi)
        #self.logger.info(f"current mainbook page {cp}   {cpText}")
                
                
        for _x in range(0, self.parentframe.wxRavenMainBook.GetPageCount()):
            _xname = notebook.GetPageText(_x)
            #self.logger.info(f"current mainbook page {_x}   {_xname}")
                    
            if _xname == viewname:
                notebook.SetSelection(_x)
                #self.logger.info(f"selecting {_x}")
    
    
              
                            
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
            #self.logger.info(e)    
        #view_base_name = getattr(obj, "view_base_name")  
        
        if view_base_name == None:
            view_base_name = view_name
            
            
        return view_name, view_base_name
             
        
    def AddInMainFrame(self, obj, nameFrame, icon=None):
        
        
        t, n = self.getFrameTitleAndName(obj, nameFrame)
        title = ""+t+" ("+ n +")" 
        if icon==None:
            #icon = wx.Bitmap( u"res/default_style/normal/view_default_frame.png", wx.BITMAP_TYPE_ANY )
            icon = self.parentframe.RessourcesProvider.GetImage('view_default_frame')
        #self.logger.info("Add Frame :" + nameFrame)
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
        
        #self.logger.info(title)
        if icon==None:
            #icon = wx.Bitmap( u"res/default_style/normal/mainnet-mini.png", wx.BITMAP_TYPE_ANY )
            icon = self.parentframe.RessourcesProvider.GetImage('ravencoin')
        
        
        #self.logger.info(str(type(notebook)))
        if str(type(notebook)).__contains__("wx._aui.AuiNotebook"):
            notebook.AddPage(obj, t, bitmap = icon)
            self.logger.info("notebook.AddPage()")
        elif str(type(notebook)).__contains__("RavenNotebookToolbox"):
            notebook.AddPage(obj, t, icon)
            self.logger.info("notebook.AddPage()")
        
        elif str(type(notebook)).__contains__("wx._core.Notebook"): 
            self.RaiseViewLog("Unable to addview '"+ nameFrame+"' not supported type target : " + str(type(notebook)) , "warning")  
            
        else: 
            self.RaiseViewLog("Unable to addview '"+ nameFrame+"' unknown type : " + str(type(notebook)) , "error")
        #self.AddView(nameFrame, obj, icon)
        self.UpdateGUIManager()
        
        
        
        
        
        
    
    
    
    def ShowAddViewDialog(self):
        
        _defaultViewSett = self.parentframe.GetPluginSetting("General", 'defaultviewarea')#main
        #self.logger.info(_defaultViewSett)
        
        
        nViewDialog = RavenAddViewDialog(self.parentframe, _defaultViewSett)
        nViewDialog.Show()    
        
        nViewDialog.Bind(wx.EVT_CLOSE, self.OnAddViewClose )
        
        self.nViewDialog = nViewDialog
        
        
        
        
    def OnAddViewClose(self, evt):
        if self.nViewDialog  != None :
            self.nViewDialog.Destroy()
            self.nViewDialog=None
        
        
        
class RavenAddViewDialog(wxRavenAddView):
    
    parentframe = None
    
    imagesListReference = {}
    
    
    
    _selected_plugin = ""
    _selected_view = {}
    
    _target = "mgr"
    
    def __init__(self, parentFrame, targetDefault="main"):
        super().__init__(parentFrame)
        self.parentframe = parentFrame
        
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap( parentFrame.RessourcesProvider.GetImage('new_view') )
        self.SetIcon(icon)
        self.logger = logging.getLogger('wxRaven')
        self._selected_plugin = ""
        self._selected_view = {}
        
        self._target = targetDefault
        
        self.openButton.Enable(False)
        
        self.imagesListReference = {}
        
        self.SetupTreeView()
        
        self.FillAreaList()
        self.FillTree()
    
        
    
    
    
    
    
    def SetupTreeView(self):
        
        
        
        
        isz = (16,16)
        il = wx.ImageList(isz[0], isz[1])
        
        
        
        
        fldridx     = il.Add(self.parentframe.RessourcesProvider.GetImage('packagefolder_obj') )
        fldrOpenidx     = il.Add(self.parentframe.RessourcesProvider.GetImage('packagefolder_obj'))
        viewIdx     = il.Add( self.parentframe.RessourcesProvider.GetImage('view_default_frame'))
        
        
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
            
        
        
        
        #_defaultViewSett = self.parentframe.GetPluginSetting("General", 'defaultviewarea')#main
        #self.logger.info(_defaultViewSett)
        #if _defaultViewSett == None:
        #    _defaultViewSett = "main"
        
        
        #self.logger.info(_defaultViewSett)
        
        default = self.m_choice1.FindString(self._target)
        self.m_choice1.SetSelection(default)
        
        
        
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
        
        
       
        
        #self.logger.info(self.item)
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
                
                #self.logger.info(itemtext)
                #self.logger.info(_itemData)
                
            #items = self.tree.GetSelections()
            #self.logger.info(map(self.tree.GetItemText, items))
        event.Skip()
        
        
        
        
    def OnCancel(self, event):
        self.Close(force=True)
        
        
    def OnOpen(self, event):   
        #self.logger.info("OnOpen")
   
        if self._selected_plugin != "" and self._selected_view != None:
            
            if self._selected_view['position']=='dialog':
                self._target = 'dialog'
                
                df_class = self._selected_view['class']
                df_name = self._selected_view['name']
                df_icon = self._selected_view['icon']
                self.logger.info(self._selected_view)
                #self.parentframe.Views.AddDialog(self._selected_view, df_name, position="dialog", icon=df_icon)
                wx.CallAfter(self.parentframe.Views.AddDialog, (self._selected_view,))
            else:
                self.parentframe.GetPlugin(self._selected_plugin).LoadView(self._selected_view, self._target)
            wx.CallAfter(self.parentframe.MenusAndTool.refreshViewsListMenu, ())
            self.Close(force=True)
        
        
        
        
        
        
        
        
        
        
        
        
        