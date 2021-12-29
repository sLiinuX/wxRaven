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
import wx.html2 as webview
import wx.aui

###########################################################################
## Class wxRavenAssetExplorer
###########################################################################

class wxRavenAssetExplorer ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 672,352 ), style = wx.TAB_TRAVERSAL )
		
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
		
		self.m_staticText1 = wx.StaticText( self.searchOptionsPanel, wx.ID_ANY, u"Max Result :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.searchopt_maxresults = wx.SpinCtrl( self.searchOptionsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), wx.SP_ARROW_KEYS, 1, 500, 50 )
		bSizer3.Add( self.searchopt_maxresults, 0, wx.ALL, 5 )
		
		self.searchopt_onlymain = wx.CheckBox( self.searchOptionsPanel, wx.ID_ANY, u"Filter Asset Type(s)...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.searchopt_onlymain, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.searchopt_strictmode = wx.CheckBox( self.searchOptionsPanel, wx.ID_ANY, u"Name must match exactly (strict search)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.searchopt_strictmode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
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
		self.searchopt_maxresults.Bind( wx.EVT_SPINCTRL, self.SearchOptionsChanged )
		self.searchopt_maxresults.Bind( wx.EVT_TEXT, self.SearchOptionsChanged )
		self.searchopt_onlymain.Bind( wx.EVT_CHECKBOX, self.SearchOptionsChanged )
		self.searchopt_strictmode.Bind( wx.EVT_CHECKBOX, self.SearchOptionsChanged )
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
## Class wxRavenHTMLViewer
###########################################################################

class wxRavenHTMLViewer ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 587,366 ), style = wx.TAB_TRAVERSAL )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.wv = webview.WebView.New(self)
		bSizer11.Add( self.wv, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenAssetNavigator
###########################################################################

class wxRavenAssetNavigator ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 966,541 ), style = wx.TAB_TRAVERSAL )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.navigatorToolboxPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auiToolBar2 = wx.aui.AuiToolBar( self.navigatorToolboxPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_saveBookmarkButton = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/save_bkmrk.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Save Bookmark List", wx.EmptyString, None ) 
		
		self.m_auiToolBar2.AddSeparator()
		
		self.m_addBookmarkButton = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/addbkmrk_co.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Add an Asset in Bookmark", wx.EmptyString, None ) 
		
		self.m_removeBookmarkButton = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/rembkmrk_co.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Remove Current Asset From Bookmark", wx.EmptyString, None ) 
		
		self.m_auiToolBar2.AddSeparator()
		
		self.m_useCacheButton = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/fastload.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Use Cache after first load", wx.EmptyString, None ) 
		
		self.m_auiToolBar2.Realize() 
		
		bSizer21.Add( self.m_auiToolBar2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.navigatorToolboxPanel.SetSizer( bSizer21 )
		self.navigatorToolboxPanel.Layout()
		bSizer21.Fit( self.navigatorToolboxPanel )
		bSizer12.Add( self.navigatorToolboxPanel, 0, wx.EXPAND |wx.ALL, 0 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/bookmarks_view.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_bitmap2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bookmarkChoiceListChoices = []
		self.bookmarkChoiceList = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bookmarkChoiceListChoices, 0 )
		self.bookmarkChoiceList.SetSelection( 0 )
		bSizer20.Add( self.bookmarkChoiceList, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_showBookmarkToolbarButton = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/view_menu.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_AUTODRAW )
		bSizer20.Add( self.m_showBookmarkToolbarButton, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( bSizer20, 0, wx.EXPAND, 5 )
		
		self.assetTreeView = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer14.Add( self.assetTreeView, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.treeExplorerToolboxPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auiToolBar4 = wx.aui.AuiToolBar( self.treeExplorerToolboxPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_staticText3 = wx.StaticText( self.m_auiToolBar4, wx.ID_ANY, u"EXPERIMENTAL : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_auiToolBar4.AddControl( self.m_staticText3 )
		self.m_TreeDisplayOption_OrganizeByMainAsset = self.m_auiToolBar4.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/reorg_main.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Reorganize Wallet by Main Asset", wx.EmptyString, None ) 
		
		self.m_auiToolBar4.AddSeparator()
		
		self.m_TreeDisplayOption_ReorganizeSubCat = self.m_auiToolBar4.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/reorg_virtual.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Reorganize Virtual Categories", wx.EmptyString, None ) 
		
		self.m_auiToolBar4.AddSeparator()
		
		self.m_TreeDisplayOption_ResetDisplay = self.m_auiToolBar4.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/synch_toc_nav.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Reset Display Options", wx.EmptyString, None ) 
		
		self.m_auiToolBar4.Realize() 
		
		bSizer22.Add( self.m_auiToolBar4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.treeExplorerToolboxPanel.SetSizer( bSizer22 )
		self.treeExplorerToolboxPanel.Layout()
		bSizer22.Fit( self.treeExplorerToolboxPanel )
		bSizer14.Add( self.treeExplorerToolboxPanel, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.m_searchCtrl4 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl4.ShowSearchButton( True )
		self.m_searchCtrl4.ShowCancelButton( False )
		bSizer14.Add( self.m_searchCtrl4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 11, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer19.Add( self.m_staticText2, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_auiToolBar3 = wx.aui.AuiToolBar( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_OpenAssetIpfsButton = self.m_auiToolBar3.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/raven_ipfs.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Open IPFS in Browser", wx.EmptyString, None ) 
		
		self.m_shareAssetButton = self.m_auiToolBar3.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/copy_clipboard.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Copy IPFS URL", wx.EmptyString, None ) 
		
		self.m_auiToolBar3.Realize() 
		
		bSizer19.Add( self.m_auiToolBar3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer18.Add( bSizer19, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer18.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.AssetDetailsContainerPanel = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18.Add( self.AssetDetailsContainerPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel4.SetSizer( bSizer18 )
		self.m_panel4.Layout()
		bSizer18.Fit( self.m_panel4 )
		bSizer17.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer17, 3, wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer12 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnSaveBookmarkList, id = self.m_saveBookmarkButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnAddBookmarkListItem, id = self.m_addBookmarkButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnRemoveBookmarkListItem, id = self.m_removeBookmarkButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnUseCacheToggle, id = self.m_useCacheButton.GetId() )
		self.m_showBookmarkToolbarButton.Bind( wx.EVT_BUTTON, self.OnToggleBookmarkToolbar )
		self.Bind( wx.EVT_TOOL, self.OnTreeDisplayOptionsChanged, id = self.m_TreeDisplayOption_OrganizeByMainAsset.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnTreeDisplayOptionsChanged, id = self.m_TreeDisplayOption_ReorganizeSubCat.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnResetTreeDisplay, id = self.m_TreeDisplayOption_ResetDisplay.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnOpenCurrentAssetIPFS, id = self.m_OpenAssetIpfsButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnShareCurrentAssetIPFS, id = self.m_shareAssetButton.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSaveBookmarkList( self, event ):
		event.Skip()
	
	def OnAddBookmarkListItem( self, event ):
		event.Skip()
	
	def OnRemoveBookmarkListItem( self, event ):
		event.Skip()
	
	def OnUseCacheToggle( self, event ):
		event.Skip()
	
	def OnToggleBookmarkToolbar( self, event ):
		event.Skip()
	
	def OnTreeDisplayOptionsChanged( self, event ):
		event.Skip()
	
	
	def OnResetTreeDisplay( self, event ):
		event.Skip()
	
	def OnOpenCurrentAssetIPFS( self, event ):
		event.Skip()
	
	def OnShareCurrentAssetIPFS( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenAssetDetails_OverviewPanel
###########################################################################

class wxRavenAssetDetails_OverviewPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 683,441 ), style = wx.TAB_TRAVERSAL )
		
		bSizer76 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer77 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel10 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer78 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer79 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText30 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Asset Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		self.m_staticText30.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer79.Add( self.m_staticText30, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_assetNameText = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer79.Add( self.m_assetNameText, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer78.Add( bSizer79, 0, wx.EXPAND, 5 )
		
		bSizer791 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText301 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"IPFS  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )
		self.m_staticText301.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer791.Add( self.m_staticText301, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_assetIPFStext = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer791.Add( self.m_assetIPFStext, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer78.Add( bSizer791, 0, wx.EXPAND, 5 )
		
		bSizer7911 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3011 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Type  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3011.Wrap( -1 )
		self.m_staticText3011.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer7911.Add( self.m_staticText3011, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_assetTypeText = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer7911.Add( self.m_assetTypeText, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer78.Add( bSizer7911, 0, wx.EXPAND, 5 )
		
		bSizer79111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer90 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText30111 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Supply  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30111.Wrap( -1 )
		self.m_staticText30111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer90.Add( self.m_staticText30111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_assetSupplyTxt = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer90.Add( self.m_assetSupplyTxt, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer79111.Add( bSizer90, 1, wx.EXPAND, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText301111 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Created  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301111.Wrap( -1 )
		self.m_staticText301111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer91.Add( self.m_staticText301111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_assetCreatedTxt = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer91.Add( self.m_assetCreatedTxt, 1, wx.ALL, 5 )
		
		
		bSizer79111.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		
		bSizer78.Add( bSizer79111, 1, wx.EXPAND, 5 )
		
		
		self.m_panel10.SetSizer( bSizer78 )
		self.m_panel10.Layout()
		bSizer78.Fit( self.m_panel10 )
		bSizer77.Add( self.m_panel10, 3, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel11 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer92 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bpButton27 = wx.BitmapButton( self.m_panel11, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer92.Add( self.m_bpButton27, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel11.SetSizer( bSizer92 )
		self.m_panel11.Layout()
		bSizer92.Fit( self.m_panel11 )
		bSizer77.Add( self.m_panel11, 2, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel8.SetSizer( bSizer77 )
		self.m_panel8.Layout()
		bSizer77.Fit( self.m_panel8 )
		bSizer76.Add( self.m_panel8, 2, wx.EXPAND |wx.ALL, 1 )
		
		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer76.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer76.Add( self.m_panel9, 4, wx.EXPAND |wx.ALL, 1 )
		
		
		self.SetSizer( bSizer76 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenRavencoreSettingPanel_Search
###########################################################################

class wxRavenRavencoreSettingPanel_Search ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 465,374 ), style = wx.TAB_TRAVERSAL )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/inspect_wx.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_bitmap3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Search Options :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer27.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer27, 0, wx.EXPAND, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.searchopt_strictmode = wx.CheckBox( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.searchopt_strictmode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Strict Search (name must match exactly)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer28.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer30.Add( self.m_staticText8, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer28.Add( bSizer30, 0, 0, 5 )
		
		
		bSizer26.Add( bSizer28, 0, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Asset Search Limit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer29.Add( self.m_staticText9, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.searchopt_maxresults = wx.TextCtrl( self, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.searchopt_maxresults.SetMinSize( wx.Size( 100,-1 ) )
		
		bSizer29.Add( self.searchopt_maxresults, 0, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer29, 0, wx.EXPAND, 5 )
		
		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer26.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.searchopt_onlymain = wx.CheckBox( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.searchopt_onlymain, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Filter on Asset Types", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer31.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		
		bSizer26.Add( bSizer31, 0, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"                                  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer32.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Types :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer32.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		m_assetTypeListChoices = []
		self.m_assetTypeList = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_assetTypeListChoices, 0 )
		bSizer33.Add( self.m_assetTypeList, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer32.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		
		bSizer26.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer26 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenRavencoreSettingPanel_IPFS
###########################################################################

class wxRavenRavencoreSettingPanel_IPFS ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,374 ), style = wx.TAB_TRAVERSAL )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raven_ipfs.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_bitmap4, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"IPFS Gateway :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer32.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.ipfs_text_area = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.ipfs_text_area, 0, wx.ALL|wx.EXPAND, 5 )
		
		ipfs_provider_listChoices = []
		self.ipfs_provider_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ipfs_provider_listChoices, 0 )
		bSizer33.Add( self.ipfs_provider_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer32.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.ipfs_provider_addbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/add_plus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer34.Add( self.ipfs_provider_addbt, 0, wx.ALL, 5 )
		
		self.ipfs_provider_upbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/prev_nav.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer34.Add( self.ipfs_provider_upbt, 0, wx.ALL, 5 )
		
		self.ipfs_provider_rembt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/remove_minus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer34.Add( self.ipfs_provider_rembt, 0, wx.ALL, 5 )
		
		
		bSizer32.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer32.Add( bSizer35, 0, wx.EXPAND, 5 )
		
		
		bSizer26.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer26 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenRavencoreSettingPanel_Bookmarks
###########################################################################

class wxRavenRavencoreSettingPanel_Bookmarks ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,374 ), style = wx.TAB_TRAVERSAL )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/bookmarks_view.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_bitmap4, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"My Bookmarks :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer32.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.bookmark_text_area = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.bookmark_text_area, 0, wx.ALL|wx.EXPAND, 5 )
		
		bookmark_listChoices = []
		self.bookmark_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bookmark_listChoices, 0 )
		bSizer33.Add( self.bookmark_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer32.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.bookmark_addbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/add_plus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer34.Add( self.bookmark_addbt, 0, wx.ALL, 5 )
		
		self.bookmark_rembt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/remove_minus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer34.Add( self.bookmark_rembt, 0, wx.ALL, 5 )
		
		self.ipfs_provider_upbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/prev_nav.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.ipfs_provider_upbt.Enable( False )
		
		bSizer34.Add( self.ipfs_provider_upbt, 0, wx.ALL, 5 )
		
		
		bSizer32.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer32.Add( bSizer35, 0, wx.EXPAND, 5 )
		
		
		bSizer26.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer26 )
		self.Layout()
	
	def __del__( self ):
		pass
	

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
	

