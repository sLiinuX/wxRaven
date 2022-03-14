'''
Created on 16 févr. 2022

@author: slinux
'''


import logging

from .CodeEditorEngine import *

from .wxRavenShellDesign import *
import threading
import time 

from wxRavenGUI.application.wxcustom import *
import wx.lib.mixins.listctrl as listmix 

from datetime import date
import datetime


from plugins.RavenRPC.wxRaven_CodeEditor_FileObj import *



class wxRavenRavenRPC_CodeEditorLogic(wxRaven_General_CodeEditor):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Code Editor"
    view_name = "Code Editor"
    parent_frame = None
    default_position = "main"
    icon = 'python_editor'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, position = "main", viewName= "Code Editor", isInternalPluginView=False,):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Code Editor"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self._allTabs= {}
        self._allIcons= {}
        self._defaultIcon = 'code_codeeditor_file'
        self.logger = logging.getLogger('wxRaven')
        self.SetupIconsList()
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
        
        #self.LoadSearchOptions()
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
    
    
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.waitApplicationReady()
    
    
    def SetupIconsList(self):
        self._allIcons['py'] = 'code_python_file'
        self._allIcons['pyc'] = 'code_python_custom_file'
        self._allIcons['wxr'] = 'code_python_custom_file'
    
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.setupPanels,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
    
     
    
    def setupPanels(self, evt=None):
        
        plugin = self.parent_frame.GetPlugin('RavenRPC')
        _f = plugin.getData("code_editor_file_open")
        
        if _f != None:
            if _f != '':
                self.LoadFileCodePagePanel(_f) 
            else:
                self.createEmptyCodePagePanel()
        else:
            self.createEmptyCodePagePanel()
            
        #self.createTxHistoryPanel()
        
        #self.createAddinsPanels()
        
    
     
    def createEmptyCodePagePanel(self, evt=None):
        _codePanel = wxRavenRavenRPC_CodeEditorPageTabLogic(self, self.parent_frame, isInternalPluginView=True)
        _icon = self.parent_frame.RessourcesProvider.GetImage(self._defaultIcon)
        self.m_CodeEditorTab.AddPage(_codePanel, _codePanel.fileobj._name, bitmap = _icon)
        self._allTabs[_codePanel.fileobj._name] = _codePanel
        self.ShowPage(_codePanel.fileobj._name)
        self.Layout()
        
        
    def LoadFileCodePagePanel(self, filepath):
        #
        #to check if already open
        #
        self.logger.info(f'LoadFileCodePagePanel {filepath}')
        plugin = self.parent_frame.GetPlugin('RavenRPC')
        fileobj = plugin.CodeEditor_OpenFile(filepath)
        
        
        
        if not self._allTabs.__contains__(fileobj._name):
            self.logger.info(f'NEW PANEL {filepath}  : {filepath.split(".")[1]}')
            
            _iconImg = self._defaultIcon
            if self._allIcons.__contains__(filepath.split('.')[1]):
                _iconImg = self._allIcons[filepath.split('.')[1]]
            
            
            _codePanel = wxRavenRavenRPC_CodeEditorPageTabLogic(self, self.parent_frame, isInternalPluginView=True, fileobj=fileobj)
            _icon = self.parent_frame.RessourcesProvider.GetImage(_iconImg)
            self.m_CodeEditorTab.AddPage(_codePanel, _codePanel.fileobj._name, bitmap = _icon)
            self._allTabs[_codePanel.fileobj._name] = _codePanel
            self.Layout()
        
        self.ShowPage(fileobj._name)
            
    
    
    def ShowPage(self, pagename):
        if self._allTabs.__contains__(pagename):
            index= self.m_CodeEditorTab.GetPageIndex(self._allTabs[pagename])
            if index != wx.NOT_FOUND:
                self.m_CodeEditorTab.SetSelection(index)
            else:
                self.logger.info(f'PAGE NOT FOUND {pagename}')
        else:
            self.logger.info(f'PAGE NOT FOUND {pagename}')
        
        
    def OnNewPageClicked(self, evt):
        self.createEmptyCodePagePanel()
        
        
        
    def OnOpenPageClicked(self, evt):
        wildcard = "Python source (*.py)|*.py|"     \
           "All files (*.*)|*.*"


        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST |   wx.FD_PREVIEW   )

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            paths = dlg.GetPath()   
            self.LoadFileCodePagePanel(paths)
            
            #plugin = self.parent_frame.GetPlugin('RavenRPC')
            #if plugin != None:
            #    plugin.CodeEditor_OpenFile(paths, )
    
    
    
    def OnSavePageClicked(self, evt=None):
        _page: wxRavenRavenRPC_CodeEditorPageTabLogic
        _page = self.m_CodeEditorTab.GetPage(evt.GetSelection())
        _save = UserUnsavedFileMessage(self.parent_frame, _page.fileobj._name , _page.fileobj._filepath)
        print(_save)
                
        if not _save['result_method'] == 'Cancel' :
            ravencorep = self.parent_frame.GetPlugin("RavenRPC")
            ravencorep.CodeEditor_SaveFile( filename=_page.fileobj._name,method=_save['result_method'], _dobackup=_save['result_backup'])
                
                
    
    
    
    def OnPageClose(self, evt):
        #IsModified
        #print(evt)
        #print(evt.GetId())
        #print(evt.GetSelection())
        #print(self.m_CodeEditorTab.GetCurrentPage())

        _page: wxRavenRavenRPC_CodeEditorPageTabLogic
        _page = self.m_CodeEditorTab.GetPage(evt.GetSelection())
        #print(_page)
        
        if _page != None:
            if _page.isModified() :
                _save = UserUnsavedFileMessage(self.parent_frame, _page.fileobj._name , _page.fileobj._filepath)
                print(_save)
                
                if not _save['result_method'] == 'Cancel' :
                    ravencorep = self.parent_frame.GetPlugin("RavenRPC")
                    ravencorep.CodeEditor_SaveFile( filename=_page.fileobj._name,method=_save['result_method'], _dobackup=_save['result_backup'])
                
                
        self._allTabs.pop(_page.fileobj._name)
    
    def OnPageChanged(self, evt):
        pass
        
    '''
    def createAddinsPanels(self, evt=None):
        ravencorep = self.parent_frame.GetPlugin("open_log")
        _adds_callbacks = ravencorep.getData("_utxo_manager_views_addons_callbacks") 
        
        
        for cb in _adds_callbacks:
            try:
                cb()
            except Exception as e:
                self.parent_frame.Log("Unable to load code addins tab: " + str(e) , type="warning")
                
                
    '''        
    
    def createNewPluginPanel(self, panelName, panelClass, pannelIcon):    
        
        if not self._allTabs.__contains__(panelName):
            _Panel = panelClass(self, self.parent_frame, isInternalPluginView=True)
            _icon = self.parent_frame.RessourcesProvider.GetImage(pannelIcon)
            self.m_CodeEditorTab.AddPage(_Panel, panelName, bitmap = _icon)
            self._allTabs[panelName] = _Panel
        
        
        self.Layout() 
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        
        self.UpdateDataFromPluginDatas()
        self.Layout()
            
            
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        if True:
        #try:
            
            
            for t in self._allTabs:
                
                if True:
                #try:
                    self._allTabs[t].UpdateView()
                #except Exception as e:
                #    self.parent_frame.Log("Unable to UpdateView for tab : " + str(t) , type="warning")   
            #ravencoin = self.parent_frame.getRvnRPC()
            

            





class wxRavenRavenRPC_CodeEditorPageTabLogic(wxRaven_General_CodePage):

    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Code Page"
    view_name = "Code Page"
    parent_frame = None
    default_position = "main"
    icon = 'open_log'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self,parent,  parentFrame, position = "main", viewName= "Code Page", isInternalPluginView=False, fileobj:wxRaven_CodeEditor_File=None):
        '''
        Constructor
        '''
        super().__init__(parent=parent)
        
        
        #
        #    Your constructor here
        #
        self.parent=parent
        self.view_base_name = "Code Page"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self.allIcons  = {}
        self.fileobj = fileobj
        
        

        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
        
        #self.LoadSearchOptions()
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        
        self.editorConfigurator=PythonSTC(self.m_codeEditorText)
        self.editorConfigurator.SetUpEditor()
        
        if self.fileobj == None:
            self.fileobj = self.parent_frame.GetPlugin('RavenRPC').CodeEditor_NewFile()
        else:
            self.m_codeEditorText.LoadFile(self.fileobj._filepath )
        
        
        self.fileobj._editor = self.m_codeEditorText
        p = self.parent_frame.GetPlugin('RavenRPC')
        p.__UpdateFileObj_Editor__(self.fileobj) 
        #else:
            
        '''
        
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.m_listCtrl1)
        self.m_listCtrl1.Bind(wx.EVT_RIGHT_UP, self.OnRightClick)
        self.m_listCtrl1.Bind(wx.EVT_COMMAND_RIGHT_CLICK, self.OnRightClick)
        
        
        
        self.m_addressFilterText.Bind(wx.EVT_TEXT, self.UpdateView)
        '''
        
        #self.waitApplicationReady()
    
    '''
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.AppReady,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 

    def AppReady(self, evt=None):
        if self.fileobj == None:
            self.fileobj = self.parent_frame.GetPlugin('RavenRPC').CodeEditor_NewFile()

    '''
    def UpdateView(self, evt=None):
        
        self.UpdateDataFromPluginDatas()
        self.Layout()  
            
   
    def isModified(self):
        return self.m_codeEditorText.IsModified()
   
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):  
        pass

    
    
    
    
    
    
    
    

