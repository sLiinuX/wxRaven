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
		
		self.m_auiToolBar3.AddSeparator()
		
		self.m_CreateNewAssetButton = self.m_auiToolBar3.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/asset_new.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Create a new asset under this position", wx.EmptyString, None ) 
		
		self.m_auiToolBar3.Realize() 
		
		bSizer19.Add( self.m_auiToolBar3, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_auiToolBar5 = wx.aui.AuiToolBar( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT|wx.TRANSPARENT_WINDOW ) 
		self.m_auiToolBar5.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_auiToolBar5.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		self.m_auiToolBar5.Realize() 
		
		bSizer19.Add( self.m_auiToolBar5, 0, wx.ALL|wx.EXPAND, 5 )
		
		
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
		self.Bind( wx.EVT_TOOL, self.OnCreateNewAsset, id = self.m_CreateNewAssetButton.GetId() )
	
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
	
	def OnCreateNewAsset( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenAssetIssuer
###########################################################################

class wxRavenAssetIssuer ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 435,336 ), style = wx.TAB_TRAVERSAL )
		
		bSizer96 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer97 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, u"Asset Type :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		self.m_staticText43.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer97.Add( self.m_staticText43, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_assetTypeChoiceChoices = []
		self.m_assetTypeChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_assetTypeChoiceChoices, 0 )
		self.m_assetTypeChoice.SetSelection( 0 )
		bSizer97.Add( self.m_assetTypeChoice, 5, wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer97, 0, wx.EXPAND, 5 )
		
		bSizer971 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.mainAssetChoicePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer109 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText431 = wx.StaticText( self.mainAssetChoicePanel, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText431.Wrap( -1 )
		self.m_staticText431.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer109.Add( self.m_staticText431, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_assetMainChoiceChoices = []
		self.m_assetMainChoice = wx.Choice( self.mainAssetChoicePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_assetMainChoiceChoices, 0 )
		self.m_assetMainChoice.SetSelection( 0 )
		bSizer109.Add( self.m_assetMainChoice, 5, wx.ALL, 5 )
		
		
		self.mainAssetChoicePanel.SetSizer( bSizer109 )
		self.mainAssetChoicePanel.Layout()
		bSizer109.Fit( self.mainAssetChoicePanel )
		bSizer971.Add( self.mainAssetChoicePanel, 1, 0, 1 )
		
		
		bSizer96.Add( bSizer971, 0, wx.ALL|wx.EXPAND, 0 )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		self.m_staticText44.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer98.Add( self.m_staticText44, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AssetNameTxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer98.Add( self.m_AssetNameTxt, 5, wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer98, 0, wx.EXPAND, 5 )
		
		bSizer981 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText441 = wx.StaticText( self, wx.ID_ANY, u"IPFS :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText441.Wrap( -1 )
		self.m_staticText441.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer981.Add( self.m_staticText441, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_IPFSlinkTxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer981.Add( self.m_IPFSlinkTxt, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer981, 0, wx.EXPAND, 5 )
		
		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer96.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer99 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkAssetNameLabel = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkAssetNameLabel.Wrap( -1 )
		bSizer99.Add( self.checkAssetNameLabel, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer96.Add( bSizer99, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer991 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkAssetNameIcon1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/error_tsk.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer991.Add( self.checkAssetNameIcon1, 0, wx.ALL, 5 )
		
		self.checkErrorLabel = wx.StaticText( self, wx.ID_ANY, u"You must enter a name for the asset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkErrorLabel.Wrap( -1 )
		self.checkErrorLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		bSizer991.Add( self.checkErrorLabel, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer96.Add( bSizer991, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer96.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer100 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_reissuableOpt = wx.CheckBox( self, wx.ID_ANY, u"Reissuable", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer100.Add( self.m_reissuableOpt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Quantity :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		bSizer100.Add( self.m_staticText49, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_quantityTxt = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer100.Add( self.m_quantityTxt, 0, wx.ALL, 5 )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Units :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		bSizer100.Add( self.m_staticText50, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_unitsOpt = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 8, 0 )
		bSizer100.Add( self.m_unitsOpt, 0, wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer100, 0, wx.EXPAND, 5 )
		
		self.m_staticline101 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer96.Add( self.m_staticline101, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer982 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText442 = wx.StaticText( self, wx.ID_ANY, u"Destination :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText442.Wrap( -1 )
		self.m_staticText442.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer982.Add( self.m_staticText442, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_Destination = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer982.Add( self.m_Destination, 5, wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer982, 0, wx.EXPAND, 5 )
		
		bSizer104 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_issueButton = wx.Button( self, wx.ID_ANY, u"Issue Asset !", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer104.Add( self.m_issueButton, 0, wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer104, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer96 )
		self.Layout()
		
		# Connect Events
		self.m_AssetNameTxt.Bind( wx.EVT_TEXT, self.OnAssetNameChanged )
		self.m_reissuableOpt.Bind( wx.EVT_CHECKBOX, self.EvtOptionsChanged )
		self.m_quantityTxt.Bind( wx.EVT_TEXT, self.EvtOptionsChanged )
		self.m_unitsOpt.Bind( wx.EVT_SPINCTRL, self.EvtOptionsChanged )
		self.m_unitsOpt.Bind( wx.EVT_TEXT, self.EvtOptionsChanged )
		self.m_Destination.Bind( wx.EVT_TEXT, self.OnAssetNameChanged )
		self.m_issueButton.Bind( wx.EVT_BUTTON, self.OnIssueAsset )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnAssetNameChanged( self, event ):
		event.Skip()
	
	def EvtOptionsChanged( self, event ):
		event.Skip()
	
	
	
	
	
	def OnIssueAsset( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenAssetIssuerDialog
###########################################################################

class wxRavenAssetIssuerDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 557,437 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenAssetDetails_OverviewPanel
###########################################################################

class wxRavenAssetDetails_OverviewPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 677,477 ), style = wx.TAB_TRAVERSAL )
		
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
		bSizer90.Add( self.m_assetSupplyTxt, 1, wx.ALL, 5 )
		
		
		bSizer79111.Add( bSizer90, 1, 0, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText301111 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Created  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301111.Wrap( -1 )
		self.m_staticText301111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer91.Add( self.m_staticText301111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_assetCreatedTxt = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer91.Add( self.m_assetCreatedTxt, 1, wx.ALL, 5 )
		
		
		bSizer79111.Add( bSizer91, 1, 0, 5 )
		
		
		bSizer78.Add( bSizer79111, 0, wx.EXPAND, 5 )
		
		
		self.m_panel10.SetSizer( bSizer78 )
		self.m_panel10.Layout()
		bSizer78.Fit( self.m_panel10 )
		bSizer77.Add( self.m_panel10, 5, wx.ALL|wx.EXPAND, 5 )
		
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
		bSizer93 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer94 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap13 = wx.StaticBitmap( self.m_panel9, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/group_users.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer94.Add( self.m_bitmap13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Owner(s) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		self.m_staticText41.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer94.Add( self.m_staticText41, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self.m_panel9, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		bSizer94.Add( self.m_staticText42, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_ownerCount = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT )
		bSizer94.Add( self.m_ownerCount, 1, wx.ALL, 5 )
		
		
		bSizer93.Add( bSizer94, 0, wx.EXPAND, 5 )
		
		self.listCtrlContainer = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer95 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrl1 = wxRavenListCtrl( self.listCtrlContainer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT|wx.LC_EDIT_LABELS )
		bSizer95.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.listCtrlContainer.SetSizer( bSizer95 )
		self.listCtrlContainer.Layout()
		bSizer95.Fit( self.listCtrlContainer )
		bSizer93.Add( self.listCtrlContainer, 1, wx.EXPAND |wx.ALL, 1 )
		
		
		self.m_panel9.SetSizer( bSizer93 )
		self.m_panel9.Layout()
		bSizer93.Fit( self.m_panel9 )
		bSizer76.Add( self.m_panel9, 4, wx.EXPAND |wx.ALL, 1 )
		
		
		self.SetSizer( bSizer76 )
		self.Layout()
		
		# Connect Events
		self.m_bpButton27.Bind( wx.EVT_BUTTON, self.OnQrCodeClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnQrCodeClick( self, event ):
		event.Skip()
	

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
	

###########################################################################
## Class DONOTUSE_TestPanel2
###########################################################################

class DONOTUSE_TestPanel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer105 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer105.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer105 )
		self.Layout()
	
	def __del__( self ):
		pass
	

