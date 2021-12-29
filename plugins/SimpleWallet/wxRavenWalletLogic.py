'''
Created on 13 déc. 2021

@author: slinux
'''
from .wxRavenWalletDesign import *



class walletMainPanel(wxRavenWalletMain):
    
    view_base_name = "Simple Wallet"
    view_name = "Simple Wallet"
    parent_frame = None
    default_position = "main"
    
    icon = 'wallet'#wx.Bitmap( u"res/default_style/normal/wallet.png", wx.BITMAP_TYPE_ANY )
    

    def __init__(self, parentFrame, position = "main", viewName= "Simple Wallet"):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        #parentFrame.AddInNotebook(self, self.plugin_name,parentFrame.wxRavenToolBook3 , self.icon)
        self.view_base_name = "Simple Wallet"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        parentFrame.Add(self, self.view_name ,position,  parentFrame.RessourcesProvider.GetImage(self.icon))
        self.initAllPanels()
        
        
        
    def initAllPanels(self):
        
        self.panelOverview = walletOverviewPane(self.parent_frame )
        # self.parent_frame.RessourcesProvider.GetImage(self.panelOverview.icon)
        self.wxRavenWalletBook.AddPage(self.panelOverview, "Wallet Overview" , bitmap = self.parent_frame.RessourcesProvider.GetImage(self.panelOverview.icon))
        
        self.panelAssets = walletAssetsOverview(self.parent_frame )
        
        self.wxRavenWalletBook.AddPage(self.panelAssets, "Assets", bitmap = self.parent_frame.RessourcesProvider.GetImage(self.panelAssets.icon))
        
        self.pannelSend = walletSendPane(self.parent_frame )
        
        self.wxRavenWalletBook.AddPage(self.pannelSend, "Send", bitmap = self.parent_frame.RessourcesProvider.GetImage(self.pannelSend.icon))
        
        

    def UpdateView(self):
        self.panelOverview.UpdateView()
        self.pannelSend.UpdateView()
        self.panelAssets.UpdateView()
        self.Layout()



class walletOverviewPane(wxRavenWalletOverview):
    plugin_name = "SimpleWallet Overview"
    parent_frame = None
    
    
    icon = 'UserAccount' #wx.Bitmap( u"res/default_style/normal/UserAccount.png", wx.BITMAP_TYPE_ANY )
    

    def __init__(self, parentFrame):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        
        """
        Oldway
        """
        #parentFrame.AddInNotebook(self, self.plugin_name,parentFrame.wxRavenToolBook1 , self.icon)

        
        self.parent_frame = parentFrame
        
        
        self.setupDataViewTable()
        self.updatePanel()
        #parentFrame.RegisterOnConnexionChanged(self.OnConnexionChanged)
    
        
       
    
    def setupDataViewTable(self):
        self.addressViewListCtrl.AppendTextColumn('account', width=150)
        self.addressViewListCtrl.AppendTextColumn('addresses', width=150)
        self.addressViewListCtrl.AppendTextColumn('balance', width=25)
        
        #self.assetsViewListCtrl.AppendTextColumn('asset', width=200)
        #self.assetsViewListCtrl.AppendTextColumn('balance', width=25)
    
    
    def OnRefreshButton(self, event):
        self.updatePanel()
    
    #Deprecated
    def OnConnexionChanged(self, con=""):
        self.updatePanel()
    
    
    def UpdateView(self):
        self.updatePanel()
        self.Layout()
    
    
    def updatePanel(self):
        
        
        try:
            showAdd=self.showAddressCheckbox.IsChecked()
            globalBalance = 0.0
            allAccountsDatas = []
            allAddresses = []
            
            
            
            
            if self.parent_frame.isCurrentNetworkActive() and self.parent_frame._isReady:
            
                try:
                    
                    
                    globalBalance = self.parent_frame.GetPluginData("SimpleWallet","globalBalance")
                    allAccountsDatas = self.parent_frame.GetPluginData("SimpleWallet","allAccountsDatas")
                    allAddresses = self.parent_frame.GetPluginData("SimpleWallet","allAddresses")
                    
                
                except Exception as e:
                    self.parent_frame.Log("Unable to load wallet datas" , type="warning")
                    #print("updatePanel getData ERROR> " + str(e))
            
            else:
                #pass    
                print("Data retreive Skipped due to connexion error.")
            
            
            
            tableData = []
            for ac in allAccountsDatas:
                
                dataAc = allAccountsDatas[ac]
                dataAd = str(dataAc['address'])
                dataBal = dataAc['balance']
                acBal = 0.0
                #if dataAc['address'] != "?":
                #    allAddresses = allAddresses+dataAc['address']       
                for bl in dataBal :
                    if bl['assetName'] == "RVN":
                        acBal = bl['balance']
                        
                        if not showAdd:
                            dataAd = "*"
                
                
                tableData.append([ac,dataAd , str(acBal)] )
            
            
            self.balanceStaticText.SetLabel(str(globalBalance.__round__(2)))
            
            self.addressViewListCtrl.DeleteAllItems()
            for item in tableData:
                self.addressViewListCtrl.AppendItem(item)
            
        except Exception as e:
            self.parent_frame.Log("Unable to display wallet datas" , type="error")
    
        
    def updatePanelOLD(self):
        
        
        try:
            showAdd=self.showAddressCheckbox.IsChecked()
            globalBalance = 0.0
            allAccountsDatas = []
            globalAssetBalance = []
            
            if self.parent_frame.isCurrentNetworkActive() and self.parent_frame._isReady:
            
                try:
                    
                    
                    globalBalance = self.parent_frame.GetPluginData("SimpleWallet","globalBalance")
                    allAccountsDatas = self.parent_frame.GetPluginData("SimpleWallet","allAccountsDatas")
                    #globalBalance = self.parent_frame.getNetwork().getbalance()['result']
                    #allAccountsDatas = self.parent_frame.getRvnRPC().wallet.getAllAccounts(displayAddress=showAdd)
                        
                    
                
                except Exception as e:
                    print("updatePanel ERROR> " + str(e))
            
            else:
                    
                print("Data retreive Skipped due to connexion error.")
            
            
            allAddresses = self.parent_frame.GetPluginData("SimpleWallet","allAddresses")
            
            
            tableData = []
            for ac in allAccountsDatas:
                
                dataAc = allAccountsDatas[ac]
                dataAd = str(dataAc['address'])
                
                dataBal = dataAc['balance']
                
                acBal = 0.0
                #if dataAc['address'] != "?":
                #    allAddresses = allAddresses+dataAc['address']
                            
                for bl in dataBal :
                    
                    if bl['assetName'] == "RVN":
                        
                        
                        acBal = bl['balance']
                        
                        #if showAdd:
                        #    acBal = self.RVN_balance_friendly(bl['balance'])
                
                
                tableData.append([ac,dataAd , str(acBal)] )
            
            
            #self.balanceStaticText.SetLabel(str(self.RVN_balance_friendly(globalBalance))) 
            self.balanceStaticText.SetLabel(str(globalBalance)) 
            
            self.addressViewListCtrl.DeleteAllItems()
            for item in tableData:
                self.addressViewListCtrl.AppendItem(item)
              
              
              
              
            if self.parent_frame.isCurrentNetworkActive():
                try:
    
                    #globalAssetBalance = self.parent_frame.getRvnRPC().wallet.getAddressAssetsBalance(allAddresses)
                    globalAssetBalance = self.parent_frame.GetPluginData("SimpleWallet","globalAssetBalance")
                    
                except Exception as e:
                    print("updatePanel ERROR> " + str(e)) 
            
            
            self.assetsViewListCtrl.DeleteAllItems()
            for item in globalAssetBalance:
                self.assetsViewListCtrl.AppendItem(item)   
            
            
        except Exception as e:
            print(e)



class walletAssetsOverview(wxRavenWalletAssetsOverview):
    plugin_name = "SimpleWallet Send"
    parent_frame = None
    
    
    icon = 'asset'#wx.Bitmap( u"res/default_style/normal/asset.png", wx.BITMAP_TYPE_ANY )
    
    
    lastaddresses = []

    def __init__(self, parentFrame):
        super().__init__(parent=parentFrame)
        self.parent_frame = parentFrame
        self.setupDataViewTable()
        self.UpdateView()
        #parentFrame.RegisterOnConnexionChanged(self.reloadSenderList)


    
    def setupDataViewTable(self):
        #self.addressViewListCtrl.AppendTextColumn('account', width=150)
        #self.addressViewListCtrl.AppendTextColumn('addresses', width=150)
        #self.addressViewListCtrl.AppendTextColumn('balance', width=25)
        
        self.assetsViewListCtrl.AppendTextColumn('asset', width=200)
        self.assetsViewListCtrl.AppendTextColumn('balance', width=25)


    
    def UpdateView(self):
        self.UpdateAssetList()
        self.Layout()
    
    
    
    
    
    
    def UpdateAssetList(self):
        
        if self.parent_frame._isReady:
            try:
                
                
                globalAssetBalance = []
                
                
                if self.parent_frame.isCurrentNetworkActive():
                
                    try:
                        
                        
                        globalAssetBalance = self.parent_frame.GetPluginData("SimpleWallet","globalAssetBalance")
                        
                    
                    except Exception as e:
                        #print("updatePanel getData ERROR> " + str(e))
                        self.parent_frame.Log("Unable to load wallet assets datas" , type="warning")
                
                else:
                    #pass    
                    print("Data retreive Skipped due to connexion error.")
                
                
                
                self.assetsViewListCtrl.DeleteAllItems()
                for item in globalAssetBalance:
                    self.assetsViewListCtrl.AppendItem(item)   
                
            except Exception as e:
                self.parent_frame.Log("Unable to display wallet assets" , type="error")



class walletSendPane(wxRavenWalletSend):
    plugin_name = "SimpleWallet Send"
    parent_frame = None
    
    
    icon = 'send_from_wallet' #wx.Bitmap( u"res/default_style/normal/send_from_wallet.png", wx.BITMAP_TYPE_ANY )
    #self.parent_frame.RessourcesProvider.GetImage(self.pannelSend.icon)
    
    lastaddresses = []

    def __init__(self, parentFrame):
        super().__init__(parent=parentFrame)
        self.parent_frame = parentFrame
        
        self.UpdateView()
        #parentFrame.RegisterOnConnexionChanged(self.reloadSenderList)

    
    def UpdateView(self):
        self.reloadSenderList()
        self.Layout()

    def reloadSenderList(self, con=""):
        if self.parent_frame._isReady:
            try:
                allAccountsDatas = []
                
            
                allAddresses = self.parent_frame.GetPluginData("SimpleWallet","allAddresses")
                
                # refresh your items with .Clear, .Append(), etc
                # I'm just adding new item every time user clicks on control     
                self.sendFromTextbox.Clear()  
                self.sendFromTextbox.Append("Any")    
                for ad in allAddresses:
                    self.sendFromTextbox.Append(ad)
                
                self.lastaddresses = allAddresses
                self.sendFromTextbox.SetSelection(0)
                
            except Exception as e:
                self.parent_frame.Log("Unable to load sending address list" , type="warning")

    def OnChoiceChanged(self, evt):
        newChoice=evt.GetString()
        
        
        adList = []
        availableAmount=0.0 
        
        
        
        if newChoice == "Any":
            
            try:
                availableAmount = self.parent_frame.getNetwork().getbalance()['result']
            except Exception as e:
                self.parent_frame.Log("Unable to retreive available balance" , type="warning")
                #print("availableAmount ERROR> " + str(e))
        
        else:
            adList.append(newChoice)
            
            allbalances= []
            try:
                allbalances = self.parent_frame.getRvnRPC().wallet.getaddressbalance(adList, showAsset=True)['result']
             
            except Exception as e:
                self.parent_frame.Log("Unable to retreive sending address avaailable balance" , type="warning")
                #print("allbalances ERROR> " + str(e))
             
            #print(allbalances)
            
            if allbalances !=None:
                for assets in allbalances:
                
                    if assets['assetName'] == "RVN":
                        availableAmount = assets['balance']
                        availableAmount = self.parent_frame.getRvnRPC().wallet.RVN_balance_friendly(availableAmount)
                        availableAmount = str(availableAmount)
                
            
        
        
        self.balanceStaticText.SetLabel(str(availableAmount)) 
        self.Layout()    
        
    
    
    def OnSendClick(self, evt):
        
        
        sendToAddr = self.sendToTextbox.GetValue()
        amount = self.sendAmountTextbox.GetValue()
        
        sendFromAddr = self.sendFromTextbox.GetString(self.sendFromTextbox.GetCurrentSelection())
        
        pwd = self.passwordTextbox.GetValue()
        
        
        
        dlg = wx.MessageDialog(self, 'Confirm transaction',
                               'Are you sure to send ?',
                               wx.YES_NO | wx.ICON_QUESTION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
        resultDialog=dlg.ShowModal()
        dlg.Destroy()
        
        
        
        if sendFromAddr== "Any":
            sendFromAddr = ""
        
        if resultDialog == wx.ID_YES:
            resultSend = self.parent_frame.getRvnRPC().wallet.sendRVN(toAd=sendToAddr, amount=amount, fromAd=sendFromAddr, pwd=pwd)
            
            
            dlgRes = wx.MessageDialog(self, 'transaction : '+resultSend,
                              resultSend,
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
            dlgRes.ShowModal()
            dlgRes.Destroy()
        
        
        