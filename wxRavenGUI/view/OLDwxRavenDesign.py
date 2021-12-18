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
		
		self.wxRavenMenuBar.Append( self.wxRavenMenuBar_Window, u"Window" ) 
		
		self.wxRavenMenuBar_Help = wx.Menu()
		self.wxRavenMenuBar_Help_WidgetInspector = wx.MenuItem( self.wxRavenMenuBar_Help, wx.ID_ANY, u"Open &Widget Inspector\tF6", wx.EmptyString, wx.ITEM_NORMAL )
		self.wxRavenMenuBar_Help_WidgetInspector.SetBitmap( wx.Bitmap( u"res/default_style/normal/inspect_wx.png", wx.BITMAP_TYPE_ANY ) )
		self.wxRavenMenuBar_Help.AppendItem( self.wxRavenMenuBar_Help_WidgetInspector )
		
		self.wxRavenMenuBar.Append( self.wxRavenMenuBar_Help, u"Help" ) 
		
		self.SetMenuBar( self.wxRavenMenuBar )
		
		self.m_auiToolBar2 = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.rpcConnexions_dropdown_button = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )
		self.m_auiToolBar2.SetToolDropDown( self.rpcConnexions_dropdown_button.GetId(), True );
		
		
		self.m_auiToolBar2.Realize()
		self.m_mgr.AddPane( self.m_auiToolBar2, wx.aui.AuiPaneInfo().Name( u"wxRavenToolBar" ).Top().PinButton( True ).Movable( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).Layer( 10 ).ToolbarPane() )
		
		self.rpcConnexions_dropdown_menu = wx.Menu()
		self.Bind( wx.EVT_RIGHT_DOWN, self.wxRavenMainFrameOnContextMenu ) 
		
		self.wxRavenStatusBar = self.CreateStatusBar( 3, 0, wx.ID_ANY )
		self.wxRavenMainBook = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.wxRavenMainBook, wx.aui.AuiPaneInfo() .Name( u"wxRavenMainBook" ).Left() .Caption( u"> wxRaven - App" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).MinSize( wx.Size( 250,-1 ) ).CentrePane() )
		
		
		self.wxRavenToolBook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE|wx.HSCROLL )
		self.m_mgr.AddPane( self.wxRavenToolBook1, wx.aui.AuiPaneInfo() .Name( u"wxRavenToolBook1" ).Left() .Caption( u"Toolbox1" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).MinSize( wx.Size( 200,-1 ) ) )
		
		
		self.wxRavenToolBook2 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.wxRavenToolBook2, wx.aui.AuiPaneInfo() .Name( u"wxRavenToolBook2" ).Right() .Caption( u"Toolbox2" ).MaximizeButton( True ).MinimizeButton( True ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).MinSize( wx.Size( 200,-1 ) ) )
		
		
		self.wxRavenToolBook3 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_mgr.AddPane( self.wxRavenToolBook3, wx.aui.AuiPaneInfo() .Name( u"wxRavenToolBook3" ).Bottom() .Caption( u"Toolbox3" ).PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ).MinSize( wx.Size( -1,100 ) ) )
		
		
		
		self.m_mgr.Update()
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_MENU, self.OnNewView, id = self.wxRavenMenuBar_Window_NewView.GetId() )
		self.Bind( wx.EVT_MENU, self.OnLoadLastPerspectiveClick, id = self.wxRavenMenuBar_Window_Perspectives_LoadLast.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDeleteLastPerspectiveClick, id = self.wxRavenMenuBar_Window_Perspectives_DeleteLast.GetId() )
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
	
	def OnContextMenu_ShowNetworkList( self, event ):
		event.Skip()
	
	def wxRavenMainFrameOnContextMenu( self, event ):
		self.PopupMenu( self.rpcConnexions_dropdown_menu, event.GetPosition() )
		

###########################################################################
## Class wxRavenSplashScreen
###########################################################################

class wxRavenSplashScreen ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 599,372 ), style = wx.DIALOG_NO_PARENT|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
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
## Class wxRavenErrorLogConsolePanel
###########################################################################

class wxRavenErrorLogConsolePanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 697,387 ), style = wx.TAB_TRAVERSAL )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auiToolBar2 = wx.aui.AuiToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_tool2 = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/disconnect_co.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool3 = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/nav_stop.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_auiToolBar2.Realize() 
		
		bSizer2.Add( self.m_auiToolBar2, 0, wx.ALL, 5 )
		
		self.m_dataViewListCtrl1 = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataViewListColumn1 = self.m_dataViewListCtrl1.AppendIconTextColumn( wx.EmptyString )
		self.m_dataViewListColumn2 = self.m_dataViewListCtrl1.AppendTextColumn( u"Message" )
		self.m_dataViewListColumn3 = self.m_dataViewListCtrl1.AppendTextColumn( u"Plugin" )
		self.m_dataViewListColumn4 = self.m_dataViewListCtrl1.AppendTextColumn( u"Date" )
		bSizer2.Add( self.m_dataViewListCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
	
	def __del__( self ):
		pass
	

