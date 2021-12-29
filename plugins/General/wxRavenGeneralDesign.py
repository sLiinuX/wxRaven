# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
from wxRavenGUI.application.wxcustom.CustomListCtrl import *
import wx.richtext

###########################################################################
## Class wxRavenErrorLogConsolePanel
###########################################################################

class wxRavenErrorLogConsolePanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 697,387 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auiToolBar1 = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_tool1 = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/export_log.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool2 = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/import_log.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
		self.m_auiToolBar1.SetToolDropDown( self.m_tool2.GetId(), True );
		
		
		self.m_auiToolBar1.AddSeparator()
		
		self.m_tool3 = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/clear_co.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar1.AddSeparator()
		
		self.m_tool4 = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/restore_log.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool5 = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/view_menu.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar1.Realize() 
		
		bSizer1.Add( self.m_auiToolBar1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_listCtrl1 = wxRavenListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer1.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxNotebookToolbar
###########################################################################

class wxNotebookToolbar ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 513,308 ), style = wx.TAB_TRAVERSAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		
		bSizer2.Add( self.m_auinotebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		# Connect Events
		self.m_auinotebook1.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnPageClose( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenWelcomeTab
###########################################################################

class wxRavenWelcomeTab ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 852,611 ), style = wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.imagePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.imagePanel.SetMaxSize( wx.Size( -1,250 ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self.imagePanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/logosquare.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_bitmap3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.imagePanel, wx.ID_ANY, u"Welcome to wxRaven,", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetFont( wx.Font( 10, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer9.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer9, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self.imagePanel, wx.ID_ANY, u"Getting started with wxRaven from this welcome page !\nYour may want to have a look on the preferences / settings before starting your exploration of the Ravencoin Blockchain.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText6.Wrap( -1 )
		bSizer10.Add( self.m_staticText6, 1, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		
		self.imagePanel.SetSizer( bSizer7 )
		self.imagePanel.Layout()
		bSizer7.Fit( self.imagePanel )
		bSizer5.Add( self.imagePanel, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 2 )
		
		
		bSizer4.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.GridMainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_panel3 = wx.Panel( self.GridMainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetMinSize( wx.Size( -1,150 ) )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap4 = wx.StaticBitmap( self.m_panel3, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/changelog_obj.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_bitmap4, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"What's New ?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		self.m_staticText14.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer24.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer11.Add( bSizer24, 0, wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_richText1 = wx.richtext.RichTextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer25.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 1 )
		
		
		bSizer11.Add( bSizer25, 1, wx.EXPAND, 1 )
		
		
		self.m_panel3.SetSizer( bSizer11 )
		self.m_panel3.Layout()
		bSizer11.Fit( self.m_panel3 )
		gSizer1.Add( self.m_panel3, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel8 = wx.Panel( self.GridMainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer111 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap41 = wx.StaticBitmap( self.m_panel8, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/quick_actions.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer241.Add( self.m_bitmap41, 0, wx.ALL, 5 )
		
		self.m_staticText141 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Getting Started !", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )
		self.m_staticText141.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer241.Add( self.m_staticText141, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer111.Add( bSizer241, 0, wx.EXPAND, 5 )
		
		bSizer251 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel9 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel12 = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bpButton13 = wx.BitmapButton( self.m_panel12, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/search_45.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer41.Add( self.m_bpButton13, 0, wx.ALL, 5 )
		
		bSizer45 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText20 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Search Asset on the Ravencoin Network", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		self.m_staticText20.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer45.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"     The Quickest wat to find an asset and start navigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		self.m_staticText23.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		bSizer45.Add( self.m_staticText23, 0, wx.ALL, 0 )
		
		
		bSizer41.Add( bSizer45, 1, wx.EXPAND, 5 )
		
		
		bSizer40.Add( bSizer41, 0, wx.EXPAND, 5 )
		
		bSizer411 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bpButton131 = wx.BitmapButton( self.m_panel12, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/navigate_45.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer411.Add( self.m_bpButton131, 0, wx.ALL, 5 )
		
		bSizer451 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText201 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Navigate in Asset Tree", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )
		self.m_staticText201.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer451.Add( self.m_staticText201, 0, wx.ALL, 5 )
		
		self.m_staticText231 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"     Consult and  Preview Assets, Store bookmarks.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText231.Wrap( -1 )
		self.m_staticText231.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		bSizer451.Add( self.m_staticText231, 0, wx.ALL, 0 )
		
		
		bSizer411.Add( bSizer451, 1, wx.EXPAND, 5 )
		
		
		bSizer40.Add( bSizer411, 0, wx.EXPAND, 5 )
		
		bSizer4111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bpButton1311 = wx.BitmapButton( self.m_panel12, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/wallet_45.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer4111.Add( self.m_bpButton1311, 0, wx.ALL, 5 )
		
		bSizer4511 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2011 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Consult your Wallet", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2011.Wrap( -1 )
		self.m_staticText2011.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer4511.Add( self.m_staticText2011, 0, wx.ALL, 5 )
		
		self.m_staticText2311 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"     Consult your wallet balances, including assets", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2311.Wrap( -1 )
		self.m_staticText2311.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		bSizer4511.Add( self.m_staticText2311, 0, wx.ALL, 0 )
		
		
		bSizer4111.Add( bSizer4511, 1, wx.EXPAND, 5 )
		
		
		bSizer40.Add( bSizer4111, 1, wx.EXPAND, 5 )
		
		
		self.m_panel12.SetSizer( bSizer40 )
		self.m_panel12.Layout()
		bSizer40.Fit( self.m_panel12 )
		bSizer34.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 15 )
		
		
		self.m_panel9.SetSizer( bSizer34 )
		self.m_panel9.Layout()
		bSizer34.Fit( self.m_panel9 )
		bSizer251.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer111.Add( bSizer251, 1, wx.EXPAND, 1 )
		
		
		self.m_panel8.SetSizer( bSizer111 )
		self.m_panel8.Layout()
		bSizer111.Fit( self.m_panel8 )
		gSizer1.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.GridMainPanel.SetSizer( gSizer1 )
		self.GridMainPanel.Layout()
		gSizer1.Fit( self.GridMainPanel )
		bSizer6.Add( self.GridMainPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap9 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/warning_obj.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_bitmap9, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Warning : This software is still in development and may contains un-finished features, non-working icons and bugs !", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer8.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer8, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer4.Add( bSizer6, 5, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_SIZE, self.UpdateUI )
		self.Bind( wx.EVT_UPDATE_UI, self.UpdateUI )
		self.m_bpButton13.Bind( wx.EVT_BUTTON, self.OnSearch )
		self.m_bpButton131.Bind( wx.EVT_BUTTON, self.OnNavigate )
		self.m_bpButton1311.Bind( wx.EVT_BUTTON, self.OnWallet )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def UpdateUI( self, event ):
		event.Skip()
	
	
	def OnSearch( self, event ):
		event.Skip()
	
	def OnNavigate( self, event ):
		event.Skip()
	
	def OnWallet( self, event ):
		event.Skip()
	

###########################################################################
## Class GeneralSettingPanel
###########################################################################

class GeneralSettingPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		m_comboBox1Choices = []
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		bSizer3.Add( self.m_comboBox1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
	
	def __del__( self ):
		pass
	

