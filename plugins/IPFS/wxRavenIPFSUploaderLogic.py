'''
Created on 5 janv. 2022

@author: slinux
'''

from .wxRavenIPFSDesign import wxRavenIPFSFileUploaderDialog
import threading
import time 
import wx 
from wxRavenGUI.application.wxcustom.CustomLoading import *


class wxRavenIPFSFileUploader(wxRavenIPFSFileUploaderDialog):
    '''
    classdocs
    '''


    view_base_name = "IPFS File Uploader"
    view_name = "IPFS File Uploader"
    parent_frame = None
    default_position = "dialog"
    icon = 'ipfs_add'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent, parentFrame, position = "dialog", viewName= "IPFS File Uploader", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "IPFS File Uploader"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        
        self._fileSent = False
        self._waitingAnswer = False
        self._filename = ""
        self._loadingPanel = None
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        #if not isInternalPluginView:
        #    parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
        #
        # Dialog modification
        #
        
    
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.waitApplicationReady()
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.UpdateView,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(1)
            
        wx.CallAfter(callback, ()) 
    
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        
        self.UpdateDataFromPluginDatas()
        self.Layout()
            
            
    
    
    
    def OnSendButton(self, evt):
        
        fts = self.m_filePicker1.GetPath()
        self._filename = fts
        print(f"file to send : {fts}")
     
        _p = self.parent_frame.GetPlugin("IPFS")
        _p.__setHashResult__(fts, -1)
        _p.UploadFileToIPFS_RPC(fts)
     
        self._fileSent = True
        self._waitingAnswer = True
        
        self.m_SendButton.Enable(False)
        
        self.ShowLoading()
        
        
        t=threading.Thread(target=self.__waitHashResultLoop_T__)
        t.start()
    
    
    
    def __waitHashResultLoop_T__(self, evt=None):
        _p = self.parent_frame.GetPlugin("IPFS")
        fts = self.m_filePicker1.GetPath()
        _hashResult = -1
        
        
        
        
        while _hashResult == -1:
            time.sleep(1)
            _hashResult = _p.__getHashResult__(fts)
        
        
        
        wx.CallAfter(self.UpdateDataFromPluginDatas, ())    
        
        
    def ShowLoading(self):
        
        if self._loadingPanel  == None:
            self._loadingPanel =  wxBackgroundWorkerAnimation(self)
        
        self._loadingPanel.Show(show=True)
        self.Layout()
        
    def HideLoading(self):
        if self._loadingPanel  != None:
            self._loadingPanel.Hide()
            self.Layout()
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self, evt=None): 
        self.HideLoading()
              
        if self._filename == "":
            self.m_SendButton.Enable(True)
            return
        print(f"UpdateDataFromPluginDatas IPFS  {self._filename}")
        
        
        try:
            
            print("Hash received !")
            if self._filename != "":
                myPluginData = self.parent_frame.GetPluginData("IPFS","_uploadedFiles")
                if myPluginData.__contains__(self._filename):
                    self.m_hashResult.SetValue(myPluginData[self._filename])
                    self.m_bitmap2.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('passed'))
            
            else:
                self.m_bitmap2.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('error_tsk'))
                 
            #
            #myPluginSetting =  self.parent_frame.GetPluginSetting("Tutorial","booleansetting")#SavePanelSettings GetPluginSetting
            #
            #Update your panel
            #       
            
            pass
            #textToPrint = " booleansetting = " + str(myPluginSetting)
            #textToPrint = textToPrint + "\n\n myPluginData2 = " + str(myPluginData)
             
            #self.m_staticText2.SetLabel(str(textToPrint)) 
             
                
        except Exception as e:
            self.parent_frame.Log("Unable to load ipfs upload datas" , type="warning")
            self.m_bitmap2.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('error_tsk'))
        
        
        self.m_SendButton.Enable(True)            
            