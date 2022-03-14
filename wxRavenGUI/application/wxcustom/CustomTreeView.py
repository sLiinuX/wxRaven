'''
Created on 19 déc. 2021

@author: slinux
'''

import wx


class wxRavenTreeView(object):
    '''
    classdocs
    '''

    _imagesListReference = {}
    _currentItem = None
    _currentText = None
    _currentData = None
    
    _tree = None
    
    
    _treeChangeCB = None

    def __init__(self, _treeObj, _icons={}, _fillTreeCallback=None, _onChangeCallback=None):
        '''
        Constructor
        '''
        
        
        self._imagesListReference = {}
        self._tree =_treeObj
        
        if _icons != {}:
            self.setupImageList(_icons)
            
        
        
        
        self._tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self._tree)
        if _onChangeCallback!= None:
            self._treeChangeCB = _onChangeCallback
        
            
        if _fillTreeCallback != None:
            _fillTreeCallback()
        
        
        
    def setupImageList(self, _icons):
        
        isz = (16,16)
        self.il = wx.ImageList(isz[0], isz[1])
        
        for _i in _icons:
            _iBitmap = _icons[_i]
            
            _newId  = self.il.Add(_iBitmap)
            self._imagesListReference[_i] = _newId
            
        self._tree.SetImageList(self.il)
        
    def addImage(self,_name, _image):
        if not self._imagesListReference.__contains__(_name):
            _viewIconIdx     = self.il.Add(_image)
            self._imagesListReference[_name] = _viewIconIdx 
        
    def getImage(self, _name):    
        if self._imagesListReference.__contains__(_name):
            return self._imagesListReference[_name]
        else:
            return None
            
    
    
    def addItem(self, parentItem, text, data, iconname_normal=None, iconname_expanded=None ):
        
        if parentItem!=None:
            _last = self._tree.AppendItem(parentItem, text)
        else:
            self.root = self._tree.AddRoot(text)
            _last= self.root
        
        self._tree.SetItemData(_last, data)

        if iconname_normal != None:
            
            if self._imagesListReference.__contains__(iconname_normal):
                self._tree.SetItemImage(_last, self._imagesListReference[iconname_normal], wx.TreeItemIcon_Normal)
                
                if iconname_expanded == None:
                    iconname_expanded = iconname_normal
        
        
        if iconname_expanded != None :  
            if self._imagesListReference.__contains__(iconname_expanded):   
                self._tree.SetItemImage(_last, self._imagesListReference[iconname_expanded], wx.TreeItemIcon_Selected)
            
        
        return _last
    
    
        
    def OnSelChanged(self, event):
        self._currentItem = event.GetItem()
        #self.openButton.Enable(False)
        if self._currentItem:
            
            self._currentData = self._tree.GetItemData(self._currentItem)
            self._currentText  = self._tree.GetItemText(self._currentItem)
            
            
        if self._treeChangeCB != None:
            self._treeChangeCB(event)
            
        event.Skip()    
        
        
        
        
        
        
        
        
        
        
        