'''
Created on 16 févr. 2022

@author: slinux
'''
import os 



class wxRaven_CodeEditor_File(object):
    '''
    classdocs
    '''

    _new = False
    _usaved = False
    _name = ''
    _filepath=''
    _editorInstance = None
    
    def __init__(self, filename='', _isnew=False, _editor=None):
        '''
        Constructor
        '''
        
        if not _isnew:
            self._filepath = filename
            head, tail = os.path.split(filename)
            self._name = tail
            
        else:
            self._name = filename
        self._new = _isnew
        self._editor = _editor
        
        if _editor != None:
            _editor.ClearAll()
            _editor.CreateDocument()
            
            
            if not _isnew:
                _editor.LoadFile(filename )
            
            
            
        
        
        