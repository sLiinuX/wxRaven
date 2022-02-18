

'''
Created on 10 déc. 2021

@author: slinux
'''

import threading
from .wxRavenShellLogic import *
from wxRavenGUI.application.pluginsframework import *
import datetime

import re

from .wxRaven_CodeEditorLogic import *
from .pluginSettings import wxRavenRPCPluginSettings


from .wxRaven_CodeEditor_FileObj import wxRaven_CodeEditor_File
from .wxRaven_CodeFileBrowserLogic import *
from plugins.RavenRPC import wxRaven_CodeEditor_FileObj

import shutil


class wxRavenPlugin(PluginObject):
    
    

    
    
    
    def __init__(self, parentFrame, position="mgr"):
        PluginObject.__init__(self, parentFrame, position=position)
        
        
        self.PLUGIN_NAME = "RavenRPC"
        self.PLUGIN_ICON = self.RessourcesProvider.GetImage('shell') 
        self.PLUGINS_VIEWS= [ 
                    {
                     'viewid':'RavenRPC Shell', 
                     'name':'RavenRPC Shell', 
                     'title':'RavenRPC Shell', 
                     'position':position, 
                     'icon':self.PLUGIN_ICON, 
                     'class': shellMainPanel ,
                     'default':False,
                     'multipleViewAllowed':True
                     },
                    
                     {
                     'viewid':'RavenRPC Advanced Shell', 
                     'name':'RavenRPC Advanced Shell', 
                     'title':'RavenRPC Advanced Shell', 
                     'position':position, 
                     'icon':wx.Bitmap( u"res/default_style/normal/shell_adv.png", wx.BITMAP_TYPE_ANY ), 
                     'class': shellAdvancedPanel ,
                     'default':False,
                     'multipleViewAllowed':True
                     },
                    
                     {
                     'viewid':'RPC Documentation Helper', 
                     'name':'RPC Documentation Helper', 
                     'title':'RPC Documentation Helper', 
                     'position':'main', 
                     'icon':wx.Bitmap( u"res/default_style/normal/bookmarks_view.png", wx.BITMAP_TYPE_ANY ), 
                     'class': ShellDocumentationHelper ,
                     'default':False,
                     'multipleViewAllowed':True
                     }
                    
                    ,
                    
                     {
                     'viewid':'Code Editor', 
                     'name':'Code Editor', 
                     'title':'Code Editor', 
                     'position':'main', 
                     'icon':wx.Bitmap( u"res/default_style/normal/python_editor.png", wx.BITMAP_TYPE_ANY ), 
                     'class': wxRavenRavenRPC_CodeEditorLogic ,
                     'default':False,
                     'multipleViewAllowed':False
                     }
                     
                     ,
                    
                     {
                     'viewid':'Source Code Browser', 
                     'name':'Source Code Browser', 
                     'title':'Source Code Browser', 
                     'position':'main', 
                     'icon':wx.Bitmap( u"res/default_style/normal/folder_python_browser.png", wx.BITMAP_TYPE_ANY ), 
                     'class': wxRaven_General_CodeBrowserLogic ,
                     'default':False,
                     'multipleViewAllowed':False
                     }
                    
                    
                    
                ]
        
        
        """
        ShellDocumentationHelper
        
        self.setData("all_connexion", [])
        self.setData("current_connexion", '')
        self.setData("_icon", wx.Bitmap( u"res/default_style/normal/network.png", wx.BITMAP_TYPE_ANY ))
        self.setData("_dataTimeStamp", '')
        """
        
        
        #
        # Lets put some setting pannels from pluginsetting file (to define as well)
        #
        self.PLUGIN_SETTINGS_GUI = []
        
        _Icon = self.RessourcesProvider.GetImage('shell')
        _setPanel = PluginSettingsTreeObject("RavenRPC", _Icon, classPanel=wxRavenRPCPluginSettings, _childs=None)
        self.PLUGIN_SETTINGS_GUI.append(_setPanel)
       
        self.setData("_icon", self.RessourcesProvider.GetImage('network') )
        
        self.setData("_CmdList", {})
        self.setData("_CmdListInCache", False)
        
        self.setData("_ShellLocalsAddins", {})
        
        
        
        
        self._codeEditorPath = self.parentFrame.GetPath('USERDATA')+'CodeEditor/'
        if not os.path.exists(self._codeEditorPath):
            os.makedirs(self._codeEditorPath)
        self._backupFolderFiles = self._codeEditorPath+'Backups/'
        if not os.path.exists(self._backupFolderFiles):
            os.makedirs(self._backupFolderFiles)
        
        #files in instance in the format {name:path}
        self.setData("code_editor_filelist", {})
        self.setData("code_editor_new_count", 1)
        self.setData("code_editor_file_open", '')
        
        self.setData("code_editor_user_folder", self._codeEditorPath)
        self.setData("code_editor_backup_folder", self._backupFolderFiles)
        
        
        
        
        
        self.ALLOW_MULTIPLE_VIEWS_INSTANCE = True
        self.parentFrame.ConnexionManager.RegisterOnConnexionChanged(self.OnNetworkChanged_T)
        #self.LoadPluginFrames()
        
        #self.LoadView(self.PLUGINS_VIEWS[1], 'mgr')
        
        #self.demoTest()
        
        #For test purpose
        self.waitApplicationReady()
    
    #
    # Run a thread and wait app to be fully loaded
    #
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.__applicationReady__,))
        t.start()
        
    #
    #  thread to wait
    #    
    def __waitLoop_T__(self,callback):
        while not self.parentFrame._isReady:
            time.sleep(1)
            
        wx.CallAfter(callback, ()) 
        
        
        #self.initializeAssetManagerBackgroundService()
    
    #
    #  thread callback
    #
    def __applicationReady__(self, evt=None):
        self.OnNetworkChanged_T()
    
    
    def demoTest(self):   
        self.LoadView(self.PLUGINS_VIEWS[0], 'mgr')
        self.LoadView(self.PLUGINS_VIEWS[0], 'mgr')
        self.LoadView(self.PLUGINS_VIEWS[0], 'mgr')
        self.LoadView(self.PLUGINS_VIEWS[0], 'mgr')
        self.LoadView(self.PLUGINS_VIEWS[0], 'main')
        self.LoadView(self.PLUGINS_VIEWS[0], 'toolbox1')
        self.LoadView(self.PLUGINS_VIEWS[0], 'toolbox2')
        self.LoadView(self.PLUGINS_VIEWS[0], 'toolbox2')
        self.LoadView(self.PLUGINS_VIEWS[0], 'toolbox3')
        
        #self.LoadView(self.PLUGINS_VIEWS[0])
        #self.LoadView(self.PLUGINS_VIEWS[0])
        
    
    
    
    
    
    
    #
    # Code editor functions
    #
    
    def OpenCodeEditor(self, filename=''):
        self.setData("code_editor_file_open", filename)
        _newView = self.parentFrame.Views.OpenView("Code Editor", "RavenRPC", open)
        
        print(_newView)
        if _newView == None:
            _vi = self.parentFrame.Views.SearchViewInstance("Code Editor")
            _newView = _vi
            
            
        if filename!= '':
            self.logger.info(f'LoadFileCodePagePanel : {filename}')
            _newView['instance'].LoadFileCodePagePanel(filename)
            
            
        return _newView['instance']
    
    
        
    
    
    def CodeEditor_NewFile(self, editor=None):
        
        
        
        _currentList = self.getData("code_editor_filelist")
        _currentIndex = self.getData("code_editor_new_count")
        
        _newfilename = f'new {_currentIndex}'
        _currentIndex = _currentIndex+1
        self.setData("code_editor_new_count", _currentIndex)
        
        _newfile = wxRaven_CodeEditor_File(filename=_newfilename, _isnew=True, _editor=editor)
        
        _currentList[_newfilename] = _newfile
        self.setData("code_editor_filelist", _currentList)
        
        self.logger.info(f'New file created in Code Editor : {_newfilename}')
        
        return _newfile
        
        
    
    
    def GetOpenFile(self, filename ):
        _currentList = self.getData("code_editor_filelist")
        self.logger.info(f'Searching in openned Code Editor files : {filename}')
        self.logger.info(f'Cachelist : {_currentList}')
        if _currentList.__contains__(filename):
            return _currentList[filename]
        else :
            return None
        
    
        
    
    
    def CodeEditor_OpenFile(self, filename,editor=None):
        
        head, tail = os.path.split(filename)
        _exist = self.GetOpenFile(tail)
        _filetoload=None
        if _exist != None:
            _filetoload= _exist
        
        else:
            _filetoload = wxRaven_CodeEditor_File(filename=filename, _isnew=False, _editor=editor)
            _currentList = self.getData("code_editor_filelist")
            
            _currentList[_filetoload._name] = _filetoload
            self.setData("code_editor_filelist", _currentList)
            
        self.logger.info(f'New file opened in Code Editor : {filename}')    
            
        return _filetoload
    
    
    
    
    def CodeEditor_OpenCodeEditor(self, filename=''):
        ce = self.OpenCodeEditor(filename)    
        #ce.LoadFileCodePagePanel(filename)
    
    
    def __UpdateFileObj_Editor__(self, fileobj:wxRaven_CodeEditor_File):
        self.logger.info(f'Code Editor update : {fileobj._name}')    
        _currentList = self.getData("code_editor_filelist")
        _currentList[fileobj._name] = fileobj
        self.setData("code_editor_filelist", _currentList)
    
    
    
    def CodeEditor_SaveFile(self, filename,method='Save', _dobackup=False):
        _f:wxRaven_CodeEditor_File
        _f = self.GetOpenFile(filename)
        if _f == None:
            head, tail = os.path.split(filename)
            _f = self.GetOpenFile(tail)
            
        if _f !=None:
            
            if _dobackup and not _f._new:
                shutil.copy2(_f._filepath, self._backupFolderFiles + _f._name + '.backup') 
            
            
            _savePath = _f._filepath
            head, tail = os.path.split(_savePath)
            if method == 'SaveAs':
                wildcard = "Python source (*.py)|*.py|"     \
                   "All files (*.*)|*.*"
        
        
                dlg = wx.FileDialog(
                    self, message="Choose a file",
                    defaultDir=head,
                    defaultFile=tail,
                    wildcard=wildcard,
                    style=wx.FD_SAVE  |   wx.FD_PREVIEW   )
        
                # Show the dialog and retrieve the user response. If it is the OK response,
                # process the data.
                if dlg.ShowModal() == wx.ID_OK:
                    _savePath = dlg.GetPath() 
                else:
                    print('canceled by user..')
                    _savePath = None
                    
            
            if _savePath != None:
                _f._editor.SaveFile(_savePath)
                
                
                self.RaisePluginLog(f"{_savePath} Saved", 'info')
    
    def CodeEditor_PushToGit(self, filename):
        pass
    
    
    def CodeEditor_FetchLocal(self, filename):
        pass
    
    
    
    """
     allow other plugins to add some locals var , warning this is dangerous !
    """
    
    #self.parent_frame.GetPlugin("RavenRPC").addLocalVarInShell( _data, _dataName)
    def addLocalVarInShell(self, _data, _dataName):
        
        _added=False
        _ShellLocalsAddins = self.getData("_ShellLocalsAddins")
        
        
        if not _ShellLocalsAddins.__contains__(_dataName):
        
            _ShellLocalsAddins[_dataName] = _data
            _added=True
        
        
        self.setData("_ShellLocalsAddins", _ShellLocalsAddins)
    
    
    def removeLocalVarInShell(self, _dataName):
        
        _added=False
        _ShellLocalsAddins = self.getData("_ShellLocalsAddins")
        
        
        if not _ShellLocalsAddins.__contains__(_dataName):
        
            _ShellLocalsAddins[_dataName] = None
            _added=True
        
        
        self.setData("_ShellLocalsAddins", _ShellLocalsAddins)
    
    
    def getAddinsLocals(self):
        _ShellLocalsAddins = self.getData("_ShellLocalsAddins")
        _addinsLocals= {}
        for key in _ShellLocalsAddins:
            
            _data = _ShellLocalsAddins[key]
            
            if _data != None:
                _addinsLocals[key] = _data
    
        return _addinsLocals
    '''
    
    Plugin Triggers for data update , DO NOT CALL WX UPDATE OUT OUF wx.CallAfter(cb, param)
    '''
        
            
        
    def OnNetworkChanged_T(self, networkName=""):    
        
        if not self.parentFrame._isReady:
            return None 
        
        t=threading.Thread(target=self.OnNetworkChanged)
        t.start()
        
        
    def OnNetworkChanged(self):
        
        self.setData("all_connexion", [])
        self.setData("current_connexion", '')
        self.setData("_icon", self.RessourcesProvider.GetImage('network') )
        self.setData("_dataTimeStamp", '')
        
        try:
            _data_all_connexion = self.parentFrame.ConnexionManager.getAllConnexions()
            _data_current_connexion = self.parentFrame.ConnexionManager.getCurrent()
            
            _icon = self.parentFrame.ConnexionManager.getIcon(_data_current_connexion)
            _dataTimeStamp = datetime.datetime.now()
            
            
            self.setData("all_connexion", _data_all_connexion)
            self.setData("current_connexion", _data_current_connexion)
            self.setData("_icon", _icon)
            self.setData("_dataTimeStamp", _dataTimeStamp)
            
            
            if self.getData("_CmdListInCache") == False:
                self.LoadRPCCommandsCache()
            
            wx.CallAfter(self.UpdateActiveViews, ())
            
        except Exception as e:
            self.RaisePluginLog( "Unable to retreive connexion informations :"+ str(e), type="error")
            #print(self.PLUGIN_NAME + " > OnNetworkChanged " + str(e))
            
            
    
    def LoadRPCCommandsCache(self):
        
        _CmdListInCache = False
        _CmdList = {}
        
        
        
        try:
            _globalHelp = self.parentFrame.getNetwork().help()['result']
            _allCommands = re.findall('[\n]([\S]*)',_globalHelp)
            
            
            for _cmd in _allCommands:
                
                if _cmd == "" or _cmd== "==":
                    continue
                try:
                    _cmdDesc = self.parentFrame.getNetwork().help(_cmd)['result']
                    _CmdList[_cmd] = _cmdDesc
                except Exception as e:
                    pass
                    #print(self.PLUGIN_NAME + " > error in command '"+_cmd+"' : "+ str(e))
        
        
            self.setData("_CmdList", _CmdList) 
            self.setData("_CmdListInCache", True) 
        
        except Exception as e:
            
            self.RaisePluginLog( "Unable to load RPC Commands list in cache", type="error")
            #print(self.PLUGIN_NAME + " > LoadRPCCommandsCache " + str(e))
        