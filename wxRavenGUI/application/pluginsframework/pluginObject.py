'''
Created on 13 déc. 2021

@author: slinux
'''
import wx 
import os
import pickle
import inspect


from ._pluginSettingsTreeObject import *

#
#
# Plugin object to create as basic for your plugin
#

class PluginObject(object):
    '''
    classdocs
    '''
    
    PLUGIN_NAME = "defaultName"
    PLUGIN_ICON = None#wx.Bitmap( u"res/default_style/normal/install-handler.png", wx.BITMAP_TYPE_ANY )
    
    
    CONFIG_PATH = os.getcwd() + "/config/plugins"
    
    
    PLUGINS_VIEWS = []
    
    
    ALLOW_MULTIPLE_VIEWS_INSTANCE = False
    
    
    
    VIEWS_INSTANCES = []
    
    
    PLUGINS_DATAS_CACHE = {}
    
    
    PLUGIN_SETTINGS = {}
    
    
    
    PLUGIN_SETTINGS_GUI = []
    
    
    #parentFrame = None
    position = None

    def __init__(self, parentFrame, position = "mgr"):
        '''
        Constructor
        '''
        self.parentFrame = parentFrame
        self.position = position
        self.PLUGIN_NAME = "defaultName"
        self.PLUGIN_ICON = None
        
        
        
        
        self.RessourcesProvider = parentFrame.RessourcesProvider
        
        
        self.VIEWS_INSTANCES = []
        self.PLUGINS_VIEWS = []
        self.PLUGIN_SETTINGS = {}
        self.ALLOW_MULTIPLE_VIEWS_INSTANCE = False
        self.PLUGINS_DATAS_CACHE = {}
        
        
        self.PLUGIN_SETTINGS_GUI = []
        
        
        
        
       
        
        
        
        
    
    def checkSaveDirectory(self):
        if not os.path.exists(self.CONFIG_PATH):
            os.makedirs(self.CONFIG_PATH)
            
            
    
    def RaisePluginLog(self, message, type="error"):
        try:
            _source = str(inspect.stack()[1][0])
            self.parentFrame.Log( message, source=str(_source), type=type)
        except Exception as e:
            print("RaisePluginLog() " + str(e))  
    
    """
    
    Datas centralized at plugin level to refresh all view in the less queries 
    
    """
    
    def getData(self, varName):
        _data = None
        if self.PLUGINS_DATAS_CACHE.__contains__(varName):
            _data =  self.PLUGINS_DATAS_CACHE[varName]
        return _data
    
    def setData(self, varName, _data):
        self.PLUGINS_DATAS_CACHE[varName] = _data
    
    """
    
    Frames and view stuff
    
    """
    
    
    def UpdateActiveViews(self, args):
        
        
        for r in self.VIEWS_INSTANCES:
            rView = r['instance']
            vName = r['name']
            
            rView.UpdateView()
            
            """
            try:
                rView.UpdateView()
            except Exception as e:
                print(self.PLUGIN_NAME + " > "+vName+" UpdateView() method failed :" + str(e))
            """
    
    def getDefaultFrames(self):
        defaultFrames = [] 
         
        for row in self.PLUGINS_VIEWS:
            isDef = row['default']
            
            if isDef:
                #defaultFrame = row
                defaultFrames.append(row)
            
        return defaultFrames
    
    def getDefaultFrame(self):
        defaultFrame = None 
         
        for row in self.PLUGINS_VIEWS:
            isDef = row['default']
            
            if isDef:
                defaultFrame = row
                break
            
        return row
    
    

    def GetViewIdInstanceCount(self, viewId):
        
        result=0
        
        for row in self.VIEWS_INSTANCES:
            vid = row['viewid']
            
            if vid == viewId:
                result = result+1
    
        return result
    
    
    
    
    def GetViewAttrInstance(self, viewId, attr="viewid"):
        
        result=None
        
        for row in self.VIEWS_INSTANCES:
            vid = row[attr]
            
            if vid == viewId:
                result = row['instance']
    
        return result
    
    def GetViewIdInstance(self, viewId):
        return self.GetViewAttrInstance(viewId)
    
    def GetViewNameInstance(self, viewName):
        return self.GetViewAttrInstance(viewName,  attr="name")
    
    """
    
    Return the view, todo add the check for multiple frames
    
    """
    
    
    
    
    def LoadView(self, view, positionOverride=""):
        
        
        df_class = view['class']
        df_name = view['name']
        df_icon = view['icon']
        
        
        isArea = False
        
        if view.__contains__('isArea'):
            isArea = True
        
        df_position = view['position']
        
        if positionOverride != "":
            #print("override pos to " + positionOverride)
            df_position = positionOverride
        
        
        df_id = -1
        
        if view.__contains__('viewid'):
            df_id = view['viewid'] 
            
            
        exist = self.GetViewIdInstance(df_id)
        id_view = df_name
        
        
        createNew = False
        
        
        if exist == None:     
            
            #print("no existing instance found !")
            
               
            
            createNew = True        
            id_view = df_name   
            
    
        else:
            
            multi_allowed = view['multipleViewAllowed'] 
            
            
            #print("existing instance found ! MultiAllow["+str(multi_allowed)+"]")
            
            
            createNew = multi_allowed
            
            currentCount = self.GetViewIdInstanceCount(df_id)
            newid = currentCount+1
            
            id_view = df_id
            df_name = df_name+'-'+str(newid)
        
        
        
        
        
        
        if createNew:
            
            newview = df_class(self.parentFrame , position=df_position, viewName=df_name )
            
            
            viewInstanceData = {'viewid': id_view, 
                                'name': df_name,
                                'title': df_name,
                                'icon': df_icon,
                                 'instance':newview, 
                                 'position': df_position,
                                 'isArea': isArea}
            self.VIEWS_INSTANCES.append(viewInstanceData)
            
            if isArea:
                self.parentFrame.Views.AddArea(df_name, newview)
            
            #print(self.PLUGIN_NAME+" load+1  " + str(self.VIEWS_INSTANCES) )
            
            wx.CallAfter(self.parentFrame.MenusAndTool.refreshViewsListMenu, ())
        
        else:
            
            self.RaisePluginLog("nothing created.", "warning")
        
        
        
    
    def SearchPluginView(self, viewName, attr="viewid"):
        result = None 
        for row in self.PLUGINS_VIEWS:
            vname = row[attr]
            
            #print(vname + " vs " + viewName)
            
            if viewName == vname:
                result = row
                break
                
        return result
    
    
    def SavePluginFrames(self):
        
        toSaveArray = []
        for r in self.VIEWS_INSTANCES:
            viewInstanceData = {'viewid': r['viewid'],  'name': r['name'],  'position': r['position'],  'isArea': r['isArea']}
            toSaveArray.append(viewInstanceData)
        self.checkSaveDirectory()
        self.__saveVar__(self.PLUGIN_NAME, toSaveArray)
    
    
    
    def LoadPluginFrames(self):
        
        existingDatas = None
        
        
        if self.parentFrame.Settings.resumePluginState:
            existingDatas = self.__LoadVar__(self.PLUGIN_NAME, None)
        
        
        
        
        if existingDatas != None:
            
            #print("PREVIOUS PLUGIN STATE FOUND  : " + str(existingDatas))
            for oldView in existingDatas:
                
                
                v = self.SearchPluginView(oldView['viewid'])
                if v != None:
                    
                    
                    
                    self.LoadView(v, oldView['position'])
      
        
        
        else:
            defaultFrames = self.getDefaultFrames()
            if defaultFrames != None and defaultFrames != []:
                
                for f in defaultFrames:
                
                    self.LoadView(f)
                
    
    
    
    def getIcon(self):
        return self.PLUGIN_ICON

    def getViews(self):
        return self.PLUGINS_VIEWS
    
    
    
    
    
    """
    
    Plugins setting management
    
    Note, this method must be overwritten on plugins that use settings since
    config parser only use STRING values.
    
    
    """
    
    def _LoadPluginSettings(self):
        _recordedSettings = self.parentFrame.Settings._GetPluginSettings(self.PLUGIN_NAME)
        
        
        for key in _recordedSettings:
            self.PLUGIN_SETTINGS[key] = _recordedSettings[key]
            
            #print("" +key + " : " +_recordedSettings[key] )
    
    
    

    
    """
    
    Var Saving management (for the view persistence)
    
    """
    
    def __saveVar__(self, varName, varData):
        try:
            print(""+varName+" : "+str(varData))
            pickle.dump( varData, open(self.CONFIG_PATH+"/" +varName+".p", "wb" ) )
        except Exception as e:
            print(e) 
    
    def __LoadVar__(self, varName, defaultTeturn=None):
        result = defaultTeturn
        try:
            result = pickle.load( open( self.CONFIG_PATH+"/" +varName+".p", "rb" ) )
        except Exception as e:
            print(e) 
        
        return result