# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 697,387 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_auiToolBar1 = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT )
		self.m_bitmap17 = wx.StaticBitmap( self.m_auiToolBar1, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/filter_ps.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_auiToolBar1.AddControl( self.m_bitmap17 )
		self.m_showInfos = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/logtype_info.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Show 'Informations' Logs", wx.EmptyString, None )

		self.m_showMessages = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/logtype_msg.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Show 'Messages' Logs", wx.EmptyString, None )

		self.m_showWarnings = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/logtype_warning.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Show 'Warnings' Logs", wx.EmptyString, None )

		self.m_showErrors = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/logtype_error.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Show 'Errors' Logs", wx.EmptyString, None )

		self.m_auiToolBar1.AddSeparator()

		self.m_showDebug = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/debug_exc.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None )

		self.m_tool5 = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/view_menu.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_auiToolBar1.Realize()

		bSizer1.Add( self.m_auiToolBar1, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_listCtrl1 = wxRavenListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer1.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.Bind( wx.aui.EVT_AUI_PANE_CLOSE, self.OnAuiPaneClose )
		self.Bind( wx.aui.EVT_AUI_PANE_RESTORE, self.OnAuiPaneRestore )
		self.Bind( wx.aui.EVT_AUI_RENDER, self.OnAuiPaneRender )
		self.Bind( wx.EVT_TOOL, self.OnViewOptionsChanged, id = self.m_showInfos.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnViewOptionsChanged, id = self.m_showMessages.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnViewOptionsChanged, id = self.m_showWarnings.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnViewOptionsChanged, id = self.m_showErrors.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnViewOptionsChanged, id = self.m_showDebug.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnAuiPaneClose( self, event ):
		event.Skip()

	def OnAuiPaneRestore( self, event ):
		event.Skip()

	def OnAuiPaneRender( self, event ):
		event.Skip()

	def OnViewOptionsChanged( self, event ):
		event.Skip()






###########################################################################
## Class wxRavenDebugConsolePanel
###########################################################################

class wxRavenDebugConsolePanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 575,332 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer131 = wx.BoxSizer( wx.VERTICAL )

		self.m_debugLog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer131.Add( self.m_debugLog, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer131 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxNotebookToolbar
###########################################################################

class wxNotebookToolbar ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 513,308 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )

		bSizer2.Add( self.m_auinotebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.m_auinotebook1.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnPageClose( self, event ):
		event.Skip()


###########################################################################
## Class wxRavenWelcomeTab
###########################################################################

class wxRavenWelcomeTab ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 947,544 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

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

		self.m_staticText3.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer9.Add( self.m_staticText3, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer9, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self.imagePanel, wx.ID_ANY, u"Getting started with wxRaven from this welcome page !\nYour may want to have a look on the preferences / settings before starting your exploration of the Ravencoin Blockchain.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
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

		self.m_staticText14.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer24.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer11.Add( bSizer24, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_richText1 = wx.richtext.RichTextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.WANTS_CHARS|wx.BORDER_NONE )
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

		self.m_staticText141.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer241.Add( self.m_staticText141, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer111.Add( bSizer241, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer251 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel12 = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer40 = wx.BoxSizer( wx.VERTICAL )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bpButton13 = wx.BitmapButton( self.m_panel12, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton13.SetBitmap( wx.Bitmap( u"res/default_style/normal/search_45.png", wx.BITMAP_TYPE_ANY ) )
		bSizer41.Add( self.m_bpButton13, 0, wx.ALL, 5 )

		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText20 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Search Asset on the Ravencoin Network", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer45.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"     The Quickest wat to find an asset and start navigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		self.m_staticText23.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer45.Add( self.m_staticText23, 0, wx.ALL, 1 )


		bSizer41.Add( bSizer45, 1, wx.EXPAND, 5 )


		bSizer40.Add( bSizer41, 0, wx.EXPAND, 5 )

		bSizer411 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bpButton131 = wx.BitmapButton( self.m_panel12, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton131.SetBitmap( wx.Bitmap( u"res/default_style/normal/navigate_45.png", wx.BITMAP_TYPE_ANY ) )
		bSizer411.Add( self.m_bpButton131, 0, wx.ALL, 5 )

		bSizer451 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText201 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Navigate in Asset Tree", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )

		self.m_staticText201.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer451.Add( self.m_staticText201, 0, wx.ALL, 5 )

		self.m_staticText231 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"     Consult and  Preview Assets, Store bookmarks.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText231.Wrap( -1 )

		self.m_staticText231.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer451.Add( self.m_staticText231, 0, wx.ALL, 1 )


		bSizer411.Add( bSizer451, 1, wx.EXPAND, 5 )


		bSizer40.Add( bSizer411, 0, wx.EXPAND, 5 )

		bSizer4111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bpButton1311 = wx.BitmapButton( self.m_panel12, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton1311.SetBitmap( wx.Bitmap( u"res/default_style/normal/wallet_45.png", wx.BITMAP_TYPE_ANY ) )
		bSizer4111.Add( self.m_bpButton1311, 0, wx.ALL, 5 )

		bSizer4511 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2011 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Consult your Wallet", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2011.Wrap( -1 )

		self.m_staticText2011.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer4511.Add( self.m_staticText2011, 0, wx.ALL, 5 )

		self.m_staticText2311 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"     Consult your wallet balances, including assets", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2311.Wrap( -1 )

		self.m_staticText2311.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer4511.Add( self.m_staticText2311, 0, wx.ALL, 1 )


		bSizer4111.Add( bSizer4511, 1, wx.EXPAND, 5 )


		bSizer40.Add( bSizer4111, 0, wx.EXPAND, 5 )

		bSizer41111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bpButton13111 = wx.BitmapButton( self.m_panel12, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton13111.SetBitmap( wx.Bitmap( u"res/default_style/normal/issue_45.png", wx.BITMAP_TYPE_ANY ) )
		bSizer41111.Add( self.m_bpButton13111, 0, wx.ALL, 5 )

		bSizer45111 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText20111 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Issue an Asset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20111.Wrap( -1 )

		self.m_staticText20111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer45111.Add( self.m_staticText20111, 0, wx.ALL, 5 )

		self.m_staticText23111 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"     Already have an IPFS to submit ?!\n     Quick, Simple, Issue an Asset here !\n     ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23111.Wrap( -1 )

		self.m_staticText23111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer45111.Add( self.m_staticText23111, 0, wx.ALL|wx.EXPAND, 1 )


		bSizer41111.Add( bSizer45111, 1, wx.EXPAND, 5 )


		bSizer40.Add( bSizer41111, 1, wx.EXPAND, 5 )


		self.m_panel12.SetSizer( bSizer40 )
		self.m_panel12.Layout()
		bSizer40.Fit( self.m_panel12 )
		bSizer34.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 15 )


		self.m_scrolledWindow1.SetSizer( bSizer34 )
		self.m_scrolledWindow1.Layout()
		bSizer34.Fit( self.m_scrolledWindow1 )
		bSizer251.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


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

		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

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
		self.m_bpButton13111.Bind( wx.EVT_BUTTON, self.OnIssueAsset )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def UpdateUI( self, event ):
		event.Skip()


	def OnSearch( self, event ):
		event.Skip()

	def OnNavigate( self, event ):
		event.Skip()

	def OnWallet( self, event ):
		event.Skip()

	def OnIssueAsset( self, event ):
		event.Skip()


###########################################################################
## Class ApplicationSettingPanel
###########################################################################

class ApplicationSettingPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 594,548 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer6212 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap18 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/view_default_frame.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6212.Add( self.m_bitmap18, 0, wx.ALL, 5 )

		self.m_staticText362 = wx.StaticText( self, wx.ID_ANY, u"Graphical Interface :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText362.Wrap( -1 )

		self.m_staticText362.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6212.Add( self.m_staticText362, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer3.Add( bSizer6212, 0, wx.EXPAND, 5 )

		bSizer62121 = wx.BoxSizer( wx.HORIZONTAL )

		m_radioBox1Choices = [ u"Simple View", u"Advanced View" ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"Choose a mode :", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_ROWS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer62121.Add( self.m_radioBox1, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer62121, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer62122 = wx.BoxSizer( wx.HORIZONTAL )

		self.modeIllustrationBmp = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/app_simple_mode.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer62122.Add( self.modeIllustrationBmp, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer3.Add( bSizer62122, 1, wx.EXPAND, 5 )

		bSizer62113 = wx.BoxSizer( wx.HORIZONTAL )

		self.defaultAreaOptionPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText451 = wx.StaticText( self.defaultAreaOptionPanel, wx.ID_ANY, u"Select a default area :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText451.Wrap( -1 )

		self.m_staticText451.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer111.Add( self.m_staticText451, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		defaultAreaChoiceListChoices = [ u"main", u"mgr", wx.EmptyString ]
		self.defaultAreaChoiceList = wx.Choice( self.defaultAreaOptionPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, defaultAreaChoiceListChoices, 0 )
		self.defaultAreaChoiceList.SetSelection( 0 )
		bSizer111.Add( self.defaultAreaChoiceList, 1, wx.ALL, 5 )


		self.defaultAreaOptionPanel.SetSizer( bSizer111 )
		self.defaultAreaOptionPanel.Layout()
		bSizer111.Fit( self.defaultAreaOptionPanel )
		bSizer62113.Add( self.defaultAreaOptionPanel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer3.Add( bSizer62113, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer6211 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap19 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6211.Add( self.m_bitmap19, 0, wx.ALL, 5 )

		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"Description :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )

		self.m_staticText45.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6211.Add( self.m_staticText45, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer3.Add( bSizer6211, 0, wx.EXPAND, 5 )

		bSizer62112 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer107 = wx.BoxSizer( wx.VERTICAL )

		self.descriptionText = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"The simple mode provide only one main areas where all views will be instanciated as a new tab in the notebook.\n\nThe main notebook allow simple placement of the different views, \nbut doesn't allow to create Floating panels.\n\nClosing a notebook page close completely the view.\nNotebook perspective is not saved yet between sessions.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.descriptionText.Wrap( -1 )

		bSizer107.Add( self.descriptionText, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_scrolledWindow2.SetSizer( bSizer107 )
		self.m_scrolledWindow2.Layout()
		bSizer107.Fit( self.m_scrolledWindow2 )
		bSizer62112.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 1 )


		bSizer3.Add( bSizer62112, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		# Connect Events
		self.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.OnModeSelectionChange )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnModeSelectionChange( self, event ):
		event.Skip()


###########################################################################
## Class GeneralSettingPanel
###########################################################################

class GeneralSettingPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 535,527 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer132 = wx.BoxSizer( wx.VERTICAL )

		bSizer6212 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap18 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/power_on.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6212.Add( self.m_bitmap18, 0, wx.ALL, 5 )

		self.m_staticText362 = wx.StaticText( self, wx.ID_ANY, u"Application Startup", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText362.Wrap( -1 )

		self.m_staticText362.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6212.Add( self.m_staticText362, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer132.Add( bSizer6212, 0, wx.EXPAND, 5 )

		bSizer1361 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBoxDisclaimer = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1361.Add( self.m_checkBoxDisclaimer, 0, wx.ALL, 5 )

		self.m_staticText681 = wx.StaticText( self, wx.ID_ANY, u"DO NOT Show Disclaimer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText681.Wrap( -1 )

		bSizer1361.Add( self.m_staticText681, 0, wx.ALL, 5 )


		bSizer132.Add( bSizer1361, 0, wx.EXPAND, 5 )

		bSizer136 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBoxWelcome = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer136.Add( self.m_checkBoxWelcome, 0, wx.ALL, 5 )

		self.m_staticText68 = wx.StaticText( self, wx.ID_ANY, u"DO NOT Show Welcome View", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )

		bSizer136.Add( self.m_staticText68, 0, wx.ALL, 5 )


		bSizer132.Add( bSizer136, 0, wx.EXPAND, 5 )

		bSizer1362 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBoxResume = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1362.Add( self.m_checkBoxResume, 0, wx.ALL, 5 )

		self.m_staticText682 = wx.StaticText( self, wx.ID_ANY, u"Resume views from previous session (if save option active)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText682.Wrap( -1 )

		bSizer1362.Add( self.m_staticText682, 0, wx.ALL, 5 )


		bSizer132.Add( bSizer1362, 0, wx.EXPAND, 5 )

		bSizer62121 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap181 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/power_off.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer62121.Add( self.m_bitmap181, 0, wx.ALL, 5 )

		self.m_staticText3621 = wx.StaticText( self, wx.ID_ANY, u"Application Shutdown", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3621.Wrap( -1 )

		self.m_staticText3621.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer62121.Add( self.m_staticText3621, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer132.Add( bSizer62121, 0, wx.EXPAND, 5 )

		bSizer136211 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBoxPurgeOnClose = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxPurgeOnClose.SetValue(True)
		bSizer136211.Add( self.m_checkBoxPurgeOnClose, 0, wx.ALL, 5 )

		self.m_staticText68211 = wx.StaticText( self, wx.ID_ANY, u"Purge hidden views", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68211.Wrap( -1 )

		bSizer136211.Add( self.m_staticText68211, 0, wx.ALL, 5 )


		bSizer132.Add( bSizer136211, 0, wx.EXPAND, 5 )

		bSizer13621 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBoxSaveSession = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBoxSaveSession.SetValue(True)
		bSizer13621.Add( self.m_checkBoxSaveSession, 0, wx.ALL, 5 )

		self.m_staticText6821 = wx.StaticText( self, wx.ID_ANY, u"Save Session (open views)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6821.Wrap( -1 )

		bSizer13621.Add( self.m_staticText6821, 0, wx.ALL, 5 )


		bSizer132.Add( bSizer13621, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer132 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxRavenConnexionSettings_SettingPanel
###########################################################################

class wxRavenConnexionSettings_SettingPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,374 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer113 = wx.BoxSizer( wx.VERTICAL )

		bSizer118 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Use the format :  connexion_name = user:password@ip:port\nExample : mainnet_localhost = mylogin:mypwd@127.0.0.1:8766", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_STATIC )
		self.m_staticText61.Wrap( -1 )

		bSizer118.Add( self.m_staticText61, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer113.Add( bSizer118, 0, wx.EXPAND, 5 )

		bSizer114 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer114.Add( self.m_bitmap4, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"My Connexions :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer114.Add( self.m_staticText12, 0, wx.ALL, 5 )

		bSizer115 = wx.BoxSizer( wx.VERTICAL )

		self.bookmark_text_area = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bookmark_text_area.SetMaxLength( 0 )
		bSizer115.Add( self.bookmark_text_area, 0, wx.ALL|wx.EXPAND, 5 )

		bookmark_listChoices = []
		self.bookmark_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bookmark_listChoices, 0 )
		bSizer115.Add( self.bookmark_list, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer114.Add( bSizer115, 1, wx.EXPAND, 5 )

		bSizer116 = wx.BoxSizer( wx.VERTICAL )

		self.bookmark_addbt = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bookmark_addbt.SetBitmap( wx.Bitmap( u"res/default_style/normal/add_plus.png", wx.BITMAP_TYPE_ANY ) )
		bSizer116.Add( self.bookmark_addbt, 0, wx.ALL, 5 )

		self.bookmark_rembt = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bookmark_rembt.SetBitmap( wx.Bitmap( u"res/default_style/normal/remove_minus.png", wx.BITMAP_TYPE_ANY ) )
		bSizer116.Add( self.bookmark_rembt, 0, wx.ALL, 5 )

		self.ipfs_provider_upbt = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.ipfs_provider_upbt.SetBitmap( wx.Bitmap( u"res/default_style/normal/prev_nav.png", wx.BITMAP_TYPE_ANY ) )
		self.ipfs_provider_upbt.Enable( False )

		bSizer116.Add( self.ipfs_provider_upbt, 0, wx.ALL, 5 )


		bSizer114.Add( bSizer116, 0, wx.EXPAND, 5 )

		bSizer117 = wx.BoxSizer( wx.VERTICAL )


		bSizer114.Add( bSizer117, 0, wx.EXPAND, 5 )


		bSizer113.Add( bSizer114, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer113 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxRavenConnexionRelaysSettings_SettingPanel
###########################################################################

class wxRavenConnexionRelaysSettings_SettingPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,374 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer113 = wx.BoxSizer( wx.VERTICAL )

		bSizer118 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Use the format :  connexion_name = user:password@ip:port\nExample : wxRaven_Relay1 = mylogin:mypwd@127.0.0.1:8766", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_STATIC )
		self.m_staticText61.Wrap( -1 )

		bSizer118.Add( self.m_staticText61, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer113.Add( bSizer118, 0, wx.EXPAND, 5 )

		bSizer114 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/connexion_share_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer114.Add( self.m_bitmap4, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"My Relays :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer114.Add( self.m_staticText12, 0, wx.ALL, 5 )

		bSizer115 = wx.BoxSizer( wx.VERTICAL )

		self.bookmark_text_area = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bookmark_text_area.SetMaxLength( 0 )
		bSizer115.Add( self.bookmark_text_area, 0, wx.ALL|wx.EXPAND, 5 )

		bookmark_listChoices = []
		self.bookmark_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bookmark_listChoices, 0 )
		bSizer115.Add( self.bookmark_list, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer114.Add( bSizer115, 1, wx.EXPAND, 5 )

		bSizer116 = wx.BoxSizer( wx.VERTICAL )

		self.bookmark_addbt = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bookmark_addbt.SetBitmap( wx.Bitmap( u"res/default_style/normal/add_plus.png", wx.BITMAP_TYPE_ANY ) )
		bSizer116.Add( self.bookmark_addbt, 0, wx.ALL, 5 )

		self.bookmark_rembt = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bookmark_rembt.SetBitmap( wx.Bitmap( u"res/default_style/normal/remove_minus.png", wx.BITMAP_TYPE_ANY ) )
		bSizer116.Add( self.bookmark_rembt, 0, wx.ALL, 5 )

		self.ipfs_provider_upbt = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.ipfs_provider_upbt.SetBitmap( wx.Bitmap( u"res/default_style/normal/prev_nav.png", wx.BITMAP_TYPE_ANY ) )
		self.ipfs_provider_upbt.Enable( False )

		bSizer116.Add( self.ipfs_provider_upbt, 0, wx.ALL, 5 )


		bSizer114.Add( bSizer116, 0, wx.EXPAND, 5 )

		bSizer117 = wx.BoxSizer( wx.VERTICAL )


		bSizer114.Add( bSizer117, 0, wx.EXPAND, 5 )


		bSizer113.Add( bSizer114, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer113 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxRavenPluginsSettings_SettingPanel
###########################################################################

class wxRavenPluginsSettings_SettingPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,374 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer113 = wx.BoxSizer( wx.VERTICAL )

		bSizer1181 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap19 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/ravencoin.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1181.Add( self.m_bitmap19, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"Software Edition :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )

		self.m_staticText38.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1181.Add( self.m_staticText38, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_choiceEditionChoices = []
		self.m_choiceEdition = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceEditionChoices, 0 )
		self.m_choiceEdition.SetSelection( 0 )
		bSizer1181.Add( self.m_choiceEdition, 1, wx.ALL, 5 )


		bSizer113.Add( bSizer1181, 0, wx.EXPAND, 5 )

		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer113.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer118 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Check in the list below the plugin you want to DISABLE.\nThis additional option is only available in Developer/Server Mode.", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.BORDER_STATIC )
		self.m_staticText61.Wrap( -1 )

		bSizer118.Add( self.m_staticText61, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer113.Add( bSizer118, 0, wx.EXPAND, 5 )

		bSizer114 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/install-handler.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer114.Add( self.m_bitmap4, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"All Plugins :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer114.Add( self.m_staticText12, 0, wx.ALL, 5 )

		bSizer115 = wx.BoxSizer( wx.VERTICAL )

		m_pluginCheckListboxChoices = []
		self.m_pluginCheckListbox = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_pluginCheckListboxChoices, 0 )
		bSizer115.Add( self.m_pluginCheckListbox, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer114.Add( bSizer115, 1, wx.EXPAND, 5 )

		bSizer117 = wx.BoxSizer( wx.VERTICAL )


		bSizer114.Add( bSizer117, 0, wx.EXPAND, 5 )


		bSizer113.Add( bSizer114, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer113 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxRaven_General_WalletSettings
###########################################################################

class wxRaven_General_WalletSettings ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer154 = wx.BoxSizer( wx.VERTICAL )

		bSizer6212 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap18 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/wallet.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6212.Add( self.m_bitmap18, 0, wx.ALL, 5 )

		self.m_staticText362 = wx.StaticText( self, wx.ID_ANY, u"Wallet Operations", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText362.Wrap( -1 )

		self.m_staticText362.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer6212.Add( self.m_staticText362, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_bitmap31 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6212.Add( self.m_bitmap31, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_NetworkChoiceChoices = []
		self.m_NetworkChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_NetworkChoiceChoices, 0 )
		self.m_NetworkChoice.SetSelection( 0 )
		bSizer6212.Add( self.m_NetworkChoice, 1, wx.ALL, 5 )


		bSizer154.Add( bSizer6212, 0, wx.EXPAND, 5 )

		self.m_staticline7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer154.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer158 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox15 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox15.SetValue(True)
		self.m_checkBox15.Enable( False )

		bSizer158.Add( self.m_checkBox15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText83 = wx.StaticText( self, wx.ID_ANY, u"Favorite address for transactions :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		bSizer158.Add( self.m_staticText83, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_bitmap26 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/mail_send.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer158.Add( self.m_bitmap26, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_AddrSendChoiceChoices = []
		self.m_AddrSendChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AddrSendChoiceChoices, 0 )
		self.m_AddrSendChoice.SetSelection( 0 )
		bSizer158.Add( self.m_AddrSendChoice, 1, wx.ALL, 5 )


		bSizer154.Add( bSizer158, 0, wx.EXPAND, 5 )

		bSizer1581 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox151 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox151.SetValue(True)
		self.m_checkBox151.Enable( False )

		bSizer1581.Add( self.m_checkBox151, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText831 = wx.StaticText( self, wx.ID_ANY, u"Favorite address for receiving :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText831.Wrap( -1 )

		bSizer1581.Add( self.m_staticText831, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_bitmap261 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/mail_in_green.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1581.Add( self.m_bitmap261, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_AddreReceiveChoiceChoices = []
		self.m_AddreReceiveChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AddreReceiveChoiceChoices, 0 )
		self.m_AddreReceiveChoice.SetSelection( 0 )
		bSizer1581.Add( self.m_AddreReceiveChoice, 1, wx.ALL, 5 )


		bSizer154.Add( bSizer1581, 0, wx.EXPAND, 5 )

		bSizer15811 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox1511 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1511.SetValue(True)
		self.m_checkBox1511.Enable( False )

		bSizer15811.Add( self.m_checkBox1511, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText8311 = wx.StaticText( self, wx.ID_ANY, u"Favorite address for change :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8311.Wrap( -1 )

		bSizer15811.Add( self.m_staticText8311, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_bitmap2611 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/mail_in_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15811.Add( self.m_bitmap2611, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_AddrChangeChoiceChoices = []
		self.m_AddrChangeChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AddrChangeChoiceChoices, 0 )
		self.m_AddrChangeChoice.SetSelection( 0 )
		bSizer15811.Add( self.m_AddrChangeChoice, 1, wx.ALL, 5 )


		bSizer154.Add( bSizer15811, 0, wx.EXPAND, 5 )

		bSizer165 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText88 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )

		bSizer165.Add( self.m_staticText88, 1, wx.ALL, 5 )

		self.m_SaveNetwork = wx.Button( self, wx.ID_ANY, u"Save Network Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer165.Add( self.m_SaveNetwork, 0, wx.ALL, 5 )


		bSizer154.Add( bSizer165, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer154 )
		self.Layout()

	def __del__( self ):
		pass


