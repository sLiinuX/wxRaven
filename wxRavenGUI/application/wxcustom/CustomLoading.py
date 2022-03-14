'''
Created on 21 déc. 2021

@author: slinux
'''

import wx
import wx.xrc
from wx.adv import Animation, AnimationCtrl



class wxBackgroundWorkerAnimation ( wx.Panel ):
    
    def __init__( self, parent ):
        #wx.PopupWindow.__init__(self, parent, wx.SIMPLE_BORDER)
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 150,150 ), style = wx.TAB_TRAVERSAL )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        #self.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
        
        #self.m_animCtrl1 = Animation(u"res/default_style/normal/default_style/normal/ravencoin_asking_chain.gif" )
        ani = Animation(u"res/default_style/normal/ravencoin_asking_chain.gif" )
        self.m_animCtrl1 = AnimationCtrl(self, -1, ani , style=wx.EXPAND, size = wx.Size( 150,150 ))
          
        #self.m_animCtrl1.SetBackgroundColour(self.GetBackgroundColour())
        
        self.m_animCtrl1.Play()
        self.Center()
        
        bSizer1.Add( self.m_animCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.Layout()
    
    def __del__( self ):
        pass
    
    
    
    