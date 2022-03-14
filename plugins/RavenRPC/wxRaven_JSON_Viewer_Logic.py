'''
Created on 6 mars 2022

@author: slinux
'''
from wxRavenGUI.application.wxcustom import *
from .wxRavenShellDesign import wxRaven_General_JSONViewer

import threading
import time
import sys,math
import json

import requests
import libs.pyperclip
import ast


class wxRaven_JSON_ViewerLogic(wxRaven_General_JSONViewer):
    '''
    classdocs
    '''
    view_base_name = "JSON Viewer"
    view_name = "JSON Viewer"
    parent_frame = None
    default_position = "main"
    icon = 'json_file_icon'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, position = "main", viewName= "JSON Viewer", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "JSON Viewer"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        self._allTabs= {
            'URL':self.m_optionpanel_url,
            'File':self.m_optionpanel_file,
            'Jobs':self.m_optionpanel_jobs,
            'RAW':self.m_optionpanel_raw,
            }
        self._currentInput= "URL"
        self._jobCache = {}
        self._currentJson = {}
        #self.imageList = None
        
        _icons = {
            'json':parentFrame.RessourcesProvider.GetImage('json_tree_icon')  ,
            'dict': parentFrame.RessourcesProvider.GetImage('dict_tree_icon'),
            'list': parentFrame.RessourcesProvider.GetImage('list_tree_icon'),
            'str': parentFrame.RessourcesProvider.GetImage('str_tree_icon'),
            'int': parentFrame.RessourcesProvider.GetImage('int_tree_icon'),
            'bool': parentFrame.RessourcesProvider.GetImage('int_tree_icon'),
            'float': parentFrame.RessourcesProvider.GetImage('int_tree_icon'),
            'unknown': parentFrame.RessourcesProvider.GetImage('unknown_tree_icon'),
            'class': parentFrame.RessourcesProvider.GetImage('class_tree_obj')
            #console_view.png
            }
        
        
        self.wxTree = wxRavenTreeView(self.m_treeListCtrl1, _icons, _fillTreeCallback=None, _onChangeCallback=self.onChangeTest)
        
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
        
        #self.LoadSearchOptions()
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(self)
        self.defaultRoot = parentFrame.GetPath('ROOT')
        #self.m_pythonSourceCodeExplorer.SetPath(self.defaultRoot)
        #self.m_pythonSourceCodeExplorer.SetDefaultPath(self.defaultRoot)
        
        #self.m_choice1.Bind(wx.EVT_CHOICE, self.OnInputSourceChanged) 
        #self.m_pythonSourceCodeExplorer.Bind(wx.EVT_DIRCTRL_FILEACTIVATED, self.OnFileClicked)
        
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.waitApplicationReady()
    
    
    def OnClose(self, evt=None):
        pass
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.setupPanel,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
        
        
    def setupPanel(self, evt=None): 
        
        self.OnInputSourceChanged()
    
    
    def __appendElement__(self, elem, parentTree, strType):
        
        
        elem_str = strType
        elem_type = str(type(elem).__name__)
        elem_size = self.convert_size(sys.getsizeof(str(elem)))
        
        
        _icon = self.wxTree.getImage('unknown') 
        
        _matchIcon = self.wxTree.getImage(type(elem).__name__)
        
        if _matchIcon!=None:
            _icon = _matchIcon
            
        if _matchIcon == None and self.__isExplorableObject__(elem):
            _icon = self.wxTree.getImage('class')
        
        
        child = self.wxTree._tree.AppendItem(parentTree, elem_str)
        self.wxTree._tree.SetItemText(child, 1, elem_type)
        self.wxTree._tree.SetItemText(child, 2, elem_size)
        
        self.wxTree._tree.SetItemImage(child, closed=_icon, opened=_icon)
        
        
        return child
        
        
    def __isExplorableObject__(self,objdata):
        _res=True
        
        #if not isinstance(objdata, dict) and not isinstance(objdata, list) :
        #    _res = False
        if isinstance(objdata, int)  :
            _res = False
        if isinstance(objdata, float)  :
            _res = False
        if isinstance(objdata, complex)  :
            _res = False
            
        if isinstance(objdata, str)  :
            _res = False
            
        if isinstance(objdata, tuple)  :
            _res = False
                
        if isinstance(objdata, int)  :
            _res = False
               
        if isinstance(objdata, bool)  :
            _res = False      
            
        
        return _res
    
    
    def __exploreObject__(self, objJson, parent=None):
        
        
        if parent == None:
            parent = self.root
         
        #_icon = self.wxTree.getImage('unknown') 
            
        if isinstance(objJson, dict):
            counter=0
            for _subKey in objJson:
                _subValue = objJson[_subKey]
                #_icon = self.wxTree.getImage('dict') 
                
                if self.__isExplorableObject__(_subValue):
                    child = self.__appendElement__(_subValue, parent, f"{_subKey}")
                    self.__exploreObject__(_subValue, child)
                else:
                    child = self.__appendElement__(_subValue, parent, f'{_subKey}  :  {str(_subValue)}')
                counter = counter+1
                
        elif isinstance(objJson, list):
            counter=0
            for _subValue in objJson:
                
                #_icon = self.wxTree.getImage('list') 
                
                if self.__isExplorableObject__(_subValue):
                    child = self.__appendElement__(_subValue, parent, f"[{counter}]")
                    self.__exploreObject__(_subValue, child)
                else:
                    child = self.__appendElement__(_subValue, parent, f'[{counter}]  :  {str(_subValue)}')
                
                
                counter = counter+1
        
        elif self.__isExplorableObject__(objJson):
            try: 
                objJsonRetry = objJson.__json__()
                self.__exploreObject__(objJsonRetry, parent)
            except Exception as e:
                child =self.__appendElement__(objJson, parent, f"{str(objJson)}")    
            '''
            try: 
                objJsonRetry = objJson.__repr__()
                self.__exploreObject__(objJsonRetry, parent)
            except Exception as e:
                pass
            #__json__
            '''
            
        else:
            child =self.__appendElement__(objJson, parent, f"{str(objJson)}")    
    
    
    
    def onChangeTest(self,evt):    
        toplabel = self.wxTree._currentText 
    
    def UpdateView(self, evt=None):
        #self.root=None
        self.wxTree._tree.DeleteAllItems()
        #DeleteAllItems
        w,h=self.wxTree._tree.GetSize()
        czise = 0.8*w
        self.wxTree._tree.SetColumnWidth(0, czise)
        
        print(czise)
        self.root = self.wxTree._tree.InsertItem(self.wxTree._tree.GetRootItem(), wx.dataview.TLI_FIRST, self._currentInput)
        
        
        
        self.wxTree._tree.SetItemText(self.root, 1, str(type(self._currentJson)))
        self.wxTree._tree.SetItemText(self.root, 2, self.convert_size(sys.getsizeof(str(self._currentJson))))
        
        self.wxTree._tree.SetItemImage(self.root, closed=self.wxTree.getImage('json'), opened=self.wxTree.getImage('json'))
        
        self.__exploreObject__(self._currentJson, None)
        
        
    
    
    def convert_size(self,size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])    
    
    def OnInputSourceChanged(self, evt=None):
        _val= self.m_choice1.GetString(self.m_choice1.GetCurrentSelection()) 
        
        for _k in self._allTabs:
            if _k == _val:
                self._allTabs[_k].Show()    
        
            else:
                self._allTabs[_k].Hide()    
    
        self._currentInput= _val
        self.Layout()
    
    
    
    
    def OnRefreshJobList(self, evt):
        self.__RefreshJobList__(evt)
    
    def __RefreshJobList__(self, evt=None):
        listofJobJson = {}
        
        self.m_choice_job.Clear()
        
        jlist=self.parent_frame.JobManager.GetJobs()
        for _j in jlist:
            
            _jnameStr = _j.getJobFriendlyName()
            _jdatasJson = _j.ExportRemoteJobStatusJson(_withResult=True)
            self.m_choice_job.Append(_jnameStr)
            listofJobJson[_jnameStr]=_jdatasJson    
            
        self._jobCache = listofJobJson
        #return listofJobJson
    
    def OnJobSelected(self,evt=None):
        _val= self.m_choice_job.GetString(self.m_choice_job.GetCurrentSelection()) 
        
        jsondatas = self._jobCache[_val]
        self._currentJson = jsondatas
        
        self.UpdateView(None)
    
    
    
    def OnFileChanged(self, evt=None, forceFile=''):
        print('OnFileChanged')
        self._lastFileName = str(self.m_filePicker1.GetPath())
        
        if forceFile != '':
            self._lastFileName = forceFile
        
        
        self.__LoadTextFile__(self._lastFileName)
        
    
    
    def __LoadTextFile__(self, file):
        print('__LoadTextFile__')
        _excp=False
        #_excp = True
        
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                self._currentJson = data
                self.UpdateView(None)
                
        except Exception as e:
            _excp = True
            #UserError(self.parent_frame, f"Invalid JSON File or Data : {e}")
        
        
        if _excp:   
            try:
                import ast
                f = open(file, "r")
                jsonData = ast.literal_eval(f.read())
                self._currentJson = jsonData
                self.UpdateView(None)
                    
            except Exception as e:
                UserError(self.parent_frame, f"Invalid JSON File or Data : {e}")
            
    
    
    def OnLoadURLClicked(self, evt):
        print('OnLoadURLClicked')
        _url = self.m_textCtrl3.GetValue()
        self.__LoadUrl__(_url)
    
    def __LoadUrl__(self, url):
        try:
            response = requests.get(url)
            data = response.json()
            self._currentJson = data
            self.UpdateView(None)
        #print(data)
        except Exception as e:
            UserError(self.parent_frame, f"Invalid JSON URL or Data : {e}")
    
    
    
    def __LoadRaw__(self, strData):
        print('__LoadTextFile__')
        
        _excp=False
        try:
           
            data = json.loads(strData)
            self._currentJson = data
            self.UpdateView(None)
                
        except Exception as e:
            _excp = True
            #UserError(self.parent_frame, f"Invalid JSON File or Data : {e}")
            
        if _excp:    
            try:
                
                jsonData = ast.literal_eval(strData)
                self._currentJson = jsonData
                self.UpdateView(None)
                    
            except Exception as e:
                UserError(self.parent_frame, f"Invalid JSON File or Data : {e}")
    
    
    def OnRawTextChanged(self,evt=None):
        self.__LoadRaw__(self.m_textCtrl6.GetValue())
    
    
    def OnPasteRawClicked(self, evt):
        
        s = libs.pyperclip.paste()
        
        self.m_textCtrl6.SetValue(s)
    
    
    
    
    
    
    
    