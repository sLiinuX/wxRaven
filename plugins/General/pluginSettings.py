'''
Created on 20 déc. 2021

@author: slinux
'''



from .wxRavenGeneralDesign import GeneralSettingPanel, ApplicationSettingPanel

from wxRavenGUI.application.pluginsframework import PluginSettingsPanelObject



import wx

class wxRavenApplicationSettingPanel(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _panel = ApplicationSettingPanel(parent)
        self._parent = parent
        self.parentFrame = parentFrame
        parentFrame.RessourcesProvider.ApplyThemeOnPanel(_panel)
        PluginSettingsPanelObject.__init__(self,_panel, parentFrame, pluginName)
    
        self._Panel = _panel
        self._panel = _panel
        
        
        self._viewMode = 0
        self._defaultArea = "main"
    
        self._Panel.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.OnModeSelectionChange )
        self._Panel.Bind(wx.EVT_CHOICE, self.OnModeDefaultAreaChange, self._panel.defaultAreaChoiceList)
        
        #self._Panel.m_radioBox1.Bind( wx.EVT_RADIOBOX, self.OnChanged )
    
        self.textAdv = """The advanced mode few containers areas which provide additional options in the display :

The Manager place the view at the Top level (same as main and toolbox)
The Manager and Toolbox are Floatable panels.


Closing a view in those area do not completely close the view.
Views and perspective in those areas are resumed at next session.
            """
        self.textSimple = """The simple mode provide only one main areas where all views will be instanciated as a new tab in the notebook.

The main notebook allow simple placement of the different views, 
but doesn't allow to create Floating panels.

Closing a notebook page close completely the view.
Notebook perspective is not saved yet between sessions.
            """
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        if self._viewMode == 0:
            self.parentFrame.Settings.forceinprincipalauimanager = True
        else:
            self.parentFrame.Settings.forceinprincipalauimanager = False
    
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)  
        myPlugin.PLUGIN_SETTINGS['defaultviewarea'] = self._defaultArea
        
        
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        myPlugin = self.parentFrame.GetPlugin(self.pluginName)  
        
        
        
        forceinprincipalauimanager = self.parentFrame.Settings.forceinprincipalauimanager
        """
        if forceinprincipalauimanager :
            
            self._panel.m_radioBox1.SetSelection(0)
            self._panel.descriptionText.SetLabel(self.textSimple)
            self._panel.defaultAreaOptionPanel.Hide()
            
        else:
            self._panel.m_radioBox1.SetSelection(1)
            self._panel.descriptionText.SetLabel(self.textAdv)
            self._panel.defaultAreaOptionPanel.Show()
        """
        
        self._panel.defaultAreaOptionPanel.Layout()
        defaultArea = myPlugin.PLUGIN_SETTINGS['defaultviewarea']
        self._defaultArea = defaultArea
        id  = self._panel.defaultAreaChoiceList.FindString(defaultArea)
        self._panel.defaultAreaChoiceList.SetSelection(id)
        
        
        if not forceinprincipalauimanager:
            self._panel.m_radioBox1.SetSelection(1)
            self.OnModeSelectionChange(evt=None,Override=1 )
        else:
            self._panel.m_radioBox1.SetSelection(0)
            self.OnModeSelectionChange(evt=None,Override=0 )
            
    def OnModeDefaultAreaChange(self, evt):
        self._defaultArea = evt.GetString()
        self.OnChanged(evt)
    
    def OnModeSelectionChange(self, evt=None, Override=-1):
        _newNode= None
        
         
        if Override != -1:
            _newNode = Override
            print("Called override")
        else:
            _newNode = evt.GetInt()
            print("Called normal")
        #print(_newNode)
        self._viewMode = _newNode
        
        
        
        if _newNode == 1:
            
            self._panel.defaultAreaOptionPanel.Show()
            self._panel.descriptionText.SetLabel(self.textAdv)
            self._panel.modeIllustrationBmp.SetBitmap(self.parentFrame.RessourcesProvider.GetImage('app_avanced_mode'))
        else:
            self._panel.modeIllustrationBmp.SetBitmap(self.parentFrame.RessourcesProvider.GetImage('app_simple_mode'))
            self._panel.defaultAreaOptionPanel.Hide()
            #self._panel.m_radioBox1.SetSelection(0)
            self._panel.descriptionText.SetLabel(self.textSimple)
        
        #myPlugin = self.parentFrame.GetPlugin(self.pluginName)
        if Override==-1:
            self.OnChanged(evt)
        #self.Layout()
        #_parent
        self._panel.Layout()  
        self._panel.defaultAreaOptionPanel.Layout()
        self._parent.Layout()  
        #modeIllustrationBmp


class wxRavenGeneralSettingPanel(PluginSettingsPanelObject):
    '''
    classdocs
    '''


    def __init__(self,parent, parentFrame, pluginName):
        
        _panel = GeneralSettingPanel(parent)
        PluginSettingsPanelObject.__init__(self,_panel, parentFrame, pluginName)
    
    
    
    
    
    
    #
    #
    # method to be called on close and apply
    #    
    def SavePanelSettings(self):
        pass
    
    
    #
    #
    # method to be called at first panel creation
    # 
    def LoadPanelSettings(self):
        pass    