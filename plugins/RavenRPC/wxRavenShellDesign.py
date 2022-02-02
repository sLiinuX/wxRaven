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

###########################################################################
## Class wxRavenShellPanel
###########################################################################

class wxRavenShellPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_auiToolBar2 = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_runPython = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/run_python.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar2.Realize() 
		
		bSizer8.Add( self.m_auiToolBar2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer8, 0, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_shellPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9.Add( self.m_shellPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenAdvancedShellPanel
###########################################################################

class wxRavenAdvancedShellPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auiToolBar1 = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.rpcConnexions_dropdown_button = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
		self.m_auiToolBar1.SetToolDropDown( self.rpcConnexions_dropdown_button.GetId(), True );
		
		
		self.rpcConnexions_autoswitch = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/iu_update_obj.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar1.AddSeparator()
		
		self.rpcConnexions_newterminal = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/open_terminal_new_tab.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.rpcConnexions_closeterminal = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/close_terminal.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar1.AddSeparator()
		
		self.rpcConnexions_help = self.m_auiToolBar1.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/bookmarks_view.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar1.Realize() 
		
		bSizer1.Add( self.m_auiToolBar1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.wxRavenAdvancedShellPanelNotebook = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		
		bSizer1.Add( self.wxRavenAdvancedShellPanelNotebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.rpcConnexions_dropdown_menu = wx.Menu()
		self.Bind( wx.EVT_RIGHT_DOWN, self.wxRavenAdvancedShellPanelOnContextMenu ) 
		
		
		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnContextMenu_ShowNetworkList, id = self.rpcConnexions_dropdown_button.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnAutoswitchChanged, id = self.rpcConnexions_autoswitch.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnNewTerminal, id = self.rpcConnexions_newterminal.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnCloseTerminal, id = self.rpcConnexions_closeterminal.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnRPCHelp, id = self.rpcConnexions_help.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnContextMenu_ShowNetworkList( self, event ):
		event.Skip()
	
	def OnAutoswitchChanged( self, event ):
		event.Skip()
	
	def OnNewTerminal( self, event ):
		event.Skip()
	
	def OnCloseTerminal( self, event ):
		event.Skip()
	
	def OnRPCHelp( self, event ):
		event.Skip()
	
	def wxRavenAdvancedShellPanelOnContextMenu( self, event ):
		self.PopupMenu( self.rpcConnexions_dropdown_menu, event.GetPosition() )
		

###########################################################################
## Class wxRavenShellDocumentation
###########################################################################

class wxRavenShellDocumentation ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 627,425 ), style = wx.TAB_TRAVERSAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( True )
		bSizer3.Add( self.m_searchCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_customControl2 = wx.Treebook(self, wx.ID_ANY, style= wx.BK_DEFAULT)
		bSizer3.Add( self.m_customControl2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		# Connect Events
		self.m_searchCtrl1.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.OnCancel )
		self.m_searchCtrl1.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnSearch )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT, self.OnSearch )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT_ENTER, self.OnSearch )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCancel( self, event ):
		event.Skip()
	
	def OnSearch( self, event ):
		event.Skip()
	
	
	

###########################################################################
## Class wxRavenShellCommandDescriber
###########################################################################

class wxRavenShellCommandDescriber ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.cmdHelper = wx.TextCtrl( self, wx.ID_ANY, u"sdvsd\n\nsa\n\n\nsa\n\nsa\nsa\nsa\nsa\nsa\nsasa\n\nas", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer4.Add( self.cmdHelper, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenShell_SettingsPanel
###########################################################################

class wxRavenShell_SettingsPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 547,450 ), style = wx.TAB_TRAVERSAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/shell.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Integrate your own classes in the CONSOLE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 11, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer5.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"- addLocalVarInShell(_data, _dataName)\n\tAdd the variable in the shell _locals_\n\n- removeLocalVarInShell( _dataName)\n\tRemove the variable in the shell _locals_\n\n\nExemple :\n\n<data> = <plugin>.getData(<dataname>)\nself.parent_frame.GetPlugin(\"RavenRPC\").addLocalVarInShell(  <data>, <dataname>)", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer6.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
	
	def __del__( self ):
		pass
	

