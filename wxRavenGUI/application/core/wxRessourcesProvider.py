'''
Created on 19 déc. 2021

@author: slinux
'''
import os 
import wx
from pathlib import Path
import logging

class RessourcesProvider(object):
    '''
    classdocs
    '''

    _rootPath = ""
    _resMainTheme = "default_style"
    
    _resFullPath = ""
    
    enable_list = {}
    disable_list = {}
    
    icon_list={}
    icon_conversion_needed = ['error_icon_45','info_icon_45' , 'success_icon_45', 'warning_icon_45', 'ressource_picture']
    
    
    '''
    _THEME_PANEL_BACKGROUND_COLOR = wx.Colour( 255, 255, 255 ) White
    _THEME_PANEL_BACKGROUND_COLOR = wx.Colour( 239, 172, 167 ) Red Std edition
    
    '''
    _THEME_PANEL_BACKGROUND_COLOR = wx.Colour( 255, 255, 255 )
    
    #_THEME_PANEL_SETTINGS_BACKGROUND_COLOR = wx.Colour( 217, 228, 255 )
    _THEME_PANEL_SETTINGS_BACKGROUND_COLOR = wx.Colour( 255, 255, 255 )
    
    
    
    sounds_list = {}
    
    def __init__(self, path="", theme="default_style" ):
        '''
        Constructor
        '''
        
        
        self.sounds_list = {}
        self.enable_list = {}
        self.disable_list = {}
        self.icon_list = {}
        
        if path == "":
            path = os.getcwd() + ""
        
        self._rootPath = path
        
        if theme == '':
            theme = "default_style"
        self._resMainTheme = theme
        
        
        #todo, check if theme exist and manage error case
        self._resFullPath = path +"/"+ theme + "/"
        
        self.logger = logging.getLogger('wxRaven')
        self.LoadRessources()
        self.LoadSounds()
    
    
    
    

    """
    
    Loader
    
    """
    
    
    def CreateEquivalentIcon(self, path, key):
        icon = wx.Icon(path, wx.BITMAP_TYPE_ANY )
        
        self.icon_list[key] = icon
        #self.logger.info(f"CreateEquivalentIcon {icon}: " + key + "")
        return icon
        #self.SetIcon(icon)
        #self.RessourcesProvider.ApplyThemeOnPanel(self)
    
    def LoadSounds(self):
        pass    
    
    def LoadRessources(self):
        
        _normalRessourcePath = self._resFullPath  + "normal/"
        self.logger.info("Load ressources in : " + _normalRessourcePath)
        self.LoadPNGRessourcesFromPath(_normalRessourcePath)

    
        
    def LoadPNGRessourcesFromPath(self, directory):

        for filename in os.listdir(directory):
            if filename.endswith(".png"):
                #self.logger.info(os.path.join(directory, filename))
                self.LoadPNGRessourceFile(os.path.join(directory, filename))
                s = os.path.join(directory, filename)
                
            else:
                continue
    
    def LoadPNGRessourceFile(self, _filefullname):
        
        try:
            _newRes = wx.Bitmap( _filefullname, wx.BITMAP_TYPE_ANY )
            _key = Path(_filefullname).stem
            self.enable_list[_key] = _newRes
            
            if self.icon_conversion_needed.__contains__(_key):
                self.CreateEquivalentIcon(_filefullname, _key)
            
        except Exception as e:
            self.logger.error("ressource error :" + str(e))
            
            
            
    """
    
    Getters
    
    """
    
    
    def GetIcon(self, _key):
        #print('GetIcon')
        #print(self.icon_list)
        #_iconBase = self.icon_list['ressource_picture']
        if self.icon_list.__contains__(_key):
            _iconBase= self.icon_list[_key]
        else:
            
            _iconBase = self.CreateEquivalentIcon(u"res/default_style/normal/"+_key+".png", _key)
            #_iconBase = self.CreateEquivalentIcon(_key)
        
            
        return _iconBase
    
    def GetImage(self, _key, normal=True):
        
        #a default picture in case
        _img = wx.Bitmap( u"res/default_style/normal/ressource_picture.png", wx.BITMAP_TYPE_ANY )
        
        
        _catalog = self.enable_list
        if not normal :
            _catalog = self.disable_list
        
        if _catalog.__contains__(_key):
            _img= _catalog[_key]
            
        return _img
            
    
    
    def GetTopicImage(self, _key):
        return self.GetImage(''+_key.lower())    
    
    
    
        
    def GetPanelBackground(self):
        return self._THEME_PANEL_BACKGROUND_COLOR    
    
    def GetSettingsBackground(self):
        return self._THEME_PANEL_SETTINGS_BACKGROUND_COLOR   
        
        
    def ApplyThemeOnPanel(self, panel):  
        try:  
            panel.SetBackgroundColour(self.GetPanelBackground())
            #panel.SetForegroundColour(self.GetPanelBackground())
        except Exception as e:
            self.logger.error("unable to themize :" + str(e))
            
    
    def ApplyThemeOnSettingsPanel(self, panel):  
        try:  
            #panel.SetBackgroundColour(self.GetSettingsBackground())
            panel._Panel.SetBackgroundColour(self.GetSettingsBackground())
            #panel.SetForegroundColour(self.GetPanelBackground())
        except Exception as e:
            self.logger.error("unable to themize :" + str(e))    
        