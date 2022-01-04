'''
Created on 15 déc. 2021

@author: slinux
'''

from .wxRavenGeneralDesign import *


import wx.lib as lib
import wx.lib.mixins.listctrl as listmix








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
    icon = "error_log"
    
    
    allIcons = {}
    
    

    def __init__(self, parentFrame, position = "toolbox1", viewName= "ErrorLog"):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        self.view_base_name = "ErrorLog"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        
        self._display = [] 
        #self._msg = True
        #self._warning = True
        #self._error = True
        
        
        self.itemDataMap = {}
        self.allIcons = { }
        
        self.InitConsoleLog()
        self.InitToolbar()
        
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
        
        
        
        self._logCurrentCursor = -1
        
        #self.dummyTest()
        
        self.SetAutoLayout(True)
    
    
    
    
    
    def UpdateView(self):
        
        
        #print("RavenErrorLogConsole Update !")
        
        _allLogs = self.parent_frame.GetPluginData("General","allLogs").copy()
        
        
        _currentViewCursor = self._logCurrentCursor
        #self.itemDataMap = {}
        items = _allLogs.items()
        for key, data in items:
            #print(str(key) + " VS" + str(_currentViewCursor) )
            if key>_currentViewCursor:
                #print("newrow")
                
                
                _icon = self.allIcons['info']
                
                
                _type=data[0]
                #print(_type)
                #print(self._display)
                
                
                _foundInFilter=False
                
                for _t in  self._display:
                    if _type.__contains__(_t):
                        _foundInFilter=True
                
                #if not _foundInFilter:
                #    continue
                    
                
                
                if self.allIcons.__contains__(data[0].lower()):
                    _icon= self.allIcons[data[0].lower()]
                
                
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
        
        
        if alloptions.__contains__('info'):
            self.m_auiToolBar1.ToggleTool(self.m_showInfos.GetId(), True)
            
        if alloptions.__contains__('message') or alloptions.__contains__('msg') :
            self.m_auiToolBar1.ToggleTool(self.m_showMessages.GetId(), True)
             
        if alloptions.__contains__('warning'):
            self.m_auiToolBar1.ToggleTool(self.m_showWarnings.GetId(), True)
        
        if alloptions.__contains__('error'):
            self.m_auiToolBar1.ToggleTool(self.m_showErrors.GetId(), True)
              
        self._display = alloptions
        
        
    def OnViewOptionsChanged(self, evt):
        #GetToolToggled
        myPlugin = self.parent_frame.GetPlugin("General")
        alloptions = []
        
        if self.m_auiToolBar1.GetToolToggled(self.m_showInfos.GetId()):
            alloptions.append('info')
            
            
        if self.m_auiToolBar1.GetToolToggled(self.m_showMessages.GetId()):
            alloptions.append('msg')
           
            
        if self.m_auiToolBar1.GetToolToggled(self.m_showWarnings.GetId()):
            alloptions.append('warning')
           
            
        if self.m_auiToolBar1.GetToolToggled(self.m_showErrors.GetId()):
            alloptions.append('error')
           
        
        self._display = alloptions
        
        
        
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
        