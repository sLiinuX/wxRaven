# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class wxRaven_Webservices_SettingsPanel
###########################################################################

class wxRaven_Webservices_SettingsPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,435 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/connexion_share_3.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_bitmap4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"JSON Webservice Daemon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer7.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer7.Add( self.m_staticText18, 1, wx.ALL, 5 )

		self.m_serviceStatusText = wx.StaticText( self, wx.ID_ANY, u"[STATUS]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_serviceStatusText.Wrap( -1 )

		bSizer7.Add( self.m_serviceStatusText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton1.SetBitmap( wx.Bitmap( u"res/default_style/normal/process_stop.png", wx.BITMAP_TYPE_ANY ) )
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

		self.m_bpButtonGenerateAdmin = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButtonGenerateAdmin.SetBitmap( wx.Bitmap( u"res/default_style/normal/refresh.png", wx.BITMAP_TYPE_ANY ) )
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


###########################################################################
## Class wxRaven_Webservices_RemoteJobs_Settings
###########################################################################

class wxRaven_Webservices_RemoteJobs_Settings ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,385 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap7 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/job_remote_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_bitmap7, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Remote Jobs Webservices :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		self.m_staticText12.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer15.Add( self.m_staticText12, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer15, 0, wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_MeasureJobQueryResult = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_MeasureJobQueryResult.SetValue(True)
		bSizer24.Add( self.m_MeasureJobQueryResult, 0, wx.ALL, 5 )

		self.m_bitmap10 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/speedmeter_icon_2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_bitmap10, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Measure and limit remote jobs query result size (see WS Limiter)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		bSizer24.Add( self.m_staticText15, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer24, 0, wx.EXPAND, 5 )

		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer14.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap1111 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/blacklist.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer141.Add( self.m_bitmap1111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText2021 = wx.StaticText( self, wx.ID_ANY, u"Do Not Allow Jobs from remote :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2021.Wrap( -1 )

		bSizer141.Add( self.m_staticText2021, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer14.Add( bSizer141, 0, wx.EXPAND, 5 )

		bSizer42 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_MeasureJobQueryResult1 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_MeasureJobQueryResult1.SetValue(True)
		self.m_MeasureJobQueryResult1.Enable( False )

		bSizer42.Add( self.m_MeasureJobQueryResult1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Redirect to :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		bSizer42.Add( self.m_staticText34, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer14.Add( bSizer42, 0, wx.EXPAND, 5 )

		bSizer421 = wx.BoxSizer( wx.HORIZONTAL )

		m_choiceJobRedirectionChoices = [ u"plugins.Webservices.jobs.RemoteJobs_NotAllowedJob.Job_NotAllowedRemoteJob", u"plugins.Webservices.jobs.RemoteJobs_NotAllowedJob.Job_NotAllowedRemoteJobAlternate" ]
		self.m_choiceJobRedirection = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceJobRedirectionChoices, 0 )
		self.m_choiceJobRedirection.SetSelection( 0 )
		bSizer421.Add( self.m_choiceJobRedirection, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer421, 0, wx.EXPAND, 5 )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		m_checkList1Choices = []
		self.m_checkList1 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList1Choices, 0 )
		bSizer16.Add( self.m_checkList1, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer151.Add( bSizer16, 1, wx.EXPAND, 5 )


		bSizer14.Add( bSizer151, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxRaven_Webservices_ServerOptions_Settings
###########################################################################

class wxRaven_Webservices_ServerOptions_Settings ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,376 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap11 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/settings_2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_bitmap11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Webservice : Services options and limiter", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer26.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer26.Add( self.m_staticText17, 1, wx.ALL, 5 )

		self.m_bpButton3 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton3.SetBitmap( wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ) )
		self.m_bpButton3.SetToolTip( u"This section represent the server_config.json file at the plugin location.\n\nyou can setup webservices options and limitations.\n\nUsersession (if the API service is enable) provide a User Session Token mechanism to identify Specific wxRaven users and provide them a increased limitation compare to an anonymous query.\n" )

		bSizer26.Add( self.m_bpButton3, 0, wx.ALL, 5 )


		bSizer25.Add( bSizer26, 0, wx.EXPAND, 5 )

		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer25.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox4 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox4.SetValue(True)
		self.m_checkBox4.Enable( False )

		bSizer27.Add( self.m_checkBox4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_bitmap12 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/unknown_user.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_bitmap12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self, wx.ID_ANY, u"Anonymous Query Result Max Size :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		bSizer27.Add( self.m_staticText18, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		bSizer27.Add( self.m_staticText19, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, u"512000", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 512000, 10485760, 512000 )
		bSizer27.Add( self.m_spinCtrl1, 1, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Bytes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer27.Add( self.m_staticText20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer25.Add( bSizer27, 0, wx.EXPAND, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		bSizer34.Add( self.m_staticText21, 1, wx.ALL, 5 )

		self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"= 512 Kb", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer34.Add( self.m_staticText22, 0, wx.ALL, 5 )


		bSizer25.Add( bSizer34, 0, wx.EXPAND, 5 )

		bSizer271 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox41 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox41.SetValue(True)
		self.m_checkBox41.Enable( False )

		bSizer271.Add( self.m_checkBox41, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_bitmap121 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/UserAccount_custom.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer271.Add( self.m_bitmap121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText181 = wx.StaticText( self, wx.ID_ANY, u"User Session Query Result Max Size :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText181.Wrap( -1 )

		bSizer271.Add( self.m_staticText181, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText191 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )

		bSizer271.Add( self.m_staticText191, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_spinCtrl11 = wx.SpinCtrl( self, wx.ID_ANY, u"10485760", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 512000, 104857600, 10485760 )
		bSizer271.Add( self.m_spinCtrl11, 1, wx.ALL, 5 )

		self.m_staticText201 = wx.StaticText( self, wx.ID_ANY, u"Bytes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText201.Wrap( -1 )

		bSizer271.Add( self.m_staticText201, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer25.Add( bSizer271, 0, wx.EXPAND, 5 )

		bSizer341 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText211 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )

		bSizer341.Add( self.m_staticText211, 1, wx.ALL, 5 )

		self.m_staticText221 = wx.StaticText( self, wx.ID_ANY, u"= 10 Mb", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText221.Wrap( -1 )

		self.m_staticText221.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer341.Add( self.m_staticText221, 0, wx.ALL, 5 )


		bSizer25.Add( bSizer341, 0, wx.EXPAND, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_checkBox7 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox7.SetValue(True)
		self.m_checkBox7.Enable( False )

		bSizer41.Add( self.m_checkBox7, 0, wx.ALL, 5 )

		self.m_bitmap15 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/lock_key.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_bitmap15, 0, wx.ALL, 5 )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Enable User Session Private Token (DEMO)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		bSizer41.Add( self.m_staticText33, 0, wx.ALL, 5 )


		bSizer25.Add( bSizer41, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer25 )
		self.Layout()

	def __del__( self ):
		pass


