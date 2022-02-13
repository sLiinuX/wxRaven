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
## Class wxRaven_Webservices_SettingsPanel
###########################################################################

class wxRaven_Webservices_SettingsPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,435 ), style = wx.TAB_TRAVERSAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/connexion_share_3.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_bitmap4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"JSON Webservice", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer7.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		bSizer7.Add( self.m_staticText18, 1, wx.ALL, 5 )
		
		self.m_serviceStatusText = wx.StaticText( self, wx.ID_ANY, u"[STATUS]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_serviceStatusText.Wrap( -1 )
		bSizer7.Add( self.m_serviceStatusText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/process_stop.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer7.Add( self.m_bpButton1, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_enableService = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_enableService, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Enable JSON Webservice", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer8.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer9.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline13, 0, wx.EXPAND|wx.ALL, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap11 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/computer_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_bitmap11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Server IP :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		bSizer11.Add( self.m_staticText20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_serverIP = wx.TextCtrl( self, wx.ID_ANY, u"127.0.0.1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_serverIP.SetMaxLength( 0 ) 
		bSizer11.Add( self.m_serverIP, 1, wx.ALL, 5 )
		
		self.m_staticText201 = wx.StaticText( self, wx.ID_ANY, u"Server Port :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )
		bSizer11.Add( self.m_staticText201, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_serverPort = wx.TextCtrl( self, wx.ID_ANY, u"9090", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_serverPort.SetMaxLength( 0 ) 
		bSizer11.Add( self.m_serverPort, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap1112 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/changelog_obj.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_bitmap1112, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText2022 = wx.StaticText( self, wx.ID_ANY, u"Service Log :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2022.Wrap( -1 )
		bSizer12.Add( self.m_staticText2022, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_filePickerService = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.log", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		bSizer12.Add( self.m_filePickerService, 1, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap111 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/webservice_admin.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_bitmap111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText202 = wx.StaticText( self, wx.ID_ANY, u"Webservice Admin Token :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText202.Wrap( -1 )
		bSizer13.Add( self.m_staticText202, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textAdminToken = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_textAdminToken, 1, wx.ALL, 5 )
		
		self.m_bpButtonGenerateAdmin = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer13.Add( self.m_bpButtonGenerateAdmin, 0, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		bSizer131 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_forceNetwork = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer131.Add( self.m_forceNetwork, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap1113 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer131.Add( self.m_bitmap1113, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText2023 = wx.StaticText( self, wx.ID_ANY, u"Force Network :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2023.Wrap( -1 )
		bSizer131.Add( self.m_staticText2023, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_NetworkChoiceChoices = []
		self.m_NetworkChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_NetworkChoiceChoices, 0 )
		self.m_NetworkChoice.SetSelection( 0 )
		bSizer131.Add( self.m_NetworkChoice, 1, wx.ALL, 5 )
		
		
		bSizer10.Add( bSizer131, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer10, 0, wx.EXPAND, 5 )
		
		self.m_staticline131 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline131, 0, wx.EXPAND|wx.ALL, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap1111 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/blacklist.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_bitmap1111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText2021 = wx.StaticText( self, wx.ID_ANY, u"Do Not Start Modules :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2021.Wrap( -1 )
		bSizer14.Add( self.m_staticText2021, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer14, 0, wx.EXPAND, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		m_checkList1Choices = []
		self.m_checkList1 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList1Choices, 0 )
		bSizer16.Add( self.m_checkList1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer15.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		self.m_timer2 = wx.Timer()
		self.m_timer2.SetOwner( self, wx.ID_ANY )
		self.m_timer2.Start( 1000 )
		
	
	def __del__( self ):
		pass
	

