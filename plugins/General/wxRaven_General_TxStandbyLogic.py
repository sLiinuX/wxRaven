'''
Created on 9 mars 2022

@author: slinux
'''

'''
Created on 8 mars 2022

@author: slinux
'''
import threading
import time 

import wx 
import sys

import uuid  
from .wxRavenGeneralDesign import wxRaven_General_TxStandbyFrame


import qrcode
from PIL import Image
from libs import PILutils



class wxRaven_General_TxStandby_Logic(wxRaven_General_TxStandbyFrame):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Transaction Standby Dialog"
    view_name = "Transaction Standby Dialog"
    parent_frame = None
    default_position = "dialog"
    icon = 'credit_card'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent, parentFrame, position = "dialog", viewName= "Transaction Standby Dialog", isInternalPluginView=True):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        #print(parent)
        #print(parentFrame)
        
        
        self.view_base_name = "Transaction Standby Dialog"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parent
        self._dataCache= {}
        
        self._JobId = None
        self._isRemote = False
        #wx.LogTextCtrl(self.m_debugLog)
        
        #self._oldOut = sys.stdout
        #self._oldErr = sys.stderr
        
        
        #if parentFrame.GetPluginSetting("General",'debug_out') == 'stderr':
        #    sys.stderr=self.m_debugLog
        #else:
        #sys.stdout=self.m_debugLog
        
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
    
            
    
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.waitApplicationReady()
        self.Layout()
        self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
        
        self.parent.ResizeDialog()
        
        
        
        
    '''
    def OnClose(self, evt=None):
        pass
        #print("Onlose!")
        #sys.stdout=self._oldOut
        #sys.stderr=self._oldErr
    
    '''
    
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.DoNothing,), daemon=True)
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
    
    
    
    
    def DoNothing(self,evt=None):
        pass
    
    def __loadListOfConnexion__(self, evt=None):
        self._dataCache={}
        allCons = self.parent_frame.ConnexionManager.getAllConnexions()
        
        
        self.m_choiceConnexion.Clear()
        
        
        for _key in allCons:
            
            
            if self.parent_frame.ConnexionManager.getConnexionType(_key) == "WS-RPC":
            
                #_scheme = self.parent_frame.ConnexionManager.getConnexionScheme(_key)
                
                #self.m_choiceConnexion.Append(_scheme['title'])
                self.m_choiceConnexion.Append(_key)
                self._dataCache[_key] = allCons[_key]
                #self._dataCache[_scheme['title']] = _scheme
            
            
            
        
        
        
        _dc = self.m_choiceConnexion.FindString(self.parent_frame.ConnexionManager.getCurrent())
        if _dc != wx.NOT_FOUND:
            self.m_choiceConnexion.SetSelection(_dc)
        
        
        self.UpdateView()
    
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        print("update view !!!")
        self.UpdateDataFromPluginDatas()
        self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
        self.parent.ResizeDialog()
        self.Layout()
            
    
    
    def __SetDatas__(self,datas=None):
        print(f"__SetDatas__ data not none {datas}")
        if datas!=None:
            #print("__SetDatas__ data not none")
            self._datas = datas
            #self.UpdateView()
            
            wx.CallAfter(self.UpdateView)
    
    def SetRemoteJobId(self, jobId):
        self._JobId = jobId
        self._isRemote = True
    
    
    def OnSelectedConnexionChanged(self,evt):
        self.UpdateView()
        self.Layout()
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):   
        #print(self._datas)    
        if self._datas != None:
            
            self.m_staticTextTitle.SetLabel(str(self._datas['_jobTxStandbyDescription']))
            self.parent.SetTitle(str(self._datas['_jobTxStandbyDescription']))   
            
            
            if self._datas['_jobPaymentAmount'] != None:
                self.m_staticTextAmount.SetLabel(str(self._datas['_jobPaymentAmount']))
                
            else:
                self.m_staticTextAmount.SetLabel(str(self._datas['_jobPaymentAmount']))
                #imgbmp = self.GenerateQRcodeBitmap(self._datas['_jobPaymentAmount']) 
                
                
             
                
            
    
            
            if self._datas['_jobPaymentStandby'] != None:
                self.m_txTargetAddress.SetValue(str(self._datas['_jobPaymentStandby']))
                imgbmp = self.GenerateQRcodeBitmap(self._datas['_jobPaymentStandby']) 
                self.m_bpButton12.SetBitmap(imgbmp)
                
            else:
                self.m_bpButton12.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('qrcode_not_available'))
                #self.m_staticTextAmount.SetLabel(str('??? RVN'))   
                
            
            if self._datas['_jobPaymentStatus'] != None:
                self.m_staticTextStatus.SetLabel(str(self._datas['_jobPaymentStatus']))
                
                
                if str(self._datas['_jobPaymentStatus']).__contains__('Waiting'):
                    self.m_bitmap45.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('clock_2'))
                
                if str(self._datas['_jobPaymentStatus']).__contains__('Complete'):    
                    self.m_bitmap45.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('passed'))
                    
                    _txConfirm = self._datas['_jobTxStandbyDescription']
                    
                    if self._datas['_jobTxStandby'] != None:
                        
                        self.m_staticTextTitle.SetLabel('TXID :')
                        #wxraven_icon_small
                    newimg = self.GenerateQRcodeBitmap(_txConfirm, True, "wxraven_icon_small")
                    self.m_bpButton12.SetBitmap(newimg)
    

            
            if self._datas['_jobStatus'] == "Done" and self._datas['_jobDone'] == True  :
                self.m_buttonClose.Show()
            
            if self._datas['_jobError'] != None  :
                self.m_buttonClose.Show()
                #self.m_txTargetAddress.SetValue()
                self.m_staticTextStatus.SetLabel(self._datas['_jobError']['message'])
                self.m_bitmap45.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('error_tsk'))
        """
        if self._JobId == None:
            return
    
        if self._JobId != None:
        
        """
        #try:
        #pass
             
                
        #except Exception as e:
        #    self.parent_frame.Log("Unable to load debug datas" , type="warning")
                    
    
    def OnCloseClicked(self, evt):
        self.parent.Close()
    
    def OnClose(self,evt):
        pass
            
    def GenerateQRcodeBitmap(self, text, addRavencoinLogo=True, logo='ravencoin'):
        qr = qrcode.QRCode(
            version=8,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=3,
            border=4,
        )    
        
        #img = qr.make(text)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        
        
        
        if addRavencoinLogo:
            
            rvnLogo = self.parent_frame.RessourcesProvider.GetImage(logo)
            
            
            logo_display = Image.open(self.parent_frame.GetPath("ROOT")+f'/res/default_style/normal/{logo}.png')
            #logo_display.thumbnail((60, 60))
            #logo_display = PILutils.PilImageFromWxBitmap(rvnLogo, True, False)
            #logo_display  = self.imagetopil(rvnLogo.ConvertToImage())
            #logo_display = Image.open('./')
            logo_display.thumbnail((16, 16))
            logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
            img.paste(logo_display, logo_pos)
        
        
        #img.save("sample.png")
        imgbmp = self.PIL2wx(img)    
        return imgbmp
            
            
    def PIL2wx (self,image):
        width, height = image.size
        #return wx.BitmapFromBuffer(width, height, image.tobytes())
        return wx.Bitmap.FromBuffer(width, height, image.convert("RGB").tobytes())

    def wx2PIL (self,bitmap):
        size = tuple(bitmap.GetSize())
        try:
            buf = size[0]*size[1]*3*"\x00"
            bitmap.CopyToBuffer(buf)
        except:
            del buf
            buf = bitmap.ConvertToImage().GetDataBuffer()
        return Image.frombuffer("RGB", size, buf, "raw", "RGB", 0, 1)
    
    def imagetopil(self,image):
        """Convert wx.Image to PIL Image."""
        pil = Image.new('RGB', (image.GetWidth(), image.GetHeight()))
        pil.fromstring(image.GetData())
        return pil
    
    
    def WxBitmapToPilImage(self, myBitmap ) :
        return self.WxImageToPilImage( self.WxBitmapToWxImage( myBitmap ) )
    
    def WxBitmapToWxImage(self, myBitmap ) :
        return wx.ImageFromBitmap( myBitmap )            