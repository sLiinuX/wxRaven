'''
Created on 8 janv. 2022

@author: slinux
'''
import inspect
import wx
from .CustomUserIO_Advanced import wxRavenAdvancedMessageDialog, wxRavenUnSavedFileDialog
import wx.adv



def UserInfo(parent, err):
    dlg = wx.MessageDialog(parent, f'{err}',
                               'Info',
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
    dlg.ShowModal()
    _res = dlg.GetValue()
    dlg.Destroy()
    
    return _res

def RequestUserWalletPassword(parent):
    _res = None
    dlg = wx.TextEntryDialog(
                parent, 'Enter your wallet passphrase if any',
                'protected wallet??', '', style=wx.TE_PASSWORD | wx.OK | wx.CANCEL)

    dlg.SetValue("")
    _dialogres=dlg.ShowModal()
    print(_dialogres)
    if _dialogres == wx.OK or _dialogres == 5100:
        _res = dlg.GetValue()
    
    dlg.Destroy()
    
    
    return _res
    

    
    
    
def UserAdvancedMessage(parentf, message, type, msgdetails='', showCancel=False):
    dlg =wxRavenAdvancedMessageDialog(parentf, message, type, msgdetails, showCancel)
    res = dlg.ShowModal()
    dlg.Destroy()



def UserUnsavedFileMessage(parentf, filename='', details=''):
    
    result = {'result_dialog:' : None, 'result_method': 'Cancel', 'result_backup':False}
    dlg =wxRavenUnSavedFileDialog(parentframe=parentf, message=filename, type='warning', msgdetails=details)
    res = dlg.ShowModal()
    
    result['result_dialog'] = res
    
    result['result_method'] = dlg.method
    result['result_backup'] = dlg.doBackup
    
    
    
    dlg.Destroy()
    
    
    return result

    
def ReportRPCResult(parentf, resultObj, _type="info", bypassMessage="", bypassError="", _showCancel=False):
    
    
    
    #
    # Treat Result Object
    #
    
    _message = ""
    _type = _type
    _msgdetails = ""
    _showCancel = False
    
    _callerName = inspect.stack()[1][3]
    
    if resultObj != None:
        
        
        if type(resultObj) is dict:
        
            _isError=False
            if resultObj.__contains__('error'):
                
                #if str(type(resultObj['error'])) == "<class 'dict'>"
                
                if resultObj['error'] != None:
                    _type = 'error'
                    _isError=True
                    if bypassError != '':
                        _message = bypassError 
                        _msgdetails = f"Error {resultObj['error']['code']} : {resultObj['error']['message']}\nCaller : {_callerName}"
                    else:
                        _message = f"Error {resultObj['error']['code']} : {resultObj['error']['message']}"     
                        _msgdetails = f"Caller : {_callerName}"#f"Error {resultObj['error']['code']} : {resultObj['error']['message']}"
            
            if not _isError:
                if resultObj.__contains__('result'):
                    if resultObj['result'] != None:
                        _type = 'success'
                        if bypassMessage != '':
                            _message = bypassMessage 
                            _msgdetails = f"Result : {resultObj['result']}\nCaller : {_callerName}"
                        else:
                            _message = f"Result : {resultObj['result']}"     
                            _msgdetails = f"Caller : {_callerName}"#f"Error {resultObj['error']['code']} : {resultObj['error']['message']}"
            
                        
                else:
                    if bypassMessage != '':
                        _message = bypassMessage 
                        _msgdetails = f"Result : {resultObj}\nCaller : {_callerName}"
                    else:
                        _message = f"Result : {resultObj}"     
                        _msgdetails = f"Caller : {_callerName}"#f"Error {resultObj['error']['code']} : {resultObj['error']['message']}"
        else :    
            if bypassMessage != '':
                _message = bypassMessage 
                _msgdetails = f"Result : {resultObj}\nCaller : {_callerName}"
            else:
                _message = f"Result : {resultObj}"     
                _msgdetails = f"Caller : {_callerName}"
                
    else:
        _type = 'warning'
        
        _message = f'no result received from {_callerName}'
        _msgdetails = "Check wxRaven logfile for more details."
    
    
    
    dlg =wxRavenAdvancedMessageDialog(parentf, _message, _type, _msgdetails, _showCancel)
    res = dlg.ShowModal()
    dlg.Destroy()
    return res
    
    


def UserSystemNotification(parentframe, title, message, _type='info'):
        sTitle = title
        sMsg = message

        
        icons={
            'info':parentframe.RessourcesProvider.GetIcon('info_icon_45'),
            'warning':parentframe.RessourcesProvider.GetIcon('warning_icon_45'),
            'error':parentframe.RessourcesProvider.GetIcon('error_icon_45'),
            'success':parentframe.RessourcesProvider.GetIcon('success_icon_45')
            }
        
        typesFlag={
            'info':wx.ICON_INFORMATION,
            'warning':wx.ICON_INFORMATION,
            'error':wx.ICON_INFORMATION,
            'success':wx.ICON_INFORMATION
            }
        
        
        if not icons.__contains__(_type):
            _type = 'info'

        nmsg = wx.adv.NotificationMessage(title=sTitle, message=sMsg)
        nmsg.SetFlags(typesFlag[_type])
        
        nmsg.SetIcon(icons[_type])
        
        
        nmsg.Show(timeout=wx.adv.NotificationMessage.Timeout_Auto)    
    
    