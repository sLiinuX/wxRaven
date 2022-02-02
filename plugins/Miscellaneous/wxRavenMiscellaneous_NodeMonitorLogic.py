'''
Created on 28 janv. 2022

@author: slinux
'''

from .wxRavenMiscellaneousDesign import *
import threading
import time 



class wxRavenMiscellaneous_NodeMonitorLogic(wxRavenMiscellaneous_NodeMonitor):
    '''
    classdocs
    '''


    #
    #
    # Datas for the plugin display style
    #
    #
    
    view_base_name = "Monitoring Panel"
    view_name = "Monitoring Panel"
    parent_frame = None
    default_position = "main"
    icon = 'monitoring_dashboard_2'#wx.Bitmap( u"res/default_style/normal/help_view.png", wx.BITMAP_TYPE_ANY )
    
    
    
    

    def __init__(self, parentFrame, position = "main", viewName= "Monitoring Panel", isInternalPluginView=False):
        '''
        Constructor
        '''
        super().__init__(parent=parentFrame)
        
        
        #
        #    Your constructor here
        #
        
        self.view_base_name = "Monitoring Panel"
        self.view_name = viewName
        self.parent_frame = parentFrame
        self.default_position = position
        
        
        #This is to add the view in the appropriate place using the mainapp to do so
        #
        #The only exception is when the pannel itself is called by the plugin or another view 
        #In this case the position in main app must not be managed (see rpc command panel as example)
        #
        if not isInternalPluginView:
            parentFrame.Add(self, self.view_name ,position, parentFrame.RessourcesProvider.GetImage(self.icon))
            
    
    
    
        #
        # If your app need to load a bunch of data, it may want to wait the app is ready
        # specially at startup + resume of plugins
        # Use this thread method + callback to manage the 1sec/2sec init delay
        #
        #
        self.waitApplicationReady()
    
    
    def waitApplicationReady(self):
        t=threading.Thread(target=self.__waitLoop_T__, args=(self.UpdateView,))
        t.start()
        
        
    def __waitLoop_T__(self,callback):
        while not self.parent_frame._isReady:
            time.sleep(2)
            
        wx.CallAfter(callback, ()) 
    
    
    
    
    def OnTimerTick(self, evt=None):
        print('OnTimerTick')
        self.UpdateView()
         
    
    
    def OnAutoRefreshClicked(self, evt=None):
        _activate = self.m_checkBox2.GetValue()
        
        if _activate:
            if not self.m_timer1.IsRunning():
                self.m_timer1.Start()
                print('OnTimer Started')
        else:
            self.m_timer1.Stop()    
            print('OnTimer Stopped')
    
    
            
    #Override the UpdateView method to define what happen when plugin call UpdateViews()        
    def UpdateView(self, evt=None):
        
        self.UpdateDataFromPluginDatas()
        self.Layout()
            
            
    
    #Example to show how plugin data are retreived
    def UpdateDataFromPluginDatas(self):       
        
        try:
            
            
            ravencoin = self.parent_frame.getRvnRPC()
            
            #myPluginData = self.parent_frame.GetPluginData("Tutorial","myPluginData2")
            #myPluginSetting =  self.parent_frame.GetPluginSetting("Tutorial","booleansetting")#SavePanelSettings GetPluginSetting
            #
            #Update your panel
            #       
            _netinfos = ravencoin.network.GetNetworkInfos()
            #_bcinfos =  ravencoin.network.getblockchaininfo()
            
            
            if _netinfos != None:
                self.m_textCtrl30.SetValue(str(_netinfos['blocks']))
                self.m_textCtrl3011.SetValue(str(_netinfos['difficulty'][2]))
                self.m_textCtrl301.SetValue(str(_netinfos['networkhashps'][2]))
                
                self.m_textCtrl302.SetValue(str(_netinfos['headers']))
                self.m_textCtrl3012.SetValue(str(_netinfos['mempool_size']))
                self.m_textCtrl30121.SetValue(str(_netinfos['mempool_usage_percentage']) + " %" )
                
                '''
                _netInfos['headers'] = _blockInfos['headers']
                _netInfos['mempool_size'] = _mempoolInfos['size']
                _netInfos['mempool_usage'] = _mempoolInfos['usage']
                _netInfos['mempool_max'] = _mempoolInfos['maxmempool']
                
                _netInfos['mempool_usage_percentage'] = _retval
                _netInfos['mempool_usage_ratio'] = _ratio
                '''
            #textToPrint = " booleansetting = " + str(myPluginSetting)
            #textToPrint = textToPrint + "\n\n myPluginData2 = " + str(myPluginData)
             
            #self.m_staticText2.SetLabel(str(textToPrint)) 
             
                
        except Exception as e:
            self.parent_frame.Log("Unable to load network infos datas : " + str(e) , type="warning")
                    
            
            
            