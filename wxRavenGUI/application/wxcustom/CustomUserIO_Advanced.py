'''
Created on 24 janv. 2022

@author: slinux
'''
import wx
from .wxCustomComponentDesign import wxRavenMessageDialog

class wxRavenAdvancedMessageDialog(wxRavenMessageDialog):
    
    
    def __init__(self, parentframe, message, type='info', msgdetails='', showCancel=False):
        super().__init__(parentframe)
        
        
        
        
        self.icons={
            'info':parentframe.RessourcesProvider.GetImage('info_icon_45'),
            'warning':parentframe.RessourcesProvider.GetImage('warning_icon_45'),
            'error':parentframe.RessourcesProvider.GetImage('error_icon_45'),
            'success':parentframe.RessourcesProvider.GetImage('success_icon_45')
            }
        
        self._expanded=True
        self.m_messageText.SetLabel(message)
        self.m_messageIcon.SetBitmap(self.icons[type])
        if msgdetails =='':
            self.m_textCtrl1.SetValue(msgdetails)
            self.m_ExpandButton.Enable(enable=False)
            self.m_detailsPanel.Hide()
            
            self.m_staticText2.Hide()
            self.m_ExpandButton.Hide()
            
            self._expanded=False
        else:
            self.m_textCtrl1.SetValue(msgdetails)
            self.OnExpand(None)
        
            
        if not showCancel:
            self.m_CancelButton.Hide()
            
        self.Layout()
        self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
        
        
        
        self.m_ExpandButton.Bind(wx.EVT_BUTTON, self.OnExpand)
        self.m_OKButton.Bind(wx.EVT_BUTTON, self.OnOkClicked)
        self.m_CancelButton.Bind(wx.EVT_BUTTON, self.OnCancelClicked)
        
        
        
    def OnOkClicked(self, evt=None):
        self.EndModal(wx.OK)
    
    
    def OnCancelClicked(self, evt=None):
        self.EndModal(wx.CANCEL)
    
        
        
        
    def OnExpand(self, evt=None):  
        self._expanded = not self._expanded 
        
        
        if self._expanded:
            self.m_detailsPanel.Show()
        else:
            self.m_detailsPanel.Hide()
        self.Layout()
        self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
        
        