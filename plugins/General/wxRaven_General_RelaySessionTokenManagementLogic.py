'''
Created on 8 mars 2022

@author: slinux
'''
import threading
import time 

import wx 
import sys

import uuid  
from .wxRavenGeneralDesign import wxRaven_General_RelaySessionTokenManagement

class wxRaven_General_RelaySessionTokenManagement_Logic(wxRaven_General_RelaySessionTokenManagement):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Relay Session Token Management"
    view_name = "Relay Session Token Management"
    parent_frame = None
    default_position = "dialog"
    icon = 'help_view'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent, parentFrame, position = "dialog", viewName= "Relay Session Token Management", isInternalPluginView=True):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        #print(parent)
        #print(parentFrame)
        
        
        self.view_base_name = "Relay Session Token Management"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.parent = parent
        self._dataCache= {}
        
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
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.__loadListOfConnexion__,), daemon=True)
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
    
    
    
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
        self.Layout()
            
            
    
    
    
    
    def OnSelectedConnexionChanged(self,evt):
        self.UpdateView()
    
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        if True:
        #try:
            _currentChoice =  self.m_choiceConnexion.GetString(self.m_choiceConnexion.GetCurrentSelection())      
            
            if self._dataCache.__contains__(_currentChoice):
                _connexion = self._dataCache[_currentChoice]
                _datas = None
                
                
                generalPlugin = self.parent_frame.GetPlugin('General')
                
                
                #self.m_bitmap32.SetBitmap(self.parent_frame.RessourcesProvider.GetImage(_datas['scheme']))
                #self.m_textURL.SetValue(_datas['url'])
                #if _datas['secure'] != None:
                #    if _datas['secure'] != "None":
                #        self.m_checkBoxSecure.SetValue(_datas['secure'])
                #self.m_checkBoxLocal.SetValue(_datas['local'])
                #self.m_checkBoxRelay.SetValue(_datas['relay'])
                wsInfos = _connexion.rpc_status()
                tokenDatas=_connexion.__CheckSessionToken__()
                #
                
                self.m_textUUID.SetValue(str(uuid.UUID(int=uuid.getnode())))
                disabled_relay_user_session_token = not generalPlugin.PLUGIN_SETTINGS['relay_user_session_token']
                #self._Panel.m_checkNoPublicAuth.SetValue(relay_user_session_token)   
                
                relay_private_session_key = generalPlugin.PLUGIN_SETTINGS['relay_private_session_key']
                #self._Panel.m_checkPrivateAuth.SetValue(relay_private_session_key)   
                
                relay_private_session_key_value = generalPlugin.PLUGIN_SETTINGS['relay_private_session_key_value']
                #self._Panel.m_textUserSessionToken.SetValue(relay_private_session_key_value)  
                '''
                
                if disabled_relay_user_session_token:
                    pass
                if relay_private_session_key:
                    self.m_textSESSIONTOKEN.SetValue(relay_private_session_key_value)
                else:
                    
                '''
                
                
                _valid=False
                if tokenDatas['result']!=None:
                    _valid = tokenDatas['result']['valid']
                    
                self.m_checkBoxValid.SetValue(_valid)
                
                _remaining = "500 Kb"
                if tokenDatas['result']!=None:
                    _remaining = tokenDatas['result']['size_friendly']
                    
                self.m_textCtrl15.SetValue(_remaining)
                if _connexion._user_token!=None:
                    self.m_textSESSIONTOKEN.SetValue(str(_connexion._user_token))
                _desc=''    
                if wsInfos['result']!=None:
                    if wsInfos['result'].__contains__('service_description'):
                        _desc = wsInfos['result']["service_description"]
                        
                if _desc!='':
                    self.m_textCtrl9.SetValue(str(_desc))
            #myPluginData = self.parent_frame.GetPluginData("Tutorial","myPluginData2")
            #myPluginSetting =  self.parent_frame.GetPluginSetting("Tutorial","booleansetting")#SavePanelSettings GetPluginSetting
            #
            #Update your panel
            #       
            
            
            #textToPrint = " booleansetting = " + str(myPluginSetting)
            #textToPrint = textToPrint + "\n\n myPluginData2 = " + str(myPluginData)
            pass 
            #self.m_staticText2.SetLabel(str(textToPrint)) 
             
                
        #except Exception as e:
        #    self.parent_frame.Log("Unable to load debug datas" , type="warning")
                    
            
            