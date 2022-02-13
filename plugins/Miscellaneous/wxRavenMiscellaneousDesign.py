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
## Class wxRavenMiscellaneous_Advertising
###########################################################################

class wxRavenMiscellaneous_Advertising ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 678,311 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap126 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap126, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText178 = wx.StaticText( self, wx.ID_ANY, u"Asset :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText178.Wrap( -1 )
		bSizer2.Add( self.m_staticText178, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_AssetChoiceChoices = []
		self.m_AssetChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AssetChoiceChoices, 0 )
		self.m_AssetChoice.SetSelection( 0 )
		bSizer2.Add( self.m_AssetChoice, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap127 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/mailbox_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_bitmap127, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText179 = wx.StaticText( self, wx.ID_ANY, u"Distribution Amount :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText179.Wrap( -1 )
		bSizer3.Add( self.m_staticText179, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AssetAmount = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_AssetAmount.SetMaxLength( 0 ) 
		bSizer3.Add( self.m_AssetAmount, 0, wx.ALL, 5 )
		
		self.m_staticText184 = wx.StaticText( self, wx.ID_ANY, u"Unit(s)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_staticText184.Wrap( -1 )
		bSizer3.Add( self.m_staticText184, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap129 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_bitmap129, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText182 = wx.StaticText( self, wx.ID_ANY, u"Available : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText182.Wrap( -1 )
		self.m_staticText182.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.m_staticText182, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_availableText = wx.StaticText( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_availableText.Wrap( -1 )
		bSizer3.Add( self.m_availableText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer4.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox7Choices = []
		self.m_listBox7 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox7Choices, 0 )
		bSizer4.Add( self.m_listBox7, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.m_panel37 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_ProgressText = wx.StaticText( self.m_panel37, wx.ID_ANY, u"Progress :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ProgressText.Wrap( -1 )
		bSizer6.Add( self.m_ProgressText, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer6, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_gauge1 = wx.Gauge( self.m_panel37, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,20 ), wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 ) 
		bSizer7.Add( self.m_gauge1, 1, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		self.m_panel37.SetSizer( bSizer5 )
		self.m_panel37.Layout()
		bSizer5.Fit( self.m_panel37 )
		bSizer1.Add( self.m_panel37, 0, wx.EXPAND|wx.ALL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_CreateUTXOButton_OLD = wx.Button( self, wx.ID_ANY, u"DROP !", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_CreateUTXOButton_OLD.Hide()
		
		bSizer8.Add( self.m_CreateUTXOButton_OLD, 0, wx.ALL, 5 )
		
		self.m_CreateUTXOButton = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/airdrop_icon_35.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_CreateUTXOButton.Hide()
		
		bSizer8.Add( self.m_CreateUTXOButton, 0, wx.ALL, 5 )
		
		self.m_RocketDrop = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/advertiser_icon_45.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer8.Add( self.m_RocketDrop, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer8, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_AssetChoice.Bind( wx.EVT_CHOICE, self.OnAssetChanged )
		self.m_AssetAmount.Bind( wx.EVT_TEXT, self.OnAmountChanged )
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChanged )
		self.m_RocketDrop.Bind( wx.EVT_BUTTON, self.OnRocketDropClicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnAssetChanged( self, event ):
		event.Skip()
	
	def OnAmountChanged( self, event ):
		event.Skip()
	
	def OnFileChanged( self, event ):
		event.Skip()
	
	def OnRocketDropClicked( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenMiscellaneous_Airdrop
###########################################################################

class wxRavenMiscellaneous_Airdrop ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 678,311 ), style = wx.TAB_TRAVERSAL )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap126 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_bitmap126, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText178 = wx.StaticText( self, wx.ID_ANY, u"Airdrop Asset :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText178.Wrap( -1 )
		bSizer10.Add( self.m_staticText178, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_AssetChoiceChoices = []
		self.m_AssetChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AssetChoiceChoices, 0 )
		self.m_AssetChoice.SetSelection( 0 )
		bSizer10.Add( self.m_AssetChoice, 1, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap129 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_bitmap129, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText182 = wx.StaticText( self, wx.ID_ANY, u"Available : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText182.Wrap( -1 )
		self.m_staticText182.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer11.Add( self.m_staticText182, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_availableText = wx.StaticText( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_availableText.Wrap( -1 )
		bSizer11.Add( self.m_availableText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer11, 0, wx.ALIGN_RIGHT, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap127 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/airdrop_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_bitmap127, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText179 = wx.StaticText( self, wx.ID_ANY, u"Distribute :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText179.Wrap( -1 )
		bSizer12.Add( self.m_staticText179, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AssetAmount = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_AssetAmount.SetMaxLength( 0 ) 
		bSizer12.Add( self.m_AssetAmount, 0, wx.ALL, 5 )
		
		self.m_staticText184 = wx.StaticText( self, wx.ID_ANY, u"Asset(s) to :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText184.Wrap( -1 )
		bSizer12.Add( self.m_staticText184, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap128 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/formula.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_bitmap128, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_UTXOcount = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 500, 1 )
		bSizer12.Add( self.m_UTXOcount, 0, wx.ALL, 5 )
		
		self.m_staticText180 = wx.StaticText( self, wx.ID_ANY, u"Max Winner(s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText180.Wrap( -1 )
		bSizer12.Add( self.m_staticText180, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText202 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText202.Wrap( -1 )
		bSizer13.Add( self.m_staticText202, 1, wx.ALL, 5 )
		
		self.m_checkBox26 = wx.CheckBox( self, wx.ID_ANY, u"Pickup Random Winners from list", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_checkBox26, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer13, 0, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer14.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )
		
		m_listBox7Choices = []
		self.m_listBox7 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox7Choices, 0 )
		bSizer14.Add( self.m_listBox7, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer9.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_CreateUTXOButton_OLD = wx.Button( self, wx.ID_ANY, u"DROP !", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_CreateUTXOButton_OLD.Hide()
		
		bSizer15.Add( self.m_CreateUTXOButton_OLD, 0, wx.ALL, 5 )
		
		self.m_CreateUTXOButton = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/airdrop_icon_35.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer15.Add( self.m_CreateUTXOButton, 0, wx.ALL, 5 )
		
		self.m_RocketDrop = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/rocketdrop_35.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.m_RocketDrop.Hide()
		
		bSizer15.Add( self.m_RocketDrop, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer15, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		# Connect Events
		self.m_AssetChoice.Bind( wx.EVT_CHOICE, self.OnAssetChanged )
		self.m_AssetAmount.Bind( wx.EVT_TEXT, self.OnAmountChanged )
		self.m_UTXOcount.Bind( wx.EVT_SPINCTRL, self.OnUTXOChanged )
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChanged )
		self.m_CreateUTXOButton.Bind( wx.EVT_BUTTON, self.OnClickCreateUTXO )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnAssetChanged( self, event ):
		event.Skip()
	
	def OnAmountChanged( self, event ):
		event.Skip()
	
	def OnUTXOChanged( self, event ):
		event.Skip()
	
	def OnFileChanged( self, event ):
		event.Skip()
	
	def OnClickCreateUTXO( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenMiscellaneous_NodeMonitor
###########################################################################

class wxRavenMiscellaneous_NodeMonitor ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 428,370 ), style = wx.TAB_TRAVERSAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap28 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/monitoring_dashboard_2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_bitmap28, 0, wx.ALL, 5 )
		
		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"Monitoring Panel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )
		self.m_staticText57.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer17.Add( self.m_staticText57, 0, wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer17, 0, wx.ALIGN_CENTER, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"Auto-Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.SetValue(True) 
		bSizer35.Add( self.m_checkBox2, 0, wx.ALL, 5 )
		
		
		bSizer16.Add( bSizer35, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer16.Add( self.m_staticline14, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.m_networkPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap19 = wx.StaticBitmap( self.m_networkPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/blockchain_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_bitmap19, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self.m_networkPanel, wx.ID_ANY, u"Network :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		self.m_staticText36.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer31.Add( self.m_staticText36, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer18.Add( bSizer31, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap29 = wx.StaticBitmap( self.m_networkPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/mining_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.m_bitmap29, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText58 = wx.StaticText( self.m_networkPanel, wx.ID_ANY, u"Current Block :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )
		self.m_staticText58.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer19.Add( self.m_staticText58, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextSPACER = wx.StaticText( self.m_networkPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSPACER.Wrap( -1 )
		bSizer19.Add( self.m_staticTextSPACER, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl30 = wx.TextCtrl( self.m_networkPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl30.SetMaxLength( 0 ) 
		bSizer19.Add( self.m_textCtrl30, 1, wx.ALL, 5 )
		
		
		bSizer18.Add( bSizer19, 0, wx.EXPAND, 5 )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap291 = wx.StaticBitmap( self.m_networkPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/speedmeter_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_bitmap291, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText581 = wx.StaticText( self.m_networkPanel, wx.ID_ANY, u"Network Hashrate :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText581.Wrap( -1 )
		self.m_staticText581.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer20.Add( self.m_staticText581, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextSPACER1 = wx.StaticText( self.m_networkPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSPACER1.Wrap( -1 )
		bSizer20.Add( self.m_staticTextSPACER1, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl301 = wx.TextCtrl( self.m_networkPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl301.SetMaxLength( 0 ) 
		bSizer20.Add( self.m_textCtrl301, 1, wx.ALL, 5 )
		
		
		bSizer18.Add( bSizer20, 0, wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2911 = wx.StaticBitmap( self.m_networkPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/traffic_light.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_bitmap2911, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText5811 = wx.StaticText( self.m_networkPanel, wx.ID_ANY, u"Network Diff :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5811.Wrap( -1 )
		self.m_staticText5811.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer21.Add( self.m_staticText5811, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextSPACER11 = wx.StaticText( self.m_networkPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSPACER11.Wrap( -1 )
		bSizer21.Add( self.m_staticTextSPACER11, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl3011 = wx.TextCtrl( self.m_networkPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl3011.SetMaxLength( 0 ) 
		bSizer21.Add( self.m_textCtrl3011, 1, wx.ALL, 5 )
		
		
		bSizer18.Add( bSizer21, 0, wx.EXPAND, 5 )
		
		
		self.m_networkPanel.SetSizer( bSizer18 )
		self.m_networkPanel.Layout()
		bSizer18.Fit( self.m_networkPanel )
		bSizer16.Add( self.m_networkPanel, 0, wx.EXPAND|wx.ALL, 5 )
		
		self.m_staticline141 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer16.Add( self.m_staticline141, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_nodePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer181 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer311 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap191 = wx.StaticBitmap( self.m_nodePanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/node_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer311.Add( self.m_bitmap191, 0, wx.ALL, 5 )
		
		self.m_staticText361 = wx.StaticText( self.m_nodePanel, wx.ID_ANY, u"Node :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText361.Wrap( -1 )
		self.m_staticText361.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer311.Add( self.m_staticText361, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer181.Add( bSizer311, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap292 = wx.StaticBitmap( self.m_nodePanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/block_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer191.Add( self.m_bitmap292, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText582 = wx.StaticText( self.m_nodePanel, wx.ID_ANY, u"Current Header :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText582.Wrap( -1 )
		self.m_staticText582.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer191.Add( self.m_staticText582, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextSPACER2 = wx.StaticText( self.m_nodePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSPACER2.Wrap( -1 )
		bSizer191.Add( self.m_staticTextSPACER2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl302 = wx.TextCtrl( self.m_nodePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl302.SetMaxLength( 0 ) 
		bSizer191.Add( self.m_textCtrl302, 1, wx.ALL, 5 )
		
		
		bSizer181.Add( bSizer191, 0, wx.EXPAND, 5 )
		
		bSizer201 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2912 = wx.StaticBitmap( self.m_nodePanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/speedmeter_icon_2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer201.Add( self.m_bitmap2912, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText5812 = wx.StaticText( self.m_nodePanel, wx.ID_ANY, u"Mempool Size :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5812.Wrap( -1 )
		self.m_staticText5812.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer201.Add( self.m_staticText5812, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextSPACER12 = wx.StaticText( self.m_nodePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSPACER12.Wrap( -1 )
		bSizer201.Add( self.m_staticTextSPACER12, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl3012 = wx.TextCtrl( self.m_nodePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl3012.SetMaxLength( 0 ) 
		bSizer201.Add( self.m_textCtrl3012, 1, wx.ALL, 5 )
		
		
		bSizer181.Add( bSizer201, 0, wx.EXPAND, 5 )
		
		bSizer2011 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap29121 = wx.StaticBitmap( self.m_nodePanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/speedmeter_icon_2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2011.Add( self.m_bitmap29121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText58121 = wx.StaticText( self.m_nodePanel, wx.ID_ANY, u"Mempool Usage :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58121.Wrap( -1 )
		self.m_staticText58121.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer2011.Add( self.m_staticText58121, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextSPACER121 = wx.StaticText( self.m_nodePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSPACER121.Wrap( -1 )
		bSizer2011.Add( self.m_staticTextSPACER121, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl30121 = wx.TextCtrl( self.m_nodePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrl30121.SetMaxLength( 0 ) 
		bSizer2011.Add( self.m_textCtrl30121, 1, wx.ALL, 5 )
		
		
		bSizer181.Add( bSizer2011, 0, wx.EXPAND, 5 )
		
		
		self.m_nodePanel.SetSizer( bSizer181 )
		self.m_nodePanel.Layout()
		bSizer181.Fit( self.m_nodePanel )
		bSizer16.Add( self.m_nodePanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer16 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_timer1.Start( 1000 )
		
		
		# Connect Events
		self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.OnAutoRefreshClicked )
		self.Bind( wx.EVT_TIMER, self.OnTimerTick, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnAutoRefreshClicked( self, event ):
		event.Skip()
	
	def OnTimerTick( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenMiscellaneous_CreateUTXO
###########################################################################

class wxRavenMiscellaneous_CreateUTXO ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 513,144 ), style = wx.TAB_TRAVERSAL )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap126 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_bitmap126, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText178 = wx.StaticText( self, wx.ID_ANY, u"UTXO Asset :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText178.Wrap( -1 )
		bSizer30.Add( self.m_staticText178, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_AssetChoiceChoices = []
		self.m_AssetChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_AssetChoiceChoices, 0 )
		self.m_AssetChoice.SetSelection( 0 )
		bSizer30.Add( self.m_AssetChoice, 1, wx.ALL, 5 )
		
		
		bSizer29.Add( bSizer30, 0, wx.EXPAND, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap129 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.m_bitmap129, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText182 = wx.StaticText( self, wx.ID_ANY, u"Available : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText182.Wrap( -1 )
		self.m_staticText182.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer31.Add( self.m_staticText182, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_availableText = wx.StaticText( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_availableText.Wrap( -1 )
		bSizer31.Add( self.m_availableText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer29.Add( bSizer31, 0, wx.ALIGN_RIGHT, 5 )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap127 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/supply_2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_bitmap127, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText179 = wx.StaticText( self, wx.ID_ANY, u"Amount :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText179.Wrap( -1 )
		bSizer32.Add( self.m_staticText179, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AssetAmount = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_AssetAmount.SetMaxLength( 0 ) 
		bSizer32.Add( self.m_AssetAmount, 0, wx.ALL, 5 )
		
		self.m_staticText184 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText184.Wrap( -1 )
		bSizer32.Add( self.m_staticText184, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap128 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/formula.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_bitmap128, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText180 = wx.StaticText( self, wx.ID_ANY, u"UTXO's :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText180.Wrap( -1 )
		bSizer32.Add( self.m_staticText180, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_UTXOcount = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 1000, 1 )
		bSizer32.Add( self.m_UTXOcount, 0, wx.ALL, 5 )
		
		
		bSizer29.Add( bSizer32, 0, wx.EXPAND, 5 )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_CreateUTXOButton = wx.Button( self, wx.ID_ANY, u"Create !", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_CreateUTXOButton, 0, wx.ALL, 5 )
		
		
		bSizer29.Add( bSizer33, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer29 )
		self.Layout()
		
		# Connect Events
		self.m_AssetChoice.Bind( wx.EVT_CHOICE, self.OnAssetChanged )
		self.m_AssetAmount.Bind( wx.EVT_TEXT, self.OnAmountChanged )
		self.m_UTXOcount.Bind( wx.EVT_SPINCTRL, self.OnUTXOChanged )
		self.m_CreateUTXOButton.Bind( wx.EVT_BUTTON, self.OnClickCreateUTXO )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnAssetChanged( self, event ):
		event.Skip()
	
	def OnAmountChanged( self, event ):
		event.Skip()
	
	def OnUTXOChanged( self, event ):
		event.Skip()
	
	def OnClickCreateUTXO( self, event ):
		event.Skip()
	

