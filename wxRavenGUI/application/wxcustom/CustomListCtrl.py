import wx
import wx.lib.mixins.listctrl as listmix

"""

This file intend to create some quick custom control to enhance some basics components

"""

#
#    Was a test list control with autocolumn size a default style
#
class TestListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        
        
    
        
 
#
#    a better name for the same controle as above.
#    an example of usage in the plugin 'general' : the error console log
#       
class wxRavenListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        
        
class wxRavenVirtualListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.LC_REPORT|wx.LC_VIRTUAL|wx.LC_HRULES|wx.LC_VRULES):
        wx.ListCtrl.__init__(self, parent, ID, pos=wx.DefaultPosition, size=size, style=style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)
        self._parentPanel = parent
        
    def OnGetItemText(self, item, col):
        return self._parentPanel.OnGetItemText(item, col)
        #print(f'OnGetItemText {item} {col}')
        #return self.itemDataMap[item][col]

    def OnGetItemImage(self, item):
        return self._parentPanel.OnGetItemImage(item)
        #_datas = self._datacache[item]
        #_icon = self.allIcons[_datas.getStatus().lower()]
        #return _icon
        '''
        if item % 3 == 0:
            return self.idx1
        else:
            return self.idx2
            
        '''

    def OnGetItemAttr(self, item):
        return self._parentPanel.OnGetItemAttr(item)
        
        
class wxRavenListCtrlPanel ( wx.Panel,listmix.ColumnSorterMixin ):
    
    def __init__( self, parent , id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 222,103 ), style = wx.TAB_TRAVERSAL):
        wx.Panel.__init__ ( self, parent, id , pos, size , style )
        self.list = None
        self.allIcons= {}
        self._curColumnSort =0
        
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetListCtrl(self):
        return self.list
    
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetSortImages(self):
        
        if self._curColumnSort ==0:
            return (self.allIcons['alphab_down'], self.allIcons['alphab_up'])
        else:
            return (self.allIcons['sort_down_2'], self.allIcons['sort_up_2'])