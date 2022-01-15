'''
Created on 8 janv. 2022

@author: slinux
'''

import wx

def UserInfo(parent, err):
    dlg = wx.MessageDialog(parent, f'{err}',
                               'Error',
                               wx.OK| wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
    res = dlg.ShowModal()
    dlg.Destroy()

def UserError(parent, err):
    dlg = wx.MessageDialog(parent, f'{err}',
                               'Error',
                               wx.OK| wx.ICON_ERROR
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
    res = dlg.ShowModal()
    dlg.Destroy()
    
def UserQuestion(parent, question):
    dlg = wx.MessageDialog(parent, f'{question}',
                               'Confirm',
                               wx.YES_NO| wx.ICON_QUESTION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
    res = dlg.ShowModal()
    dlg.Destroy()
    _res = False
    if res==5103:
        _res = True
    return _res



def RequestUserTextInput(parent, question, title="Userinput"):
    dlg = wx.TextEntryDialog(
                parent, question,
                title, '')

    dlg.SetValue("")
    _res = dlg.GetValue()
    dlg.Destroy()
    
    return _res

def RequestUserWalletPassword(parent):
    dlg = wx.TextEntryDialog(
                parent, 'Enter your wallet passphrase if any',
                'protected wallet??', '')

    dlg.SetValue("")
    _res = dlg.GetValue()
    dlg.Destroy()
    
    return _res
    
    