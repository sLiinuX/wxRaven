# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wxRavenGUI.application.wxcustom.CustomListCtrl import *
import wx.aui
from wxRavenGUI.application.wxcustom.CustomListCtrl import *
from wxRavenGUI.application.wxcustom import *
import wx.html2 as webview
from wxRavenGUI.application.wxcustom import *

###########################################################################
## Class wxRavenNetInfos
###########################################################################

class wxRavenNetInfos ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 395,157 ), style = wx.TAB_TRAVERSAL )
		
		bSizer116 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer117 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap28 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/connexion_speed_2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer117.Add( self.m_bitmap28, 0, wx.ALL, 5 )
		
		self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"Network Infos :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )
		self.m_staticText57.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer117.Add( self.m_staticText57, 0, wx.ALL, 5 )
		
		
		bSizer116.Add( bSizer117, 0, wx.ALIGN_CENTER, 5 )
		
		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer116.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_infoPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer118 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer119 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap29 = wx.StaticBitmap( self.m_infoPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/mining_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer119.Add( self.m_bitmap29, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText58 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"Current Block :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )
		self.m_staticText58.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer119.Add( self.m_staticText58, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextSPACER = wx.StaticText( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSPACER.Wrap( -1 )
		bSizer119.Add( self.m_staticTextSPACER, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl30 = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer119.Add( self.m_textCtrl30, 1, wx.ALL, 5 )
		
		
		bSizer118.Add( bSizer119, 0, wx.EXPAND, 5 )
		
		bSizer1191 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap291 = wx.StaticBitmap( self.m_infoPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/connexion_speed.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1191.Add( self.m_bitmap291, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText581 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"Network Hashrate :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText581.Wrap( -1 )
		self.m_staticText581.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1191.Add( self.m_staticText581, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextSPACER1 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSPACER1.Wrap( -1 )
		bSizer1191.Add( self.m_staticTextSPACER1, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl301 = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer1191.Add( self.m_textCtrl301, 1, wx.ALL, 5 )
		
		
		bSizer118.Add( bSizer1191, 0, wx.EXPAND, 5 )
		
		bSizer11911 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2911 = wx.StaticBitmap( self.m_infoPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/traffic_light.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11911.Add( self.m_bitmap2911, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText5811 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, u"Network Diff :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5811.Wrap( -1 )
		self.m_staticText5811.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer11911.Add( self.m_staticText5811, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticTextSPACER11 = wx.StaticText( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticTextSPACER11.Wrap( -1 )
		bSizer11911.Add( self.m_staticTextSPACER11, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl3011 = wx.TextCtrl( self.m_infoPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer11911.Add( self.m_textCtrl3011, 1, wx.ALL, 5 )
		
		
		bSizer118.Add( bSizer11911, 0, wx.EXPAND, 5 )
		
		
		self.m_infoPanel.SetSizer( bSizer118 )
		self.m_infoPanel.Layout()
		bSizer118.Fit( self.m_infoPanel )
		bSizer116.Add( self.m_infoPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer116 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRaven_RavencoreTxReader
###########################################################################

class wxRaven_RavencoreTxReader ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1048,761 ), style = wx.TAB_TRAVERSAL )
		
		bSizer126 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_DataPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer152 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer12711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap3411 = wx.StaticBitmap( self.m_DataPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/wallet_in_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12711.Add( self.m_bitmap3411, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText6911 = wx.StaticText( self.m_DataPanel, wx.ID_ANY, u"Tx ID :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6911.Wrap( -1 )
		self.m_staticText6911.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer12711.Add( self.m_staticText6911, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_txIdText = wx.TextCtrl( self.m_DataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12711.Add( self.m_txIdText, 3, wx.ALL, 5 )
		
		
		bSizer152.Add( bSizer12711, 0, wx.EXPAND, 5 )
		
		bSizer127 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap34 = wx.StaticBitmap( self.m_DataPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raw_datas.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer127.Add( self.m_bitmap34, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText69 = wx.StaticText( self.m_DataPanel, wx.ID_ANY, u"Hash :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )
		self.m_staticText69.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer127.Add( self.m_staticText69, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_hashText = wx.TextCtrl( self.m_DataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer127.Add( self.m_hashText, 3, wx.ALL, 5 )
		
		
		bSizer152.Add( bSizer127, 0, wx.EXPAND, 5 )
		
		bSizer165 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1271 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap341 = wx.StaticBitmap( self.m_DataPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/clock_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1271.Add( self.m_bitmap341, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText691 = wx.StaticText( self.m_DataPanel, wx.ID_ANY, u"Timestamp :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText691.Wrap( -1 )
		self.m_staticText691.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1271.Add( self.m_staticText691, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_timestampText = wx.TextCtrl( self.m_DataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer1271.Add( self.m_timestampText, 1, wx.ALL, 5 )
		
		
		bSizer165.Add( bSizer1271, 1, wx.EXPAND, 5 )
		
		bSizer12712 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap3412 = wx.StaticBitmap( self.m_DataPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/cash_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12712.Add( self.m_bitmap3412, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText6912 = wx.StaticText( self.m_DataPanel, wx.ID_ANY, u"Fees :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6912.Wrap( -1 )
		self.m_staticText6912.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer12712.Add( self.m_staticText6912, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_locktimeText = wx.TextCtrl( self.m_DataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer12712.Add( self.m_locktimeText, 1, wx.ALL, 5 )
		
		
		bSizer165.Add( bSizer12712, 0, wx.EXPAND, 5 )
		
		bSizer127121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap34121 = wx.StaticBitmap( self.m_DataPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raw_datas_verified.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer127121.Add( self.m_bitmap34121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText69121 = wx.StaticText( self.m_DataPanel, wx.ID_ANY, u"Confirmations :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69121.Wrap( -1 )
		self.m_staticText69121.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer127121.Add( self.m_staticText69121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_ConfirmationsText = wx.TextCtrl( self.m_DataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer127121.Add( self.m_ConfirmationsText, 1, wx.ALL, 5 )
		
		
		bSizer165.Add( bSizer127121, 0, wx.EXPAND, 5 )
		
		
		bSizer152.Add( bSizer165, 0, wx.EXPAND, 5 )
		
		
		self.m_DataPanel.SetSizer( bSizer152 )
		self.m_DataPanel.Layout()
		bSizer152.Fit( self.m_DataPanel )
		bSizer126.Add( self.m_DataPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline15 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer126.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_paneTools = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer234 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_toggleBtnVIN = wx.ToggleButton( self.m_paneTools, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer234.Add( self.m_toggleBtnVIN, 0, wx.ALL, 5 )
		
		self.m_toggleBtnDetails = wx.ToggleButton( self.m_paneTools, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer234.Add( self.m_toggleBtnDetails, 0, wx.ALL, 5 )
		
		self.m_toggleBtnAssetDetails = wx.ToggleButton( self.m_paneTools, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer234.Add( self.m_toggleBtnAssetDetails, 0, wx.ALL, 5 )
		
		
		self.m_paneTools.SetSizer( bSizer234 )
		self.m_paneTools.Layout()
		bSizer234.Fit( self.m_paneTools )
		bSizer126.Add( self.m_paneTools, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline152 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer126.Add( self.m_staticline152, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer106 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_txDetailsAdvanced = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1701 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1711 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1711.SetMinSize( wx.Size( -1,200 ) ) 
		bSizer1722 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1742 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1732 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap502 = wx.StaticBitmap( self.m_txDetailsAdvanced, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/vin_icon1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1732.Add( self.m_bitmap502, 0, wx.ALL, 5 )
		
		self.m_staticText862 = wx.StaticText( self.m_txDetailsAdvanced, wx.ID_ANY, u"VINs :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText862.Wrap( -1 )
		self.m_staticText862.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1732.Add( self.m_staticText862, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1742.Add( bSizer1732, 0, wx.EXPAND, 5 )
		
		self.m_VINsText = wx.TextCtrl( self.m_txDetailsAdvanced, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer1742.Add( self.m_VINsText, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1722.Add( bSizer1742, 1, wx.EXPAND, 5 )
		
		bSizer17311 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer235 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap5011 = wx.StaticBitmap( self.m_txDetailsAdvanced, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/vout_icon1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer235.Add( self.m_bitmap5011, 0, wx.ALL, 5 )
		
		self.m_staticText8611 = wx.StaticText( self.m_txDetailsAdvanced, wx.ID_ANY, u"VOUTs :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8611.Wrap( -1 )
		self.m_staticText8611.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer235.Add( self.m_staticText8611, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer17311.Add( bSizer235, 0, wx.EXPAND, 5 )
		
		self.m_VOUTsText = wx.TextCtrl( self.m_txDetailsAdvanced, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer17311.Add( self.m_VOUTsText, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1722.Add( bSizer17311, 1, wx.EXPAND, 5 )
		
		
		bSizer1711.Add( bSizer1722, 1, wx.EXPAND, 5 )
		
		
		bSizer1701.Add( bSizer1711, 0, wx.EXPAND, 5 )
		
		
		self.m_txDetailsAdvanced.SetSizer( bSizer1701 )
		self.m_txDetailsAdvanced.Layout()
		bSizer1701.Fit( self.m_txDetailsAdvanced )
		bSizer106.Add( self.m_txDetailsAdvanced, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_txDetailsPanel = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer170 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_sentPanel = wxRavenListCtrlPanel( self.m_txDetailsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer172 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer172.SetMinSize( wx.Size( -1,100 ) ) 
		bSizer173 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap50 = wx.StaticBitmap( self.m_sentPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/wallet_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer173.Add( self.m_bitmap50, 0, wx.ALL, 5 )
		
		self.m_staticText86 = wx.StaticText( self.m_sentPanel, wx.ID_ANY, u"Sent :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )
		self.m_staticText86.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer173.Add( self.m_staticText86, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer172.Add( bSizer173, 0, wx.EXPAND, 5 )
		
		bSizer174 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlInputs = wxRavenListCtrl( self.m_sentPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer174.Add( self.m_listCtrlInputs, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer172.Add( bSizer174, 1, wx.EXPAND, 5 )
		
		
		self.m_sentPanel.SetSizer( bSizer172 )
		self.m_sentPanel.Layout()
		bSizer172.Fit( self.m_sentPanel )
		bSizer170.Add( self.m_sentPanel, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_ReceivedPanel = wxRavenListCtrlPanel( self.m_txDetailsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1721 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1721.SetMinSize( wx.Size( -1,100 ) ) 
		bSizer1731 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap501 = wx.StaticBitmap( self.m_ReceivedPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/wallet_in.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1731.Add( self.m_bitmap501, 0, wx.ALL, 5 )
		
		self.m_staticText861 = wx.StaticText( self.m_ReceivedPanel, wx.ID_ANY, u"Received :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText861.Wrap( -1 )
		self.m_staticText861.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1731.Add( self.m_staticText861, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1721.Add( bSizer1731, 0, wx.EXPAND, 5 )
		
		bSizer1741 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrOutputs = wxRavenListCtrl( self.m_ReceivedPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer1741.Add( self.m_listCtrOutputs, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1721.Add( bSizer1741, 1, wx.EXPAND, 5 )
		
		
		self.m_ReceivedPanel.SetSizer( bSizer1721 )
		self.m_ReceivedPanel.Layout()
		bSizer1721.Fit( self.m_ReceivedPanel )
		bSizer170.Add( self.m_ReceivedPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_txDetailsPanel.SetSizer( bSizer170 )
		self.m_txDetailsPanel.Layout()
		bSizer170.Fit( self.m_txDetailsPanel )
		bSizer106.Add( self.m_txDetailsPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_txDetailsPanel1 = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1702 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_sentPanel1 = wxRavenListCtrlPanel( self.m_txDetailsPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1723 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1723.SetMinSize( wx.Size( -1,100 ) ) 
		bSizer1733 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap503 = wx.StaticBitmap( self.m_sentPanel1, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1733.Add( self.m_bitmap503, 0, wx.ALL, 5 )
		
		self.m_staticText863 = wx.StaticText( self.m_sentPanel1, wx.ID_ANY, u"Asset(s) Sent :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText863.Wrap( -1 )
		self.m_staticText863.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1733.Add( self.m_staticText863, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1723.Add( bSizer1733, 0, wx.EXPAND, 5 )
		
		bSizer1743 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlInputs1 = wxRavenListCtrl( self.m_sentPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer1743.Add( self.m_listCtrlInputs1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1723.Add( bSizer1743, 1, wx.EXPAND, 5 )
		
		
		self.m_sentPanel1.SetSizer( bSizer1723 )
		self.m_sentPanel1.Layout()
		bSizer1723.Fit( self.m_sentPanel1 )
		bSizer1702.Add( self.m_sentPanel1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_ReceivedPanel1 = wxRavenListCtrlPanel( self.m_txDetailsPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17212 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17212.SetMinSize( wx.Size( -1,100 ) ) 
		bSizer17312 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap5012 = wx.StaticBitmap( self.m_ReceivedPanel1, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset_in.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17312.Add( self.m_bitmap5012, 0, wx.ALL, 5 )
		
		self.m_staticText8612 = wx.StaticText( self.m_ReceivedPanel1, wx.ID_ANY, u"Asset(s) Received :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8612.Wrap( -1 )
		self.m_staticText8612.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer17312.Add( self.m_staticText8612, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer17212.Add( bSizer17312, 0, wx.EXPAND, 5 )
		
		bSizer17412 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrOutputs1 = wxRavenListCtrl( self.m_ReceivedPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer17412.Add( self.m_listCtrOutputs1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer17212.Add( bSizer17412, 1, wx.EXPAND, 5 )
		
		
		self.m_ReceivedPanel1.SetSizer( bSizer17212 )
		self.m_ReceivedPanel1.Layout()
		bSizer17212.Fit( self.m_ReceivedPanel1 )
		bSizer1702.Add( self.m_ReceivedPanel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_txDetailsPanel1.SetSizer( bSizer1702 )
		self.m_txDetailsPanel1.Layout()
		bSizer1702.Fit( self.m_txDetailsPanel1 )
		bSizer106.Add( self.m_txDetailsPanel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizer106 )
		self.m_scrolledWindow1.Layout()
		bSizer106.Fit( self.m_scrolledWindow1 )
		bSizer126.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline151 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer126.Add( self.m_staticline151, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_TxHexPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer207 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer199 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17221 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17221.SetMinSize( wx.Size( -1,125 ) ) 
		bSizer17321 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap5021 = wx.StaticBitmap( self.m_TxHexPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raw_datas_verified.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17321.Add( self.m_bitmap5021, 0, wx.ALL, 5 )
		
		self.m_staticText8621 = wx.StaticText( self.m_TxHexPanel, wx.ID_ANY, u"HEX :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8621.Wrap( -1 )
		self.m_staticText8621.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer17321.Add( self.m_staticText8621, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer17221.Add( bSizer17321, 0, wx.EXPAND, 5 )
		
		bSizer17421 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_HEXText = wx.TextCtrl( self.m_TxHexPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer17421.Add( self.m_HEXText, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer17221.Add( bSizer17421, 1, wx.EXPAND, 5 )
		
		
		bSizer199.Add( bSizer17221, 1, wx.EXPAND, 5 )
		
		
		bSizer207.Add( bSizer199, 0, wx.EXPAND, 5 )
		
		
		self.m_TxHexPanel.SetSizer( bSizer207 )
		self.m_TxHexPanel.Layout()
		bSizer207.Fit( self.m_TxHexPanel )
		bSizer126.Add( self.m_TxHexPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_ActionPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer148 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer182 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button5 = wx.Button( self.m_ActionPanel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer182.Add( self.m_button5, 0, wx.ALL, 5 )
		
		
		bSizer148.Add( bSizer182, 1, wx.ALIGN_RIGHT, 5 )
		
		
		self.m_ActionPanel.SetSizer( bSizer148 )
		self.m_ActionPanel.Layout()
		bSizer148.Fit( self.m_ActionPanel )
		bSizer126.Add( self.m_ActionPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer126 )
		self.Layout()
		
		# Connect Events
		self.m_txIdText.Bind( wx.EVT_TEXT, self.OnTxIdChanged )
		self.m_toggleBtnVIN.Bind( wx.EVT_TOGGLEBUTTON, self.OnToggleChanged )
		self.m_toggleBtnDetails.Bind( wx.EVT_TOGGLEBUTTON, self.OnToggleChanged )
		self.m_toggleBtnAssetDetails.Bind( wx.EVT_TOGGLEBUTTON, self.OnToggleChanged )
		self.m_HEXText.Bind( wx.EVT_TEXT, self.OnHexTextChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnTxIdChanged( self, event ):
		event.Skip()
	
	def OnToggleChanged( self, event ):
		event.Skip()
	
	
	
	def OnHexTextChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRaven_Ravencore_TxViewer
###########################################################################

class wxRaven_Ravencore_TxViewer ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1048,761 ), style = wx.TAB_TRAVERSAL )
		
		bSizer126 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_DataPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer152 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer12711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap3411 = wx.StaticBitmap( self.m_DataPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/wallet_in_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12711.Add( self.m_bitmap3411, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText6911 = wx.StaticText( self.m_DataPanel, wx.ID_ANY, u"Tx ID :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6911.Wrap( -1 )
		self.m_staticText6911.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer12711.Add( self.m_staticText6911, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_txIdText = wx.TextCtrl( self.m_DataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12711.Add( self.m_txIdText, 3, wx.ALL, 5 )
		
		
		bSizer152.Add( bSizer12711, 0, wx.EXPAND, 5 )
		
		bSizer127 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap34 = wx.StaticBitmap( self.m_DataPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raw_datas.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer127.Add( self.m_bitmap34, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText69 = wx.StaticText( self.m_DataPanel, wx.ID_ANY, u"Hash :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )
		self.m_staticText69.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer127.Add( self.m_staticText69, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_hashText = wx.TextCtrl( self.m_DataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer127.Add( self.m_hashText, 3, wx.ALL, 5 )
		
		
		bSizer152.Add( bSizer127, 0, wx.EXPAND, 5 )
		
		bSizer165 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1271 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap341 = wx.StaticBitmap( self.m_DataPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/clock_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1271.Add( self.m_bitmap341, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText691 = wx.StaticText( self.m_DataPanel, wx.ID_ANY, u"Timestamp :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText691.Wrap( -1 )
		self.m_staticText691.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1271.Add( self.m_staticText691, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_timestampText = wx.TextCtrl( self.m_DataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer1271.Add( self.m_timestampText, 1, wx.ALL, 5 )
		
		
		bSizer165.Add( bSizer1271, 1, wx.EXPAND, 5 )
		
		bSizer12712 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap3412 = wx.StaticBitmap( self.m_DataPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/cash_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12712.Add( self.m_bitmap3412, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText6912 = wx.StaticText( self.m_DataPanel, wx.ID_ANY, u"Fees :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6912.Wrap( -1 )
		self.m_staticText6912.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer12712.Add( self.m_staticText6912, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_locktimeText = wx.TextCtrl( self.m_DataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer12712.Add( self.m_locktimeText, 1, wx.ALL, 5 )
		
		
		bSizer165.Add( bSizer12712, 0, wx.EXPAND, 5 )
		
		bSizer127121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap34121 = wx.StaticBitmap( self.m_DataPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raw_datas_verified.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer127121.Add( self.m_bitmap34121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText69121 = wx.StaticText( self.m_DataPanel, wx.ID_ANY, u"Confirmations :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69121.Wrap( -1 )
		self.m_staticText69121.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer127121.Add( self.m_staticText69121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_ConfirmationsText = wx.TextCtrl( self.m_DataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer127121.Add( self.m_ConfirmationsText, 1, wx.ALL, 5 )
		
		
		bSizer165.Add( bSizer127121, 0, wx.EXPAND, 5 )
		
		bSizer1271211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap341211 = wx.StaticBitmap( self.m_DataPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/density.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1271211.Add( self.m_bitmap341211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText691211 = wx.StaticText( self.m_DataPanel, wx.ID_ANY, u"Size :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText691211.Wrap( -1 )
		self.m_staticText691211.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1271211.Add( self.m_staticText691211, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_SizeText = wx.TextCtrl( self.m_DataPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer1271211.Add( self.m_SizeText, 1, wx.ALL, 5 )
		
		
		bSizer165.Add( bSizer1271211, 0, wx.EXPAND, 5 )
		
		
		bSizer152.Add( bSizer165, 0, wx.EXPAND, 5 )
		
		
		self.m_DataPanel.SetSizer( bSizer152 )
		self.m_DataPanel.Layout()
		bSizer152.Fit( self.m_DataPanel )
		bSizer126.Add( self.m_DataPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_auinotebook2 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		
		bSizer126.Add( self.m_auinotebook2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer126 )
		self.Layout()
		
		# Connect Events
		self.m_txIdText.Bind( wx.EVT_TEXT, self.OnTxIdChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnTxIdChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRaven_Ravencore_TxViewer_VINOUT_Panel
###########################################################################

class wxRaven_Ravencore_TxViewer_VINOUT_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 677,330 ), style = wx.TAB_TRAVERSAL )
		
		bSizer233 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_txDetailsAdvanced = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1701 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1711 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1711.SetMinSize( wx.Size( -1,200 ) ) 
		bSizer1722 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1742 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1732 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap502 = wx.StaticBitmap( self.m_txDetailsAdvanced, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/vin_icon1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1732.Add( self.m_bitmap502, 0, wx.ALL, 5 )
		
		self.m_staticText862 = wx.StaticText( self.m_txDetailsAdvanced, wx.ID_ANY, u"VINs :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText862.Wrap( -1 )
		self.m_staticText862.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1732.Add( self.m_staticText862, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1742.Add( bSizer1732, 0, wx.EXPAND, 5 )
		
		self.m_VINsText = wx.TextCtrl( self.m_txDetailsAdvanced, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer1742.Add( self.m_VINsText, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1722.Add( bSizer1742, 1, wx.EXPAND, 5 )
		
		bSizer17311 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer235 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap5011 = wx.StaticBitmap( self.m_txDetailsAdvanced, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/vout_icon1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer235.Add( self.m_bitmap5011, 0, wx.ALL, 5 )
		
		self.m_staticText8611 = wx.StaticText( self.m_txDetailsAdvanced, wx.ID_ANY, u"VOUTs :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8611.Wrap( -1 )
		self.m_staticText8611.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer235.Add( self.m_staticText8611, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer17311.Add( bSizer235, 0, wx.EXPAND, 5 )
		
		self.m_VOUTsText = wx.TextCtrl( self.m_txDetailsAdvanced, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer17311.Add( self.m_VOUTsText, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1722.Add( bSizer17311, 1, wx.EXPAND, 5 )
		
		
		bSizer1711.Add( bSizer1722, 1, wx.EXPAND, 5 )
		
		
		bSizer1701.Add( bSizer1711, 1, wx.EXPAND, 5 )
		
		
		self.m_txDetailsAdvanced.SetSizer( bSizer1701 )
		self.m_txDetailsAdvanced.Layout()
		bSizer1701.Fit( self.m_txDetailsAdvanced )
		bSizer233.Add( self.m_txDetailsAdvanced, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer233 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRaven_Ravencore_TxViewer_VINOUT_List_Panel
###########################################################################

class wxRaven_Ravencore_TxViewer_VINOUT_List_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 714,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer248 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_txDetailsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer170 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_sentPanel = wxRavenListCtrlPanel( self.m_txDetailsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer172 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer172.SetMinSize( wx.Size( -1,100 ) ) 
		bSizer173 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap50 = wx.StaticBitmap( self.m_sentPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/vin_icon1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer173.Add( self.m_bitmap50, 0, wx.ALL, 5 )
		
		self.m_staticText86 = wx.StaticText( self.m_sentPanel, wx.ID_ANY, u"VINs :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )
		self.m_staticText86.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer173.Add( self.m_staticText86, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer172.Add( bSizer173, 0, wx.EXPAND, 5 )
		
		bSizer174 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlInputs = wxRavenListCtrl( self.m_sentPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer174.Add( self.m_listCtrlInputs, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer172.Add( bSizer174, 1, wx.EXPAND, 5 )
		
		
		self.m_sentPanel.SetSizer( bSizer172 )
		self.m_sentPanel.Layout()
		bSizer172.Fit( self.m_sentPanel )
		bSizer170.Add( self.m_sentPanel, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_ReceivedPanel = wxRavenListCtrlPanel( self.m_txDetailsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1721 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1721.SetMinSize( wx.Size( -1,100 ) ) 
		bSizer1731 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap501 = wx.StaticBitmap( self.m_ReceivedPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/vout_icon1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1731.Add( self.m_bitmap501, 0, wx.ALL, 5 )
		
		self.m_staticText861 = wx.StaticText( self.m_ReceivedPanel, wx.ID_ANY, u"VOUTs :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText861.Wrap( -1 )
		self.m_staticText861.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1731.Add( self.m_staticText861, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1721.Add( bSizer1731, 0, wx.EXPAND, 5 )
		
		bSizer1741 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrOutputs = wxRavenListCtrl( self.m_ReceivedPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer1741.Add( self.m_listCtrOutputs, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1721.Add( bSizer1741, 1, wx.EXPAND, 5 )
		
		
		self.m_ReceivedPanel.SetSizer( bSizer1721 )
		self.m_ReceivedPanel.Layout()
		bSizer1721.Fit( self.m_ReceivedPanel )
		bSizer170.Add( self.m_ReceivedPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_txDetailsPanel.SetSizer( bSizer170 )
		self.m_txDetailsPanel.Layout()
		bSizer170.Fit( self.m_txDetailsPanel )
		bSizer248.Add( self.m_txDetailsPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer248 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRaven_Ravencore_TxViewer_RVN_Panel
###########################################################################

class wxRaven_Ravencore_TxViewer_RVN_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 730,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer248 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_txDetailsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer170 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_sentPanel = wxRavenListCtrlPanel( self.m_txDetailsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer172 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer172.SetMinSize( wx.Size( -1,100 ) ) 
		bSizer173 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap50 = wx.StaticBitmap( self.m_sentPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/wallet_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer173.Add( self.m_bitmap50, 0, wx.ALL, 5 )
		
		self.m_staticText86 = wx.StaticText( self.m_sentPanel, wx.ID_ANY, u"Sent :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText86.Wrap( -1 )
		self.m_staticText86.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer173.Add( self.m_staticText86, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer172.Add( bSizer173, 0, wx.EXPAND, 5 )
		
		bSizer174 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlInputs = wxRavenListCtrl( self.m_sentPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer174.Add( self.m_listCtrlInputs, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer172.Add( bSizer174, 1, wx.EXPAND, 5 )
		
		
		self.m_sentPanel.SetSizer( bSizer172 )
		self.m_sentPanel.Layout()
		bSizer172.Fit( self.m_sentPanel )
		bSizer170.Add( self.m_sentPanel, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_ReceivedPanel = wxRavenListCtrlPanel( self.m_txDetailsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1721 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1721.SetMinSize( wx.Size( -1,100 ) ) 
		bSizer1731 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap501 = wx.StaticBitmap( self.m_ReceivedPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/wallet_in.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1731.Add( self.m_bitmap501, 0, wx.ALL, 5 )
		
		self.m_staticText861 = wx.StaticText( self.m_ReceivedPanel, wx.ID_ANY, u"Received :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText861.Wrap( -1 )
		self.m_staticText861.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1731.Add( self.m_staticText861, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1721.Add( bSizer1731, 0, wx.EXPAND, 5 )
		
		bSizer1741 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrOutputs = wxRavenListCtrl( self.m_ReceivedPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer1741.Add( self.m_listCtrOutputs, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1721.Add( bSizer1741, 1, wx.EXPAND, 5 )
		
		
		self.m_ReceivedPanel.SetSizer( bSizer1721 )
		self.m_ReceivedPanel.Layout()
		bSizer1721.Fit( self.m_ReceivedPanel )
		bSizer170.Add( self.m_ReceivedPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_txDetailsPanel.SetSizer( bSizer170 )
		self.m_txDetailsPanel.Layout()
		bSizer170.Fit( self.m_txDetailsPanel )
		bSizer248.Add( self.m_txDetailsPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer248 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRaven_Ravencore_TxViewer_Asset_Panel
###########################################################################

class wxRaven_Ravencore_TxViewer_Asset_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 777,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer277 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_txDetailsPanel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1702 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_sentPanel1 = wxRavenListCtrlPanel( self.m_txDetailsPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1723 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1723.SetMinSize( wx.Size( -1,100 ) ) 
		bSizer1733 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap503 = wx.StaticBitmap( self.m_sentPanel1, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1733.Add( self.m_bitmap503, 0, wx.ALL, 5 )
		
		self.m_staticText863 = wx.StaticText( self.m_sentPanel1, wx.ID_ANY, u"Asset(s) Sent :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText863.Wrap( -1 )
		self.m_staticText863.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer1733.Add( self.m_staticText863, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer1723.Add( bSizer1733, 0, wx.EXPAND, 5 )
		
		bSizer1743 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrlInputs1 = wxRavenListCtrl( self.m_sentPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer1743.Add( self.m_listCtrlInputs1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer1723.Add( bSizer1743, 1, wx.EXPAND, 5 )
		
		
		self.m_sentPanel1.SetSizer( bSizer1723 )
		self.m_sentPanel1.Layout()
		bSizer1723.Fit( self.m_sentPanel1 )
		bSizer1702.Add( self.m_sentPanel1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_ReceivedPanel1 = wxRavenListCtrlPanel( self.m_txDetailsPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17212 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17212.SetMinSize( wx.Size( -1,100 ) ) 
		bSizer17312 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap5012 = wx.StaticBitmap( self.m_ReceivedPanel1, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset_in.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17312.Add( self.m_bitmap5012, 0, wx.ALL, 5 )
		
		self.m_staticText8612 = wx.StaticText( self.m_ReceivedPanel1, wx.ID_ANY, u"Asset(s) Received :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8612.Wrap( -1 )
		self.m_staticText8612.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer17312.Add( self.m_staticText8612, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer17212.Add( bSizer17312, 0, wx.EXPAND, 5 )
		
		bSizer17412 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrOutputs1 = wxRavenListCtrl( self.m_ReceivedPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer17412.Add( self.m_listCtrOutputs1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer17212.Add( bSizer17412, 1, wx.EXPAND, 5 )
		
		
		self.m_ReceivedPanel1.SetSizer( bSizer17212 )
		self.m_ReceivedPanel1.Layout()
		bSizer17212.Fit( self.m_ReceivedPanel1 )
		bSizer1702.Add( self.m_ReceivedPanel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_txDetailsPanel1.SetSizer( bSizer1702 )
		self.m_txDetailsPanel1.Layout()
		bSizer1702.Fit( self.m_txDetailsPanel1 )
		bSizer277.Add( self.m_txDetailsPanel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer277 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRaven_Ravencore_TxViewer_HEX_Panel
###########################################################################

class wxRaven_Ravencore_TxViewer_HEX_Panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,197 ), style = wx.TAB_TRAVERSAL )
		
		bSizer305 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_TxHexPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer207 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer199 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17221 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17221.SetMinSize( wx.Size( -1,125 ) ) 
		bSizer17321 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap5021 = wx.StaticBitmap( self.m_TxHexPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raw_datas_verified.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17321.Add( self.m_bitmap5021, 0, wx.ALL, 5 )
		
		self.m_staticText8621 = wx.StaticText( self.m_TxHexPanel, wx.ID_ANY, u"HEX :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8621.Wrap( -1 )
		self.m_staticText8621.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer17321.Add( self.m_staticText8621, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer17221.Add( bSizer17321, 0, wx.EXPAND, 5 )
		
		bSizer17421 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_HEXText = wx.TextCtrl( self.m_TxHexPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer17421.Add( self.m_HEXText, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer17221.Add( bSizer17421, 1, wx.EXPAND, 5 )
		
		
		bSizer199.Add( bSizer17221, 1, wx.EXPAND, 5 )
		
		
		bSizer207.Add( bSizer199, 1, wx.EXPAND, 5 )
		
		
		self.m_TxHexPanel.SetSizer( bSizer207 )
		self.m_TxHexPanel.Layout()
		bSizer207.Fit( self.m_TxHexPanel )
		bSizer305.Add( self.m_TxHexPanel, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer305 )
		self.Layout()
		
		# Connect Events
		self.m_HEXText.Bind( wx.EVT_TEXT, self.OnHexTextChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnHexTextChanged( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRaven_RavencoreUTXOManager
###########################################################################

class wxRaven_RavencoreUTXOManager ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 790,485 ), style = wx.TAB_TRAVERSAL )
		
		bSizer110 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap39 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/wallet.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer111.Add( self.m_bitmap39, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( self, wx.ID_ANY, u"Wallet :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		self.m_staticText48.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer111.Add( self.m_staticText48, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer110.Add( bSizer111, 0, wx.EXPAND, 5 )
		
		bSizer115 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		
		bSizer115.Add( self.m_auinotebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer110.Add( bSizer115, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer110 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRaven_RavencoreUTXOManager_RVN_View
###########################################################################

class wxRaven_RavencoreUTXOManager_RVN_View ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 700,445 ), style = wx.TAB_TRAVERSAL )
		
		bSizer112 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_FilterPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer116 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer117 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap34 = wx.StaticBitmap( self.m_FilterPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/ravencoin.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer117.Add( self.m_bitmap34, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_filterAddressChoices = [ u"RVN", u"ASSETS" ]
		self.m_filterAddress = wx.Choice( self.m_FilterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_filterAddressChoices, 0 )
		self.m_filterAddress.SetSelection( 0 )
		bSizer117.Add( self.m_filterAddress, 3, wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( self.m_FilterPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		bSizer117.Add( self.m_staticText49, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap35 = wx.StaticBitmap( self.m_FilterPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/lock_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer117.Add( self.m_bitmap35, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_showLocked = wx.CheckBox( self.m_FilterPanel, wx.ID_ANY, u"Show Locked", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_showLocked.SetValue(True) 
		bSizer117.Add( self.m_showLocked, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap351 = wx.StaticBitmap( self.m_FilterPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/unlock.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer117.Add( self.m_bitmap351, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_showUnlock = wx.CheckBox( self.m_FilterPanel, wx.ID_ANY, u"Show Unlocked", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_showUnlock.SetValue(True) 
		bSizer117.Add( self.m_showUnlock, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer116.Add( bSizer117, 1, wx.EXPAND, 5 )
		
		bSizer118 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap40 = wx.StaticBitmap( self.m_FilterPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/filter_ps.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer118.Add( self.m_bitmap40, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_addressFilterText = wx.TextCtrl( self.m_FilterPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer118.Add( self.m_addressFilterText, 3, wx.ALL, 5 )
		
		
		bSizer116.Add( bSizer118, 1, wx.EXPAND, 5 )
		
		
		self.m_FilterPanel.SetSizer( bSizer116 )
		self.m_FilterPanel.Layout()
		bSizer116.Fit( self.m_FilterPanel )
		bSizer112.Add( self.m_FilterPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer113 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrl1 = wxRavenListCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer113.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow2.SetSizer( bSizer113 )
		self.m_scrolledWindow2.Layout()
		bSizer113.Fit( self.m_scrolledWindow2 )
		bSizer112.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer112 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRaven_RavencoreUTXOManager_TxHistory_View
###########################################################################

class wxRaven_RavencoreUTXOManager_TxHistory_View ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 756,498 ), style = wx.TAB_TRAVERSAL )
		
		bSizer112 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_FilterPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer116 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer117 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap34 = wx.StaticBitmap( self.m_FilterPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/wallet_in_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer117.Add( self.m_bitmap34, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_filterAddressChoices = [ u"ALL", u"SENT", u"RECEIVED" ]
		self.m_filterAddress = wx.Choice( self.m_FilterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_filterAddressChoices, 0 )
		self.m_filterAddress.SetSelection( 0 )
		bSizer117.Add( self.m_filterAddress, 3, wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( self.m_FilterPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		bSizer117.Add( self.m_staticText49, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap35 = wx.StaticBitmap( self.m_FilterPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/calendar_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer117.Add( self.m_bitmap35, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_startDCheck = wx.CheckBox( self.m_FilterPanel, wx.ID_ANY, u"From :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_startDCheck.SetValue(True) 
		bSizer117.Add( self.m_startDCheck, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_datePicker1 = wxRavenDatePicker( self.m_FilterPanel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer117.Add( self.m_datePicker1, 0, wx.ALL, 5 )
		
		self.m_stopDCheck = wx.CheckBox( self.m_FilterPanel, wx.ID_ANY, u"To :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_stopDCheck.SetValue(True) 
		bSizer117.Add( self.m_stopDCheck, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_datePicker2 = wxRavenDatePicker( self.m_FilterPanel, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer117.Add( self.m_datePicker2, 0, wx.ALL, 5 )
		
		self.m_refreshButton = wx.BitmapButton( self.m_FilterPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer117.Add( self.m_refreshButton, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer116.Add( bSizer117, 1, wx.EXPAND, 5 )
		
		bSizer118 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap40 = wx.StaticBitmap( self.m_FilterPanel, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/filter_ps.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer118.Add( self.m_bitmap40, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_addressFilterText = wx.TextCtrl( self.m_FilterPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer118.Add( self.m_addressFilterText, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer116.Add( bSizer118, 1, wx.EXPAND, 5 )
		
		
		self.m_FilterPanel.SetSizer( bSizer116 )
		self.m_FilterPanel.Layout()
		bSizer116.Fit( self.m_FilterPanel )
		bSizer112.Add( self.m_FilterPanel, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer113 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrl1 = wxRavenListCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer113.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer346 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap112 = wx.StaticBitmap( self.m_scrolledWindow2, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/table_total_in.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer346.Add( self.m_bitmap112, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText119 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Total IN (Period) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText119.Wrap( -1 )
		bSizer346.Add( self.m_staticText119, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textTotalIn = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textTotalIn.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer346.Add( self.m_textTotalIn, 1, wx.ALL, 5 )
		
		self.m_bitmap1121 = wx.StaticBitmap( self.m_scrolledWindow2, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/table_total_out.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer346.Add( self.m_bitmap1121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText1191 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Total OUT (Period) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1191.Wrap( -1 )
		bSizer346.Add( self.m_staticText1191, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textTotalOut = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textTotalOut.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer346.Add( self.m_textTotalOut, 1, wx.ALL, 5 )
		
		self.m_bitmap3412 = wx.StaticBitmap( self.m_scrolledWindow2, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/cash_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer346.Add( self.m_bitmap3412, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText6912 = wx.StaticText( self.m_scrolledWindow2, wx.ID_ANY, u"Fees :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6912.Wrap( -1 )
		self.m_staticText6912.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer346.Add( self.m_staticText6912, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textFee = wx.TextCtrl( self.m_scrolledWindow2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textFee.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer346.Add( self.m_textFee, 1, wx.ALL, 5 )
		
		
		bSizer113.Add( bSizer346, 0, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow2.SetSizer( bSizer113 )
		self.m_scrolledWindow2.Layout()
		bSizer113.Fit( self.m_scrolledWindow2 )
		bSizer112.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer112 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenAssetExplorer
###########################################################################

class wxRavenAssetExplorer ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 672,352 ), style = wx.TAB_TRAVERSAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( False )
		bSizer2.Add( self.m_searchCtrl1, 10, wx.ALL, 5 )
		
		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/filter_ps.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer2.Add( self.m_bpButton1, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
		
		self.searchOptionsPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self.searchOptionsPanel, wx.ID_ANY, u"Max Result :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer3.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.searchopt_maxresults = wx.SpinCtrl( self.searchOptionsPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 110,-1 ), wx.SP_ARROW_KEYS, 1, 500, 50 )
		bSizer3.Add( self.searchopt_maxresults, 0, wx.ALL, 5 )
		
		self.searchopt_onlymain = wx.CheckBox( self.searchOptionsPanel, wx.ID_ANY, u"Filter Asset Type(s)...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.searchopt_onlymain, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.searchopt_strictmode = wx.CheckBox( self.searchOptionsPanel, wx.ID_ANY, u"Name must match exactly (strict search)", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.searchopt_strictmode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer3, 0, 0, 0 )
		
		
		self.searchOptionsPanel.SetSizer( bSizer4 )
		self.searchOptionsPanel.Layout()
		bSizer4.Fit( self.searchOptionsPanel )
		bSizer1.Add( self.searchOptionsPanel, 0, wx.ALL|wx.EXPAND, 2 )
		
		self.m_listCtrl1 = wxRavenListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer1.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.resultControl = wx.InfoBar( self )
		self.resultControl.SetShowHideEffects( wx.SHOW_EFFECT_NONE, wx.SHOW_EFFECT_NONE )
		self.resultControl.SetEffectDuration( 500 )
		bSizer1.Add( self.resultControl, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )
		
		# Connect Events
		self.m_searchCtrl1.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnSearch )
		self.m_searchCtrl1.Bind( wx.EVT_TEXT_ENTER, self.OnSearch )
		self.m_bpButton1.Bind( wx.EVT_BUTTON, self.ToggleFilterPanel )
		self.searchopt_maxresults.Bind( wx.EVT_SPINCTRL, self.SearchOptionsChanged )
		self.searchopt_maxresults.Bind( wx.EVT_TEXT, self.SearchOptionsChanged )
		self.searchopt_onlymain.Bind( wx.EVT_CHECKBOX, self.SearchOptionsChanged )
		self.searchopt_strictmode.Bind( wx.EVT_CHECKBOX, self.SearchOptionsChanged )
		self.Bind( wx.EVT_TIMER, self.OnTimerTick, id=wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSearch( self, event ):
		event.Skip()
	
	
	def ToggleFilterPanel( self, event ):
		event.Skip()
	
	def SearchOptionsChanged( self, event ):
		event.Skip()
	
	
	
	
	def OnTimerTick( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenHTMLViewer
###########################################################################

class wxRavenHTMLViewer ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 587,366 ), style = wx.TAB_TRAVERSAL )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		#self.wv = webview.WebView.New(self)
		self.wv = wxRavenWebview.GetWebView(self)
		bSizer11.Add( self.wv, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer11 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenAssetNavigator
###########################################################################

class wxRavenAssetNavigator ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 966,541 ), style = wx.TAB_TRAVERSAL )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.navigatorToolboxPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auiToolBar2 = wx.aui.AuiToolBar( self.navigatorToolboxPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_saveBookmarkButton = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/save_bkmrk.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Save Bookmark List", wx.EmptyString, None ) 
		
		self.m_auiToolBar2.AddSeparator()
		
		self.m_addBookmarkButton = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/addbkmrk_co.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Add an Asset in Bookmark", wx.EmptyString, None ) 
		
		self.m_removeBookmarkButton = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/rembkmrk_co.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Remove Current Asset From Bookmark", wx.EmptyString, None ) 
		
		self.m_auiToolBar2.AddSeparator()
		
		self.m_useCacheButton = self.m_auiToolBar2.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/fastload.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Use Cache after first load", wx.EmptyString, None ) 
		
		self.m_auiToolBar2.Realize() 
		
		bSizer21.Add( self.m_auiToolBar2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.navigatorToolboxPanel.SetSizer( bSizer21 )
		self.navigatorToolboxPanel.Layout()
		bSizer21.Fit( self.navigatorToolboxPanel )
		bSizer12.Add( self.navigatorToolboxPanel, 0, wx.EXPAND |wx.ALL, 0 )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/bookmarks_view.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_bitmap2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bookmarkChoiceListChoices = []
		self.bookmarkChoiceList = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bookmarkChoiceListChoices, 0 )
		self.bookmarkChoiceList.SetSelection( 0 )
		bSizer20.Add( self.bookmarkChoiceList, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_showBookmarkToolbarButton = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/view_menu.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_AUTODRAW )
		bSizer20.Add( self.m_showBookmarkToolbarButton, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( bSizer20, 0, wx.EXPAND, 5 )
		
		self.assetTreeView = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		bSizer14.Add( self.assetTreeView, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.treeExplorerToolboxPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_auiToolBar4 = wx.aui.AuiToolBar( self.treeExplorerToolboxPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_staticText3 = wx.StaticText( self.m_auiToolBar4, wx.ID_ANY, u"EXPERIMENTAL : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_auiToolBar4.AddControl( self.m_staticText3 )
		self.m_TreeDisplayOption_OrganizeByMainAsset = self.m_auiToolBar4.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/reorg_main.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Reorganize Wallet by Main Asset", wx.EmptyString, None ) 
		
		self.m_auiToolBar4.AddSeparator()
		
		self.m_TreeDisplayOption_ReorganizeSubCat = self.m_auiToolBar4.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/reorg_virtual.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Reorganize Virtual Categories", wx.EmptyString, None ) 
		
		self.m_auiToolBar4.AddSeparator()
		
		self.m_TreeDisplayOption_ResetDisplay = self.m_auiToolBar4.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/synch_toc_nav.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Reset Display Options", wx.EmptyString, None ) 
		
		self.m_auiToolBar4.Realize() 
		
		bSizer22.Add( self.m_auiToolBar4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.treeExplorerToolboxPanel.SetSizer( bSizer22 )
		self.treeExplorerToolboxPanel.Layout()
		bSizer22.Fit( self.treeExplorerToolboxPanel )
		bSizer14.Add( self.treeExplorerToolboxPanel, 0, wx.EXPAND |wx.ALL, 0 )
		
		self.m_searchCtrl4 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl4.ShowSearchButton( True )
		self.m_searchCtrl4.ShowCancelButton( False )
		bSizer14.Add( self.m_searchCtrl4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetFont( wx.Font( 11, 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer19.Add( self.m_staticText2, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_auiToolBar3 = wx.aui.AuiToolBar( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT ) 
		self.m_OpenAssetIpfsButton = self.m_auiToolBar3.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/raven_ipfs.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Open IPFS in Browser", wx.EmptyString, None ) 
		
		self.m_shareAssetButton = self.m_auiToolBar3.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/copy_clipboard.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Copy IPFS URL", wx.EmptyString, None ) 
		
		self.m_auiToolBar3.AddSeparator()
		
		self.m_CreateNewAssetButton = self.m_auiToolBar3.AddTool( wx.ID_ANY, u"tool", wx.Bitmap( u"res/default_style/normal/asset_new.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Create a new asset under this position", wx.EmptyString, None ) 
		
		self.m_auiToolBar3.Realize() 
		
		bSizer19.Add( self.m_auiToolBar3, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_auiToolBar5 = wx.aui.AuiToolBar( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_TB_HORZ_LAYOUT|wx.TRANSPARENT_WINDOW ) 
		self.m_auiToolBar5.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.m_auiToolBar5.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		self.m_auiToolBar5.Realize() 
		
		bSizer19.Add( self.m_auiToolBar5, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer18.Add( bSizer19, 0, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer18.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.AssetDetailsContainerPanel = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18.Add( self.AssetDetailsContainerPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel4.SetSizer( bSizer18 )
		self.m_panel4.Layout()
		bSizer18.Fit( self.m_panel4 )
		bSizer17.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer17, 3, wx.EXPAND, 5 )
		
		
		bSizer12.Add( bSizer13, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer12 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnSaveBookmarkList, id = self.m_saveBookmarkButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnAddBookmarkListItem, id = self.m_addBookmarkButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnRemoveBookmarkListItem, id = self.m_removeBookmarkButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnUseCacheToggle, id = self.m_useCacheButton.GetId() )
		self.m_showBookmarkToolbarButton.Bind( wx.EVT_BUTTON, self.OnToggleBookmarkToolbar )
		self.Bind( wx.EVT_TOOL, self.OnTreeDisplayOptionsChanged, id = self.m_TreeDisplayOption_OrganizeByMainAsset.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnTreeDisplayOptionsChanged, id = self.m_TreeDisplayOption_ReorganizeSubCat.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnResetTreeDisplay, id = self.m_TreeDisplayOption_ResetDisplay.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnOpenCurrentAssetIPFS, id = self.m_OpenAssetIpfsButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnShareCurrentAssetIPFS, id = self.m_shareAssetButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.OnCreateNewAsset, id = self.m_CreateNewAssetButton.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSaveBookmarkList( self, event ):
		event.Skip()
	
	def OnAddBookmarkListItem( self, event ):
		event.Skip()
	
	def OnRemoveBookmarkListItem( self, event ):
		event.Skip()
	
	def OnUseCacheToggle( self, event ):
		event.Skip()
	
	def OnToggleBookmarkToolbar( self, event ):
		event.Skip()
	
	def OnTreeDisplayOptionsChanged( self, event ):
		event.Skip()
	
	
	def OnResetTreeDisplay( self, event ):
		event.Skip()
	
	def OnOpenCurrentAssetIPFS( self, event ):
		event.Skip()
	
	def OnShareCurrentAssetIPFS( self, event ):
		event.Skip()
	
	def OnCreateNewAsset( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenAssetDetails_OverviewPanel
###########################################################################

class wxRavenAssetDetails_OverviewPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 688,477 ), style = wx.TAB_TRAVERSAL )
		
		bSizer76 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer77 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel10 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer78 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer79 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap17 = wx.StaticBitmap( self.m_panel10, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/reflog.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer79.Add( self.m_bitmap17, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Asset Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		self.m_staticText30.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer79.Add( self.m_staticText30, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_assetNameText = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer79.Add( self.m_assetNameText, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer78.Add( bSizer79, 0, wx.EXPAND, 5 )
		
		bSizer791 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap18 = wx.StaticBitmap( self.m_panel10, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raven_ipfs.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer791.Add( self.m_bitmap18, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText301 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"IPFS  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )
		self.m_staticText301.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer791.Add( self.m_staticText301, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_assetIPFStext = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer791.Add( self.m_assetIPFStext, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer78.Add( bSizer791, 0, wx.EXPAND, 5 )
		
		bSizer7911 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap19 = wx.StaticBitmap( self.m_panel10, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset_admin.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7911.Add( self.m_bitmap19, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText3011 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Type  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3011.Wrap( -1 )
		self.m_staticText3011.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer7911.Add( self.m_staticText3011, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_assetTypeText = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer7911.Add( self.m_assetTypeText, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer78.Add( bSizer7911, 0, wx.EXPAND, 5 )
		
		bSizer79111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer90 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap21 = wx.StaticBitmap( self.m_panel10, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/supply_2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer90.Add( self.m_bitmap21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText30111 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Supply  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30111.Wrap( -1 )
		self.m_staticText30111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer90.Add( self.m_staticText30111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_assetSupplyTxt = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer90.Add( self.m_assetSupplyTxt, 1, wx.ALL, 5 )
		
		
		bSizer79111.Add( bSizer90, 1, 0, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap20 = wx.StaticBitmap( self.m_panel10, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/perspective-planning.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer91.Add( self.m_bitmap20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText301111 = wx.StaticText( self.m_panel10, wx.ID_ANY, u"Created  :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301111.Wrap( -1 )
		self.m_staticText301111.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer91.Add( self.m_staticText301111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_assetCreatedTxt = wx.TextCtrl( self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer91.Add( self.m_assetCreatedTxt, 1, wx.ALL, 5 )
		
		
		bSizer79111.Add( bSizer91, 1, 0, 5 )
		
		
		bSizer78.Add( bSizer79111, 0, wx.EXPAND, 5 )
		
		
		self.m_panel10.SetSizer( bSizer78 )
		self.m_panel10.Layout()
		bSizer78.Fit( self.m_panel10 )
		bSizer77.Add( self.m_panel10, 5, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel11 = wx.Panel( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer92 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bpButton27 = wx.BitmapButton( self.m_panel11, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer92.Add( self.m_bpButton27, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel11.SetSizer( bSizer92 )
		self.m_panel11.Layout()
		bSizer92.Fit( self.m_panel11 )
		bSizer77.Add( self.m_panel11, 2, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel8.SetSizer( bSizer77 )
		self.m_panel8.Layout()
		bSizer77.Fit( self.m_panel8 )
		bSizer76.Add( self.m_panel8, 2, wx.EXPAND |wx.ALL, 1 )
		
		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer76.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel9 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer93 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer94 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap13 = wx.StaticBitmap( self.m_panel9, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/group_users.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer94.Add( self.m_bitmap13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"Owner(s) :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		self.m_staticText41.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer94.Add( self.m_staticText41, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		bSizer94.Add( self.m_staticText42, 3, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_ownerCount = wx.TextCtrl( self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT )
		bSizer94.Add( self.m_ownerCount, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_ownerListExport = wx.BitmapButton( self.m_panel9, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/ownerlist_export.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer94.Add( self.m_ownerListExport, 0, wx.ALL, 5 )
		
		
		bSizer93.Add( bSizer94, 0, wx.EXPAND, 5 )
		
		self.listCtrlContainer = wx.Panel( self.m_panel9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer95 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrl1 = wxRavenListCtrl( self.listCtrlContainer, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT|wx.LC_EDIT_LABELS )
		bSizer95.Add( self.m_listCtrl1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.listCtrlContainer.SetSizer( bSizer95 )
		self.listCtrlContainer.Layout()
		bSizer95.Fit( self.listCtrlContainer )
		bSizer93.Add( self.listCtrlContainer, 1, wx.EXPAND |wx.ALL, 1 )
		
		
		self.m_panel9.SetSizer( bSizer93 )
		self.m_panel9.Layout()
		bSizer93.Fit( self.m_panel9 )
		bSizer76.Add( self.m_panel9, 4, wx.EXPAND |wx.ALL, 1 )
		
		
		self.SetSizer( bSizer76 )
		self.Layout()
		
		# Connect Events
		self.m_bpButton27.Bind( wx.EVT_BUTTON, self.OnQrCodeClick )
		self.m_ownerListExport.Bind( wx.EVT_BUTTON, self.OnExportOwnerListClicked )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnQrCodeClick( self, event ):
		event.Skip()
	
	def OnExportOwnerListClicked( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenAssetIssuer
###########################################################################

class wxRavenAssetIssuer ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 503,336 ), style = wx.TAB_TRAVERSAL )
		
		bSizer96 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap23 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/reflog.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer98.Add( self.m_bitmap23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		self.m_staticText44.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer98.Add( self.m_staticText44, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_AssetNameTxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer98.Add( self.m_AssetNameTxt, 5, wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer98, 0, wx.EXPAND, 5 )
		
		bSizer97 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap22 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset_admin.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer97.Add( self.m_bitmap22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, u"Asset Type :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		self.m_staticText43.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer97.Add( self.m_staticText43, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_assetTypeChoiceChoices = []
		self.m_assetTypeChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_assetTypeChoiceChoices, 0 )
		self.m_assetTypeChoice.SetSelection( 0 )
		bSizer97.Add( self.m_assetTypeChoice, 5, wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer97, 0, wx.EXPAND, 5 )
		
		bSizer971 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.mainAssetChoicePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer109 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText431 = wx.StaticText( self.mainAssetChoicePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText431.Wrap( -1 )
		self.m_staticText431.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer109.Add( self.m_staticText431, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_assetMainChoiceChoices = []
		self.m_assetMainChoice = wx.Choice( self.mainAssetChoicePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_assetMainChoiceChoices, 0 )
		self.m_assetMainChoice.SetSelection( 0 )
		bSizer109.Add( self.m_assetMainChoice, 5, wx.ALL, 5 )
		
		
		self.mainAssetChoicePanel.SetSizer( bSizer109 )
		self.mainAssetChoicePanel.Layout()
		bSizer109.Fit( self.mainAssetChoicePanel )
		bSizer971.Add( self.mainAssetChoicePanel, 1, 0, 1 )
		
		
		bSizer96.Add( bSizer971, 0, wx.ALL|wx.EXPAND, 1 )
		
		bSizer981 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap24 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raven_ipfs.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer981.Add( self.m_bitmap24, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText441 = wx.StaticText( self, wx.ID_ANY, u"IPFS :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText441.Wrap( -1 )
		self.m_staticText441.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer981.Add( self.m_staticText441, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_IPFSlinkTxt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer981.Add( self.m_IPFSlinkTxt, 5, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_ipfsUploadButton = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/ipfs_add.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer981.Add( self.m_ipfsUploadButton, 0, wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer981, 0, wx.EXPAND, 5 )
		
		self.m_staticline9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer96.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer99 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkAssetNameLabel = wx.StaticText( self, wx.ID_ANY, u"_", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkAssetNameLabel.Wrap( -1 )
		bSizer99.Add( self.checkAssetNameLabel, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer96.Add( bSizer99, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer991 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.checkAssetNameIcon1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/error_tsk.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer991.Add( self.checkAssetNameIcon1, 0, wx.ALL, 5 )
		
		self.checkErrorLabel = wx.StaticText( self, wx.ID_ANY, u"You must enter a name for the asset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.checkErrorLabel.Wrap( -1 )
		self.checkErrorLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		bSizer991.Add( self.checkErrorLabel, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer96.Add( bSizer991, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer96.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer100 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap26 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/refresh.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer100.Add( self.m_bitmap26, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_reissuableOpt = wx.CheckBox( self, wx.ID_ANY, u"Reissuable", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer100.Add( self.m_reissuableOpt, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_bitmap25 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/supply_2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer100.Add( self.m_bitmap25, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Quantity :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		bSizer100.Add( self.m_staticText49, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_quantityTxt = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer100.Add( self.m_quantityTxt, 0, wx.ALL, 5 )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Units :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		bSizer100.Add( self.m_staticText50, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_unitsOpt = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 8, 0 )
		bSizer100.Add( self.m_unitsOpt, 0, wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer100, 0, wx.EXPAND, 5 )
		
		self.m_staticline101 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer96.Add( self.m_staticline101, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer982 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap27 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/send_from_wallet.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer982.Add( self.m_bitmap27, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText442 = wx.StaticText( self, wx.ID_ANY, u"Destination :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText442.Wrap( -1 )
		self.m_staticText442.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer982.Add( self.m_staticText442, 2, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_Destination = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer982.Add( self.m_Destination, 5, wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer982, 0, wx.EXPAND, 5 )
		
		bSizer104 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_issueButton = wx.Button( self, wx.ID_ANY, u"Issue Asset !", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer104.Add( self.m_issueButton, 0, wx.ALL, 5 )
		
		
		bSizer96.Add( bSizer104, 0, wx.ALIGN_RIGHT, 5 )
		
		
		self.SetSizer( bSizer96 )
		self.Layout()
		
		# Connect Events
		self.m_AssetNameTxt.Bind( wx.EVT_TEXT, self.OnAssetNameChanged )
		self.m_ipfsUploadButton.Bind( wx.EVT_BUTTON, self.OnIpfsButtonClick )
		self.m_reissuableOpt.Bind( wx.EVT_CHECKBOX, self.EvtOptionsChanged )
		self.m_quantityTxt.Bind( wx.EVT_TEXT, self.EvtOptionsChanged )
		self.m_unitsOpt.Bind( wx.EVT_SPINCTRL, self.EvtOptionsChanged )
		self.m_unitsOpt.Bind( wx.EVT_TEXT, self.EvtOptionsChanged )
		self.m_Destination.Bind( wx.EVT_TEXT, self.OnAssetNameChanged )
		self.m_issueButton.Bind( wx.EVT_BUTTON, self.OnIssueAsset )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnAssetNameChanged( self, event ):
		event.Skip()
	
	def OnIpfsButtonClick( self, event ):
		event.Skip()
	
	def EvtOptionsChanged( self, event ):
		event.Skip()
	
	
	
	
	
	def OnIssueAsset( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenAssetIssuerDialog
###########################################################################

class wxRavenAssetIssuerDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 557,437 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	

###########################################################################
## Class wxRavenRavencoreSettingPanel_IPFS
###########################################################################

class wxRavenRavencoreSettingPanel_IPFS ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,374 ), style = wx.TAB_TRAVERSAL )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/raven_ipfs.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_bitmap4, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"IPFS Gateway :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer32.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.ipfs_text_area = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.ipfs_text_area, 0, wx.ALL|wx.EXPAND, 5 )
		
		ipfs_provider_listChoices = []
		self.ipfs_provider_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, ipfs_provider_listChoices, 0 )
		bSizer33.Add( self.ipfs_provider_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer32.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.ipfs_provider_addbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/add_plus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer34.Add( self.ipfs_provider_addbt, 0, wx.ALL, 5 )
		
		self.ipfs_provider_upbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/prev_nav.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer34.Add( self.ipfs_provider_upbt, 0, wx.ALL, 5 )
		
		self.ipfs_provider_rembt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/remove_minus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer34.Add( self.ipfs_provider_rembt, 0, wx.ALL, 5 )
		
		
		bSizer32.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer32.Add( bSizer35, 0, wx.EXPAND, 5 )
		
		
		bSizer26.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer26 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenRavencoreSettingPanel_Bookmarks
###########################################################################

class wxRavenRavencoreSettingPanel_Bookmarks ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 505,374 ), style = wx.TAB_TRAVERSAL )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap4 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/bookmarks_view.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.m_bitmap4, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"My Bookmarks :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer32.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.bookmark_text_area = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.bookmark_text_area, 0, wx.ALL|wx.EXPAND, 5 )
		
		bookmark_listChoices = []
		self.bookmark_list = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, bookmark_listChoices, 0 )
		bSizer33.Add( self.bookmark_list, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer32.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.bookmark_addbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/add_plus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer34.Add( self.bookmark_addbt, 0, wx.ALL, 5 )
		
		self.bookmark_rembt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/remove_minus.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		bSizer34.Add( self.bookmark_rembt, 0, wx.ALL, 5 )
		
		self.ipfs_provider_upbt = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/prev_nav.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.ipfs_provider_upbt.Enable( False )
		
		bSizer34.Add( self.ipfs_provider_upbt, 0, wx.ALL, 5 )
		
		
		bSizer32.Add( bSizer34, 0, wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer32.Add( bSizer35, 0, wx.EXPAND, 5 )
		
		
		bSizer26.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer26 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRavenRavencoreSettingPanel_Search
###########################################################################

class wxRavenRavencoreSettingPanel_Search ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 465,374 ), style = wx.TAB_TRAVERSAL )
		
		bSizer210 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap3 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/inspect_wx.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer211.Add( self.m_bitmap3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Search Options :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer211.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer210.Add( bSizer211, 0, wx.EXPAND, 5 )
		
		bSizer212 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.searchopt_strictmode = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer212.Add( self.searchopt_strictmode, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Strict Search (name must match exactly)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer212.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		bSizer213 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer213.Add( self.m_staticText8, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer212.Add( bSizer213, 0, 0, 5 )
		
		
		bSizer210.Add( bSizer212, 0, wx.EXPAND, 5 )
		
		bSizer214 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Asset Search Limit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer214.Add( self.m_staticText9, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.searchopt_maxresults = wx.TextCtrl( self, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.searchopt_maxresults.SetMaxLength( 0 ) 
		bSizer214.Add( self.searchopt_maxresults, 0, wx.ALL, 5 )
		
		
		bSizer210.Add( bSizer214, 0, wx.EXPAND, 5 )
		
		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer210.Add( self.m_staticline21, 0, wx.EXPAND|wx.ALL, 5 )
		
		bSizer215 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.searchopt_onlymain = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer215.Add( self.searchopt_onlymain, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Filter on Asset Types", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer215.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		
		bSizer210.Add( bSizer215, 0, wx.EXPAND, 5 )
		
		bSizer216 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer216.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Types :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer216.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		bSizer217 = wx.BoxSizer( wx.VERTICAL )
		
		m_assetTypeListChoices = []
		self.m_assetTypeList = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_assetTypeListChoices, 0 )
		bSizer217.Add( self.m_assetTypeList, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer216.Add( bSizer217, 1, wx.EXPAND, 5 )
		
		
		bSizer210.Add( bSizer216, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer210 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DONOTUSE_TestPanel
###########################################################################

class DONOTUSE_TestPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 150,150 ), wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer8.Add( self.m_panel2, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer7.Add( bSizer8, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DONOTUSE_TestPanel2
###########################################################################

class DONOTUSE_TestPanel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		bSizer105 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer105.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer105 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class wxRaven_RavencoreAsset_OwnerListExporter
###########################################################################

class wxRaven_RavencoreAsset_OwnerListExporter ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 499,123 ), style = wx.TAB_TRAVERSAL )
		
		bSizer341 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer342 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap18 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/asset.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer342.Add( self.m_bitmap18, 0, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"1/?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer342.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u": [AssetName]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		bSizer342.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		
		bSizer341.Add( bSizer342, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer343 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 ) 
		bSizer343.Add( self.m_gauge1, 1, wx.ALL, 5 )
		
		
		bSizer341.Add( bSizer343, 0, wx.EXPAND, 5 )
		
		bSizer344 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap19 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"res/default_style/normal/mailbox_1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer344.Add( self.m_bitmap19, 0, wx.ALL, 5 )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"0 Addresses found", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		bSizer344.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		
		bSizer341.Add( bSizer344, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer345 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer345.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		bSizer341.Add( bSizer345, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer341 )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.OnStartFullIndex )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnStartFullIndex( self, event ):
		event.Skip()
	

