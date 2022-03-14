# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.stc
import wx.dataview

###########################################################################
## Class wxRavenShellPanel
###########################################################################

class wxRavenShellPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

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

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnRunPythonScript, id = self.m_runPython.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnRunPythonScript( self, event ):
		event.Skip()


###########################################################################
## Class wxRavenAdvancedShellPanel
###########################################################################

class wxRavenAdvancedShellPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

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


	# Virtual event handlers, override them in your derived class
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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 627,425 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

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


	# Virtual event handlers, override them in your derived class
	def OnCancel( self, event ):
		event.Skip()

	def OnSearch( self, event ):
		event.Skip()




###########################################################################
## Class wxRavenShellCommandDescriber
###########################################################################

class wxRavenShellCommandDescriber ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 547,450 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/shell.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Integrate your own classes in the CONSOLE :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer5.Add( self.m_staticText1, 0, wx.ALL, 5 )


		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"- addLocalVarInShell(_data, _dataName)\n\tAdd the variable in the shell _locals_\n\n- removeLocalVarInShell( _dataName)\n\tRemove the variable in the shell _locals_\n\n\nExemple :\n\n<data> = <plugin>.getData(<dataname>)\nself.parent_frame.addLocalVarInShell(  <data>, <dataname>)", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer6.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND, 5 )


		bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxRaven_General_CodeEditor
###########################################################################

class wxRaven_General_CodeEditor ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 673,441 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_CodeEditorToolBar = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT )
		self.m_CodeEditorToolBar_New = self.m_CodeEditorToolBar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/code_create_python_module.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_CodeEditorToolBar_Open = self.m_CodeEditorToolBar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/packagefolder_obj.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_CodeEditorToolBar_Save = self.m_CodeEditorToolBar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/save_edit.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_CodeEditorToolBar.AddSeparator()

		self.m_staticText2 = wx.StaticText( self.m_CodeEditorToolBar, wx.ID_ANY, u"Quick Fix :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_CodeEditorToolBar.AddControl( self.m_staticText2 )
		self.m_CodeEditorToolBar_Fetch = self.m_CodeEditorToolBar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/pull.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_CodeEditorToolBar_Pull = self.m_CodeEditorToolBar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/push.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_CodeEditorToolBar.AddSeparator()

		self.m_CodeEditorToolBar.Realize()

		bSizer11.Add( self.m_CodeEditorToolBar, 1, wx.ALL, 0 )


		bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_CodeEditorTab = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )

		bSizer12.Add( self.m_CodeEditorTab, 1, wx.EXPAND|wx.ALL, 0 )


		bSizer10.Add( bSizer12, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnNewPageClicked, id = self.m_CodeEditorToolBar_New.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnOpenPageClicked, id = self.m_CodeEditorToolBar_Open.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnSavePageClicked, id = self.m_CodeEditorToolBar_Save.GetId() )
		self.m_CodeEditorTab.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnPageChanged )
		self.m_CodeEditorTab.Bind( wx.aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self.OnPageClose )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnNewPageClicked( self, event ):
		event.Skip()

	def OnOpenPageClicked( self, event ):
		event.Skip()

	def OnSavePageClicked( self, event ):
		event.Skip()

	def OnPageChanged( self, event ):
		event.Skip()

	def OnPageClose( self, event ):
		event.Skip()


###########################################################################
## Class wxRaven_General_CodePage
###########################################################################

class wxRaven_General_CodePage ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 673,441 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_codeEditorText = wx.stc.StyledTextCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_codeEditorText.SetUseTabs ( False )
		self.m_codeEditorText.SetTabWidth ( 4 )
		self.m_codeEditorText.SetIndent ( 4 )
		self.m_codeEditorText.SetTabIndents( False )
		self.m_codeEditorText.SetBackSpaceUnIndents( False )
		self.m_codeEditorText.SetViewEOL( False )
		self.m_codeEditorText.SetViewWhiteSpace( False )
		self.m_codeEditorText.SetMarginWidth( 2, 0 )
		self.m_codeEditorText.SetIndentationGuides( False )
		self.m_codeEditorText.SetReadOnly( False );
		self.m_codeEditorText.SetMarginWidth( 1, 0 )
		self.m_codeEditorText.SetMarginWidth ( 0, 0 )
		self.m_codeEditorText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDER, wx.stc.STC_MARK_BOXPLUS )
		self.m_codeEditorText.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDER, wx.BLACK)
		self.m_codeEditorText.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDER, wx.WHITE)
		self.m_codeEditorText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.stc.STC_MARK_BOXMINUS )
		self.m_codeEditorText.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.BLACK )
		self.m_codeEditorText.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPEN, wx.WHITE )
		self.m_codeEditorText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERSUB, wx.stc.STC_MARK_EMPTY )
		self.m_codeEditorText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEREND, wx.stc.STC_MARK_BOXPLUS )
		self.m_codeEditorText.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEREND, wx.BLACK )
		self.m_codeEditorText.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEREND, wx.WHITE )
		self.m_codeEditorText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.stc.STC_MARK_BOXMINUS )
		self.m_codeEditorText.MarkerSetBackground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.BLACK)
		self.m_codeEditorText.MarkerSetForeground( wx.stc.STC_MARKNUM_FOLDEROPENMID, wx.WHITE)
		self.m_codeEditorText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERMIDTAIL, wx.stc.STC_MARK_EMPTY )
		self.m_codeEditorText.MarkerDefine( wx.stc.STC_MARKNUM_FOLDERTAIL, wx.stc.STC_MARK_EMPTY )
		self.m_codeEditorText.SetSelBackground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT ) )
		self.m_codeEditorText.SetSelForeground( True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		bSizer14.Add( self.m_codeEditorText, 1, wx.EXPAND |wx.ALL, 0 )


		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxRaven_General_CodeBrowser
###########################################################################

class wxRaven_General_CodeBrowser ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 341,408 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.wxRaven_General_CodeBrowser_Toolbar = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT )
		self.wxRaven_General_CodeBrowser_Toolbar_expand = self.wxRaven_General_CodeBrowser_Toolbar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/expandall.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.wxRaven_General_CodeBrowser_Toolbar.AddSeparator()

		self.wxRaven_General_CodeBrowser_Toolbar_Parent = self.wxRaven_General_CodeBrowser_Toolbar.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/code_goto_up.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.wxRaven_General_CodeBrowser_Toolbar.Realize()

		bSizer16.Add( self.wxRaven_General_CodeBrowser_Toolbar, 0, wx.ALL, 0 )


		bSizer15.Add( bSizer16, 0, wx.EXPAND, 5 )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.m_pythonSourceCodeExplorer = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.DIRCTRL_SHOW_FILTERS|wx.SUNKEN_BORDER, u"Python source (*.py)|*.py|JSON files (*.json)|*.json|All files (*.*)|*.*", 0 )

		self.m_pythonSourceCodeExplorer.ShowHidden( False )
		bSizer17.Add( self.m_pythonSourceCodeExplorer, 1, wx.EXPAND |wx.ALL, 0 )


		bSizer15.Add( bSizer17, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer15 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxRaven_General_JSONViewer
###########################################################################

class wxRaven_General_JSONViewer ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,391 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/json_file_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer22.Add( self.m_bitmap2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Select a Source :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer22.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_choice1Choices = [ u"URL", u"File", u"Jobs", u"RAW" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 2 )
		bSizer22.Add( self.m_choice1, 1, wx.ALL, 5 )


		bSizer18.Add( bSizer22, 0, wx.EXPAND, 5 )

		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_optionpanel_url = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl3 = wx.TextCtrl( self.m_optionpanel_url, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer21.Add( self.m_textCtrl3, 4, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_Proceed = wx.Button( self.m_optionpanel_url, wx.ID_ANY, u"Load URL", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_Proceed.SetBitmap( wx.Bitmap( u"res/default_style/normal/raven_ipfs.png", wx.BITMAP_TYPE_ANY ) )
		bSizer21.Add( self.m_Proceed, 1, wx.ALL, 5 )


		self.m_optionpanel_url.SetSizer( bSizer21 )
		self.m_optionpanel_url.Layout()
		bSizer21.Fit( self.m_optionpanel_url )
		bSizer19.Add( self.m_optionpanel_url, 1, wx.EXPAND |wx.ALL, 1 )


		bSizer18.Add( bSizer19, 0, wx.EXPAND, 5 )

		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_optionpanel_file = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_filePicker1 = wx.FilePickerCtrl( self.m_optionpanel_file, wx.ID_ANY, wx.EmptyString, u"Select a file", u"JSON File (*.json)|*.json|All files (*.*)|*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		bSizer211.Add( self.m_filePicker1, 1, wx.ALL, 5 )


		self.m_optionpanel_file.SetSizer( bSizer211 )
		self.m_optionpanel_file.Layout()
		bSizer211.Fit( self.m_optionpanel_file )
		bSizer191.Add( self.m_optionpanel_file, 1, wx.EXPAND |wx.ALL, 1 )


		bSizer18.Add( bSizer191, 0, wx.EXPAND, 5 )

		bSizer1911 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_optionpanel_jobs = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2111 = wx.BoxSizer( wx.HORIZONTAL )

		m_choice_jobChoices = []
		self.m_choice_job = wx.Choice( self.m_optionpanel_jobs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_jobChoices, 0 )
		self.m_choice_job.SetSelection( 0 )
		bSizer2111.Add( self.m_choice_job, 1, wx.ALL, 5 )

		self.m_bpButtonRefreshJobs = wx.BitmapButton( self.m_optionpanel_jobs, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButtonRefreshJobs.SetBitmap( wx.Bitmap( u"res/default_style/normal/refresh.png", wx.BITMAP_TYPE_ANY ) )
		bSizer2111.Add( self.m_bpButtonRefreshJobs, 0, wx.ALL, 5 )


		self.m_optionpanel_jobs.SetSizer( bSizer2111 )
		self.m_optionpanel_jobs.Layout()
		bSizer2111.Fit( self.m_optionpanel_jobs )
		bSizer1911.Add( self.m_optionpanel_jobs, 1, wx.EXPAND |wx.ALL, 1 )


		bSizer18.Add( bSizer1911, 0, wx.EXPAND, 5 )

		bSizer19111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_optionpanel_raw = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21111 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_textCtrl6 = wx.TextCtrl( self.m_optionpanel_raw, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer21111.Add( self.m_textCtrl6, 1, wx.ALL, 5 )

		self.m_bpButtonPaste = wx.BitmapButton( self.m_optionpanel_raw, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButtonPaste.SetBitmap( wx.Bitmap( u"res/default_style/normal/paste_edit.png", wx.BITMAP_TYPE_ANY ) )
		bSizer21111.Add( self.m_bpButtonPaste, 0, wx.ALL, 5 )


		self.m_optionpanel_raw.SetSizer( bSizer21111 )
		self.m_optionpanel_raw.Layout()
		bSizer21111.Fit( self.m_optionpanel_raw )
		bSizer19111.Add( self.m_optionpanel_raw, 1, wx.EXPAND |wx.ALL, 1 )


		bSizer18.Add( bSizer19111, 0, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_treeListCtrl1 = wx.dataview.TreeListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.m_treeListCtrl1.AppendColumn( u"StructureColumn", wx.COL_WIDTH_AUTOSIZE, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		self.m_treeListCtrl1.AppendColumn( u"TypeColumn", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		self.m_treeListCtrl1.AppendColumn( u"SizeColumn", wx.COL_WIDTH_AUTOSIZE, wx.ALIGN_RIGHT, wx.COL_RESIZABLE )

		bSizer20.Add( self.m_treeListCtrl1, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer18.Add( bSizer20, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer18 )
		self.Layout()

		# Connect Events
		self.m_choice1.Bind( wx.EVT_CHOICE, self.OnInputSourceChanged )
		self.m_Proceed.Bind( wx.EVT_BUTTON, self.OnLoadURLClicked )
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChanged )
		self.m_choice_job.Bind( wx.EVT_CHOICE, self.OnJobSelected )
		self.m_bpButtonRefreshJobs.Bind( wx.EVT_BUTTON, self.OnRefreshJobList )
		self.m_textCtrl6.Bind( wx.EVT_TEXT, self.OnRawTextChanged )
		self.m_bpButtonPaste.Bind( wx.EVT_BUTTON, self.OnPasteRawClicked )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def OnInputSourceChanged( self, event ):
		event.Skip()

	def OnLoadURLClicked( self, event ):
		event.Skip()

	def OnFileChanged( self, event ):
		event.Skip()

	def OnJobSelected( self, event ):
		event.Skip()

	def OnRefreshJobList( self, event ):
		event.Skip()

	def OnRawTextChanged( self, event ):
		event.Skip()

	def OnPasteRawClicked( self, event ):
		event.Skip()


