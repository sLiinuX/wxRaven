'''
Created on 15 déc. 2021

@author: slinux
'''

from .wxRavenGeneralDesign import *


import wx.lib as lib
import wx.lib.mixins.listctrl as listmix











class RavenErrorLogConsole(wxRavenErrorLogConsolePanel):
    '''
    classdocs
    '''


    view_base_name = "Error Log Console"
    view_name = "Error Log Console"
    parent_frame = None
    default_position = "mgr"
    
    
    icon = wx.Bitmap( u"res/default_style/normal/error_log.png", wx.BITMAP_TYPE_ANY )
    
    
    
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
        
        
        
        
        self.allIcons = { }
        
        self.InitConsoleLog()
        
        
        parentFrame.Add(self, self.view_name ,position, self.icon)
        
        
        
        self._logCurrentCursor = -1
        
        #self.dummyTest()
        
        self.SetAutoLayout(True)
    
    
    
    
    
    def UpdateView(self):
        
        
        #print("RavenErrorLogConsole Update !")
        
        _allLogs = self.parent_frame.GetPluginData("General","allLogs")
        
        
        _currentViewCursor = self._logCurrentCursor
        
        items = _allLogs.items()
        for key, data in items:
            #print(str(key) + " VS" + str(_currentViewCursor) )
            if key>_currentViewCursor:
                #print("newrow")
                
                
                _icon = self.allIcons['info']
                
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
                self.m_listCtrl1.SetItemData(index, key)
                
                _currentViewCursor = _currentViewCursor +1
          
        self._logCurrentCursor = _currentViewCursor
         
    
    
    
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

        info.Align = 0
        info.Text = "Date"
        self.m_listCtrl1.InsertColumn(2, info)
        
        
        
        
        
        self.m_listCtrl1.SetColumnWidth(0, 200)
        self.m_listCtrl1.SetColumnWidth(1, 100)
        self.m_listCtrl1.SetColumnWidth(2, 50)
        
        
        self.il = wx.ImageList(16, 16)

        self.allIcons['error'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/error_tsk.png", wx.BITMAP_TYPE_ANY ))
        self.allIcons['info'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/info_obj.png", wx.BITMAP_TYPE_ANY ))
        self.allIcons['msg'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY ))
        self.allIcons['warning'] = self.il.Add(wx.Bitmap( u"res/default_style/normal/warning_obj.png", wx.BITMAP_TYPE_ANY ))
        
        self.m_listCtrl1.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        
       
        #listmix.ListCtrlAutoWidthMixin.__init__(self.m_listCtrl1)
        
        
        #self.setResizeColumn(0)
        #self.bSizer1.Add(self.list, 1, wx.EXPAND)
        