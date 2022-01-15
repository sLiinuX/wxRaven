'''
Created on 15 déc. 2021

@author: slinux
'''

from .wxRavenGeneralDesign import *


import wx.lib as lib
import wx.lib.mixins.listctrl as listmix




import wx.aui



import wx.lib.mixins.listctrl as listmix 


class RavenErrorLogConsole(wxRavenErrorLogConsolePanel, listmix.ColumnSorterMixin):
    '''
    classdocs
    '''


    view_base_name = "Error Log Console"
    view_name = "Error Log Console"
    parent_frame = None
    default_position = "mgr"
    
    
    #icon = wx.Bitmap( u"res/default_style/normal/error_log.png", wx.BITMAP_TYPE_ANY )
    icon = "error_console"
    
    
    allIcons = {}
    
    message_type_mapping = {}
    
    

    def __init__(self, parentFrame, position = "toolbox1", viewName= "Error Log Console"):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        self.view_base_name = "Error Log Console"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        
        self._display = [] 
        #self._msg = True
        #self._warning = True
        #self._error = True
        self._DebugWindow = None
        
        self.itemDataMap = {}
        self.allIcons = { }
        self.message_type_mapping = {}
        self.InitBasicMapping()
        self.InitPlugingAndVariousMapping()
        
        self.InitConsoleLog()
        self.InitToolbar()
        
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
        
        #parentFrame.Bind( wx.aui.EVT_AUI_PANE_RESTORE, self.OnAuiPaneRestore )
        #parentFrame.Bind( wx.aui.EVT_AUI_PANE_ACTIVATED, self.OnAuiPaneActivated )
        #parentFrame.Bind( wx.aui.EVT_AUI_RENDER, self.OnAuiPaneRender )
        #parentFrame.Bind( wx.aui.EVT_AUI_PANE_CLOSE, self.OnAuiPaneClose )
        
        self._logCurrentCursor = -1
        
        #self.dummyTest()
        
        self.SetAutoLayout(True)
    
    
        #self.m_auiToolBar1.ToggleTool(self.m_showWarnings.GetId(), True)
        
    """    
    def OnAuiPaneClose(self, evt):
        print("OnAuiPaneClose in console log")
        
    def OnAuiPaneRestore(self, evt):
        print("OnAuiPaneRestore in console log")
        
    def OnAuiPaneRender(self, evt):
        print("OnAuiPaneRender in console log")    
        
    def OnAuiPaneActivated(self, evt):
        print("OnAuiPaneActivated in console log")    
        
    """
    
    
    
    def InitBasicMapping(self):
        self.message_type_mapping['info'] = 'info'
        
        self.message_type_mapping['message'] = 'msg'
        self.message_type_mapping['msg'] = 'msg'
        
        self.message_type_mapping['warning'] = 'warning'
        
        self.message_type_mapping['error'] = 'error'
        
        self.message_type_mapping['debug'] = 'debug'
    
    
    
    def InitPlugingAndVariousMapping(self):
        self.message_type_mapping['dbsync_inprogress'] = 'info'
        self.message_type_mapping['db'] = 'info'
        self.message_type_mapping['dbsync_done'] = 'msg'
        self.message_type_mapping['db_warning'] = 'warning'
        self.message_type_mapping['db_check'] = 'info'
        
        
        self.message_type_mapping['process_run'] = 'msg'
        self.message_type_mapping['process_stop'] = 'msg'
        self.message_type_mapping['process_pause'] = 'msg'
        self.message_type_mapping['process_warning'] = 'warning'

        
    
    
    def __getMessageTypeFromMapping__(self, iconame):
        retType = 'info'
        
        if self.message_type_mapping.__contains__(iconame):
            retType = self.message_type_mapping[iconame]
            #print("MAPPING FOUND !")
        
        
        return retType
    
    
    def ClearLogs(self):
        self.m_listCtrl1.Freeze()
        self.m_listCtrl1.DeleteAllItems()    
        self.m_listCtrl1.Thaw()
    
    
    def ResetCursorAndCache(self):
        self._logCurrentCursor = 0
        self.itemDataMap = {}
         
    
    def UpdateView(self):
        
        
        #print("RavenErrorLogConsole Update !")
        
        _allLogs = self.parent_frame.GetPluginData("General","allLogs").copy()
        
        self.m_listCtrl1.Freeze()
        
        _currentViewCursor = self._logCurrentCursor
        #self.itemDataMap = {}
        items = _allLogs.items()
        for key, data in items:
            #print(str(key) + " VS" + str(_currentViewCursor) )
            if key>_currentViewCursor:
                #print("newrow")
                
                
                _icon = self.allIcons['info']
                
                
                _type=self.__getMessageTypeFromMapping__(data[0])
                #print(f"{data[0]} ==  {_type}")
                #print(_type)
                #print(self._display)                
                
                _foundInFilter=False
                
                if _type in self._display:
                    _foundInFilter = True
                """
                for _t in  self._display:
                    print(f"cehck display {_t}")    
                    if _type.__contains__(_t):
                        
                        _foundInFilter=True
                """
                
                
                #if not _foundInFilter:
                    #pass
                    #print(f"not found")     
                    #continue
                    
                
                
                if self.allIcons.__contains__(data[0].lower()):
                    _icon= self.allIcons[data[0].lower()]
                
                
                
                if _foundInFilter:
                
                    index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(), data[1], _icon )
                    
                    #item = self.m_listCtrl1.GetItem(index)
                    #item.SetColumn(1)
                    #item.SetText('John')
                    self.m_listCtrl1.SetItem(index,1, data[2])
                    self.m_listCtrl1.SetItem(index,2, data[3])
                    #item1.SetColumn(1)
                    #self.m_listCtrl1.SetItem(item)
                    self.m_listCtrl1.SetItemData(index, _currentViewCursor)
                
                self.itemDataMap[_currentViewCursor] = (str(data[1]), str(data[2]), str(data[3]) )
                    
                
                _currentViewCursor = _currentViewCursor +1
          
        self._logCurrentCursor = _currentViewCursor
        
        
        self.m_listCtrl1.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.m_listCtrl1.SetColumnWidth(1, 300)
        self.m_listCtrl1.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        listmix.ColumnSorterMixin.__init__(self, 3)
        
        listmix.ColumnSorterMixin.SortListItems(self, col=2, ascending=0)
        
        self.m_listCtrl1.Thaw()
        
        
        self.RefreshToolbarState()
        
        
        
        self.SetAutoLayout(True)
        self.Layout()
        
        
    
    
    def dummyTest(self):
        
        
        fakelog = {
        1 : ["error","error in bfdsdf", "ffrgfdg", "12.00PM"],
        2 : ["info","DNA featudsfsdring Suzanne Vega", "Tom's Diner", "12.00PM"],
        }

        print(self.m_listCtrl1.GetColumnCount())
        #self.m_listCtrl1.GetColumnIndexFromOrder(1)

        items = fakelog.items()
        for key, data in items:
            index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(), data[1],self.allIcons[data[0]] )
            
            #item = self.m_listCtrl1.GetItem(index)
            #item.SetColumn(1)
            #item.SetText('John')
            self.m_listCtrl1.SetItem(index,1, data[2])
            self.m_listCtrl1.SetItem(index,2, data[3])
            #item1.SetColumn(1)
            #self.m_listCtrl1.SetItem(item)
            self.m_listCtrl1.SetItemData(index, key)
            
            
            
        #items = musicdata.items()
        #for key, data in items:
        #    index = self.m_dataViewCtrl1.InsertItem(self.m_dataViewCtrl1.GetItemCount(), data)
            #self.list.SetItem(index, 1, data[1])
            #self.list.SetItem(index, 2, data[2])
            # self.list.SetItemData(index, key)
            
            
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetListCtrl(self):
        return self.m_listCtrl1
    
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetSortImages(self):
        return (self.allIcons['alphab_down'], self.allIcons['alphab_up'])        
        
    
    
    
    
    def InitToolbar(self):
        
        myPlugin = self.parent_frame.GetPlugin("General")
        
        alloptions = myPlugin.PLUGIN_SETTINGS['showerror']
        
        if alloptions.__contains__('debug'):
            self.m_auiToolBar1.ToggleTool(self.m_showDebug.GetId(), True)
            
        if alloptions.__contains__('info'):
            self.m_auiToolBar1.ToggleTool(self.m_showInfos.GetId(), True)
            
        if alloptions.__contains__('message') or alloptions.__contains__('msg') :
            self.m_auiToolBar1.ToggleTool(self.m_showMessages.GetId(), True)
             
        if alloptions.__contains__('warning'):
            self.m_auiToolBar1.ToggleTool(self.m_showWarnings.GetId(), True)
        
        if alloptions.__contains__('error'):
            self.m_auiToolBar1.ToggleTool(self.m_showErrors.GetId(), True)
              
        self._display = alloptions
    
    
    
    
    def RefreshToolbarState(self):
        #print(self._DebugWindow)
        
        _iv = self.parent_frame.Views.isViewVisible("Debug")
        #print(f"iv = {_iv}")
        if not _iv:
            self.m_auiToolBar1.ToggleTool(self.m_showDebug.GetId(), False)
    
    def ActivateDebugWindow(self):
        print("debug console turned on !")
        #if self._DebugWindow == None:
        #    print("debug mode was not init yet!")
        #self._DebugWindow = self.parent_frame.Views.OpenView("Debug", "General", True)['instance']
        self.parent_frame.Views.OpenView("Debug", "General", True)
        #Debug
        #self._DebugWindow = wx.LogWindow(self.parent_frame, "Debug", show=False)
        #self.parent_frame.Add(self._DebugWindow.GetFrame(), "Debug", icon=self.parent_frame.RessourcesProvider.GetImage('debug_exc'))
        #self._DebugWindow.Show(show=True)
        
    def OnViewOptionsChanged(self, evt):
        #GetToolToggled
        myPlugin = self.parent_frame.GetPlugin("General")
        alloptions = []
        
        if self.m_auiToolBar1.GetToolToggled(self.m_showDebug.GetId()):
            alloptions.append('debug')
            self.ActivateDebugWindow()
        
        if self.m_auiToolBar1.GetToolToggled(self.m_showInfos.GetId()):
            alloptions.append('info')
            
            
        if self.m_auiToolBar1.GetToolToggled(self.m_showMessages.GetId()):
            alloptions.append('msg')
           
            
        if self.m_auiToolBar1.GetToolToggled(self.m_showWarnings.GetId()):
            alloptions.append('warning')
           
            
        if self.m_auiToolBar1.GetToolToggled(self.m_showErrors.GetId()):
            alloptions.append('error')
           
        
        self._display = alloptions
        
        self.ResetCursorAndCache()
        self.ClearLogs()
        self.UpdateView()
        
        myPlugin.PLUGIN_SETTINGS['showerror'] = alloptions
    
    
    
    def InitConsoleLog(self):
        
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "Message"
        self.m_listCtrl1.InsertColumn(0, info)

        info.Align = 0#wx.LIST_FORMAT_RIGHT
        info.Text = "Source"
        self.srcCol = self.m_listCtrl1.InsertColumn(1, info)

        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "Date"
        self.m_listCtrl1.InsertColumn(2, info)
        
        
        
        
        
        self.m_listCtrl1.SetColumnWidth(0, 200)
        self.m_listCtrl1.SetColumnWidth(1, 100)
        self.m_listCtrl1.SetColumnWidth(2, 50)
        
        
        self.il = wx.ImageList(16, 16)
        
        """
        self.allIcons['error'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/error_tsk.png", wx.BITMAP_TYPE_ANY ))
        self.allIcons['info'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/info_obj.png", wx.BITMAP_TYPE_ANY ))
        self.allIcons['msg'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY ))
        self.allIcons['warning'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/warning_obj.png", wx.BITMAP_TYPE_ANY ))
        """
        
        self.allIcons['debug'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('debug_exc') )
        self.allIcons['error'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('error_tsk') )
        self.allIcons['info'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('info_obj') )
        self.allIcons['msg'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('help_view') )
        self.allIcons['warning'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('warning_obj') )
        
        self.allIcons['dbsync_inprogress'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('repository-synchronize') )
        self.allIcons['db'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('repository-blue') )
        self.allIcons['dbsync_done'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('repository_sync_done') )
        self.allIcons['db_warning'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('repository_warning') )
        self.allIcons['db_check'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('repository_check') )
        
        
        self.allIcons['process_run'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('process_run') )
        self.allIcons['process_stop'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('process_stop') )
        self.allIcons['process_pause'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('process_pause') )
        self.allIcons['process_warning'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('process_pause') )
        
        self.allIcons['alphab_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_up') )
        self.allIcons['alphab_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_co') )
        
        
        
        self.m_listCtrl1.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        
       
        #listmix.ListCtrlAutoWidthMixin.__init__(self.m_listCtrl1)
        
        
        #self.setResizeColumn(0)
        #self.bSizer1.Add(self.list, 1, wx.EXPAND)
        
        
    def AddImageInConsole(self, imgname,iconname,logtype="info" ):   
        self.allIcons[iconname] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage(imgname) )
        self.message_type_mapping['iconname'] = logtype
        
        
        
        
        
        
        
        
        
        
        
        
    
        