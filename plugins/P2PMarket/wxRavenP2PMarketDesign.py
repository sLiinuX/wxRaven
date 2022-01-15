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
## Class wxRavenP2PMarket_NewAdDialog
###########################################################################

class wxRavenP2PMarket_NewAdDialog ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 891,579 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Publish a new Ad on P2P Market :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdFileIPFSHash = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_AdFileIPFSHash.Enable( False )
		
		bSizer2.Add( self.m_AdFileIPFSHash, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_toggleAssistant = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleAssistant.SetValue( True ) 
		bSizer2.Add( self.m_toggleAssistant, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		self.m_assistantPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer55 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline1 = wx.StaticLine( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer55.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap33 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/ravencoin_marketplace_ultrasmall.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_bitmap33, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_radioBox1Choices = [ u"I'm selling - You are offering an asset for sale", u"I want to find - You want to buy an asset", u"I want to trade - You want to exchange an asset for another asset" ]
		self.m_radioBox1 = wx.RadioBox( self.m_assistantPanel, wx.ID_ANY, u"Ad Type :", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer3.Add( self.m_radioBox1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer55.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer55.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/reflog.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_bitmap2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u"Title :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdTitle = wx.TextCtrl( self.m_assistantPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_AdTitle, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer55.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		bSizer411 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap211 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/browser.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.m_bitmap211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText211 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u"Website / Gallery / IPFS Page : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		self.m_staticText211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer411.Add( self.m_staticText211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdLink = wx.TextCtrl( self.m_assistantPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.m_AdLink, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer55.Add( bSizer411, 0, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer55.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap7 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/changelog_obj.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_bitmap7, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u"Description :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer16.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		self.m_AdDescription = wx.TextCtrl( self.m_assistantPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_AdDescription.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_AdDescription.SetMinSize( wx.Size( -1,100 ) )
		
		bSizer14.Add( self.m_AdDescription, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap71 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/changelog_obj.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.m_bitmap71, 0, wx.ALL, 5 )
		
		self.m_staticText81 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u"Tags / Categories / Keywords :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		self.m_staticText81.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer161.Add( self.m_staticText81, 0, wx.ALL, 5 )
		
		
		bSizer141.Add( bSizer161, 0, wx.EXPAND, 5 )
		
		self.m_AdKeyword = wx.TextCtrl( self.m_assistantPanel, wx.ID_ANY, u"Asset", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_AdKeyword.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_AdKeyword.SetMinSize( wx.Size( -1,100 ) )
		
		bSizer141.Add( self.m_AdKeyword, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer141, 1, wx.EXPAND, 5 )
		
		
		bSizer55.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		self.m_staticline31 = wx.StaticLine( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer55.Add( self.m_staticline31, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap20 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/p2p_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.m_bitmap20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText71 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u"P2P Sell Method :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		self.m_staticText71.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer121.Add( self.m_staticText71, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_txMethodChoices = [ u"Atomic Swap", u"P2SH" ]
		self.m_txMethod = wx.Choice( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_txMethodChoices, 0 )
		self.m_txMethod.SetSelection( 0 )
		bSizer121.Add( self.m_txMethod, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_toggleRawTxDatas = wx.ToggleButton( self.m_assistantPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 32,-1 ), 0 )
		bSizer121.Add( self.m_toggleRawTxDatas, 0, wx.ALL, 5 )
		
		bSizer118 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText56 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )
		bSizer118.Add( self.m_staticText56, 0, wx.ALL, 5 )
		
		
		bSizer121.Add( bSizer118, 1, wx.EXPAND, 5 )
		
		bSizer117 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_P2PmethodErrorText = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_P2PmethodErrorText.Wrap( -1 )
		bSizer117.Add( self.m_P2PmethodErrorText, 0, wx.ALL, 5 )
		
		self.m_bitmap38 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer117.Add( self.m_bitmap38, 0, wx.ALL, 5 )
		
		
		bSizer121.Add( bSizer117, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer55.Add( bSizer121, 0, wx.EXPAND, 5 )
		
		self.m_txMethodPanel = wx.Panel( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,150 ), wx.TAB_TRAVERSAL )
		self.m_txMethodPanel.SetMinSize( wx.Size( -1,150 ) )
		self.m_txMethodPanel.SetMaxSize( wx.Size( -1,150 ) )
		
		bSizer55.Add( self.m_txMethodPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_assistantPanel.SetSizer( bSizer55 )
		self.m_assistantPanel.Layout()
		bSizer55.Fit( self.m_assistantPanel )
		bSizer1.Add( self.m_assistantPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline3111 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline3111, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer4121 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2121 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2121.Wrap( -1 )
		self.m_staticText2121.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1111.Add( self.m_staticText2121, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer4121.Add( bSizer1111, 3, wx.EXPAND, 5 )
		
		bSizer1211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap121 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/p2p_icon2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1211.Add( self.m_bitmap121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText711 = wx.StaticText( self, wx.ID_ANY, u"P2P Channel Asset :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText711.Wrap( -1 )
		self.m_staticText711.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1211.Add( self.m_staticText711, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_AdP2PChannelChoiceChoices = []
		self.m_AdP2PChannelChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AdP2PChannelChoiceChoices, 0 )
		self.m_AdP2PChannelChoice.SetSelection( 0 )
		bSizer1211.Add( self.m_AdP2PChannelChoice, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap16 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1211.Add( self.m_bitmap16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer4121.Add( bSizer1211, 2, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer4121, 0, wx.EXPAND, 5 )
		
		self.m_staticline311 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline311, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_PreviewAdBt = wx.Button( self, wx.ID_ANY, u"Preview Ad", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_PreviewAdBt, 0, wx.ALL, 5 )
		
		self.m_GeneraeteAdBt = wx.Button( self, wx.ID_ANY, u"Generate Ad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_GeneraeteAdBt.Enable( False )
		
		bSizer22.Add( self.m_GeneraeteAdBt, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer22, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_toggleAssistant.Bind( wx.EVT_TOGGLEBUTTON, self.OnWizardButtonToggle )
		self.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.OnAdTypeChanged )
		self.m_AdTitle.Bind( wx.EVT_TEXT, self.OnTitleChanged )
		self.m_AdLink.Bind( wx.EVT_TEXT, self.OnLinkChanged )
		self.m_AdDescription.Bind( wx.EVT_TEXT, self.OnDescriptionChanged )
		self.m_AdKeyword.Bind( wx.EVT_TEXT, self.OnKeywordChanged )
		self.m_txMethod.Bind( wx.EVT_CHOICE, self.OnTxMethodChanged )
		self.m_toggleRawTxDatas.Bind( wx.EVT_TOGGLEBUTTON, self.OnToggleRawTxData )
		self.m_AdP2PChannelChoice.Bind( wx.EVT_CHOICE, self.OnP2PChannelChanged )
		self.m_PreviewAdBt.Bind( wx.EVT_BUTTON, self.OnPreviewAdButtonClick )
		self.m_GeneraeteAdBt.Bind( wx.EVT_BUTTON, self.OnGenerateButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnWizardButtonToggle( self, event ):
		event.Skip()
	
	def OnAdTypeChanged( self, event ):
		event.Skip()
	
	def OnTitleChanged( self, event ):
		event.Skip()
	
	def OnLinkChanged( self, event ):
		event.Skip()
	
	def OnDescriptionChanged( self, event ):
		event.Skip()
	
	def OnKeywordChanged( self, event ):
		event.Skip()
	
	def OnTxMethodChanged( self, event ):
		event.Skip()
	
	def OnToggleRawTxData( self, event ):
		event.Skip()
	
	def OnP2PChannelChanged( self, event ):
		event.Skip()
	
	def OnPreviewAdButtonClick( self, event ):
		event.Skip()
	
	def OnGenerateButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenAtomicSwapPanel
###########################################################################

class wxRavenAtomicSwapPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 483,310 ), style = wx.TAB_TRAVERSAL )
		
		bSizer109 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panelTxType = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap211 = wx.StaticBitmap( self.m_panelTxType, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/atomic_swap.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer112.Add( self.m_bitmap211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText211 = wx.StaticText( self.m_panelTxType, wx.ID_ANY, u"Select an transaction type : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		self.m_staticText211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer112.Add( self.m_staticText211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_AtomicSwapTypeChoices = [ u"sell", u"buy", u"trade" ]
		self.m_AtomicSwapType = wx.Choice( self.m_panelTxType, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AtomicSwapTypeChoices, 0 )
		self.m_AtomicSwapType.SetSelection( 0 )
		bSizer112.Add( self.m_AtomicSwapType, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panelTxType.SetSizer( bSizer112 )
		self.m_panelTxType.Layout()
		bSizer112.Fit( self.m_panelTxType )
		bSizer109.Add( self.m_panelTxType, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline19 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer109.Add( self.m_staticline19, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_atomicswapPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer56 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_assetSellPanel = wx.Panel( self.m_atomicswapPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap21 = wx.StaticBitmap( self.m_assetSellPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_bitmap21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_assetSellPanel, wx.ID_ANY, u"Select an Asset : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer11.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_AdAssetChoiceChoices = []
		self.m_AdAssetChoice = wx.Choice( self.m_assetSellPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AdAssetChoiceChoices, 0 )
		self.m_AdAssetChoice.SetSelection( 0 )
		bSizer11.Add( self.m_AdAssetChoice, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_assetSellPanel.SetSizer( bSizer11 )
		self.m_assetSellPanel.Layout()
		bSizer11.Fit( self.m_assetSellPanel )
		bSizer41.Add( self.m_assetSellPanel, 1, wx.EXPAND |wx.ALL, 0 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u"Quantity :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer12.Add( self.m_staticText7, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdAssetQt = wx.TextCtrl( self.m_atomicswapPanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		bSizer12.Add( self.m_AdAssetQt, 1, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		
		bSizer56.Add( bSizer41, 0, wx.EXPAND, 5 )
		
		bSizer412 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_assetTradePanel = wx.Panel( self.m_atomicswapPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer113 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap212 = wx.StaticBitmap( self.m_assetTradePanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset_in.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer113.Add( self.m_bitmap212, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText212 = wx.StaticText( self.m_assetTradePanel, wx.ID_ANY, u"Select an Asset : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )
		self.m_staticText212.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer113.Add( self.m_staticText212, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_WantedAssetText = wx.TextCtrl( self.m_assetTradePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer113.Add( self.m_WantedAssetText, 1, wx.ALL, 5 )
		
		self.m_bitmap106 = wx.StaticBitmap( self.m_assetTradePanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer113.Add( self.m_bitmap106, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.m_assetTradePanel.SetSizer( bSizer113 )
		self.m_assetTradePanel.Layout()
		bSizer113.Fit( self.m_assetTradePanel )
		bSizer111.Add( self.m_assetTradePanel, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		bSizer412.Add( bSizer111, 2, wx.EXPAND, 5 )
		
		bSizer1212 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText712 = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u"Price :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText712.Wrap( -1 )
		self.m_staticText712.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1212.Add( self.m_staticText712, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdAssetPrice = wx.TextCtrl( self.m_atomicswapPanel, wx.ID_ANY, u"200", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		bSizer1212.Add( self.m_AdAssetPrice, 1, wx.ALL, 5 )
		
		
		bSizer412.Add( bSizer1212, 1, wx.EXPAND, 5 )
		
		
		bSizer56.Add( bSizer412, 0, wx.EXPAND, 5 )
		
		bSizer144 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer145 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText69 = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )
		bSizer145.Add( self.m_staticText69, 0, wx.ALL, 5 )
		
		
		bSizer144.Add( bSizer145, 1, wx.EXPAND, 5 )
		
		bSizer146 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText70 = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u"Order(s) :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText70.Wrap( -1 )
		self.m_staticText70.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer146.Add( self.m_staticText70, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_orderCount = wx.SpinCtrl( self.m_atomicswapPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 1, 1 )
		self.m_orderCount.Enable( False )
		
		bSizer146.Add( self.m_orderCount, 0, wx.ALL, 5 )
		
		
		bSizer144.Add( bSizer146, 1, 0, 5 )
		
		
		bSizer56.Add( bSizer144, 0, wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_GenerateSwapTx = wx.Button( self.m_atomicswapPanel, wx.ID_ANY, u"Generate Atomic Swap !", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.m_GenerateSwapTx, 0, wx.ALL, 5 )
		
		
		bSizer56.Add( bSizer141, 1, wx.ALIGN_RIGHT, 5 )
		
		
		self.m_atomicswapPanel.SetSizer( bSizer56 )
		self.m_atomicswapPanel.Layout()
		bSizer56.Fit( self.m_atomicswapPanel )
		bSizer109.Add( self.m_atomicswapPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline18 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer109.Add( self.m_staticline18, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_detailsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer142 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_txDatas = wx.TextCtrl( self.m_detailsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_txDatas.SetMinSize( wx.Size( -1,70 ) )
		self.m_txDatas.SetMaxSize( wx.Size( -1,70 ) )
		
		bSizer142.Add( self.m_txDatas, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_detailsPanel.SetSizer( bSizer142 )
		self.m_detailsPanel.Layout()
		bSizer142.Fit( self.m_detailsPanel )
		bSizer109.Add( self.m_detailsPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer109 )
		self.Layout()
		
		# Connect Events
		self.m_AtomicSwapType.Bind( wx.EVT_CHOICE, self.OnSwapTypeChanged )
		self.m_AdAssetChoice.Bind( wx.EVT_CHOICE, self.OnAssetChanged )
		self.m_AdAssetQt.Bind( wx.EVT_TEXT, self.OnQuantityChanged )
		self.m_WantedAssetText.Bind( wx.EVT_TEXT, self.OnWantedAssetChanged )
		self.m_AdAssetPrice.Bind( wx.EVT_TEXT, self.OnPriceChanged )
		self.m_orderCount.Bind( wx.EVT_SPINCTRL, self.OnOrderCountChange )
		self.m_orderCount.Bind( wx.EVT_TEXT, self.OnOrderCountChange )
		self.m_GenerateSwapTx.Bind( wx.EVT_BUTTON, self.OnGenerateAtomicSwap )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSwapTypeChanged( self, event ):
		event.Skip()
	
	def OnAssetChanged( self, event ):
		event.Skip()
	
	def OnQuantityChanged( self, event ):
		event.Skip()
	
	def OnWantedAssetChanged( self, event ):
		event.Skip()
	
	def OnPriceChanged( self, event ):
		event.Skip()
	
	def OnOrderCountChange( self, event ):
		event.Skip()
	
	
	def OnGenerateAtomicSwap( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenAtomicSwapPanel_NoDetails
###########################################################################

class wxRavenAtomicSwapPanel_NoDetails ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,173 ), style = wx.TAB_TRAVERSAL )
		
		bSizer109 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panelTxType = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap211 = wx.StaticBitmap( self.m_panelTxType, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/atomic_swap.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer112.Add( self.m_bitmap211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText211 = wx.StaticText( self.m_panelTxType, wx.ID_ANY, u"Select an transaction type : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		self.m_staticText211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer112.Add( self.m_staticText211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_AtomicSwapTypeChoices = [ u"sell", u"buy", u"trade" ]
		self.m_AtomicSwapType = wx.Choice( self.m_panelTxType, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AtomicSwapTypeChoices, 0 )
		self.m_AtomicSwapType.SetSelection( 0 )
		bSizer112.Add( self.m_AtomicSwapType, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panelTxType.SetSizer( bSizer112 )
		self.m_panelTxType.Layout()
		bSizer112.Fit( self.m_panelTxType )
		bSizer109.Add( self.m_panelTxType, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline19 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer109.Add( self.m_staticline19, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_atomicswapPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer56 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer229 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_assetSellPanel = wx.Panel( self.m_atomicswapPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap21 = wx.StaticBitmap( self.m_assetSellPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_bitmap21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_assetSellPanel, wx.ID_ANY, u"Select an Asset : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer11.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_AdAssetChoiceChoices = []
		self.m_AdAssetChoice = wx.Choice( self.m_assetSellPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AdAssetChoiceChoices, 0 )
		self.m_AdAssetChoice.SetSelection( 0 )
		bSizer11.Add( self.m_AdAssetChoice, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_assetSellPanel.SetSizer( bSizer11 )
		self.m_assetSellPanel.Layout()
		bSizer11.Fit( self.m_assetSellPanel )
		bSizer229.Add( self.m_assetSellPanel, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		bSizer41.Add( bSizer229, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u"Quantity :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer12.Add( self.m_staticText7, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdAssetQt = wx.TextCtrl( self.m_atomicswapPanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		bSizer12.Add( self.m_AdAssetQt, 1, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		
		bSizer56.Add( bSizer41, 0, wx.EXPAND, 5 )
		
		bSizer412 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_assetTradePanel = wx.Panel( self.m_atomicswapPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer113 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap212 = wx.StaticBitmap( self.m_assetTradePanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset_in.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer113.Add( self.m_bitmap212, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText212 = wx.StaticText( self.m_assetTradePanel, wx.ID_ANY, u"Select an Asset : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )
		self.m_staticText212.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer113.Add( self.m_staticText212, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_WantedAssetText = wx.TextCtrl( self.m_assetTradePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer113.Add( self.m_WantedAssetText, 1, wx.ALL, 5 )
		
		
		self.m_assetTradePanel.SetSizer( bSizer113 )
		self.m_assetTradePanel.Layout()
		bSizer113.Fit( self.m_assetTradePanel )
		bSizer111.Add( self.m_assetTradePanel, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		bSizer412.Add( bSizer111, 2, wx.EXPAND, 5 )
		
		bSizer1212 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText712 = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u"Price :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText712.Wrap( -1 )
		self.m_staticText712.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1212.Add( self.m_staticText712, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdAssetPrice = wx.TextCtrl( self.m_atomicswapPanel, wx.ID_ANY, u"200", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		bSizer1212.Add( self.m_AdAssetPrice, 1, wx.ALL, 5 )
		
		
		bSizer412.Add( bSizer1212, 1, wx.EXPAND, 5 )
		
		
		bSizer56.Add( bSizer412, 0, wx.EXPAND, 5 )
		
		bSizer144 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer145 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText69 = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )
		bSizer145.Add( self.m_staticText69, 0, wx.ALL, 5 )
		
		
		bSizer144.Add( bSizer145, 1, wx.EXPAND, 5 )
		
		bSizer146 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText70 = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u"Order(s) :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText70.Wrap( -1 )
		self.m_staticText70.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer146.Add( self.m_staticText70, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_orderCount = wx.SpinCtrl( self.m_atomicswapPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 1, 1 )
		self.m_orderCount.Enable( False )
		
		bSizer146.Add( self.m_orderCount, 0, wx.ALL, 5 )
		
		
		bSizer144.Add( bSizer146, 1, 0, 5 )
		
		
		bSizer56.Add( bSizer144, 0, wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer56.Add( bSizer141, 1, wx.ALIGN_RIGHT, 5 )
		
		
		self.m_atomicswapPanel.SetSizer( bSizer56 )
		self.m_atomicswapPanel.Layout()
		bSizer56.Fit( self.m_atomicswapPanel )
		bSizer109.Add( self.m_atomicswapPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer109 )
		self.Layout()
		
		# Connect Events
		self.m_AtomicSwapType.Bind( wx.EVT_CHOICE, self.OnSwapTypeChanged )
		self.m_AdAssetChoice.Bind( wx.EVT_CHOICE, self.OnAssetChanged )
		self.m_AdAssetQt.Bind( wx.EVT_TEXT, self.OnQuantityChanged )
		self.m_WantedAssetText.Bind( wx.EVT_TEXT, self.OnWantedAssetChanged )
		self.m_AdAssetPrice.Bind( wx.EVT_TEXT, self.OnPriceChanged )
		self.m_orderCount.Bind( wx.EVT_SPINCTRL, self.OnOrderCountChange )
		self.m_orderCount.Bind( wx.EVT_TEXT, self.OnOrderCountChange )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSwapTypeChanged( self, event ):
		event.Skip()
	
	def OnAssetChanged( self, event ):
		event.Skip()
	
	def OnQuantityChanged( self, event ):
		event.Skip()
	
	def OnWantedAssetChanged( self, event ):
		event.Skip()
	
	def OnPriceChanged( self, event ):
		event.Skip()
	
	def OnOrderCountChange( self, event ):
		event.Skip()
	
	

###########################################################################
## Class wxRavenRawTxPanel
###########################################################################

class wxRavenRawTxPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,132 ), style = wx.TAB_TRAVERSAL )
		
		bSizer198 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_rawDatasText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer198.Add( self.m_rawDatasText, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer198 )
		self.Layout()
		
		# Connect Events
		self.m_rawDatasText.Bind( wx.EVT_TEXT, self.OnRawDataChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnRawDataChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenP2PMarket_MarketPlaceListingPanel
###########################################################################

class wxRavenP2PMarket_MarketPlaceListingPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 723,537 ), style = wx.TAB_TRAVERSAL )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_infoCtrl1 = wx.InfoBar( self )
		self.m_infoCtrl1.SetShowHideEffects( wx.SHOW_EFFECT_NONE, wx.SHOW_EFFECT_NONE )
		self.m_infoCtrl1.SetEffectDuration( 500 )
		bSizer30.Add( self.m_infoCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer38_Top = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer40 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer40.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer38_Top.Add( bSizer40, 1, wx.EXPAND, 5 )
		
		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap13 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/ravencoin_marketplace_small.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.m_bitmap13, 1, wx.ALL, 5 )
		
		
		bSizer38_Top.Add( bSizer37, 0, 0, 5 )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer39.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer38_Top.Add( bSizer39, 1, wx.EXPAND, 5 )
		
		
		bSizer30.Add( bSizer38_Top, 0, wx.EXPAND, 5 )
		
		bSizer31_Search = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"P2P Marketplace :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		self.m_staticText35.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer34.Add( self.m_staticText35, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_marketChoiceChoices = [ u"All Marketplaces" ]
		self.m_marketChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_marketChoiceChoices, 0 )
		self.m_marketChoice.SetSelection( 0 )
		bSizer34.Add( self.m_marketChoice, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		bSizer34.Add( self.m_searchCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_toggleBtn2 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 32,-1 ), 0 )
		bSizer34.Add( self.m_toggleBtn2, 0, wx.ALL, 5 )
		
		
		bSizer33.Add( bSizer34, 1, wx.EXPAND, 5 )
		
		
		bSizer31_Search.Add( bSizer33, 1, 0, 5 )
		
		
		bSizer30.Add( bSizer31_Search, 0, wx.EXPAND, 5 )
		
		self.searchOptionsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer85 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap26 = wx.StaticBitmap( self.searchOptionsPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/p2p_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer85.Add( self.m_bitmap26, 0, wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self.searchOptionsPanel, wx.ID_ANY, u"Ad Type :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		self.m_staticText38.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer85.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		m_adTypeFilterChoices = [u"Sell", u"Buy", u"Trade"]
		self.m_adTypeFilter = wx.CheckListBox( self.searchOptionsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_adTypeFilterChoices, 0 )
		bSizer85.Add( self.m_adTypeFilter, 0, wx.ALL, 5 )
		
		
		bSizer35.Add( bSizer85, 0, wx.EXPAND, 5 )
		
		bSizer86 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap27 = wx.StaticBitmap( self.searchOptionsPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/p2p_icon2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer86.Add( self.m_bitmap27, 0, wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( self.searchOptionsPanel, wx.ID_ANY, u"Transaction Type :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		self.m_staticText39.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer86.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		m_txTypeFilterChoices = [u"Atomic Swap", u"P2SH"]
		self.m_txTypeFilter = wx.CheckListBox( self.searchOptionsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_txTypeFilterChoices, 0 )
		bSizer86.Add( self.m_txTypeFilter, 0, wx.ALL, 5 )
		
		
		bSizer35.Add( bSizer86, 0, wx.EXPAND, 5 )
		
		bSizer861 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap271 = wx.StaticBitmap( self.searchOptionsPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/changelog_obj.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer861.Add( self.m_bitmap271, 0, wx.ALL, 5 )
		
		self.m_staticText391 = wx.StaticText( self.searchOptionsPanel, wx.ID_ANY, u"Search Fields :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText391.Wrap( -1 )
		self.m_staticText391.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer861.Add( self.m_staticText391, 0, wx.ALL, 5 )
		
		m_AdInformationsFilterChoices = [u"address", u"title", u"asset", u"price_asset", u"desc", u"keywords"]
		self.m_AdInformationsFilter = wx.CheckListBox( self.searchOptionsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AdInformationsFilterChoices, wx.LB_MULTIPLE|wx.LB_NEEDED_SB )
		bSizer861.Add( self.m_AdInformationsFilter, 0, wx.ALL, 5 )
		
		
		bSizer35.Add( bSizer861, 1, wx.EXPAND, 5 )
		
		
		self.searchOptionsPanel.SetSizer( bSizer35 )
		self.searchOptionsPanel.Layout()
		bSizer35.Fit( self.searchOptionsPanel )
		bSizer30.Add( self.searchOptionsPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_feelLuckButton = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/feel_lucky.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer101.Add( self.m_feelLuckButton, 0, wx.ALL, 5 )
		
		self.m_KawButton = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/kaw_button.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer101.Add( self.m_KawButton, 0, wx.ALL, 5 )
		
		
		bSizer30.Add( bSizer101, 0, wx.ALIGN_CENTER, 5 )
		
		self.m_staticline17 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer30.Add( self.m_staticline17, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_marketViewScrollPanel = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_marketViewScrollPanel.SetScrollRate( 5, 5 )
		bSizer57 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrl1 = wxRavenListCtrl( self.m_marketViewScrollPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer57.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_marketViewScrollPanel.SetSizer( bSizer57 )
		self.m_marketViewScrollPanel.Layout()
		bSizer57.Fit( self.m_marketViewScrollPanel )
		bSizer30.Add( self.m_marketViewScrollPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer30 )
		self.Layout()
		
		# Connect Events
		self.m_marketChoice.Bind( wx.EVT_CHOICE, self.OnMarketplaceChanged )
		self.m_toggleBtn2.Bind( wx.EVT_TOGGLEBUTTON, self.OnToggleFilterButtonClicked )
		self.m_adTypeFilter.Bind( wx.EVT_CHECKLISTBOX, self.OnAdTypeFilterChanged )
		self.m_txTypeFilter.Bind( wx.EVT_CHECKLISTBOX, self.OnAdTxMethodChanged )
		self.m_AdInformationsFilter.Bind( wx.EVT_CHECKLISTBOX, self.OnAdTxMethodChanged )
		self.m_feelLuckButton.Bind( wx.EVT_BUTTON, self.OnFeelLuck )
		self.m_KawButton.Bind( wx.EVT_BUTTON, self.OnKaw )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnMarketplaceChanged( self, event ):
		event.Skip()
	
	def OnToggleFilterButtonClicked( self, event ):
		event.Skip()
	
	def OnAdTypeFilterChanged( self, event ):
		event.Skip()
	
	def OnAdTxMethodChanged( self, event ):
		event.Skip()
	
	
	def OnFeelLuck( self, event ):
		event.Skip()
	
	def OnKaw( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenDecodeTxPanel
###########################################################################

class wxRavenDecodeTxPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 567,476 ), style = wx.TAB_TRAVERSAL )
		
		bSizer230 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_TXDetailsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer255 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer231 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap71 = wx.StaticBitmap( self.m_TXDetailsPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/unknown_user.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer231.Add( self.m_bitmap71, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText111 = wx.StaticText( self.m_TXDetailsPanel, wx.ID_ANY, u"Origin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )
		self.m_staticText111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer231.Add( self.m_staticText111, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_mineText = wx.TextCtrl( self.m_TXDetailsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer231.Add( self.m_mineText, 2, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer255.Add( bSizer231, 0, wx.EXPAND, 5 )
		
		bSizer2311 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmapStatus = wx.StaticBitmap( self.m_TXDetailsPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2311.Add( self.m_bitmapStatus, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1111 = wx.StaticText( self.m_TXDetailsPanel, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1111.Wrap( -1 )
		self.m_staticText1111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2311.Add( self.m_staticText1111, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_StatusText = wx.TextCtrl( self.m_TXDetailsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer2311.Add( self.m_StatusText, 2, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer255.Add( bSizer2311, 0, wx.EXPAND, 5 )
		
		bSizer2312 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap721 = wx.StaticBitmap( self.m_TXDetailsPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2312.Add( self.m_bitmap721, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1112 = wx.StaticText( self.m_TXDetailsPanel, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1112.Wrap( -1 )
		self.m_staticText1112.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2312.Add( self.m_staticText1112, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_TypeText = wx.TextCtrl( self.m_TXDetailsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer2312.Add( self.m_TypeText, 2, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer255.Add( bSizer2312, 0, wx.EXPAND, 5 )
		
		bSizer2313 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap722 = wx.StaticBitmap( self.m_TXDetailsPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2313.Add( self.m_bitmap722, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1113 = wx.StaticText( self.m_TXDetailsPanel, wx.ID_ANY, u"Asset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1113.Wrap( -1 )
		self.m_staticText1113.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2313.Add( self.m_staticText1113, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AssetText = wx.TextCtrl( self.m_TXDetailsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer2313.Add( self.m_AssetText, 2, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer255.Add( bSizer2313, 0, wx.EXPAND, 5 )
		
		bSizer2314 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap723 = wx.StaticBitmap( self.m_TXDetailsPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/supply_2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2314.Add( self.m_bitmap723, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1114 = wx.StaticText( self.m_TXDetailsPanel, wx.ID_ANY, u"Quantity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1114.Wrap( -1 )
		self.m_staticText1114.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2314.Add( self.m_staticText1114, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_QuantityText = wx.TextCtrl( self.m_TXDetailsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer2314.Add( self.m_QuantityText, 2, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer255.Add( bSizer2314, 0, wx.EXPAND, 5 )
		
		bSizer2315 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap724 = wx.StaticBitmap( self.m_TXDetailsPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/ravencoin.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2315.Add( self.m_bitmap724, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1115 = wx.StaticText( self.m_TXDetailsPanel, wx.ID_ANY, u"Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1115.Wrap( -1 )
		self.m_staticText1115.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2315.Add( self.m_staticText1115, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_PriceText = wx.TextCtrl( self.m_TXDetailsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer2315.Add( self.m_PriceText, 2, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer255.Add( bSizer2315, 0, wx.EXPAND, 5 )
		
		bSizer23151 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmapUTXO = wx.StaticBitmap( self.m_TXDetailsPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raw_datas.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23151.Add( self.m_bitmapUTXO, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText11151 = wx.StaticText( self.m_TXDetailsPanel, wx.ID_ANY, u"UTXO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11151.Wrap( -1 )
		self.m_staticText11151.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer23151.Add( self.m_staticText11151, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_UTXOText = wx.TextCtrl( self.m_TXDetailsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer23151.Add( self.m_UTXOText, 2, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer255.Add( bSizer23151, 0, wx.EXPAND, 5 )
		
		
		self.m_TXDetailsPanel.SetSizer( bSizer255 )
		self.m_TXDetailsPanel.Layout()
		bSizer255.Fit( self.m_TXDetailsPanel )
		bSizer230.Add( self.m_TXDetailsPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_ErrorMsgPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer257 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer258 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer259 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap89 = wx.StaticBitmap( self.m_ErrorMsgPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/error_tsk.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer259.Add( self.m_bitmap89, 0, wx.ALL, 5 )
		
		self.m_staticText125 = wx.StaticText( self.m_ErrorMsgPanel, wx.ID_ANY, u"ERROR !", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText125.Wrap( -1 )
		self.m_staticText125.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer259.Add( self.m_staticText125, 0, wx.ALL, 5 )
		
		
		bSizer258.Add( bSizer259, 0, wx.ALIGN_CENTER, 5 )
		
		self.m_ErrorDetails = wx.StaticText( self.m_ErrorMsgPanel, wx.ID_ANY, u"Error : Invalid Transaction", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ErrorDetails.Wrap( -1 )
		bSizer258.Add( self.m_ErrorDetails, 0, wx.ALL, 5 )
		
		
		bSizer257.Add( bSizer258, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_ErrorMsgPanel.SetSizer( bSizer257 )
		self.m_ErrorMsgPanel.Layout()
		bSizer257.Fit( self.m_ErrorMsgPanel )
		bSizer230.Add( self.m_ErrorMsgPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_TXInputPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_TXInputPanel.SetMaxSize( wx.Size( -1,100 ) )
		
		bSizer256 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer23152 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmapPartial = wx.StaticBitmap( self.m_TXInputPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raw_datas.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23152.Add( self.m_bitmapPartial, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText11152 = wx.StaticText( self.m_TXInputPanel, wx.ID_ANY, u"Signed Partial", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11152.Wrap( -1 )
		self.m_staticText11152.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer23152.Add( self.m_staticText11152, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_SignedPartialText = wx.TextCtrl( self.m_TXInputPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE )
		self.m_SignedPartialText.SetMinSize( wx.Size( 325,60 ) )
		
		bSizer23152.Add( self.m_SignedPartialText, 2, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer256.Add( bSizer23152, 1, wx.EXPAND, 5 )
		
		bSizer231521 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap7251 = wx.StaticBitmap( self.m_TXInputPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raw_datas.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer231521.Add( self.m_bitmap7251, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText111521 = wx.StaticText( self.m_TXInputPanel, wx.ID_ANY, u"Order Number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111521.Wrap( -1 )
		self.m_staticText111521.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer231521.Add( self.m_staticText111521, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl7 = wx.SpinCtrl( self.m_TXInputPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 3, 1 )
		bSizer231521.Add( self.m_spinCtrl7, 2, wx.ALL, 5 )
		
		
		bSizer256.Add( bSizer231521, 0, wx.EXPAND, 5 )
		
		
		self.m_TXInputPanel.SetSizer( bSizer256 )
		self.m_TXInputPanel.Layout()
		bSizer256.Fit( self.m_TXInputPanel )
		bSizer230.Add( self.m_TXInputPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_InteractionPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer312 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer313 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_CloseButton = wx.Button( self.m_InteractionPanel, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer313.Add( self.m_CloseButton, 1, wx.ALL, 5 )
		
		self.m_completeButton = wx.Button( self.m_InteractionPanel, wx.ID_ANY, u"Complete Tx", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_completeButton.Enable( False )
		
		bSizer313.Add( self.m_completeButton, 1, wx.ALL, 5 )
		
		
		bSizer312.Add( bSizer313, 0, wx.ALL, 5 )
		
		
		self.m_InteractionPanel.SetSizer( bSizer312 )
		self.m_InteractionPanel.Layout()
		bSizer312.Fit( self.m_InteractionPanel )
		bSizer230.Add( self.m_InteractionPanel, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer230 )
		self.Layout()
		
		# Connect Events
		self.m_SignedPartialText.Bind( wx.EVT_TEXT, self.OnRawDataChanged )
		self.m_CloseButton.Bind( wx.EVT_BUTTON, self.OnCloseParent )
		self.m_completeButton.Bind( wx.EVT_BUTTON, self.OnCompleteTx )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnRawDataChanged( self, event ):
		event.Skip()
	
	def OnCloseParent( self, event ):
		event.Skip()
	
	def OnCompleteTx( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenP2PMarket_MarketPlace_ItemPanel
###########################################################################

class wxRavenP2PMarket_MarketPlace_ItemPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 356,192 ), style = wx.TAB_TRAVERSAL )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenP2PMarket_Settings
###########################################################################

class wxRavenP2PMarket_Settings ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 465,374 ), style = wx.TAB_TRAVERSAL )
		
		bSizer74 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer75 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/p2p_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer75.Add( self.m_bitmap3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"P2P Market (BETA) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer75.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer75, 0, wx.EXPAND, 5 )
		
		bSizer76 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.searchopt_strictmode = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer76.Add( self.searchopt_strictmode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Enable P2P Market Index/Search", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer76.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer77 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer77.Add( self.m_staticText8, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer76.Add( bSizer77, 0, 0, 5 )
		
		
		bSizer74.Add( bSizer76, 0, wx.EXPAND, 5 )
		
		bSizer78 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Ads Search Limit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer78.Add( self.m_staticText9, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.searchopt_maxresults = wx.TextCtrl( self, wx.ID_ANY, u"500", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.searchopt_maxresults.SetMaxLength( 0 ) 
		bSizer78.Add( self.searchopt_maxresults, 0, wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer78, 0, wx.EXPAND, 5 )
		
		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer74.Add( self.m_staticline21, 0, wx.EXPAND|wx.ALL, 5 )
		
		bSizer781 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_forceNetwork = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer781.Add( self.m_forceNetwork, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap25 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer781.Add( self.m_bitmap25, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Force Network :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		bSizer781.Add( self.m_staticText91, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_NetworkChoiceChoices = []
		self.m_NetworkChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_NetworkChoiceChoices, 0 )
		self.m_NetworkChoice.SetSelection( 0 )
		self.m_NetworkChoice.Enable( False )
		
		bSizer781.Add( self.m_NetworkChoice, 1, wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer781, 0, wx.EXPAND, 5 )
		
		self.m_staticline211 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer74.Add( self.m_staticline211, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer782 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap30 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/filter_ps.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer782.Add( self.m_bitmap30, 0, wx.ALL, 5 )
		
		self.m_staticText92 = wx.StaticText( self, wx.ID_ANY, u"Search Advanced Options", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )
		self.m_staticText92.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer782.Add( self.m_staticText92, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer782, 0, wx.EXPAND, 5 )
		
		bSizer761 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.searchopt_includeNoneData = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer761.Add( self.searchopt_includeNoneData, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap100 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/empty_datas.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer761.Add( self.m_bitmap100, 0, wx.ALL, 5 )
		
		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Include None Tx in Listing", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )
		bSizer761.Add( self.m_staticText101, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer761, 0, wx.EXPAND, 5 )
		
		bSizer7611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.searchopt_checkTx = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7611.Add( self.searchopt_checkTx, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap101 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raw_datas_verified.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7611.Add( self.m_bitmap101, 0, wx.ALL, 5 )
		
		self.m_staticText1011 = wx.StaticText( self, wx.ID_ANY, u"Verify and display only valid Tx", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1011.Wrap( -1 )
		bSizer7611.Add( self.m_staticText1011, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer7611, 0, wx.EXPAND, 5 )
		
		bSizer76111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.searchopt_OnlyVerifiedSellers = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer76111.Add( self.searchopt_OnlyVerifiedSellers, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap1011 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/trusted_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer76111.Add( self.m_bitmap1011, 0, wx.ALL, 5 )
		
		self.m_staticText10111 = wx.StaticText( self, wx.ID_ANY, u"Only display Trusted Sellers", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10111.Wrap( -1 )
		bSizer76111.Add( self.m_staticText10111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer76111, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer74 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenP2PMarket_MyMarketSettings
###########################################################################

class wxRavenP2PMarket_MyMarketSettings ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 465,374 ), style = wx.TAB_TRAVERSAL )
		
		bSizer74 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer75 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/my_marketplace.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer75.Add( self.m_bitmap3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"My P2P Marketplace :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer75.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer75, 0, wx.EXPAND, 5 )
		
		bSizer78 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap99 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/known_user.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer78.Add( self.m_bitmap99, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Announcer Address :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer78.Add( self.m_staticText9, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_AddressChoiceChoices = []
		self.m_AddressChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AddressChoiceChoices, 0 )
		self.m_AddressChoice.SetSelection( 0 )
		bSizer78.Add( self.m_AddressChoice, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer74.Add( bSizer78, 0, wx.EXPAND, 5 )
		
		bSizer76 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_sameAddressChangeOpt = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer76.Add( self.m_sameAddressChangeOpt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Use same address for changes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer76.Add( self.m_staticText10, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_changeAddressChoiceOptChoices = []
		self.m_changeAddressChoiceOpt = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_changeAddressChoiceOptChoices, 0 )
		self.m_changeAddressChoiceOpt.SetSelection( 0 )
		bSizer76.Add( self.m_changeAddressChoiceOpt, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer74.Add( bSizer76, 0, wx.EXPAND, 5 )
		
		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer74.Add( self.m_staticline21, 0, wx.EXPAND|wx.ALL, 5 )
		
		bSizer781 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_defaultListingChanel = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer781.Add( self.m_defaultListingChanel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Default Listing Channel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		bSizer781.Add( self.m_staticText91, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap25 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/p2p_icon2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer781.Add( self.m_bitmap25, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_NetworkChoiceChoices = []
		self.m_NetworkChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_NetworkChoiceChoices, 0 )
		self.m_NetworkChoice.SetSelection( 0 )
		self.m_NetworkChoice.Enable( False )
		
		bSizer781.Add( self.m_NetworkChoice, 1, wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer781, 0, wx.EXPAND, 5 )
		
		self.m_staticline211 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer74.Add( self.m_staticline211, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer7811 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap251 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/lock_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7811.Add( self.m_bitmap251, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_keeplocks = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7811.Add( self.m_keeplocks, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText911 = wx.StaticText( self, wx.ID_ANY, u"Keeps my trades locked", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText911.Wrap( -1 )
		bSizer7811.Add( self.m_staticText911, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText165 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText165.Wrap( -1 )
		bSizer7811.Add( self.m_staticText165, 0, wx.ALL, 5 )
		
		self.m_wipeButton = wx.Button( self, wx.ID_ANY, u"Wipe Session", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7811.Add( self.m_wipeButton, 0, wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer7811, 0, wx.EXPAND, 5 )
		
		bSizer78111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9111 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9111.Wrap( -1 )
		bSizer78111.Add( self.m_staticText9111, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1651 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1651.Wrap( -1 )
		bSizer78111.Add( self.m_staticText1651, 0, wx.ALL, 5 )
		
		self.m_bitmap2511 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/unlock.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer78111.Add( self.m_bitmap2511, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_unlockAll = wx.Button( self, wx.ID_ANY, u"Unlock all", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer78111.Add( self.m_unlockAll, 0, wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer78111, 0, wx.EXPAND, 5 )
		
		bSizer781111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText91111 = wx.StaticText( self, wx.ID_ANY, u"Required if address or channel changed :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText91111.Wrap( -1 )
		self.m_staticText91111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		bSizer781111.Add( self.m_staticText91111, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText16511 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16511.Wrap( -1 )
		bSizer781111.Add( self.m_staticText16511, 0, wx.ALL, 5 )
		
		self.m_accountstatusBitmap = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer781111.Add( self.m_accountstatusBitmap, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_initMyMarketPlace = wx.Button( self, wx.ID_ANY, u"Initialize", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer781111.Add( self.m_initMyMarketPlace, 0, wx.ALL, 5 )
		
		
		bSizer74.Add( bSizer781111, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer74 )
		self.Layout()
		
		# Connect Events
		self.m_wipeButton.Bind( wx.EVT_BUTTON, self.OnDoWipeTradeSessions )
		self.m_unlockAll.Bind( wx.EVT_BUTTON, self.OnDoUnlockAll )
		self.m_initMyMarketPlace.Bind( wx.EVT_BUTTON, self.OnDoInitMyMarketPlace )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnDoWipeTradeSessions( self, event ):
		event.Skip()
	
	def OnDoUnlockAll( self, event ):
		event.Skip()
	
	def OnDoInitMyMarketPlace( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenP2PMarket_MarketsBookmarks
###########################################################################

class wxRavenP2PMarket_MarketsBookmarks ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,374 ), style = wx.TAB_TRAVERSAL )
		
		bSizer59 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer306 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText159 = wx.StaticText( self, wx.ID_ANY, u"Use the asset or sub-asset complete name :  <asset>\nExample : WXRAVEN/P2P_MARKETPLACE", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.STATIC_BORDER )
		self.m_staticText159.Wrap( -1 )
		bSizer306.Add( self.m_staticText159, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer59.Add( bSizer306, 0, wx.EXPAND, 5 )
		
		bSizer60 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/p2p_icon2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer60.Add( self.m_bitmap4, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"P2P Markets Channels :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer60.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		self.bookmark_text_area = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bookmark_text_area.SetMaxLength( 0 ) 
		bSizer61.Add( self.bookmark_text_area, 0, wx.ALL|wx.EXPAND, 5 )
		
		bookmark_listChoices = []
		self.bookmark_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bookmark_listChoices, 0 )
		bSizer61.Add( self.bookmark_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer60.Add( bSizer61, 1, wx.EXPAND, 5 )
		
		bSizer62 = wx.BoxSizer( wx.VERTICAL )
		
		self.bookmark_addbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/add_plus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer62.Add( self.bookmark_addbt, 0, wx.ALL, 5 )
		
		self.bookmark_rembt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/remove_minus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer62.Add( self.bookmark_rembt, 0, wx.ALL, 5 )
		
		self.ipfs_provider_upbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/prev_nav.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.ipfs_provider_upbt.Enable( False )
		
		bSizer62.Add( self.ipfs_provider_upbt, 0, wx.ALL, 5 )
		
		
		bSizer60.Add( bSizer62, 0, wx.EXPAND, 5 )
		
		bSizer63 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer60.Add( bSizer63, 0, wx.EXPAND, 5 )
		
		
		bSizer59.Add( bSizer60, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer59 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenP2PMarket_AddressesBlackList
###########################################################################

class wxRavenP2PMarket_AddressesBlackList ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,374 ), style = wx.TAB_TRAVERSAL )
		
		bSizer59 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer306 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText159 = wx.StaticText( self, wx.ID_ANY, u"No special format required : only address\nExample : RDyF4itWbfryV2nM4w2L99oJ4MvNptt82F", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.STATIC_BORDER )
		self.m_staticText159.Wrap( -1 )
		bSizer306.Add( self.m_staticText159, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer59.Add( bSizer306, 0, wx.EXPAND, 5 )
		
		bSizer60 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/blacklist.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer60.Add( self.m_bitmap4, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Add an address to Blacklist :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer60.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		self.bookmark_text_area = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bookmark_text_area.SetMaxLength( 0 ) 
		bSizer61.Add( self.bookmark_text_area, 0, wx.ALL|wx.EXPAND, 5 )
		
		bookmark_listChoices = []
		self.bookmark_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bookmark_listChoices, 0 )
		bSizer61.Add( self.bookmark_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer60.Add( bSizer61, 1, wx.EXPAND, 5 )
		
		bSizer62 = wx.BoxSizer( wx.VERTICAL )
		
		self.bookmark_addbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/add_plus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer62.Add( self.bookmark_addbt, 0, wx.ALL, 5 )
		
		self.bookmark_rembt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/remove_minus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer62.Add( self.bookmark_rembt, 0, wx.ALL, 5 )
		
		self.ipfs_provider_upbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/prev_nav.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.ipfs_provider_upbt.Enable( False )
		
		bSizer62.Add( self.ipfs_provider_upbt, 0, wx.ALL, 5 )
		
		
		bSizer60.Add( bSizer62, 0, wx.EXPAND, 5 )
		
		bSizer63 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer60.Add( bSizer63, 0, wx.EXPAND, 5 )
		
		
		bSizer59.Add( bSizer60, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer59 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenP2PMarket_TrustedSellers
###########################################################################

class wxRavenP2PMarket_TrustedSellers ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,374 ), style = wx.TAB_TRAVERSAL )
		
		bSizer59 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer306 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText159 = wx.StaticText( self, wx.ID_ANY, u"Use the format :  address = alias\nExample : RDyF4itWbfryV2nM4w2L99oJ4MvNptt82F = RVN Guardian", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE|wx.STATIC_BORDER )
		self.m_staticText159.Wrap( -1 )
		bSizer306.Add( self.m_staticText159, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer59.Add( bSizer306, 0, wx.EXPAND, 5 )
		
		bSizer60 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/trusted_peer.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer60.Add( self.m_bitmap4, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Add a Trusted Peer :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer60.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		self.bookmark_text_area = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bookmark_text_area.SetMaxLength( 0 ) 
		bSizer61.Add( self.bookmark_text_area, 0, wx.ALL|wx.EXPAND, 5 )
		
		bookmark_listChoices = []
		self.bookmark_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bookmark_listChoices, 0 )
		bSizer61.Add( self.bookmark_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer60.Add( bSizer61, 1, wx.EXPAND, 5 )
		
		bSizer62 = wx.BoxSizer( wx.VERTICAL )
		
		self.bookmark_addbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/add_plus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer62.Add( self.bookmark_addbt, 0, wx.ALL, 5 )
		
		self.bookmark_rembt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/remove_minus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer62.Add( self.bookmark_rembt, 0, wx.ALL, 5 )
		
		self.ipfs_provider_upbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/prev_nav.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.ipfs_provider_upbt.Enable( False )
		
		bSizer62.Add( self.ipfs_provider_upbt, 0, wx.ALL, 5 )
		
		
		bSizer60.Add( bSizer62, 0, wx.EXPAND, 5 )
		
		bSizer63 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer60.Add( bSizer63, 0, wx.EXPAND, 5 )
		
		
		bSizer59.Add( bSizer60, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer59 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenP2PMarket_NewAdDialog_FIRSTDRAFT
###########################################################################

class wxRavenP2PMarket_NewAdDialog_FIRSTDRAFT ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 891,641 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Publish a new Ad on P2P Market :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdFileIPFSHash = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_AdFileIPFSHash.Enable( False )
		
		bSizer2.Add( self.m_AdFileIPFSHash, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_toggleAssistant = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_toggleAssistant.SetValue( True ) 
		bSizer2.Add( self.m_toggleAssistant, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		self.m_assistantPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer55 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticline1 = wx.StaticLine( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer55.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap33 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/ravencoin_marketplace_ultrasmall.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_bitmap33, 0, wx.ALL, 5 )
		
		m_radioBox1Choices = [ u"I'm selling - You are offering an asset for sale", u"I want to find - You want to buy an asset", u"I want to trade - You want to exchange an asset for another asset" ]
		self.m_radioBox1 = wx.RadioBox( self.m_assistantPanel, wx.ID_ANY, u"Ad Type :", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		bSizer3.Add( self.m_radioBox1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer55.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer55.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/reflog.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_bitmap2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u"Title :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer4.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdTitle = wx.TextCtrl( self.m_assistantPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_AdTitle, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer55.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		bSizer411 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap211 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/browser.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.m_bitmap211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText211 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u"Website / Gallery / IPFS Page : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		self.m_staticText211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer411.Add( self.m_staticText211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdLink = wx.TextCtrl( self.m_assistantPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer411.Add( self.m_AdLink, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer55.Add( bSizer411, 0, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer55.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap7 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/changelog_obj.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_bitmap7, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u"Description :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		self.m_staticText8.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer16.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		self.m_AdDescription = wx.TextCtrl( self.m_assistantPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_AdDescription.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_AdDescription.SetMinSize( wx.Size( -1,100 ) )
		
		bSizer14.Add( self.m_AdDescription, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap71 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/changelog_obj.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.m_bitmap71, 0, wx.ALL, 5 )
		
		self.m_staticText81 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u"Tags / Categories / Keywords :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		self.m_staticText81.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer161.Add( self.m_staticText81, 0, wx.ALL, 5 )
		
		
		bSizer141.Add( bSizer161, 0, wx.EXPAND, 5 )
		
		self.m_AdKeyword = wx.TextCtrl( self.m_assistantPanel, wx.ID_ANY, u"Asset", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.m_AdKeyword.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_AdKeyword.SetMinSize( wx.Size( -1,100 ) )
		
		bSizer141.Add( self.m_AdKeyword, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer141, 1, wx.EXPAND, 5 )
		
		
		bSizer55.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		self.m_staticline31 = wx.StaticLine( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer55.Add( self.m_staticline31, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap20 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/p2p_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer121.Add( self.m_bitmap20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText71 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u"P2P Sell Method :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		self.m_staticText71.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer121.Add( self.m_staticText71, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_txMethodChoices = [ u"Atomic Swap", u"P2SH", u"Raw Text" ]
		self.m_txMethod = wx.Choice( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_txMethodChoices, 0 )
		self.m_txMethod.SetSelection( 0 )
		bSizer121.Add( self.m_txMethod, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer118 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText56 = wx.StaticText( self.m_assistantPanel, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )
		bSizer118.Add( self.m_staticText56, 0, wx.ALL, 5 )
		
		
		bSizer121.Add( bSizer118, 1, wx.EXPAND, 5 )
		
		bSizer117 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap38 = wx.StaticBitmap( self.m_assistantPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer117.Add( self.m_bitmap38, 0, wx.ALL, 5 )
		
		
		bSizer121.Add( bSizer117, 0, 0, 5 )
		
		
		bSizer55.Add( bSizer121, 0, wx.EXPAND, 5 )
		
		self.m_atomicswapPanel = wx.Panel( self.m_assistantPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer56 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap21 = wx.StaticBitmap( self.m_atomicswapPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_bitmap21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u"Select an Asset : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer11.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_AdAssetChoiceChoices = []
		self.m_AdAssetChoice = wx.Choice( self.m_atomicswapPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AdAssetChoiceChoices, 0 )
		self.m_AdAssetChoice.SetSelection( 0 )
		bSizer11.Add( self.m_AdAssetChoice, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer41.Add( bSizer11, 2, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u"Quantity :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer12.Add( self.m_staticText7, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdAssetQt = wx.TextCtrl( self.m_atomicswapPanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		bSizer12.Add( self.m_AdAssetQt, 1, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		
		bSizer56.Add( bSizer41, 0, wx.EXPAND, 5 )
		
		bSizer412 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_atomicTransactionUserFeedback = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u"Click on preview to generate the atomic swap transaction", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_atomicTransactionUserFeedback.Wrap( -1 )
		self.m_atomicTransactionUserFeedback.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		bSizer111.Add( self.m_atomicTransactionUserFeedback, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer412.Add( bSizer111, 2, wx.EXPAND, 5 )
		
		bSizer1212 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText712 = wx.StaticText( self.m_atomicswapPanel, wx.ID_ANY, u"Price :", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText712.Wrap( -1 )
		self.m_staticText712.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1212.Add( self.m_staticText712, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AdAssetPrice = wx.TextCtrl( self.m_atomicswapPanel, wx.ID_ANY, u"200", wx.DefaultPosition, wx.DefaultSize, wx.TE_RIGHT )
		bSizer1212.Add( self.m_AdAssetPrice, 1, wx.ALL, 5 )
		
		
		bSizer412.Add( bSizer1212, 1, wx.EXPAND, 5 )
		
		
		bSizer56.Add( bSizer412, 0, wx.EXPAND, 5 )
		
		
		self.m_atomicswapPanel.SetSizer( bSizer56 )
		self.m_atomicswapPanel.Layout()
		bSizer56.Fit( self.m_atomicswapPanel )
		bSizer55.Add( self.m_atomicswapPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_assistantPanel.SetSizer( bSizer55 )
		self.m_assistantPanel.Layout()
		bSizer55.Fit( self.m_assistantPanel )
		bSizer1.Add( self.m_assistantPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline3111 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline3111, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer4121 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2121 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2121.Wrap( -1 )
		self.m_staticText2121.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1111.Add( self.m_staticText2121, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer4121.Add( bSizer1111, 3, wx.EXPAND, 5 )
		
		bSizer1211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap121 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/p2p_icon2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1211.Add( self.m_bitmap121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText711 = wx.StaticText( self, wx.ID_ANY, u"P2P Channel Asset :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText711.Wrap( -1 )
		self.m_staticText711.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1211.Add( self.m_staticText711, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_AdP2PChannelChoiceChoices = []
		self.m_AdP2PChannelChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AdP2PChannelChoiceChoices, 0 )
		self.m_AdP2PChannelChoice.SetSelection( 0 )
		bSizer1211.Add( self.m_AdP2PChannelChoice, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap16 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1211.Add( self.m_bitmap16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer4121.Add( bSizer1211, 2, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer4121, 0, wx.EXPAND, 5 )
		
		self.m_staticline311 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline311, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_PreviewAdBt = wx.Button( self, wx.ID_ANY, u"Preview Ad", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_PreviewAdBt, 0, wx.ALL, 5 )
		
		self.m_GeneraeteAdBt = wx.Button( self, wx.ID_ANY, u"Generate Ad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_GeneraeteAdBt.Enable( False )
		
		bSizer22.Add( self.m_GeneraeteAdBt, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer22, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_toggleAssistant.Bind( wx.EVT_TOGGLEBUTTON, self.OnWizardButtonToggle )
		self.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.OnAdTypeChanged )
		self.m_AdTitle.Bind( wx.EVT_TEXT, self.OnTitleChanged )
		self.m_AdLink.Bind( wx.EVT_TEXT, self.OnLinkChanged )
		self.m_AdDescription.Bind( wx.EVT_TEXT, self.OnDescriptionChanged )
		self.m_AdKeyword.Bind( wx.EVT_TEXT, self.OnKeywordChanged )
		self.m_txMethod.Bind( wx.EVT_CHOICE, self.OnTxMethodChanged )
		self.m_AdAssetChoice.Bind( wx.EVT_CHOICE, self.OnAssetChanged )
		self.m_AdAssetQt.Bind( wx.EVT_TEXT, self.OnQuantityChanged )
		self.m_AdAssetPrice.Bind( wx.EVT_TEXT, self.OnPriceChanged )
		self.m_AdP2PChannelChoice.Bind( wx.EVT_CHOICE, self.OnP2PChannelChanged )
		self.m_PreviewAdBt.Bind( wx.EVT_BUTTON, self.OnPreviewAdButtonClick )
		self.m_GeneraeteAdBt.Bind( wx.EVT_BUTTON, self.OnGenerateButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnWizardButtonToggle( self, event ):
		event.Skip()
	
	def OnAdTypeChanged( self, event ):
		event.Skip()
	
	def OnTitleChanged( self, event ):
		event.Skip()
	
	def OnLinkChanged( self, event ):
		event.Skip()
	
	def OnDescriptionChanged( self, event ):
		event.Skip()
	
	def OnKeywordChanged( self, event ):
		event.Skip()
	
	def OnTxMethodChanged( self, event ):
		event.Skip()
	
	def OnAssetChanged( self, event ):
		event.Skip()
	
	def OnQuantityChanged( self, event ):
		event.Skip()
	
	def OnPriceChanged( self, event ):
		event.Skip()
	
	def OnP2PChannelChanged( self, event ):
		event.Skip()
	
	def OnPreviewAdButtonClick( self, event ):
		event.Skip()
	
	def OnGenerateButtonClick( self, event ):
		event.Skip()
	

