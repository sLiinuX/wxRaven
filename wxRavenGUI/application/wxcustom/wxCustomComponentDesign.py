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
## Class wxRavenDialogbox
###########################################################################

class wxRavenDialogbox ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 470,215 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class wxRavenPanel
###########################################################################

class wxRavenPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 222,103 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class wxRavenMessageDialog
###########################################################################

class wxRavenMessageDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"wxRaven - Message", pos = wx.DefaultPosition, size = wx.Size( 580,250 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 580,-1 ), wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_messageIcon = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/info_icon_45.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_messageIcon, 0, wx.ALL, 5 )

		self.m_messageText = wx.StaticText( self, wx.ID_ANY, u"This is the default Message", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_messageText.Wrap( -1 )

		bSizer6.Add( self.m_messageText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_ExpandButton = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_ExpandButton.SetBitmap( wx.Bitmap( u"res/default_style/normal/expandall.png", wx.BITMAP_TYPE_ANY ) )
		bSizer7.Add( self.m_ExpandButton, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Show/Hide Details", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer7.Add( self.m_staticText2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_CancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_CancelButton, 0, wx.ALL, 5 )

		self.m_OKButton = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_OKButton, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_detailsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline1 = wx.StaticLine( self.m_detailsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer9.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_detailsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrl1.SetMinSize( wx.Size( -1,100 ) )

		bSizer9.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_detailsPanel.SetSizer( bSizer9 )
		self.m_detailsPanel.Layout()
		bSizer9.Fit( self.m_detailsPanel )
		bSizer8.Add( self.m_detailsPanel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class wxRavenSaveFileDialog
###########################################################################

class wxRavenSaveFileDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"wxRaven - Unsaved File", pos = wx.DefaultPosition, size = wx.Size( 580,250 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 580,-1 ), wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_messageIcon = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/warning_icon_45.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_messageIcon, 0, wx.ALL, 5 )

		self.m_messageText = wx.StaticText( self, wx.ID_ANY, u"The file has been modified, do you want to save it ?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_messageText.Wrap( -1 )

		bSizer6.Add( self.m_messageText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer16.Add( self.m_staticText7, 1, wx.ALL, 5 )

		self.m_checkBoxBackupFile = wx.CheckBox( self, wx.ID_ANY, u"Create a backup file of the original version", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer16.Add( self.m_checkBoxBackupFile, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer16, 0, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_ExpandButton = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_ExpandButton.SetBitmap( wx.Bitmap( u"res/default_style/normal/expandall.png", wx.BITMAP_TYPE_ANY ) )
		bSizer7.Add( self.m_ExpandButton, 0, wx.ALL, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Show/Hide Details", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer7.Add( self.m_staticText2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_CancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_CancelButton, 0, wx.ALL, 5 )

		self.m_SaveAsButton = wx.Button( self, wx.ID_ANY, u"Save As...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_SaveAsButton, 0, wx.ALL, 5 )

		self.m_SaveButton = wx.Button( self, wx.ID_ANY, u"Save...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_SaveButton, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_detailsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticline1 = wx.StaticLine( self.m_detailsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer9.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_detailsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		self.m_textCtrl1.SetMinSize( wx.Size( -1,100 ) )

		bSizer9.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_detailsPanel.SetSizer( bSizer9 )
		self.m_detailsPanel.Layout()
		bSizer9.Fit( self.m_detailsPanel )
		bSizer8.Add( self.m_detailsPanel, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


