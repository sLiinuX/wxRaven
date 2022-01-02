'''
Created on 19 déc. 2021

@author: slinux
'''
import os 
import wx
from pathlib import Path

class RessourcesProvider(object):
    '''
    classdocs
    '''

    _rootPath = ""
    _resMainTheme = "default_style"
    
    _resFullPath = ""
    
    enable_list = {}
    disable_list = {}
    
    
    _THEME_PANEL_BACKGROUND_COLOR = wx.Colour( 255, 255, 255 )
    
    
    
    def __init__(self, path="", theme="default_style" ):
        '''
        Constructor
        '''
        
        
        
        self.enable_list = {}
        self.disable_list = {}
        
        if path == "":
            path = os.getcwd() + ""
        
        self._rootPath = path
        self._resMainTheme = theme
        
        
        #todo, check if theme exist and manage error case
        self._resFullPath = path +"/"+ self._resMainTheme + "/"
        
        
        self.LoadRessources()
    
    
    
    
    

    """
    
    Loader
    
    """
    
        
    
    def LoadRessources(self):
        _normalRessourcePath = self._resFullPath  + "normal/"
        
        print("Load ressources in : " + _normalRessourcePath)
        
        self.LoadPNGRessourcesFromPath(_normalRessourcePath)

    
        
    def LoadPNGRessourcesFromPath(self, directory):

        for filename in os.listdir(directory):
            if filename.endswith(".png"):
                #print(os.path.join(directory, filename))
                self.LoadPNGRessourceFile(os.path.join(directory, filename))
            else:
                continue
    
    def LoadPNGRessourceFile(self, _filefullname):
        
        try:
            _newRes = wx.Bitmap( _filefullname, wx.BITMAP_TYPE_ANY )
            _key = Path(_filefullname).stem
            self.enable_list[_key] = _newRes
        except Exception as e:
            print("ressource error :" + str(e))
            
            
            
    """
    
    Getters
    
    """
    
    
    def GetImage(self, _key, normal=True):
        
        #a default picture in case
        _img = wx.Bitmap( u"res/default_style/normal/ressource_picture.png", wx.BITMAP_TYPE_ANY )
        
        
        _catalog = self.enable_list
        if not normal :
            _catalog = self.disable_list
        
        if _catalog.__contains__(_key):
            _img= _catalog[_key]
            
        return _img
            
        
        
    def GetPanelBackground(self):
        return self._THEME_PANEL_BACKGROUND_COLOR    
        
        
    def ApplyThemeOnPanel(self, panel):  
        try:  
            panel.SetBackgroundColour(self.GetPanelBackground())
            #panel.SetForegroundColour(self.GetPanelBackground())
        except Exception as e:
            print("unable to themize :" + str(e))
        
        