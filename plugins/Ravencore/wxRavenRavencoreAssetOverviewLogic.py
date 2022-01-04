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
import wx.lib.mixins.listctrl as listmix
import threading

from wxRavenGUI.application.wxcustom.CustomLoading import *


class wxRavenAssetOverviewPanel(wxRavenAssetDetails_OverviewPanel, listmix.ColumnSorterMixin):
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
        
        self._loadingPanel  = None
        self.SetupListOwners()
        
        
        self.assetName = ""
        
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, self.m_listCtrl1)
        
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
        
    
    """
    def LoadAsset(self, assetName, displayAfter=False):
        pass
    """
    def UpdateView(self):
        self.Layout()  
        
        
    
    def DisplayAsset(self, assetData, assetUrl=""):
        if assetData != None:
            self.m_assetNameText.SetValue(assetData['name'])
            self.assetName = assetData['name']
            
            isAdmin = False 
            if self.assetName.__contains__('!'):
                isAdmin = True 
                
            
            #print(assetData)
            
            if assetData.__contains__('ipfs_hash'):
                self.m_assetIPFStext.SetValue(assetData['ipfs_hash'])
            else:
                self.m_assetIPFStext.SetValue("n/a")
            self.m_assetTypeText.SetValue(assetData['type'].value)
            
            
            if assetData.__contains__('amount'):
                self.m_assetSupplyTxt.SetValue(str(assetData['amount']))
            else:
                self.m_assetSupplyTxt.SetValue(str(1))
            
            
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
            elif isAdmin:
                #asset_new_qrcode
                self.m_bpButton27.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('ipfs_not_available_4'), dir=wx.LEFT)
                
            else:
                self.m_bpButton27.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('ipfs_not_available_4'), dir=wx.LEFT)
            
            
            self.RequestOwnerList_T()
            #self.ShowOwners(assetData['name'])
            
                
        else:
            self.m_assetNameText.SetValue("")
            self.m_assetIPFStext.SetValue("")
            self.m_assetTypeText.SetValue("")
            self.m_assetSupplyTxt.SetValue("")
            self.m_assetCreatedTxt.SetValue("")
            
            
            self.m_bpButton27.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('ipfs_not_available_4'), dir=wx.LEFT)
            
            
            
            
    
    
    
    
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetListCtrl(self):
        return self.m_listCtrl1
    
    # Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
    def GetSortImages(self):
        
        if self._curColumnSort ==0:
            return (self.allIcons['alphab_down'], self.allIcons['alphab_up'])
        else:
            return (self.allIcons['sort_down_2'], self.allIcons['sort_up_2'])
    
    
    
    def OnQrCodeClick(self, evt):
        pass
    
    
    
    def RequestOwnerList_T(self):
        self.ShowLoading()
        
        self.m_listCtrl1.Freeze()
        self.ClearResults()
        self.m_listCtrl1.Thaw()
        
        t=threading.Thread(target=self.DoRequestOwnerList, args=())
        t.start() 
    
    def DoRequestOwnerList(self):
        self._resultOwnerList = self.parent_frame.getNetwork().listaddressesbyasset(self.assetName)['result']
        wx.CallAfter(self.ShowOwners, (self.assetName))
        
    def ShowLoading(self):
        
        if self._loadingPanel  == None:
            #self._loadingPanel =  wxBackgroundWorkerAnimation(self.m_listCtrl1)
            self._loadingPanel =  wxBackgroundWorkerAnimation(self.listCtrlContainer)
            #listCtrlContainer
        self._loadingPanel.Show(show=True)
        
        #self._loadingPanel.Popup()
        self.Layout()
        
    def HideLoading(self):
        if self._loadingPanel  != None:
            self._loadingPanel.Hide()
            self.Layout()
    
    
    def ShowOwners(self, assetName):
        
        self.ShowLoading()
        
        self.m_listCtrl1.Freeze()
        self.ClearResults()
        
        
        
        resultData = {}
        _cursor = 0
        if self._resultOwnerList!= None:
            
            #_cursor = 0
            for key in self._resultOwnerList:
                qt = self._resultOwnerList[str(key)]
                
                
                index = self.m_listCtrl1.InsertItem(self.m_listCtrl1.GetItemCount(),str(key), self.allIcons['wallet'] )
                self.m_listCtrl1.SetItem(index,1, str(qt))
                self.m_listCtrl1.SetItemData(index, _cursor)
                resultData[_cursor] = (str(key),qt)
                _cursor= _cursor+1
                
                
        self.m_listCtrl1.SetColumnWidth(0, 450)
        self.m_listCtrl1.SetColumnWidth(1, 100)        
                
        self.m_listCtrl1.Thaw()
        self.m_ownerCount.SetValue(str(_cursor))
        
        self.itemDataMap = resultData
        listmix.ColumnSorterMixin.__init__(self, 2)
        
        
        self.HideLoading()
        self.SetAutoLayout(True)
        self.Layout()
    
    
    def OnColClick(self, event):
        self._curColumnSort = event.GetColumn()
        #print("OnColClick: %d\n" % event.GetColumn())
        #self.log.WriteText("OnColClick: %d\n" % event.GetColumn())
        event.Skip()
        
    
    def ClearResults(self):
        self.m_listCtrl1.DeleteAllItems()
    
    def SetupListOwners(self):
        info = wx.ListItem()
        info.Mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
        info.Image = -1
        info.Align = 0
        info.Text = "Address"
        self.m_listCtrl1.InsertColumn(0, info)

        info.Align = wx.LIST_FORMAT_RIGHT
        info.Text = "Quantity"
        self.m_listCtrl1.InsertColumn(1, info)
        """
        info.Align = 0
        info.Text = "Supply"
        self.m_listCtrl1.InsertColumn(2, info)
        
        info.Align = 0
        info.Text = "Created"
        self.m_listCtrl1.InsertColumn(3, info)
        
        info.Align = 0
        info.Text = "Various"
        self.m_listCtrl1.InsertColumn(4, info)
        """
        
        
        """
        
        self.m_listCtrl1.SetColumnWidth(0, 350)
        self.m_listCtrl1.SetColumnWidth(1, 100)
        self.m_listCtrl1.SetColumnWidth(2, 100)
        self.m_listCtrl1.SetColumnWidth(3, 100)
        self.m_listCtrl1.SetColumnWidth(4, 100)
        """
        
        self.il = wx.ImageList(16, 16)
        
        self._curColumnSort = 0
        
        self.allIcons['wallet'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('wallet') )
        
        self.allIcons['asset'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('asset_ravencoin-blue') )
        self.allIcons['info'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('info_obj') )
        
        self.allIcons['sort_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up') )
        self.allIcons['sort_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down') )
        self.allIcons['sort_up_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_up_2') )
        self.allIcons['sort_down_2'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('sort_down_2') )
        
        self.allIcons['alphab_up'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_up') )
        self.allIcons['alphab_down'] = self.il.Add( self.parent_frame.RessourcesProvider.GetImage('alphab_sort_co') )
        
        
        
        
        self.m_listCtrl1.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
    
    
    
    
    
    
    
    
            
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
        