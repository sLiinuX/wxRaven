'''
Created on 5 févr. 2022

@author: slinux
'''

import wx
import wx.adv



class wxRavenDatePicker(wx.adv.DatePickerCtrl):
    
    
    
    
    def __init__(self, parent, id, defdatetime, defposition, defsize, defstyle ):
        wx.adv.DatePickerCtrl.__init__(self, parent, size=(120,-1),
                                style = wx.adv.DP_DROPDOWN
                                      | wx.adv.DP_SHOWCENTURY
                                      | wx.adv.DP_ALLOWNONE )
    
        