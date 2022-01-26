'''
Created on 18 déc. 2021

@author: slinux



This file contains the main class to define the plugin
Each plugin must have a plugin.py file which declare a class wxRavenPlugin(PluginObject)


'''


#import the class form above level, it contains predefined functions to overwrite.
#from plugins.pluginObjectTemplate import * 
from wxRavenGUI.application.pluginsframework import *
#import the design of your plugin made in FormBuilder

from .wxRavenIPFSDesign import *
#import the plugin setting panels, from another file to be more simple

from libs import RVNpyIPFS

#used for long datas requests
import threading

from .wxRavenIPFSWebViewLogic import *
from .wxRavenIPFSUploaderLogic import *


from .pluginSettings import MyIPFSSettingPanel_WithLogic

class wxRavenPlugin(PluginObject):
    '''
    classdocs
    '''


    def __init__(self, parentFrame, position="mgr"):
        
        
        #Call the parent class with ParentFrame and Position
        #This object is the plugin instance and will manage all views internally.
        PluginObject.__init__(self, parentFrame, position=position)
        
        
        #
        #ParentFrame is used to refer to the main app
        #Position is used to refer to the defaut position views are open.
        #
        
        
        
        #Define your plugin meta-datas :
        #
        # Name : Name of the plugin, It match the Plugin Folder name (not verified in other cases)
        # Icon
        # Views : All the views that contains the plugin
        
       
        self.PLUGIN_NAME = "IPFS"
        self.PLUGIN_ICON = self.RessourcesProvider.GetImage('raven_ipfs') #wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
        
        
        _iconUpload = self.RessourcesProvider.GetImage('ipfs_add')
        
        #
        #    View Object declare all the 'Views' that can be instanciated
        #    {
        #             'viewid':                  a unique id for the view
        #             'name':                    a name for the view
        #             'title':                   a title id for the view
        #             'position':, 
        #             'icon':
        #             'class': 
        #             'default':                 Boolean to determine if the view is open by default at startup
        #             'multipleViewAllowed':     Boolean to determine if the view allow multiple instance of it 
        #}
        #        
        
        
        self.PLUGINS_VIEWS= [ 
                    
                    
                    {
                     'viewid':'Ravencoin IPFS Home', 
                     'name':'Ravencoin IPFS Home', 
                     'title':'Ravencoin IPFS Home', 
                     'position':position, 
                     'icon':self.PLUGIN_ICON, 
                     'class': wxRavenIPFSWebHomepage ,
                     'default':False,
                     'multipleViewAllowed':True
                     },
                    
                     {
                         'viewid':'IPFS File Uploader', 
                     'name':'IPFS File Uploader', 
                     'title':'IPFS File Uploader', 
                     'position':'dialog', 
                     'icon':_iconUpload, 
                     'class': wxRavenIPFSFileUploader ,
                     'default':False,
                     'multipleViewAllowed':False
                     }
                    
                    
        
                    
                ]
        
        """
        {
                     'viewid':'IPFS File Uploader', 
                     'name':'IPFS File Uploader', 
                     'title':'IPFS File Uploader', 
                     'position':position, 
                     'icon':self.PLUGIN_ICON, 
                     'class': wxRavenIPFSFileUploader ,
                     'default':False,
                     'multipleViewAllowed':False
                     }
        """    
        
        #
        #    Setting Object declare all the 'default settings' 
        #    Once the plugin loaded for the first time, those settings will be saved
        #    in the config.ini file in a dedicated section when app close.
        #
        #    On next plugin load, if the config file contains plugins settings
        #    those will be overwritten in the _LoadPluginSettings() function
        #    
        #    you need to declare your own function as later in the file to CAST datas 
        #    that come from the ConfigParser in String only
        #
        #    {
        #             'key':                 value
        #    }
        #        
        
        
        self.PLUGIN_SETTINGS = {
                'homepage_url' : "https://ipfs.ravenclause.com/",
                'ipfs_rpc_api_ip' : "ec2-3-19-32-37.us-east-2.compute.amazonaws.com",
                'ipfs_rpc_api_ip_bis' : "70.81.223.229",
                'ipfs_direct_api_ip' : "/ip4/127.0.0.1/tcp/5001",
            }
        
        
        
        
        #
        # Lets put some setting pannels from pluginsetting file (to define as well)
        #
        self.PLUGIN_SETTINGS_GUI = []
        
        _prefIcon = self.RessourcesProvider.GetImage('raven_ipfs')
        _IPFSSettingPanel_WithLogic = PluginSettingsTreeObject("IPFS", _prefIcon, classPanel=MyIPFSSettingPanel_WithLogic, _childs=None)
        self.PLUGIN_SETTINGS_GUI.append(_IPFSSettingPanel_WithLogic)

        
        
        
        #
        # Datas : In order to avoid each view to individually request the same data through RPC,
        #         the plugin can contains Global vars / datas shared to the views
        #         it also allow to request those big datas through thread and call update after
        #
        self.setData("_uploadedFiles", {})
        self.setData("rpcPluginCmdLine", None)
        #self.setData("myPluginData2", False)
        
        
        #
        # Plugin can Register on callbacks like Connexion change in this case, it will start a thread to get datas
        #
        self.parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        
        
        #
        # Finally, this last line is MANDATORY to load the default views.
        # REMOVED AND REPLACED BY AN AUTO LOAD
        #self.LoadPluginFrames()
        self.waitApplicationReady()
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.__applicationReady__,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parentFrame._isReady:
            time.sleep(1)
            
        wx.CallAfter(callback, ()) 
    
    
    def __applicationReady__(self, evt=None):
        _rpc_ip = self.PLUGIN_SETTINGS['ipfs_rpc_api_ip']
        _ipfs_direct_api_ip = self.PLUGIN_SETTINGS['ipfs_direct_api_ip']
        ipfs_rpc = RVNpyIPFS.RavenPyIPFS(ConString=_ipfs_direct_api_ip, rpcServer=_rpc_ip)
            
        self.rpcPluginCmdLine = ipfs_rpc
        self.setData("rpcPluginCmdLine", self.rpcPluginCmdLine)
        self.parentFrame.GetPlugin("RavenRPC").addLocalVarInShell( self.rpcPluginCmdLine, "ipfs")
        print("DONE !")
        
    
    """
    
    Plugins setting management
    
    Note, this method must be overwritten on plugins that use settings since
    config parser only use STRING values.
    
    
    """
    
    #
    # Seems not mandatory with new LoadSetting Generic function but in case of specific
    # Types, better redeclare it!
    #
    
    """
    def _LoadPluginSettings(self):
        _recordedSettings = self.parentFrame.Settings._GetPluginSettings(self.PLUGIN_NAME)
        
        
        for key in _recordedSettings:
            
            
            #
            # _recordedSettings[key] Return string only, do your own mapping for complex datastructure
            #
            self.PLUGIN_SETTINGS[key] = _recordedSettings[key]
            
            
    """        
                
        
    '''
    
    Plugin Triggers / Callbacks for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
     
    '''
        
        
    def DoTestRPC(self):
        _rpc_ip = self.PLUGIN_SETTINGS['ipfs_rpc_api_ip']
        _ipfs_direct_api_ip = self.PLUGIN_SETTINGS['ipfs_direct_api_ip']
        ipfs_rpc = RVNpyIPFS.RavenPyIPFS(ConString=_ipfs_direct_api_ip, rpcServer=_rpc_ip)
        
        status = {'ipfs_rpc':ipfs_rpc.IPFS_RPC_Client, 'ipfs_direct_api_ip':ipfs_rpc.IPFSserverConnexion,}
        return status
        
    
    def UploadJSONToIPFS_RPC(self, json):  
        _hash = None
        if True:
        #try:
            #ipfs_rpc = RVNpyIPFS.RavenPyIPFS(rpcServer="10.0.0.144")
            _rpc_ip = self.PLUGIN_SETTINGS['ipfs_rpc_api_ip']
            _ipfs_direct_api_ip = self.PLUGIN_SETTINGS['ipfs_direct_api_ip']
            ipfs_rpc = RVNpyIPFS.RavenPyIPFS(ConString=_ipfs_direct_api_ip, rpcServer=_rpc_ip)
            
            
            _hash = ipfs_rpc.UploadP2PMarketAd(json)
            
            print(f"UploadJSONToIPFS_RPC = {_hash}")
            """
            if _hash != None:
                self.__setHashResult__(filename,_hash)
            else:
                self.__setHashResult__(filename,None)
                
            wx.CallAfter(self.UpdateActiveViews, ())
            """
        #except Exception as e:
            #self.RaisePluginLog( "Unable to upload JSON File :"+ str(e), type="error")
            #self.__setHashResult__(filename,None)  
        return _hash
    
    def UploadFileToIPFS_RPC(self, filename):
        t=threading.Thread(target=self.__DoUpload_T__, args=(filename,))
        t.start()
    
    
    def OpenIPFSUploadDialog(self):
        #_newView = self.LoadView(self.SearchPluginView("IPFS File Uploader"), "dialog")
        _newView = self.parentFrame.Views.OpenView("IPFS File Uploader", "IPFS", True)
        if _newView != None:
            _newView.Show()
        #_newView = self.parentFrame.Views.OpenView("IPFS File Uploader", "IFPS", True)
        #if txdatas!="":
        #    _newView.SetTxId(txdatas)
    
    
    
    def __getHashResult__(self, filename):
        _list = self.getData("_uploadedFiles")
        _hashResult = -1
        
        if _list.__contains__(filename):
            _hashResult = _list[filename]
            
            
        return _hashResult
        
    
    def __setHashResult__(self, filename, _hash): 
        _list = self.getData("_uploadedFiles")
        _list[filename] = _hash
        self.setData("_uploadedFiles", _list)
    
    
     
    def __DoUpload_T__(self, filename):
         
        try:
            #ipfs_rpc = RVNpyIPFS.RavenPyIPFS(rpcServer="10.0.0.144")
            _rpc_ip = self.PLUGIN_SETTINGS['ipfs_rpc_api_ip']
            ipfs_rpc = RVNpyIPFS.RavenPyIPFS(rpcServer=_rpc_ip)
            _hash = ipfs_rpc.UploadFile(filename)
            
            print(f"_hash __DoUpload_T__ = {_hash}")
            if _hash != None:
                self.__setHashResult__(filename,_hash)
            else:
                self.__setHashResult__(filename,None)
                
            wx.CallAfter(self.UpdateActiveViews, ())
            
        except Exception as e:
            self.RaisePluginLog( "Unable to upload IPFS File :"+ str(e), type="error")
            self.__setHashResult__(filename,None)
           
        
    def OnNetworkChanged_T(self, networkName=""):    
        t=threading.Thread(target=self.OnNetworkChanged)
        t.start()
        
        
    def OnNetworkChanged(self):
        
        #self.setData("myPluginData", {})
        #self.setData("myPluginData2", False)
        
        try:
            
            """
            myPluginData = self.parentFrame.ConnexionManager.getAllConnexions()
            myPluginData2 = self.parentFrame.ConnexionManager.getCurrent()
            
            
            self.setData("myPluginData", myPluginData)
            self.setData("myPluginData2", myPluginData2)
            """
            #When datas are loaded, add a call after to trigger plugins view update
            wx.CallAfter(self.UpdateActiveViews, ())
            
        except Exception as e:
            self.RaisePluginLog( "Unable to retreive connexion informations :"+ str(e), type="error")
            
            
       
        
        