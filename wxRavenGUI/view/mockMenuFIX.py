'''
Created on 13 déc. 2021

@author: slinux
'''

import wx

class MockMenu(wx.Menu):
    """
    A custom menu class in which image param can be passed to each Append method
    it also takes care of bug http://trac.wxwidgets.org/ticket/4011
    """

    def __init__(self, *args, **kwargs):
        wx.Menu.__init__(self, *args, **kwargs)
        self._count = 0

    def applyBmp(self, unboundMethod, *args, **kwargs):
        """
        there is a bug in wxPython so that it will not display first item bitmap
        http://trac.wxwidgets.org/ticket/4011
        so we keep track and add a dummy before it and delete it after words
        may not work if menu has only one item
        """

        bmp = None
        if 'image' in kwargs:
            bmp = kwargs['image']

        tempitem = None
        # add temp item so it is first item with bmp 
        if bmp and self._count == 1:
            tempitem = wx.Menu.Append(self, -1,"HACK")
            tempitem.SetBitmap(bmp)

        ret = unboundMethod(self, *args, **kwargs)
        if bmp:
            ret.SetBitmap(bmp)

        # delete temp item
        if tempitem is not None:
            self.Remove(tempitem.GetId())

        self._lastRet = ret
        return ret

    def AppendItem(self, *args, **kwargs):
        return self.applyBmp(wx.Menu.Append, *args, **kwargs)

    def Append(self, *args, **kwargs):
        return self.applyBmp(wx.Menu.Append, *args, **kwargs)

    def AppendCheckItem(self, *args, **kwargs):
        return self.applyBmp(wx.Menu.AppendCheckItem, *args, **kwargs)

    def AppendMenu(self, *args, **kwargs):
        return self.applyBmp(wx.Menu.AppendMenu, *args, **kwargs)