'''
Created on 9 déc. 2021

@author: slinux
'''

from wxRavenGUI import wxRavenMain


"""
Instance_wxRavenApplication = None


def ravencoin(network=None):
    return Instance_wxRavenApplication.appmainframe.getRvnRPC(network)

def rvnrpc(network=None): 
    return Instance_wxRavenApplication.appmainframe.getNetwork(network)
        
    


"""


    

if __name__ == '__main__':
    Instance_wxRavenApplication = wxRavenMain.wxRavenMainApp()
    #this = Instance_wxRavenApplication.appmainframe
    Instance_wxRavenApplication.runApp()
    