'''
Created on 9 déc. 2021

@author: slinux
'''

#
#
#
#    wxRaven from console or python
#
#
#
from wxRavenGUI import wxRavenMain



import wx
import sys, os
import argparse
#sys.stderr = open(os.getcwd() + "session.log", "wb")
    

if __name__ == '__main__':
    
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', help='start with specific profile directly')
    args = parser.parse_args()
    
    print(args)
    
    Instance_wxRavenApplication = wxRavenMain.wxRavenMainApp(profile=args.profile)
    Instance_wxRavenApplication.runApp()
    