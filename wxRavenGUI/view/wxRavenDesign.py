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
## Class wxRavenSplashScreen
###########################################################################

class wxRavenSplashScreen ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 599,396 ), style = wx.DIALOG_NO_PARENT|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/splash-test.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_bitmap1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Loading WxRaven...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		self.m_timer1.Start( 1000 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_TIMER, self.OnTimerTick, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnTimerTick( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenMainFrame
###########################################################################

class wxRavenMainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"wxRaven", pos = wx.DefaultPosition, size = wx.Size( 694,501 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_ALLOW_ACTIVE_PANE|wx.aui.AUI_MGR_ALLOW_FLOATING|wx.aui.AUI_MGR_DEFAULT)
		
		self.wxRavenMenuBar = wx.MenuBar( 0 )
		self.wxRavenMenuBar_File = wx.Menu()
		self.wxRavenMenuBar.Append( self.wxRavenMenuBar_File, u"File" ) 
		
		self.wxRavenMenuBar_Edit = wx.Menu()
		self.wxRavenMenuBar.Append( self.wxRavenMenuBar_Edit, u"Edit" ) 
		
		self.wxRavenMenuBar_Window = wx.Menu()
		self.wxRavenMenuBar_Window_NewWin = wx.MenuItem( self.wxRavenMenuBar_Window, wx.ID_ANY, u"New Window...", wx.EmptyString, wx.ITEM_NORMAL )
		self.wxRavenMenuBar_Window_NewWin.SetBitmap( wx.Bitmap( u"res/default_style/normal/frame_default.png", wx.BITMAP_TYPE_ANY ) )
		self.wxRavenMenuBar_Window.AppendItem( self.wxRavenMenuBar_Window_NewWin )
		self.wxRavenMenuBar_Window_NewWin.Enable( False )
		
		self.wxRavenMenuBar_Window.AppendSeparator()
		
		self.wxRavenMenuBar_Window_NewView = wx.MenuItem( self.wxRavenMenuBar_Window, wx.ID_ANY, u"New View...", wx.EmptyString, wx.ITEM_NORMAL )
		self.wxRavenMenuBar_Window_NewView.SetBitmap( wx.Bitmap( u"res/default_style/normal/new_view.png", wx.BITMAP_TYPE_ANY ) )
		self.wxRavenMenuBar_Window.AppendItem( self.wxRavenMenuBar_Window_NewView )
		
		self.wxRavenMenuBar_Window_Views = wx.Menu()
		self.wxRavenMenuBar_Window.AppendSubMenu( self.wxRavenMenuBar_Window_Views, u"Views" )
		
		self.wxRavenMenuBar_Window_Perspectives = wx.Menu()
		self.wxRavenMenuBar_Window_Perspectives_LoadLast = wx.MenuItem( self.wxRavenMenuBar_Window_Perspectives, wx.ID_ANY, u"Load Last Perspective...", wx.EmptyString, wx.ITEM_NORMAL )
		self.wxRavenMenuBar_Window_Perspectives_LoadLast.SetBitmap( wx.Bitmap( u"res/default_style/normal/last_perspective_2.png", wx.BITMAP_TYPE_ANY ) )
		self.wxRavenMenuBar_Window_Perspectives.AppendItem( self.wxRavenMenuBar_Window_Perspectives_LoadLast )
		
		self.wxRavenMenuBar_Window_Perspectives_DeleteLast = wx.MenuItem( self.wxRavenMenuBar_Window_Perspectives, wx.ID_ANY, u"Delete Last Perspective...", wx.EmptyString, wx.ITEM_NORMAL )
		self.wxRavenMenuBar_Window_Perspectives_DeleteLast.SetBitmap( wx.Bitmap( u"res/default_style/normal/delete_perspective_2.png", wx.BITMAP_TYPE_ANY ) )
		self.wxRavenMenuBar_Window_Perspectives.AppendItem( self.wxRavenMenuBar_Window_Perspectives_DeleteLast )
		
		self.wxRavenMenuBar_Window_Perspectives.AppendSeparator()
		
		self.wxRavenMenuBar_Window_Perspectives_SaveOnClose = wx.MenuItem( self.wxRavenMenuBar_Window_Perspectives, wx.ID_ANY, u"Save On Close", wx.EmptyString, wx.ITEM_CHECK )
		self.wxRavenMenuBar_Window_Perspectives.AppendItem( self.wxRavenMenuBar_Window_Perspectives_SaveOnClose )
		self.wxRavenMenuBar_Window_Perspectives_SaveOnClose.Check( True )
		
		self.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup = wx.MenuItem( self.wxRavenMenuBar_Window_Perspectives, wx.ID_ANY, u"Resume On Startup", wx.EmptyString, wx.ITEM_CHECK )
		self.wxRavenMenuBar_Window_Perspectives.AppendItem( self.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup )
		self.wxRavenMenuBar_Window_Perspectives_LoadLastOnStartup.Check( True )
		
		self.wxRavenMenuBar_Window.AppendSubMenu( self.wxRavenMenuBar_Window_Perspectives, u"Perspectives" )
		
		self.wxRavenMenuBar_Window.AppendSeparator()
		
		self.wxRavenMenuBar_Window_Preferences = wx.MenuItem( self.wxRavenMenuBar_Window, wx.ID_ANY, u"Preferences", wx.EmptyString, wx.ITEM_NORMAL )
		self.wxRavenMenuBar_Window_Preferences.SetBitmap( wx.Bitmap( u"res/default_style/normal/wizard-prefs.png", wx.BITMAP_TYPE_ANY ) )
		self.wxRavenMenuBar_Window.AppendItem( self.wxRavenMenuBar_Window_Preferences )
		
		self.wxRavenMenuBar.Append( self.wxRavenMenuBar_Window, u"Window" ) 
		
		self.wxRavenMenuBar_Help = wx.Menu()
		self.wxRavenMenuBar_Help_WidgetInspector = wx.MenuItem( self.wxRavenMenuBar_Help, wx.ID_ANY, u"Open &Widget Inspector\tF6", wx.EmptyString, wx.ITEM_NORMAL )
		self.wxRavenMenuBar_Help_WidgetInspector.SetBitmap( wx.Bitmap( u"res/default_style/normal/inspect_wx.png", wx.BITMAP_TYPE_ANY ) )
		self.wxRavenMenuBar_Help.AppendItem( self.wxRavenMenuBar_Help_WidgetInspector )
		
		self.wxRavenMenuBar_Help.AppendSeparator()
		
		self.wxRavenMenuBar_Help_About = wx.MenuItem( self.wxRavenMenuBar_Help, wx.ID_ANY, u"About wxRaven IRE", wx.EmptyString, wx.ITEM_NORMAL )
		self.wxRavenMenuBar_Help_About.SetBitmap( wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY ) )
		self.wxRavenMenuBar_Help.AppendItem( self.wxRavenMenuBar_Help_About )
		
		self.wxRavenMenuBar.Append( self.wxRavenMenuBar_Help, u"Help" ) 
		
		self.SetMenuBar( self.wxRavenMenuBar )
		
		self.m_auiToolBar2 = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT|wx.FULL_REPAINT_ON_RESIZE ) 
		self.rpcConnexions_dropdown_button = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
		self.m_auiToolBar2.SetToolDropDown( self.rpcConnexions_dropdown_button.GetId(), True );
		
		
		self.m_auiToolBar2.Realize()
		self.m_mgr.AddPane( self.m_auiToolBar2, wx.aui.AuiPaneInfo().Name( u"wxRavenToolBar" ).Top().CloseButton( False ).PaneBorder( False ).Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Layer( 10 ).ToolbarPane() )
		
		self.rpcConnexions_dropdown_menu = wx.Menu()
		self.Bind( wx.EVT_RIGHT_DOWN, self.wxRavenMainFrameOnContextMenu ) 
		
		self.wxRavenStatusBar = self.CreateStatusBar( 3, 0, wx.ID_ANY )
		self.wxRavenMainBook = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.wxRavenMainBook, wx.aui.AuiPaneInfo() .Name( u"wxRavenMainBook" ).Left() .Caption( u"> wxRaven - App" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).MinSize( wx.Size( 250,-1 ) ).CentrePane() )
		
		
		self.wxRavenToolBook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE|wx.HSCROLL )
		self.m_mgr.AddPane( self.wxRavenToolBook1, wx.aui.AuiPaneInfo() .Name( u"wxRavenToolBook1" ).Left() .Caption( u"Toolbox1" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Hide().Dock().Resizable().FloatingSize( wx.DefaultSize ).MinSize( wx.Size( 200,-1 ) ) )
		
		
		self.wxRavenToolBook2 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.wxRavenToolBook2, wx.aui.AuiPaneInfo() .Name( u"wxRavenToolBook2" ).Right() .Caption( u"Toolbox2" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Hide().Dock().Resizable().FloatingSize( wx.DefaultSize ).MinSize( wx.Size( 200,-1 ) ) )
		
		
		self.wxRavenToolBook3 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.wxRavenToolBook3, wx.aui.AuiPaneInfo() .Name( u"wxRavenToolBook3" ).Bottom() .Caption( u"Toolbox3" ).PinButton( True ).Hide().Dock().Resizable().FloatingSize( wx.DefaultSize ).MinSize( wx.Size( -1,100 ) ) )
		
		
		
		self.m_mgr.Update()
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_MENU, self.OnNewView, id = self.wxRavenMenuBar_Window_NewView.GetId() )
		self.Bind( wx.EVT_MENU, self.OnLoadLastPerspectiveClick, id = self.wxRavenMenuBar_Window_Perspectives_LoadLast.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDeleteLastPerspectiveClick, id = self.wxRavenMenuBar_Window_Perspectives_DeleteLast.GetId() )
		self.Bind( wx.EVT_MENU, self.OnPreferenceDialog, id = self.wxRavenMenuBar_Window_Preferences.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnContextMenu_ShowNetworkList, id = self.rpcConnexions_dropdown_button.GetId() )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnNewView( self, event ):
		event.Skip()
	
	def OnLoadLastPerspectiveClick( self, event ):
		event.Skip()
	
	def OnDeleteLastPerspectiveClick( self, event ):
		event.Skip()
	
	def OnPreferenceDialog( self, event ):
		event.Skip()
	
	def OnContextMenu_ShowNetworkList( self, event ):
		event.Skip()
	
	def wxRavenMainFrameOnContextMenu( self, event ):
		self.PopupMenu( self.rpcConnexions_dropdown_menu, event.GetPosition() )
		

###########################################################################
## Class wxRavenAbout
###########################################################################

class wxRavenAbout ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About wxRaven IRE - Work In Progress", pos = wx.DefaultPosition, size = wx.Size( 622,752 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/splash-test.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer8.Add( self.m_bitmap2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"WxRaven Integrated Raven Environement - Work In Progress version", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer8.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"Version: <VERSION>\nBuild id: <BUILD_ID>\nhttps://github.com/sLiinuX/wxRaven\n--\n\nwxRaven is an open-source IRE (Integrated Raven Environment) Framework for the Ravencoin community.\n\nIt provides usefull built-in functions to create and develop your own \"Use-case specific application\" as one or multiple plugin of this integrated environment itself such as :\n\n    - Built-in RPC connexion\n    - High Level RPC API Commands\n    - RPC Shell & Command list\n    - Highly Customizable End User Interface\n    - ... More to come !\n\t\t\t\t\t\t\t\t\tsLinuX\n\n--\n\nLicence Type : MIT \n(c) Copyright wxRaven contributors and others.  \nNo rights reserved.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\n", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE|wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer8.Add( self.m_textCtrl2, 4, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenAddView
###########################################################################

class wxRavenAddView ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add a new View...", pos = wx.DefaultPosition, size = wx.Size( 371,403 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( True )
		bSizer5.Add( self.m_searchCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_treeCtrl1 = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_HIDE_ROOT )
		bSizer5.Add( self.m_treeCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Open in :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer7.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_choice1Choices = []
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		bSizer7.Add( self.m_choice1, 1, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cancelButton.SetBackgroundColour( wx.Colour( 255, 159, 159 ) )
		
		bSizer6.Add( self.cancelButton, 0, wx.ALL, 5 )
		
		self.openButton = wx.Button( self, wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.openButton.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.openButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.openButton.SetBackgroundColour( wx.Colour( 0, 159, 0 ) )
		
		bSizer6.Add( self.openButton, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( bSizer6, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cancelButton.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.openButton.Bind( wx.EVT_BUTTON, self.OnOpen )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCancel( self, event ):
		event.Skip()
	
	def OnOpen( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenSettingDialog
###########################################################################

class wxRavenSettingDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Preferences", pos = wx.DefaultPosition, size = wx.Size( 712,614 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.settingsSearchCtrl = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.settingsSearchCtrl.ShowSearchButton( True )
		self.settingsSearchCtrl.ShowCancelButton( False )
		bSizer7.Add( self.settingsSearchCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.settingsTreeCtrl = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_HIDE_ROOT )
		bSizer7.Add( self.settingsTreeCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer9.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.settingNameLabel = wx.StaticText( self.m_panel1, wx.ID_ANY, u"MyLabel ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.settingNameLabel.Wrap( -1 )
		self.settingNameLabel.SetFont( wx.Font( 11, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer11.Add( self.settingNameLabel, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_auiToolBar2 = wx.aui.AuiToolBar( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_auiToolBar2.Realize() 
		
		bSizer11.Add( self.m_auiToolBar2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer10.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.settingContentPlaceHolderPannel = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.settingContentPlaceHolderPannel.SetBackgroundColour( wx.Colour( 160, 160, 160 ) )
		
		bSizer10.Add( self.settingContentPlaceHolderPannel, 20, wx.EXPAND |wx.ALL, 0 )
		
		
		self.m_panel1.SetSizer( bSizer10 )
		self.m_panel1.Layout()
		bSizer10.Fit( self.m_panel1 )
		bSizer8.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer8, 3, wx.EXPAND, 5 )
		
		
		bSizer6.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.CancelButton = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CancelButton.SetBackgroundColour( wx.Colour( 255, 159, 159 ) )
		
		bSizer12.Add( self.CancelButton, 0, wx.ALL, 5 )
		
		self.applyCloseButton = wx.Button( self, wx.ID_ANY, u"Apply and Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.applyCloseButton.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.applyCloseButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.applyCloseButton.SetBackgroundColour( wx.Colour( 0, 159, 0 ) )
		
		bSizer12.Add( self.applyCloseButton, 0, wx.ALL, 5 )
		
		
		bSizer6.Add( bSizer12, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.CancelButton.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.applyCloseButton.Bind( wx.EVT_BUTTON, self.OnApplyCloseButton )
		self.applyCloseButton.Bind( wx.EVT_ENTER_WINDOW, self.OnHover )
		self.applyCloseButton.Bind( wx.EVT_LEAVE_WINDOW, self.OnLeaveHover )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCancel( self, event ):
		event.Skip()
	
	def OnApplyCloseButton( self, event ):
		event.Skip()
	
	def OnHover( self, event ):
		event.Skip()
	
	def OnLeaveHover( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenNotAvailablePanel
###########################################################################

class wxRavenNotAvailablePanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 459,382 ), style = wx.TAB_TRAVERSAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/not_available_large.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_bitmap3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()
	
	def __del__( self ):
		pass
	

