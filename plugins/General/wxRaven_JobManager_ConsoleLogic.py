'''
Created on 27 févr. 2022

@author: slinux
'''


from .wxRavenGeneralDesign import *


import wx.lib as lib
import wx.lib.mixins.listctrl as listmix




import wx.aui



import wx.lib.mixins.listctrl as listmix 


class wxRaven_JobManager_Console_Logic(wxRavenJobManagerConsole, listmix.ColumnSorterMixin):
    '''
    classdocs
    '''


    view_base_name = "Job Manager Console"
    view_name = "Job Manager Console"
    parent_frame = None
    default_position = "mgr"
    
    
    #icon = wx.Bitmap( u"res/default_style/normal/error_log.png", wx.BITMAP_TYPE_ANY )
    icon = "pview"
    
    
    allIcons = {}
    
    message_type_mapping = {}
    
    

    def __init__(self, parentFrame, position = "toolbox1", viewName= "Job Manager Console"):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        self.view_base_name = "Job Manager Console"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        
        
        self.logger = logging.getLogger('wxRaven')
        
        self._display = [] 
        #self._msg = True
        #self._warning = True
        #self._error = True
        self._DebugWindow = None
        self._datacache = {}
        self.itemDataMap = {}
        self.allIcons = { }
        self.message_type_mapping = {}
        self._listInit = False
        self.currentJob = None
        
        
        self.InitBasicMapping()
        self.InitPlugingAndVariousMapping()
        
        self.InitConsoleLog()
        self.InitToolbar()
        
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.m_listCtrl1)
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
    def OnStopCurrent(self, evt):
        
        
        UserAdvancedMessage(self.parent_frame, "Not Implemented", "warning")
        
        #self.UpdateDatasFromManager()
    
    def OnGarbageClicked(self, evt):
        
        if self.currentJob != None:
        
            if UserQuestion(self.parent_frame, f"Purge {self.currentJob.jobName} and send to garbage ?\nJobs result will become unusable."):
                if not self.parent_frame.JobManager.PurgeCompleteJob(self.currentJob):
                    self.parent_frame.JobManager.PurgeCanceledJob(self.currentJob)
                self.UpdateView()
    
    
    def OnGarbageErrorsClicked(self, evt):
        
        
        if UserQuestion(self.parent_frame, f"Purge all errors and send to garbage ?"):
            self.parent_frame.JobManager.PurgeCanceledJob()
            self.UpdateView()    
                
                
    def OnGarbageDonesClicked(self, evt):
        

        
        if UserQuestion(self.parent_frame, f"Purge all job done and send to garbage ?\nJobs result will become unusable."):
            self.parent_frame.JobManager.PurgeCompleteJob()
            self.UpdateView()      
    
    def OnItemSelected(self, evt):
        print(f"current event  {evt.Index}")
        self._currentItem = evt.Index
        #self._currentItem = self.m_listCtrl1.GetItemData(evt.Index)
        print(f"_currentItem  {self._currentItem}")
        itemData = self._datacache[self._currentItem]
        
        self.currentJob = itemData
        
        
        #if self.currentJob.getStatus() not in ['done', 'stopped', 'error']:
            #m_stopSelected.Enable(False)
        print(f"{self.currentJob._jobUniqueId} : {itemData}")
    
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
         
    
    
    def __updateItemDataFromList__(self, listdata):
        for j in listdata.copy():
            
            _icon = self.allIcons[j.getStatus().lower()]
            
            _prefix = ''
            if j._jobFromRemote:
                _prefix = 'R'
            
            _jobName = f'[{_prefix}'+str(j._jobNumber).zfill(4)+'] ' + j.jobName
            
            
            
            self.itemDataMap[self.cursor ] = (str(_jobName), str(j.getStatus()), str(j._jobDetailedProgress) )
            self._datacache[self.cursor] = j    
            self.cursor = self.cursor +1
            
        
    
    def __updateList__(self, listData):
        
        for j in listData.copy():
            _icon = self.allIcons[j.getStatus().lower()]
            _jobName = j.jobName
            index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(), _jobName, _icon )
        
            self.m_listCtrl1.SetItem(index,1, j.getStatus())
            self.m_listCtrl1.SetItem(index,2, str(j._jobDetailedProgress))
            self.m_listCtrl1.SetItemData(index, self.cursor)
            self.itemDataMap[self.cursor ] = (str(_jobName), str(j.getStatus()), str(j._jobDetailedProgress) )
            self._datacache[self.cursor] = j    
            self.cursor = self.cursor +1
        
    
        
    
    
    #-----------------------------------------------------------------
    # These methods are callbacks for implementing the "virtualness"
    # of the list...  Normally you would determine the text,
    # attributes and/or image based on values from some external data
    # source, but for this demo we'll just calculate them
    def OnGetItemText(self, item, col):
        #return "Item %d, column %d" % (item, col)
        #print(f'OnGetItemText {item} {col}')
        return self.itemDataMap[item][col]

    def OnGetItemImage(self, item):
        
        _datas = self._datacache[item]
        _icon = self.allIcons[_datas.getStatus().lower()]
        return _icon
        '''
        if item % 3 == 0:
            return self.idx1
        else:
            return self.idx2
            
        '''

    def OnGetItemAttr(self, item):
        return None
        '''
        if item % 3 == 1:
            return self.attr1
        elif item % 3 == 2:
            return self.attr2
        else:
            return None
    
        '''
    
    def UpdateDatasFromManager(self, evt=None):
        self.itemDataMap = {}
        self.cursor = 0
        
        
        _showDone = self.m_auiToolBar1.GetToolToggled(self.m_showComplete.GetId())
        _showProgress = self.m_auiToolBar1.GetToolToggled(self.m_showProgress.GetId())
        _showWaiting = self.m_auiToolBar1.GetToolToggled(self.m_showWaiting.GetId())
        _showErrors = self.m_auiToolBar1.GetToolToggled(self.m_showErrors.GetId())
            
        jmgr= self.parent_frame.JobManager
        if _showDone:
            self.__updateItemDataFromList__(jmgr._done_list)
        if _showWaiting:
            self.__updateItemDataFromList__(jmgr._queue_list)
        if _showProgress:
            self.__updateItemDataFromList__(jmgr._running_list)
        if _showErrors:
            self.__updateItemDataFromList__(jmgr._canceled_list)
        
        
        #if not self._listInit:
        #    listmix.ColumnSorterMixin.__init__(self, 3)
        #    self._listInit = True
        
        self.m_listCtrl1.SetItemCount(len(self.itemDataMap))
        self.m_listCtrl1.Refresh()
     
    
    
    
    def CheckRegistered(self):
        jmgr= self.parent_frame.JobManager
            
        if not jmgr._callBacks.__contains__(self.UpdateView):
            self.logger.info(f'UpdateView Registered to JobManager')
            jmgr._callBacks.append(self.UpdateView)
        
     
     
    def UpdateView(self, evt=None): 
        
        #self.logger.info(f'UpdateView called.')
        #self.logger.info(str(inspect.stack()[0][0].f_code.co_name))
        #self.logger.info(str(inspect.stack()[1][0].f_code.co_name))
        #self.logger.info(str(inspect.stack()[2][0].f_code.co_name))
        if self.parent_frame._Closing or not self.parent_frame._isReady : 
            #self.logger.info(f'UpdateView Closing Request Detected.')
            return
        self.CheckRegistered() 
        self.UpdateDatasFromManager() 
        '''
        self.m_listCtrl1.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.m_listCtrl1.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.m_listCtrl1.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        
        '''
    
    def UpdateViewOLD(self, evt=None):
        if self.parent_frame._Closing or not self.parent_frame._isReady : 
            #self.logger.info(f'UpdateView Closing Request Detected.')
            return
        
        
        return
        
        self.logger.info(f'UpdateView JobManager')
        
        try:
            
            jmgr= self.parent_frame.JobManager
            '''
            if not jmgr._callBacks.__contains__(self.UpdateView):
                self.logger.info(f'UpdateView Registered to JobManager')
                jmgr._callBacks.append(self.UpdateView)
            '''
            if not self.parent_frame._isReady:
                return 
            
            self.m_listCtrl1.Freeze()
            
            
            self.itemDataMap = {}
            self.cursor = 0
            self.ClearLogs()
            
            
            _showDone = self.m_auiToolBar1.GetToolToggled(self.m_showComplete.GetId())
            _showProgress = self.m_auiToolBar1.GetToolToggled(self.m_showProgress.GetId())
            _showWaiting = self.m_auiToolBar1.GetToolToggled(self.m_showWaiting.GetId())
            _showErrors = self.m_auiToolBar1.GetToolToggled(self.m_showErrors.GetId())
            #print("RavenErrorLogConsole Update !")
            
            if _showDone:
                self.__updateList__(jmgr._done_list)
            
            if _showWaiting:
                self.__updateList__(jmgr._queue_list)
                
            if _showProgress:
                self.__updateList__(jmgr._running_list)
                
            if _showErrors:
                self.__updateList__(jmgr._canceled_list)
                
                
            self.m_listCtrl1.SetColumnWidth(0, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(1, wx.LIST_AUTOSIZE)
            self.m_listCtrl1.SetColumnWidth(2, wx.LIST_AUTOSIZE)
            
            if not self._listInit:
                listmix.ColumnSorterMixin.__init__(self, 3)
                self._listInit = True
            
            
            self.m_listCtrl1.Thaw()
            self.RefreshToolbarState()  
            self.SetAutoLayout(True)
            self.Layout()
        except Exception as e:
            pass
        
    
    
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
        
        
        
        self.m_auiToolBar1.ToggleTool(self.m_showComplete.GetId(), True)
        self.m_auiToolBar1.ToggleTool(self.m_showProgress.GetId(), True)
        self.m_auiToolBar1.ToggleTool(self.m_showErrors.GetId(), True)
        self.m_auiToolBar1.ToggleTool(self.m_showWaiting.GetId(), True)
           
       
        '''
        if alloptions.__contains__('error'):
            self.m_auiToolBar1.ToggleTool(self.m_showErrors.GetId(), True  
        self._display = alloptions
        '''
    
    
    
    def RefreshToolbarState(self):
        #print(self._DebugWindow)
        pass
        '''
        _iv = self.parent_frame.Views.isViewVisible("Debug")
        #print(f"iv = {_iv}")
        if not _iv:
            self.m_auiToolBar1.ToggleTool(self.m_showDebug.GetId(), False)
        '''
    
    def ActivateDebugWindow(self):
        pass
        #print("debug console turned on !")
        #if self._DebugWindow == None:
        #    print("debug mode was not init yet!")
        #self._DebugWindow = self.parent_frame.Views.OpenView("Debug", "General", True)['instance']
        #self.parent_frame.Views.OpenView("Debug", "General", True)
        #Debug
        #self._DebugWindow = wx.LogWindow(self.parent_frame, "Debug", show=False)
        #self.parent_frame.Add(self._DebugWindow.GetFrame(), "Debug", icon=self.parent_frame.RessourcesProvider.GetImage('debug_exc'))
        #self._DebugWindow.Show(show=True)
    
    
    
        
    def OnViewOptionsChanged(self, evt):
        #GetToolToggled
        '''
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
        '''
        #self.ResetCursorAndCache()
        #self.ClearLogs()
        self.UpdateView()
        
        #myPlugin.PLUGIN_SETTINGS['showerror'] = alloptions
    
    
    
    def InitConsoleLog(self):
        
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "Job"
        self.m_listCtrl1.InsertColumn(0, info)

        info.Align = 0#wx.LIST_FORMAT_RIGHT
        info.Text = "State"
        self.srcCol = self.m_listCtrl1.InsertColumn(1, info)

        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "Source"
        self.m_listCtrl1.InsertColumn(2, info)
        
        
        
        
        
        self.m_listCtrl1.SetColumnWidth(0, 200)
        self.m_listCtrl1.SetColumnWidth(1, 100)
        self.m_listCtrl1.SetColumnWidth(2, 100)
        
        
        self.il = wx.ImageList(16, 16)
        
        """
        self.allIcons['error'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/error_tsk.png", wx.BITMAP_TYPE_ANY ))
        self.allIcons['info'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/info_obj.png", wx.BITMAP_TYPE_ANY ))
        self.allIcons['msg'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY ))
        self.allIcons['warning'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/warning_obj.png", wx.BITMAP_TYPE_ANY ))
        """
        self.allIcons['job'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('job_icon') )
        self.allIcons['waiting'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('job_pause') )
        self.allIcons['created'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('job_pause') )
        self.allIcons['running'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('job_running') )
        self.allIcons['stopped'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('job_stopped') )
        self.allIcons['error'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('progress_error') )
        self.allIcons['done'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('job_complete') )
        
        
        self.allIcons['debug'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('debug_exc') )
        #self.allIcons['error'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('error_tsk') )
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
        
        
        