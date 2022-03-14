'''
Created on 24 janv. 2022

@author: slinux
'''

import wx
from .wxRavenDesign import *
import wx.richtext as rt

class wxRavenDisclaimerDialogLogic(wxRavenDisclaimerDialog):
    '''
    classdocs
    '''


    def __init__(self, parentFrame):
        '''
        Constructor
        '''
        super().__init__(parentFrame)
        self.parent_frame = parentFrame
        
        
        #self.m_CloseButton.SetBitmap(parentFrame.RessourcesProvider.GetImage('blacklist') )
        #self.m_CloseButton.SetBitmapLabel('REFUSE AND CLOSE')
        self.m_CloseButton.SetBitmapLabel(parentFrame.RessourcesProvider.GetImage('blacklist'))
        
        #self.m_OkButton.SetBitmap(parentFrame.RessourcesProvider.GetImage('passed') )
        #self.m_OkButton.SetBitmapLabel('CONTINUE')
        self.m_OkButton.SetBitmapLabel(parentFrame.RessourcesProvider.GetImage('passed') )
        
        ROOT_PATH = parentFrame.Paths['ROOT'] + "/DISCLAIMER.xml"
        print(ROOT_PATH)
        self.AddRTCHandlers()
        self.m_richText1.LoadFile(ROOT_PATH,2)
        
        
    def OnAcceptTerms(self, event):
        _accepted = self.m_mandatoryCheck.GetValue()
        if _accepted:
            self.m_OkButton.Enable(True)
        else:
            self.m_OkButton.Enable(False)
    
    def OnCloseRequest(self, event):
        #self.Close(force=True)
        #wx.GetApp().ExitMainLoop()
        self.EndModal(wx.CANCEL)
        
        
    def OnAccept(self, event):
        #self.Close()
        self.EndModal(wx.OK)
        
        
        
        
        
        
        
        
        
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
        
        
        