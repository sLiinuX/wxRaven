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
import wx.dataview

###########################################################################
## Class wxRavenWalletMain
###########################################################################

class wxRavenWalletMain ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 510,466 ), style = wx.TAB_TRAVERSAL )
		
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
		
		self.wxRavenWalletBook = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.wxRavenWalletBook, wx.aui.AuiPaneInfo() .Left() .CaptionVisible( False ).CloseButton( False ).PaneBorder( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).CentrePane() )
		
		
		
		self.m_mgr.Update()
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	

###########################################################################
## Class wxRavenWalletOverview
###########################################################################

class wxRavenWalletOverview ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 453,407 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_infoCtrl1 = wx.InfoBar( self )
		self.m_infoCtrl1.SetShowHideEffects( wx.SHOW_EFFECT_NONE, wx.SHOW_EFFECT_NONE )
		self.m_infoCtrl1.SetEffectDuration( 500 )
		bSizer1.Add( self.m_infoCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/wallet_64.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.balanceStaticText = wx.StaticText( self, wx.ID_ANY, u"???", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.balanceStaticText.Wrap( -1 )
		self.balanceStaticText.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.balanceStaticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"RVN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		self.m_staticText13.SetFont( wx.Font( 20, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.showAddressCheckbox = wx.CheckBox( self, wx.ID_ANY, u"Show/Hide Account(s) Addresse(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.showAddressCheckbox, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.showChangesAddress = wx.CheckBox( self, wx.ID_ANY, u"Show Changes Addresses", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.showChangesAddress.SetValue(True) 
		bSizer1.Add( self.showChangesAddress, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.addressViewListCtrl = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.addressViewListCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.showAddressCheckbox.Bind( wx.EVT_CHECKBOX, self.OnRefreshButton )
		self.showChangesAddress.Bind( wx.EVT_CHECKBOX, self.OnShowChangesAddresses )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnRefreshButton( self, event ):
		event.Skip()
	
	def OnShowChangesAddresses( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenWalletAssetsOverview
###########################################################################

class wxRavenWalletAssetsOverview ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 453,366 ), style = wx.TAB_TRAVERSAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_infoCtrl1 = wx.InfoBar( self )
		self.m_infoCtrl1.SetShowHideEffects( wx.SHOW_EFFECT_NONE, wx.SHOW_EFFECT_NONE )
		self.m_infoCtrl1.SetEffectDuration( 500 )
		bSizer3.Add( self.m_infoCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.assetsViewListCtrl = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.assetsViewListCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenWalletSend
###########################################################################

class wxRavenWalletSend ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 453,276 ), style = wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_infoCtrl1 = wx.InfoBar( self )
		self.m_infoCtrl1.SetShowHideEffects( wx.SHOW_EFFECT_NONE, wx.SHOW_EFFECT_NONE )
		self.m_infoCtrl1.SetEffectDuration( 500 )
		bSizer4.Add( self.m_infoCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline61 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline61, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Send From (Optional) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer6.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		sendFromTextboxChoices = []
		self.sendFromTextbox = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,-1 ), sendFromTextboxChoices, 0 )
		self.sendFromTextbox.SetSelection( 0 )
		bSizer6.Add( self.sendFromTextbox, 1, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Send to :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer5.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.sendToTextbox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer5.Add( self.sendToTextbox, 1, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Amount :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer7.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.sendAmountTextbox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.sendAmountTextbox, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer7, 0, wx.ALIGN_RIGHT, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.balanceStaticText = wx.StaticText( self, wx.ID_ANY, u"???", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.balanceStaticText.Wrap( -1 )
		self.balanceStaticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer9.Add( self.balanceStaticText, 1, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer9, 0, wx.ALIGN_RIGHT, 5 )
		
		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Password (Optional) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer8.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.passwordTextbox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		bSizer8.Add( self.passwordTextbox, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer8, 0, wx.ALIGN_RIGHT, 5 )
		
		self.m_staticline62 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer4.Add( self.m_staticline62, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.sendButton = wx.Button( self, wx.ID_ANY, u"Send !", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.sendButton, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer10, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		# Connect Events
		self.sendFromTextbox.Bind( wx.EVT_CHOICE, self.OnChoiceChanged )
		self.sendButton.Bind( wx.EVT_BUTTON, self.OnSendClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnChoiceChanged( self, event ):
		event.Skip()
	
	def OnSendClick( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenWalletOverview_DEPRECATED
###########################################################################

class wxRavenWalletOverview_DEPRECATED ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 542,488 ), style = wx.ALWAYS_SHOW_SB|wx.HSCROLL|wx.TAB_TRAVERSAL|wx.VSCROLL )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"RVN Balance :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.balanceStaticText = wx.StaticText( self, wx.ID_ANY, u"???", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.balanceStaticText.Wrap( -1 )
		self.balanceStaticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.balanceStaticText, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"RVN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/iu_update_obj.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		gbSizer1.Add( self.m_bpButton1, wx.GBPosition( 0, 19 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer1.Add( self.m_staticline1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 23 ), wx.EXPAND |wx.ALL, 5 )
		
		self.addressViewListCtrl = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.addressViewListCtrl, wx.GBPosition( 2, 1 ), wx.GBSpan( 10, 20 ), wx.ALL|wx.EXPAND, 5 )
		
		self.showAddressCheckbox = wx.CheckBox( self, wx.ID_ANY, u"Show addresses and display assets...", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.showAddressCheckbox, wx.GBPosition( 12, 9 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer1.Add( self.m_staticline11, wx.GBPosition( 13, 0 ), wx.GBSpan( 1, 23 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Assets :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gbSizer1.Add( self.m_staticText11, wx.GBPosition( 14, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.assetsViewListCtrl = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.assetsViewListCtrl, wx.GBPosition( 15, 1 ), wx.GBSpan( 10, 20 ), wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.OnRefreshButton )
		self.showAddressCheckbox.Bind( wx.EVT_CHECKBOX, self.OnRefreshButton )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnRefreshButton( self, event ):
		event.Skip()
	
	

###########################################################################
## Class wxRavenWalletSend_DEPRECATED
###########################################################################

class wxRavenWalletSend_DEPRECATED ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 513,332 ), style = wx.TAB_TRAVERSAL )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Available :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gbSizer1.Add( self.m_staticText1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.balanceStaticText = wx.StaticText( self, wx.ID_ANY, u"???", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.balanceStaticText.Wrap( -1 )
		self.balanceStaticText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		gbSizer1.Add( self.balanceStaticText, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 3 ), wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"RVN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gbSizer1.Add( self.m_staticText3, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer1.Add( self.m_staticline1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 23 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Send to :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		gbSizer1.Add( self.m_staticText14, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.sendToTextbox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		gbSizer1.Add( self.sendToTextbox, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 20 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Amount :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		gbSizer1.Add( self.m_staticText15, wx.GBPosition( 3, 19 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.sendAmountTextbox = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 999999999, 1420 )
		gbSizer1.Add( self.sendAmountTextbox, wx.GBPosition( 3, 20 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer1.Add( self.m_staticline11, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 23 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Send From Address (Optional) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gbSizer1.Add( self.m_staticText11, wx.GBPosition( 6, 1 ), wx.GBSpan( 1, 10 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		sendFromTextboxChoices = []
		self.sendFromTextbox = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,-1 ), sendFromTextboxChoices, 0 )
		self.sendFromTextbox.SetSelection( 0 )
		gbSizer1.Add( self.sendFromTextbox, wx.GBPosition( 7, 1 ), wx.GBSpan( 1, 21 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Password (Optional) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gbSizer1.Add( self.m_staticText16, wx.GBPosition( 8, 1 ), wx.GBSpan( 1, 15 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.passwordTextbox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gbSizer1.Add( self.passwordTextbox, wx.GBPosition( 8, 16 ), wx.GBSpan( 1, 8 ), wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline111 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		gbSizer1.Add( self.m_staticline111, wx.GBPosition( 10, 0 ), wx.GBSpan( 1, 23 ), wx.EXPAND |wx.ALL, 5 )
		
		self.sendButton = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.sendButton, wx.GBPosition( 11, 20 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		# Connect Events
		self.sendFromTextbox.Bind( wx.EVT_CHOICE, self.OnChoiceChanged )
		self.sendButton.Bind( wx.EVT_BUTTON, self.OnSendClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnChoiceChanged( self, event ):
		event.Skip()
	
	def OnSendClick( self, event ):
		event.Skip()
	

