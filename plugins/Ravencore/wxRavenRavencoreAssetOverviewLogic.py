'''
Created on 29 déc. 2021

@author: slinux
'''


from .wxRavenRavencoreDesign import wxRavenAssetDetails_OverviewPanel



import wx
import qrcode
from PIL import Image
import os
from libs import PILutils


class wxRavenAssetOverviewPanel(wxRavenAssetDetails_OverviewPanel):
    '''
    classdocs
    '''


    view_base_name = "Asset Details"
    view_name = "Asset Details"
    parent_frame = None
    default_position = "main"
    icon = 'asset_navigation'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    #self.RessourcesProvider.GetImage('asset_navigation')
    
    
    

    def __init__(self, parent, parentFrame, position = "main", viewName= "Asset Details", isInternalPluginView=True):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Asset Search"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.allIcons = {}
        
        
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
        
    
    """
    def LoadAsset(self, assetName, displayAfter=False):
        pass
    """
    
    
    def DisplayAsset(self, assetData, assetUrl=""):
        if assetData != None:
            self.m_assetNameText.SetValue(assetData['name'])
            
            
            print(assetData)
            
            if assetData.__contains__('ipfs_hash'):
                self.m_assetIPFStext.SetValue(assetData['ipfs_hash'])
            else:
                self.m_assetIPFStext.SetValue("n/a")
            self.m_assetTypeText.SetValue(assetData['type'].value)
            self.m_assetSupplyTxt.SetValue(str(assetData['amount']))
            if assetData.__contains__('datetime'):
                self.m_assetCreatedTxt.SetValue(str(assetData['datetime']))
            else:
                self.m_assetCreatedTxt.SetValue("?")
            #self.m_assetCreatedTxt.SetLabel(assetData['name'])
            
            _qrcode = ""
            if assetData.__contains__('ipfs_hash') or assetUrl !="":            
                imgbmp = self.GenerateQRcodeBitmap(assetData['ipfs_hash'])
                
                if assetUrl!= "":
                    imgbmp = self.GenerateQRcodeBitmap(assetUrl)
                
                self.m_bpButton27.SetBitmap(imgbmp, dir=wx.LEFT)
            else:
                self.m_bpButton27.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('search_45'), dir=wx.LEFT)
                
        else:
            self.m_assetNameText.SetValue("")
            self.m_assetIPFStext.SetValue("")
            self.m_assetTypeText.SetValue("")
            self.m_assetSupplyTxt.SetValue("")
            self.m_assetCreatedTxt.SetValue("")
            
            
            self.m_bpButton27.SetBitmap(self.parent_frame.RessourcesProvider.GetImage(self.icon), dir=wx.LEFT)
            
            
            
            
            
    def GenerateQRcodeBitmap(self, text, addRavencoinLogo=True):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=3,
            border=4,
        )    
        
        #img = qr.make(text)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        
        
        
        if addRavencoinLogo:
            
            rvnLogo = self.parent_frame.RessourcesProvider.GetImage('ravencoin')
            
            
            logo_display = Image.open(os.getcwd()+'/res/default_style/normal/ravencoin.png')
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
        #return myPilImage
        