'''
Created on 11 févr. 2022

@author: slinux
'''

import wx 


from wxRavenGUI.application.wxcustom import *



class RavencoreUTXOHistoryRightclickPopupMenu(object):
    '''
    classdocs
    '''


    def __init__(self, parentBinding, parentFrame, txData={}):
        '''
        Constructor
        '''
        self._menu = wx.Menu()
        
        self.popupIDS = {}
        self.popupMAP = {}
        
        
        self.parentBinding = parentBinding
        self.parent_frame = parentFrame
        
        
        self._data= txData
        #self._Locked = assetData['locked']
        #self._dataNone = False

        
        self.createMenu()
        
        
    
    
   
        
    def createMenu(self):   
        #self.__createItemsIds__()
        self.__createMenuItems__()
        
        
        
        
    def __createMenuItems__(self):
        
        # make a menu
        #menu = wx.Menu()
        self._menu = wx.Menu()
        
        
        #Navigate
        #
        nid = wx.NewId()
        _Navigate = self._menu.Append(nid, "View Tx" )
        _Navigate.SetBitmap(self.parent_frame.RessourcesProvider.GetImage('inspect_file'))
        self.parentBinding.Bind(wx.EVT_MENU, self.menuItemAction_ShowTx, id=nid)
        
        

        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.parentBinding.PopupMenu(self._menu)
        self._menu.Destroy()       
        
        
    def menuItemAction_ShowTx(self, event):
        _data= self._data
        
        
        myplugin = self.parent_frame.GetPlugin('Ravencore')
        myplugin.ShowTxInfos(_data['txid'])
        