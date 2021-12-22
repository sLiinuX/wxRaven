# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wx.adv import Animation, AnimationCtrl

###########################################################################
## Class wxBackgroundWorkerAnimation
###########################################################################

class wxBackgroundWorkerAnimationAAA ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_animCtrl1 = wx.animate.AnimationCtrl( self, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition, wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE )
		self.m_animCtrl1.LoadFile( u"res/default_style/normal/default_style/normal/ravencoin_asking_chain.gif" )
		
		self.m_animCtrl1.Play()
		bSizer1.Add( self.m_animCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	

