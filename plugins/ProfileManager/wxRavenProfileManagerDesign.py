# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class wxRaven_ProfileManager_SelectorDialog
###########################################################################

class wxRaven_ProfileManager_SelectorDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Select a Profile :", pos = wx.DefaultPosition, size = wx.Size( 484,213 ), style = wx.DEFAULT_DIALOG_STYLE|wx.DIALOG_NO_PARENT|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRaven_ProfileManager_Selector
###########################################################################

class wxRaven_ProfileManager_Selector ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 526,207 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRaven_ProfileManager_Selector_ProfileItem
###########################################################################

class wxRaven_ProfileManager_Selector_ProfileItem ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 143,184 ), style = wx.TAB_TRAVERSAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_profileButton = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/avatar_3.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer3.Add( self.m_profileButton, 1, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_profileLabel = wx.StaticText( self, wx.ID_ANY, u"Profile Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_profileLabel.Wrap( -1 )
		self.m_profileLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer4.Add( self.m_profileLabel, 1, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
	
	def __del__( self ):
		pass
	

