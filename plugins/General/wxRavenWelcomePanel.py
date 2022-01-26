'''
Created on 28 déc. 2021

@author: slinux
'''

from .wxRavenGeneralDesign import wxRavenWelcomeTab

import wx
import wx.richtext as rt

import wx.lib.buttons as buts
import os

import wx.lib.scrolledpanel



class wxRavenWelcomeTabLogic(wxRavenWelcomeTab):
    '''
    classdocs
    '''


    view_base_name = "Welcome"
    view_name = "Welcome"
    parent_frame = None
    default_position = "main"
    
    
    #icon = wx.Bitmap( u"res/default_style/normal/tab_view.png", wx.BITMAP_TYPE_ANY )
    icon = 'welcome16'
    
    
    allIcons = {}
    
    

    def __init__(self, parentFrame, position = "main", viewName= "Welcome"):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        self.view_base_name = "Welcome"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.PhotoMaxSize = 300
        self.PhotoMinSize = 150
        
        self.AddRTCHandlers()
        
    
        #self.SetBackgroundColour(parentFrame.RessourcesProvider.GetPanelBackground())
        #parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        
        
        #ROOT_PATH = os.getcwd() + "/CHANGES.xml"
        ROOT_PATH = parentFrame.Paths['ROOT'] + "/CHANGES.xml"
        print(ROOT_PATH)
        self.m_richText1.LoadFile(ROOT_PATH,2)
        #
        """
        pause_button = buts.GenBitmapTextButton(self, -1, bitmap=self.parent_frame.RessourcesProvider.GetImage("search_45"), label= "Search")
        
        
        time_button.SetBitmap(wx.Bitmap("toggle1.png"),wx.RIGHT)
        """
        #print("here")
        
        #self.m_button3.SetBitmap(self.parent_frame.RessourcesProvider.GetImage("search_45"),wx.LEFT)
        #self.m_button3.Refresh(eraseBackground=True, rect=None)
        
        
        
        #self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        #self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        #
       
        #self.UpdateUIButtons(None)
        #self.Bind(wx.EVT_SIZE, self.UpdateUIButtons)

        #self.Bind( wx.EVT_UPDATE_UI, self.UpdateUIButtons )
        #self.Bind(wx.EVT_SIZE, self.UpdateUIButtons) 
        
        self.manageScrollers()
        
        self.SetAutoLayout(True)
        
        parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
    
    
    
    
    
    
    
    
    def manageScrollers(self):
        #panel2 = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(screenWidth,400), pos=(0,28), style=wx.SIMPLE_BORDER)
        #panel2.SetupScrolling()
        #self.m_panel9.SetupScrolling()
        pass
    
    
    
    
    
    def AddRTCHandlers(self):
        # make sure we haven't already added them.
        if rt.RichTextBuffer.FindHandlerByType(rt.RICHTEXT_TYPE_HTML) is not None:
            return

        # This would normally go in your app's OnInit method.  I'm
        # not sure why these file handlers are not loaded by
        # default by the C++ richtext code, I guess it's so you
        # can change the name or extension if you wanted...
        rt.RichTextBuffer.AddHandler(rt.RichTextHTMLHandler())
        rt.RichTextBuffer.AddHandler(rt.RichTextXMLHandler())

        # ...like this
        rt.RichTextBuffer.AddHandler(rt.RichTextXMLHandler(name="Other XML",
                                                           ext="ox",
                                                           type=99))

        # This is needed for the view as HTML option since we tell it
        # to store the images in the memory file system.
        wx.FileSystem.AddHandler(wx.MemoryFSHandler())
    
    
    
    def OnSearch(self, evt):
        self.parent_frame.Views.OpenView("Asset Search", pluginname='', createIfNull=True)
    
    
    
    
    def OnNavigate(self, evt):
        self.parent_frame.Views.OpenView("Asset Navigator", pluginname='', createIfNull=True)
    
    
    
    
    def OnWallet(self, evt):
        self.parent_frame.Views.OpenView("Simple Wallet", pluginname='', createIfNull=True)
    
    
    
    def OnIssueAsset(self, evt):
        self.parent_frame.Views.OpenView("Asset Issuer", pluginname='', createIfNull=True)
    
    
    
    
    
    
    
    
    
    
    
    
    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        print("repaint")
        # yanked from ColourDB.py
        dc = evt.GetDC()
                
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = self.parent_frame.RessourcesProvider.GetImage("banner")#wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        dc.DrawBitmap(bmp, 0, 0) 
        self.SetAutoLayout(True)   
        
   
   
    
    def AddPage(self,obj, title, icon):
        pass
    
    def OnPageClose( self, event ):
        pass
  
        
    def UpdateView(self):
        pass
    
    
    
    
    def UpdateUIButtons(self, evt):
        bt_list = [self.m_bpButton9 , self.m_bpButton91, self.m_bpButton92]
        
        for bt in bt_list:
            self.AdjustButton(bt)
            #bt.SetBitmapLabel("TEST")
    
    
    
    def AdjustButton(self, bt):
        btImg = bt.GetBitmap().ConvertToImage()
        
        SizeX, SizeY = bt.GetSize()
        
        
        W = btImg.GetWidth()
        H = btImg.GetHeight()
        
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
            
            
            
        img = btImg.Scale(NewW,NewH)
        bt.SetBitmap(wx.BitmapFromImage(img))
        self.Layout()
        print("Adjsuted")
        
        
        """
        self.RatioX = 1.0 * SizeX / btImg.GetWidth()
        self.RatioY = 1.0 * SizeY / btImg.GetHeight()
        
        print(SizeX)
        print(SizeY)
        
        print(self.RatioX)
        print(self.RatioY)
        
        if SizeX<50:
            SizeX = 50
        if SizeY<50:
            SizeY = 50
        
        """
        
        

        
        
        
        
        
        
        
        
    
    def onView(self):
        #filepath = self.photoTxt.GetValue()
        #img = self.parent_frame.RessourcesProvider.GetImage("banner")#wx.Image(filepath, wx.BITMAP_TYPE_ANY)
        img = wx.Image( u"res/default_style/normal/banner.png", wx.BITMAP_TYPE_ANY )
        # scale the image, preserving the aspect ratio
        
        SizeX, SizeY = self.imagePanel.GetSize()
        self.RatioX = 1.0 * SizeX / img.GetWidth()
        self.RatioY = 1.0 * SizeY / img.GetHeight()
        
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
           
        print(f"SCALE = W{SizeX}   H{SizeY}") 
        print(f"SCALE = W{self.RatioX}   H{self.RatioY}")   
        #img = img.Scale(NewW,NewH)
        img = img.Scale(SizeX,SizeY)
        #SizeX
        self.m_bitmap2.SetBitmap(wx.BitmapFromImage(img))
        self.Refresh()
        
        
        
        