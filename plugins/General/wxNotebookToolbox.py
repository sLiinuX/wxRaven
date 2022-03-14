'''
Created on 16 déc. 2021

@author: slinux
'''

from .wxRavenGeneralDesign import *
import wx.aui

class RavenNotebookToolbox(wxNotebookToolbar):
    '''
    classdocs
    '''


    view_base_name = "Notebook Toolbox"
    view_name = "Notebook Toolbox"
    parent_frame = None
    default_position = "mgr"
    
    
    #icon = wx.Bitmap( u"res/default_style/normal/tab_view.png", wx.BITMAP_TYPE_ANY )
    icon = 'tab_view'
    
    
    allIcons = {}
    
    

    def __init__(self, parentFrame, position = "mgr", viewName= "Notebook Toolbox"):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        self.view_base_name = "Notebook Toolbox"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        
        
        parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
        

        self.SetAutoLayout(True)

        self.m_auinotebook1.Bind(wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose)
    
    def AddPage(self,obj, title, icon):
        self.m_auinotebook1.AddPage(obj, title, bitmap = icon)
    
    def OnPageClose( self, event ):
        index = event.GetSelection()
        page = self.m_auinotebook1.GetPage(index)
        label = self.m_auinotebook1.GetPageText(index)
        #print("view instance to delete !")
        self.parent_frame.Plugins.DeleteViewInstance(label)
        wx.CallAfter(self.parent_frame.Views.__refreshGUI_Job__, ())
        event.Skip()
  
        
    def UpdateView(self):
        pass