# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wxRavenGUI.application.wxcustom.CustomListCtrl import *

###########################################################################
## Class wxRavenAssetExplorer
###########################################################################

class wxRavenAssetExplorer ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 596,352 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		bSizer2.Add( self.m_searchCtrl1, 10, wx.ALL, 5 )
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/filter_ps.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.m_bpButton1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		self.searchOptionsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.searchopt_strictmode = wx.CheckBox( self.searchOptionsPanel, wx.ID_ANY, u"Name must match exactly (strict search)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.searchopt_strictmode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.searchopt_onlymain = wx.CheckBox( self.searchOptionsPanel, wx.ID_ANY, u"Only Main-Assets", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.searchopt_onlymain, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self.searchOptionsPanel, wx.ID_ANY, u"Max Result :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.searchopt_maxresults = wx.SpinCtrl( self.searchOptionsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), wx.SP_ARROW_KEYS, 1, 500, 50 )
		bSizer3.Add( self.searchopt_maxresults, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer3, 0, 0, 0 )
		
		
		self.searchOptionsPanel.SetSizer( bSizer4 )
		self.searchOptionsPanel.Layout()
		bSizer4.Fit( self.searchOptionsPanel )
		bSizer1.Add( self.searchOptionsPanel, 0, wx.ALL|wx.EXPAND, 2 )
		
		self.m_listCtrl1 = wxRavenListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer1.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.resultControl = wx.InfoBar( self )
		self.resultControl.SetShowHideEffects( wx.SHOW_EFFECT_NONE, wx.SHOW_EFFECT_NONE )
		self.resultControl.SetEffectDuration( 500 )
		bSizer1.Add( self.resultControl, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		
		# Connect Events
		self.m_searchCtrl1.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnSearch )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT_ENTER, self.OnSearch )
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.ToggleFilterPanel )
		self.searchopt_strictmode.Bind( wx.EVT_CHECKBOX, self.SearchOptionsChanged )
		self.searchopt_onlymain.Bind( wx.EVT_CHECKBOX, self.SearchOptionsChanged )
		self.searchopt_maxresults.Bind( wx.EVT_SPINCTRL, self.SearchOptionsChanged )
		self.searchopt_maxresults.Bind( wx.EVT_TEXT, self.SearchOptionsChanged )
		self.Bind( wx.EVT_TIMER, self.OnTimerTick, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSearch( self, event ):
		event.Skip()
	
	
	def ToggleFilterPanel( self, event ):
		event.Skip()
	
	def SearchOptionsChanged( self, event ):
		event.Skip()
	
	
	
	
	def OnTimerTick( self, event ):
		event.Skip()
	

###########################################################################
## Class DONOTUSE_TestPanel
###########################################################################

class DONOTUSE_TestPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,150 ), wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer8.Add( self.m_panel2, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer7.Add( bSizer8, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
	
	def __del__( self ):
		pass
	

