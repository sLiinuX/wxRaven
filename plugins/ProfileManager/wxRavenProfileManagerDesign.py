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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Select a Profile :", pos = wx.DefaultPosition, size = wx.Size( 593,213 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_DIALOG_STYLE|wx.DIALOG_NO_PARENT|wx.RESIZE_BORDER|wx.STAY_ON_TOP )
		
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
	

###########################################################################
## Class wxRaven_ProfileManager_SettingPanel
###########################################################################

class wxRaven_ProfileManager_SettingPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,403 ), style = wx.TAB_TRAVERSAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/UserAccount_custom.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_bitmap1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Profile Options :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer6.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/avatar_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_bitmap2, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Customize your Raven :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer10.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_slider1 = wx.Slider( self.m_panel1, wx.ID_ANY, -100, -100, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL )
		bSizer10.Add( self.m_slider1, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_sliderR = wx.Slider( self.m_panel1, wx.ID_ANY, 200, 0, 200, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL )
		bSizer11.Add( self.m_sliderR, 1, wx.ALL, 5 )
		
		self.m_sliderG = wx.Slider( self.m_panel1, wx.ID_ANY, 200, 0, 200, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL )
		bSizer11.Add( self.m_sliderG, 1, wx.ALL, 5 )
		
		self.m_sliderB = wx.Slider( self.m_panel1, wx.ID_ANY, 200, 0, 200, wx.DefaultPosition, wx.DefaultSize, wx.SL_AUTOTICKS|wx.SL_HORIZONTAL )
		bSizer11.Add( self.m_sliderB, 1, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_saveButton = wx.Button( self.m_panel1, wx.ID_ANY, u"Save My Avatar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_saveButton, 0, wx.ALL, 5 )
		
		self.m_buttonReload = wx.Button( self.m_panel1, wx.ID_ANY, u"Reload My Avatar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_buttonReload, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer12, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel1.SetSizer( bSizer10 )
		self.m_panel1.Layout()
		bSizer10.Fit( self.m_panel1 )
		bSizer9.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer61 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap11 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/folder.gif", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer61.Add( self.m_bitmap11, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Profile Folder :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		bSizer61.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.m_PathText = wx.StaticText( self, wx.ID_ANY, u"<PATH>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_PathText.Wrap( -1 )
		bSizer61.Add( self.m_PathText, 1, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer61, 0, wx.EXPAND, 5 )
		
		self.m_staticline111 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline111, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		# Connect Events
		self.m_slider1.Bind( wx.EVT_SCROLL, self.OnSlideChange )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSlideChange( self, event ):
		event.Skip()
	

