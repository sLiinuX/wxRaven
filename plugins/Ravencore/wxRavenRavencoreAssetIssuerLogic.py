'''
Created on 30 déc. 2021

@author: slinux
'''



from .wxRavenRavencoreDesign import *
from wxRavenGUI.application.wxcustom import *

from libs.RVNpyRPC import _asset as assetLib
from libs.RVNpyRPC._asset import AssetType



class RavencoreAssetIssuerDialog(wxRavenAssetIssuerDialog):
    '''
    classdocs
    '''

    view_base_name = "Asset Issuer"
    view_name = "Asset Issuer"
    parent_frame = None
    default_position = "mgr"
    icon = 'asset_new'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    #self.RessourcesProvider.GetImage('asset_navigation')
    
    
    

    def __init__(self, parentFrame, position = "mgr", viewName= "Asset Issuer", isInternalPluginView=True):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Asset Issuer"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.allIcons = {}
        
        
        icon = wx.EmptyIcon()
        icon.CopyFromBitmap(parentFrame.RessourcesProvider.GetImage(self.icon))
        self.SetIcon(icon)
        self.SetTitle("Issue an asset...")
        
        bSizer105 = wx.BoxSizer( wx.VERTICAL )
        
        #self.issuerPaner = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.issuerPanel = RavencoreAssetIssuerPanel(self, parentFrame, isInternalPluginView=True)
        bSizer105.Add( self.issuerPanel, 1, wx.EXPAND |wx.ALL, 5 )
        
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self.issuerPanel)
        
        
        self.SetSizer( bSizer105 )
        self.Layout()
        
        
        
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))

        else:
            self.Show()
            #pass


    def OnClose(self, evt):
        self.parent_frame.Plugins.DeleteViewInstance(self.view_name)
        #self.parent_frame.Views.
        #self.Close(force=False)
        print("OnClose")
        self.Destroy()

    def setupRoot(self,rootname):
        _id=self.issuerPanel.m_assetMainChoice.FindString( rootname, caseSensitive=False)
        self.issuerPanel.m_assetMainChoice.SetSelection(_id)



class RavencoreAssetIssuerPanel(wxRavenAssetIssuer):
    '''
    classdocs
    '''

    view_base_name = "Asset Issuer"
    view_name = "Asset Issuer"
    parent_frame = None
    default_position = "mgr"
    icon = 'asset'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    #self.RessourcesProvider.GetImage('asset_navigation')
    
    
    

    def __init__(self, parent, parentFrame, position = "mgr", viewName= "Asset Issuer", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        self.parent_frame=parentFrame
        self.pDialog = parent
        self._currentType = ""
        self._currentName = ""
        self._currentAdmin = ""
        self._finalName = ""
        #self._finalShortName = ""
        
        self._ipfs = ''
        self._hasIpfs = False
        
        self._reissuable = False 
        self._quantity = 1
        self._units = 0
        self._destination = ""
        self._change = ""
        self._prefix= ""
        
        self._implementedType = True
        
        
        self.m_issueButton.Enable(False)
        self._isValidInput = False
        
        self.setupPanel()
        
        
        
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))





    def setupPanel(self):
        
        ravencoin = self.parent_frame.getRvnRPC()
        for key in assetLib._ASSET_KEYCHAR_:
            self.m_assetTypeChoice.Append(key)

        self.Bind(wx.EVT_CHOICE, self.EvtChoice, self.m_assetTypeChoice)
        
        
        _allAdmins= ravencoin.asset.GetAllAdminAssets()
        for key in _allAdmins:
            self.m_assetMainChoice.Append(key)
            
        self.Bind(wx.EVT_CHOICE, self.EvtChoiceAdminAsset, self.m_assetMainChoice)
        
        
        self.Bind(wx.EVT_CHOICE, self.EvtOptionsChanged, self.m_reissuableOpt)
        self.Bind(wx.EVT_TEXT, self.EvtOptionsChanged, self.m_quantityTxt)
        self.Bind(wx.EVT_TEXT, self.EvtOptionsChanged, self.m_IPFSlinkTxt)
        self.Bind(wx.EVT_TEXT, self.EvtOptionsChanged, self.m_Destination)
    
    
    
    def setupRoot(self,rootname):
        _id=self.m_assetMainChoice.FindString( rootname, caseSensitive=False)
        self.m_assetMainChoice.SetSelection(_id)
        
    
    
    def EvtChoiceAdminAsset(self, event):
        str = event.GetString()
        self._currentAdmin = str
        #self.Layout()
        self.computeAssetFullName()
        
    
    
    
    
    
    def OnIpfsButtonClick(self, evt):
        ipfsPlugin = self.parent_frame.GetPlugin("IPFS")
        
        if ipfsPlugin != None:
            #self.parent_frame.Views.OpenView('IPFS File Uploader', 'IPFS', True)
            ipfsPlugin.OpenIPFSUploadDialog()
        
        else:
            self.parent_frame.Log("IPFS Plugin missing." ,  type="warning")
            self.m_ipfsUploadButton.Enable(False)
    
    def EvtOptionsChanged(self, event):
        
        self._reissuable = self.m_reissuableOpt.GetValue() 
        self._quantity = self.m_quantityTxt.GetValue() 
        self._units = self.m_unitsOpt.GetValue()  
        self._destination = self.m_Destination.GetValue()  
        
        self._ipfs = self.m_IPFSlinkTxt.GetValue()  
        
        
        self._hasIpfs = False
        
        if self._ipfs != "":
            self._hasIpfs = True
          
            
    def EvtChoice(self, event):
        str = event.GetString()
        self._currentType = str
        
        
        #if self._currentType.__contains__(key):
        if self.__Type__Require__Main__(self._currentType):
            self.mainAssetChoicePanel.Show()
        else:
            self.mainAssetChoicePanel.Hide()
        
        #self.Layout()
        self.computeAssetFullName()
        
    
    
    def __Type__Require__Main__(self, _type):
        _res=False
        
        if self._currentType.__contains__('SUB') or self._currentType.__contains__('UNIQUEASSET'): 
            _res=True
        return _res
    
    
    
    def OnAssetNameChanged(self, evt):
        print("OnAssetNameChanged")
        self._currentName = str(self.m_AssetNameTxt.GetValue()).upper()
        #self.m_AssetNameTxt.SetValue(self._currentName)
        self.computeAssetFullName()
    
    
    
    def computeAssetFullName(self):
        
        
        _prefix = self._currentAdmin.replace('!', '')
        finalName = self._currentName
        
        if self.__Type__Require__Main__(self._currentType):
            #self.mainAssetChoicePanel.Show()
            finalName = _prefix +'/'+ self._currentName
        else:
            finalName = finalName
        
        self.checkAssetNameLabel.SetLabel(finalName)    
        
        
        #self._currentName = ""
        #self._currentAdmin = ""
        self._finalName = finalName
        #self._finalShortName = 
        self._prefix= _prefix
        
        self.doVerifyAssetName()
        
        self.Layout()
        
        
        
        
        
        
    def doVerifyAssetName(self):
        self._isValidInput = True
        ravencoin = self.parent_frame.getRvnRPC()
        
        finalName = self.checkAssetNameLabel.GetLabel()
        
        if self.__Type__Require__Main__(self._currentType) and self._currentAdmin == "":
            self.checkErrorLabel.SetLabel("You must select an asset as parent !")
            self.checkAssetNameIcon1.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('error_tsk'))
            self._isValidInput = False
    
        
        if ravencoin.asset.__exist__(finalName):
            self.checkErrorLabel.SetLabel("The asset already exist !")
            self.checkAssetNameIcon1.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('error_tsk'))
            self._isValidInput = False
                
        if len(finalName) < 3:
            self.checkErrorLabel.SetLabel("The name must be at least 3 letters !")
            self.checkAssetNameIcon1.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('error_tsk'))
            self._isValidInput = False
    
        if len(finalName) > 31:
            self.checkErrorLabel.SetLabel("The name must be less than 31 letters !")
            self.checkAssetNameIcon1.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('error_tsk'))
            self._isValidInput = False
    
        if not self._implementedType:
            self.checkErrorLabel.SetLabel("The issuer is not yet implemented for this asset type !")
            self.checkAssetNameIcon1.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('error_tsk'))
            self._isValidInput = False
    
    
    
    
        fullmatch, regexp = ravencoin.asset.__verifyName__(self._currentName, self._currentType)
        if not fullmatch:
            self.checkErrorLabel.SetLabel(f"Regexp {regexp} not matching !")
            self.checkAssetNameIcon1.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('error_tsk'))
            self._isValidInput = False
    
        if self._currentType == "":
            self.checkErrorLabel.SetLabel(f"You must select an asset type !")
            self.checkAssetNameIcon1.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('error_tsk'))
            self._isValidInput = False
            
            
        if self._isValidInput:
            self.m_issueButton.Enable(enable=True)
            self.checkAssetNameIcon1.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('passed'))
            self.checkErrorLabel.SetLabel("all green !")
            
            
        else:
            self.m_issueButton.Enable(enable=False)
            
    
    
    
    
    
    
    
    
    
    def RequestDestinationFieldConfirm(self):
        dlg = wx.MessageDialog(self, f'No value has been specified for the Destination, create a new one ?',
                               'Confirm',
                               wx.YES_NO| wx.ICON_QUESTION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        res = dlg.ShowModal()
        dlg.Destroy()
        
        return res
    
    
    def RequestChangeFieldConfirm(self):
        dlg = wx.MessageDialog(self, f'No value has been specified for the Change, use destination ?',
                               'Confirm',
                               wx.YES_NO| wx.ICON_QUESTION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        res = dlg.ShowModal()
        dlg.Destroy()
        
        return res
    
            
    def RequestUserConfirm(self):
        dlg = wx.MessageDialog(self, f'Do you confirm the creation of the asset {self._finalName} ?',
                               'Confirm',
                               wx.YES_NO| wx.ICON_QUESTION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        res = dlg.ShowModal()
        dlg.Destroy()
        
        return res
    
    def ShowResult(self, res, dialgIcon=wx.ICON_INFORMATION):
        
        
        
        _textMsg = f"Asset created with success : Txid {res}"
        _textTitle = 'Asset Created !'
        
        
        if dialgIcon != wx.ICON_INFORMATION:
            _textMsg = f"{res}"
            _textTitle = 'Issue error !'
            
        
        dlg = wx.MessageDialog(self,_textMsg,
                               _textTitle,
                               wx.OK | dialgIcon
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()
            
    def OnIssueAsset(self, evt):
        
        network = self.parent_frame.getNetwork()
        
        
        
        
        
        if self._destination == "" :
            _newDest = self.RequestChangeFieldConfirm()
            if not _newDest:
                return
        
        if self._change == "" and self._destination != "" :
            _useDest = self.RequestChangeFieldConfirm()
            if _useDest:
                self._change = self._destination
        
        if not self.RequestUserConfirm():
            return
        
        
        
        if self._ipfs == "":
            self._ipfs = "QmPpYc4ZkA7E2zBMYE5m4msEmiTaEbZLyZPHgjJ5y8JoF6"
        
        
        _res = None
        
        if self._currentType =="MAINASSET" or self._currentType =="SUBASSET" :
            #issue "asset_name" qty "( to_address )" "( change_address )" ( units ) ( reissuable ) ( has_ipfs ) "( ipfs_hash )"
            #issue "ASSET_NAME" 1000 "myaddress" "changeaddress" 8 false true 
            #self._currentType   
            _res = network.issue(self._finalName, self._quantity, self._destination, self._change, self._units, self._reissuable, self._hasIpfs, self._ipfs)
            print(f"  {self._finalName} ")
            
            
            
        elif self._currentType =="UNIQUEASSET":
            #issueunique "root_name" [asset_tags] ( [ipfs_hashes] ) "( to_address )" "( change_address )"
            #issueunique "MY_ASSET" '["primo","secundo"]' '["first_hash","second_hash"]'
            _res = network.issueunique(self._prefix, [self._currentName], [self._ipfs] , self._destination, self._change)
            print(f"  {self._prefix}   - {self._currentName}")
            #pass
           
        elif self._currentType =="QUALIFIERASSET" or self._currentType =="SUBQUALIFIERASSET":
            
            #issuequalifierasset 
            #issuequalifierasset "asset_name" qty "( to_address )" "( change_address )" ( has_ipfs ) "( ipfs_hash )"
            _res = network.issuequalifierasset(self._finalName, self._quantity, self._destination, self._change,  self._hasIpfs, self._ipfs)
            print(f"  {self._finalName} ")
              
        elif self._currentType =="RESTRICTEDASSET" :
            pass
            #reissuerestrictedasset
            #issuerestrictedasset "asset_name" qty "verifier" "to_address" "( change_address )" (units) ( reissuable ) ( has_ipfs ) "( ipfs_hash )"    
            _res = network.issuerestrictedasset(self._finalName, self._quantity, self._destination, self._change,  self._units, self._reissuable, self._hasIpfs, self._ipfs)
        
            print(f"  {self._finalName} ")
        
        
        """
        if _res != None:
            
            if _res['error'] == None:
                self.ShowResult(_res['result'])
                self.pDialog.OnClose(None)
                
            else:
                self.ShowResult(_res['error'], wx.ICON_ERROR)
                
        """
        
        ReportRPCResult(self.parent_frame, _res, "success", "Asset Issued !", "Unable Issue Asset.", False)
                
                
                
        