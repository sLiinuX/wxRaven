'''
Created on 17 déc. 2021

@author: slinux
'''

from .wxRavenSquawkerDesign import *

class testPanel(basicTestMessageRead):
    '''
    classdocs
    '''
    view_base_name = "SquawkerTest"
    view_name = "SquawkerTest"
    parent_frame = None
    default_position = "main"
    
    icon = wx.Bitmap( u"res/default_style/normal/message.png", wx.BITMAP_TYPE_ANY )
    

    def __init__(self, parentFrame, position = "main", viewName= "SquawkerTest"):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        #parentFrame.AddInNotebook(self, self.plugin_name,parentFrame.wxRavenToolBook3 , self.icon)
        self.view_base_name = "SquawkerTest"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        parentFrame.Add(self, self.view_name ,position, self.icon)

    
    
    def UpdateView(self):
        
        
        try:
          
            _lastMessage = self.parent_frame.GetPluginData("Squawker","_lastMessage")
            
            self.m_textCtrl1.SetValue(str(_lastMessage))
        
        except Exception as e:
            print("updatePanel getData ERROR> " + str(e))
        
        self.Layout()