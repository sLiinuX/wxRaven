'''
Created on 29 janv. 2022

@author: slinux
'''
import threading
import time 

import os

import random

from .wxRavenProfileManagerDesign import *
from wxRavenGUI.application.wxcustom import *
import logging



from .ProfileManagerEngine import wxRavenProfileEngine

class wxRavenProfileManager_ProfileSelectorLogic(wxRaven_ProfileManager_Selector):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Profile Selector"
    view_name = "Profile Selector"
    parent_frame = None
    default_position = "dialog"
    icon = 'UserAccount_custom'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent, parentFrame,  position = "dialog", viewName= "Profile Selector", isInternalPluginView=False, isInternalPanel=False, parentDataObj=None, choosemode='profil'):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        print("wxRavenProfileManager_ProfileSelectorLogic")
        self.view_base_name = "Profile Selector"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parent
        self.parentDataObj = parentDataObj
        
        self.isInternalPluginView = isInternalPluginView
        self.isInternalPanel = isInternalPanel
        self.logger = logging.getLogger('wxRaven')
        
        self.choosemode=choosemode
        
        self.profileManager = wxRavenProfileEngine()
        self.selection = ''
        #self.profileList = {'localuser':parentFrame.GetPath('ROOT'),
        #                    
        #                    }
        self.profileList ={}
        if choosemode == 'profile':
            self.profileList = self.profileManager.profile_list
        elif choosemode == 'edition':
            self.profileList = self.profileManager.sw_editions_list
            self.parent.SetTitle("Select a SW Edition :")
            self.selection = ''
        else:
            self.profileList = self.profileManager.profile_list
            
            
        self.profileMapping = {}
        self.itemcount = 0
        self.selection = ''
        
        self.SizerObj= None
        #isInternalPanel= True
        if isInternalPanel:
            
            #self.m_GenerateSwapTx.Hide()
            #self.m_txDatas.Hide()
            #self.m_panelTxType.Hide()
            pass
            #self.Sizer = wx.BoxSizer( wx.VERTICAL )
            #self.Sizer .Add( self, 1, wx.ALL|wx.EXPAND, 5 )
            
        self.setupPanel()
        self.Layout()
        #self.parent.ResizeDialog()
        
    
    
    
    def setupPanel(self):
        
        _typeclass = wxRaven_ProfileManager_Selector_ProfileItemLogic
        if self.choosemode == 'edition':
            _typeclass = wxRaven_ProfileManager_Selector_EditionLogic
        
        
        self.sizer= wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )  
        self.sizer.Add( bSizer3, 1, wx.EXPAND, 5 ) 
        for _profile in self.profileList:
            
            _newPanelProfile = _typeclass(self,self.parent_frame, _profile,self.profileList[_profile]  )
            _newPanelProfile.m_profileButton.Bind(wx.EVT_BUTTON, self.OnProfileClicked)
            self.logger.info(f" {self.choosemode} : {_profile} --> {_newPanelProfile.m_profileButton.GetId()}" )
            
            if self.choosemode == 'profile':
                self.profileMapping[ _newPanelProfile.m_profileButton.GetId() ] = self.profileList[_profile]
            elif self.choosemode == 'edition':
                self.profileMapping[ _newPanelProfile.m_profileButton.GetId() ] = _profile
            else:
                self.profileMapping[ _newPanelProfile.m_profileButton.GetId() ] = self.profileList[_profile]
            
            self.itemcount = self.itemcount + 1
            #bSizer3 = wx.BoxSizer( wx.VERTICAL )
            bSizer3.Add(_newPanelProfile, 0,wx.ALL, 5)
    
        if self.choosemode == 'profile':
            _profileCreationItem = wxRaven_ProfileManager_Selector_ProfileItemLogic(self,self.parent_frame, 'Import / Create','', isNew=True  )
            _profileCreationItem.m_profileButton.Bind(wx.EVT_BUTTON, self.OnImportOrCreateClicked)
            bSizer3.Add(_profileCreationItem, 0,wx.ALL, 5)
            self.itemcount = self.itemcount + 1
        
        self.SetSizer(self.sizer)
        self.Layout()
    
    def OnImportOrCreateClicked(self, evt):
        dlg = wx.DirDialog(self, "Choose a directory:",
                          style=wx.DD_DEFAULT_STYLE
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )

        # If the user selects OK, then we process the dialog's data.
        # This is done by getting the path data from the dialog - BEFORE
        # we destroy it.
        if dlg.ShowModal() == wx.ID_OK:
            profilePath = dlg.GetPath()
            
            
            _exist = self.profileManager.CheckProfilePath(profilePath)
            if not _exist:
                
                
                profileName = RequestUserTextInput(self, "No profile detected at this location,\nInput a new profile name (without Spaces) :", "New Profile Name :")
                
                self.parent.Hide()
                
                #Adding SW Selection
                
                _edDialog=wxRavenProfileManager_ProfileSelectorDialogLogic( choosemode ='edition')
                _edResp = _edDialog.ShowModal()
                _editionChoosed = _edDialog._panel.selection
                _edDialog.Destroy()
                
                
                
                _created = self.profileManager.CreateProfileInPath(profilePath, profileName, sw_edition=_editionChoosed)
                
                if _created:
                    self.selection = profilePath + '/'+profileName
            
                    
            else:
                self.selection = profilePath
                
            self.CloseAfter(wx.ID_OK)
        else:  
            self.selection = None  
            self.CloseAfter(wx.ID_NO)
    
    
    def OnProfileClicked(self, evt):
        print(evt.GetId())
        _path = self.profileMapping[evt.GetId()]
        print(_path)
        self.selection = _path
        
        self.logger.info(f" OnProfileClicked Userchoice  : {self.selection}" )
        #if self.choosemode=='edition':
        
        self.CloseAfter(wx.ID_OK)
        
    
    
    
    
    def CloseAfter(self, res=wx.ID_OK):
        
        if self.isInternalPanel:
            try:
                if self.parent.IsModal():
                    self.logger.info(f" close modal {res}" )
                    self.parent.EndModal(res)
                else:
                    self.logger.info(f" close classic dialog" )
                    self.parent.Close()
            except Exception as e:
                self.logger.info(f" OnProfileClicked : {e}" )
        else:
            try:
                self.logger.info(f" close classic frame" )
                self.parent.OnClose(None)
            except Exception as e:
                self.logger.info(f" OnProfileClicked OnClose : {e}" )
    
    
        
    def UpdateView(self, evt=None):
        pass    
    






class wxRavenProfileManager_ProfileSelectorDialogLogic(wxRaven_ProfileManager_SelectorDialog):


    def __init__(self,parent=None, parentFrame=None,  position = "dialog", viewName= "Profile Selector", isInternalPluginView=False, isInternalPanel=True, parentDataObj=None, choosemode='profile'):
        super().__init__(None)
        self.curPath = os.getcwd() + '/'
        '''
        if parentFrame == None:
            parentFrame=object()
            parentFrame.
        '''
        self._panel = wxRavenProfileManager_ProfileSelectorLogic( self, None, isInternalPanel=True, choosemode=choosemode)
        self.parent = parent
        self.Sizer = wx.BoxSizer( wx.VERTICAL )
        self.Sizer .Add( self._panel, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        #_icon = #UserAccount_custom
        icon = wx.EmptyIcon()
        #icon.CopyFromBitmap(wx.Bitmap( u"res/default_style/normal/ravencoin.png", wx.BITMAP_TYPE_ANY ))
        icon.CopyFromBitmap(wx.Bitmap( self.curPath + '/res/default_style/normal/UserAccount_custom.png', wx.BITMAP_TYPE_ANY ))
        self.SetIcon(icon)
        
        self.SetSizerAndFit(self.Sizer , deleteOld=True)
        if self._panel.itemcount > 2:
            width,height = self.GetSize()
            #self.SetMaxSize((168*self._panel.itemcount,height))
            self.SetSize((168*self._panel.itemcount,250))
            #self.SetSizerAndFit(sel, deleteOld=True)
        self.Layout()
        #self.SetSize(x, y, width, height, sizeFlags=SIZE_AUTO)
        
        
        

    def ResizeDialog(self, evt=None):
        
        
        #self._Panel.Layout()
        #self.SetSizerAndFit(self.GetSizer())
        #self.SetSizerAndFit(self.Sizer)
        
        
        self.SetSizerAndFit(self.GetSizer(), deleteOld=False)
        self.Layout()




    
    

    
class wxRaven_ProfileManager_Selector_ProfileItemLogic(wxRaven_ProfileManager_Selector_ProfileItem):
    
    def __init__(self, parent, parentFrame, profileName, path, isNew=False):
        
        super().__init__(parent)
        self.m_profileLabel.SetLabel(profileName)
        
        self.curPath = os.getcwd() + '/'
        
        if not isNew:
            _profileCustomIcon = None
            if os.path.isfile(path+'/userdata/avatar.png'):
                print('avatar FOUND !')
                _profileCustomIcon = path+'/userdata/avatar.png'
                _profileCustomIcon = wx.Bitmap( _profileCustomIcon, wx.BITMAP_TYPE_ANY )
            else:
                c = random.choice(['avatar_1', 'avatar_2', 'avatar_3'])
                
                _file = self.curPath + '/res/default_style/normal/'+c+'.png'
                
                #_profileCustomIcon = parentFrame.RessourcesProvider.GetImage(c)
                _profileCustomIcon = wx.Bitmap( self.curPath + _file, wx.BITMAP_TYPE_ANY )
                
            self.m_profileButton.SetBitmap(_profileCustomIcon)
        else:
            #self.m_profileButton.SetBitmap(parentFrame.RessourcesProvider.GetImage('avatar_new'))
            self.m_profileButton.SetBitmap(wx.Bitmap( self.curPath + '/res/default_style/normal/avatar_new.png', wx.BITMAP_TYPE_ANY ))
        
        self.Layout()


#
#
# Copy cat class for the Edition Selection
#
class wxRaven_ProfileManager_Selector_EditionLogic(wxRaven_ProfileManager_Selector_ProfileItem):
    
    def __init__(self, parent, parentFrame, profileName, path ):
        
        super().__init__(parent)
        
        
        #wxRaven : Developer/Server Edition
        _nameEdition = profileName.split(':')
        
        self.m_profileLabel.SetLabel(_nameEdition[1] )
        #self.curPath = os.getcwd() + '/'
        
        if True:
            _profileCustomIcon = None
            if os.path.isfile(path+'/userdata/avatar.png'):
                print('avatar FOUND !')
                _profileCustomIcon = path+'/userdata/avatar.png'
                _profileCustomIcon = wx.Bitmap( _profileCustomIcon, wx.BITMAP_TYPE_ANY )
            else:
                print(f'{path}/userdata/avatar.png not found')
            '''
            else:
                c = random.choice(['avatar_1', 'avatar_2', 'avatar_3'])
                _file = self.curPath + '/res/default_style/normal/'+c+'.png'
                #_profileCustomIcon = parentFrame.RessourcesProvider.GetImage(c)
                _profileCustomIcon = wx.Bitmap( self.curPath + _file, wx.BITMAP_TYPE_ANY )
            '''
            self.m_profileButton.SetBitmap(_profileCustomIcon)
            
            self.Layout()
   
    