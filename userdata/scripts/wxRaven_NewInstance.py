'''
Created on 3 janv. 2022

@author: slinux
'''

#
#
#
#    wxRaven for building .exe
#
#
#


import json
import wx
import wx.xrc
import wx.dataview
import wx.dataview
import wx.aui
import wx.richtext
import wx.lib
import wx.lib.scrolledpanel
import wx.lib.buttons
import wx.adv
import wx.grid
import wx.html2
import wx.aui
import wx.py
import random

try: 
    import wx.msw
except ImportError:
    pass

try:
    import pyperclip
except ImportError:
    from libs import pyperclip


import os
import time
import wx.lib.mixins.listctrl
import webbrowser
import qrcode

from collections import namedtuple
from contextlib import contextmanager
from datetime import datetime, timedelta
from typing import List, Optional, Union
from socketio import Client
from socketio.exceptions import ConnectionError as SocketIOConnectionError
from sqlalchemy import create_engine, func, insert, select, update
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from datetime import datetime as _datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship


import base64
import logging
from logging.handlers import TimedRotatingFileHandler


from requests import post, get
from libs.jsonrpcclient.requests import Request
#import ipfshttpclient
#import ipfsapi

from PIL import Image
import PIL

import shutil


from ast import literal_eval
import threading


from wxRavenGUI import wxRavenMain


def __wxRaven__(evt=None):
    Instance_wxRavenApplication = wxRavenMain.wxRavenMainApp()
    Instance_wxRavenApplication.runApp()
    
    
def StartNew():
    t=threading.Thread(target=__wxRaven__, args=())
    t.start()

#StartNew()

#__wxRaven__()
print('script disabled for now')
    
    