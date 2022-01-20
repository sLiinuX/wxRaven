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
## Class wxRavenIPFSWebView
###########################################################################

class wxRavenIPFSWebView ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 587,366 ), style = wx.TAB_TRAVERSAL )
		
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		
		# Connect Events
		self.Bind( wx.EVT_TIMER, self.OnTick, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnTick( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenIPFSFileUploaderDialog
###########################################################################

class wxRavenIPFSFileUploaderDialog ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,111 ), style = wx.TAB_TRAVERSAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/ressource_picture.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer5.Add( self.m_filePicker1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_hashResult = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), wx.TE_READONLY )
		bSizer4.Add( self.m_hashResult, 1, wx.ALL, 5 )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_bitmap2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer4, 0, wx.ALIGN_CENTER, 5 )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_SendButton = wx.Button( self, wx.ID_ANY, u"Upload File", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_SendButton, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		# Connect Events
		self.m_SendButton.Bind( wx.EVT_BUTTON, self.OnSendButton )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSendButton( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenIPFS_SettingsPanel
###########################################################################

class wxRavenIPFS_SettingsPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raven_ipfs.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_bitmap3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Default IPFS Hosting Website :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer7.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_ipfsHomepage = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_ipfsHomepage, 1, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap31 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raven_ipfs.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.m_bitmap31, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Prim. IPFS Hosting RPC :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		self.m_staticText21.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer71.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_ipfsRPC = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.m_ipfsRPC, 1, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer71, 0, wx.EXPAND, 5 )
		
		bSizer712 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap312 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raven_ipfs.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer712.Add( self.m_bitmap312, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText212 = wx.StaticText( self, wx.ID_ANY, u"Sec. IPFS Hosting RPC :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText212.Wrap( -1 )
		self.m_staticText212.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer712.Add( self.m_staticText212, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_ipfsRPC2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ipfsRPC2.Enable( False )
		
		bSizer712.Add( self.m_ipfsRPC2, 1, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer712, 0, wx.EXPAND, 5 )
		
		bSizer711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap311 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raven_ipfs.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer711.Add( self.m_bitmap311, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText211 = wx.StaticText( self, wx.ID_ANY, u"Default IPFS Hosting API :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText211.Wrap( -1 )
		self.m_staticText211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText211.Enable( False )
		
		bSizer711.Add( self.m_staticText211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_ipfsAPI = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_ipfsAPI.Enable( False )
		
		bSizer711.Add( self.m_ipfsAPI, 1, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer711, 0, wx.EXPAND, 5 )
		
		bSizer7111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap3111 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/help_contents.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7111.Add( self.m_bitmap3111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Check !", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7111.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer7111, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnDoCheckIPFS )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnDoCheckIPFS( self, event ):
		event.Skip()
	

