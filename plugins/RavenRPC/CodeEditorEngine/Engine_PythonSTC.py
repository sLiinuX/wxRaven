'''
Created on 16 févr. 2022

@author: slinux
'''
import  wx
import  wx.stc  as  stc
from wx import stc
import  wx.stc


import keyword

if wx.Platform == '__WXMSW__':
    faces = { 'times': 'Times New Roman',
              'mono' : 'Courier New',
              'helv' : 'Arial',
              'other': 'Comic Sans MS',
              'size' : 10,
              'size2': 8,
             }
elif wx.Platform == '__WXMAC__':
    faces = { 'times': 'Times New Roman',
              'mono' : 'Monaco',
              'helv' : 'Arial',
              'other': 'Comic Sans MS',
              'size' : 12,
              'size2': 10,
             }
else:
    faces = { 'times': 'Times',
              'mono' : 'Courier',
              'helv' : 'Helvetica',
              'other': 'new century schoolbook',
              'size' : 12,
              'size2': 10,
             }
    
    
    
    
class PythonSTC():
    '''
    classdocs
    '''


    def __init__(self, STC_Object:stc.StyledTextCtrl):
        '''
        Constructor
        '''
        self.STC_Object=STC_Object
        
        STC_Object.fold_symbols = 2
        STC_Object.CmdKeyAssign(ord('B'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)
        STC_Object.CmdKeyAssign(ord('N'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)

        STC_Object.SetLexer(stc.STC_LEX_PYTHON)
        #self.SetKeyWords(0, " ".join(keyword.kwlist))
        
        STC_Object.SetProperty("fold", "1")
        STC_Object.SetProperty("tab.timmy.whinge.level", "1")
        STC_Object.SetMargins(0,0)

        STC_Object.SetViewWhiteSpace(False)
        
        #self.SetBufferedDraw(False)
        #self.SetViewEOL(True)
        #self.SetEOLMode(stc.STC_EOL_CRLF)
        #self.SetUseAntiAliasing(True)

        STC_Object.SetEdgeMode(stc.STC_EDGE_BACKGROUND)
        STC_Object.SetEdgeColumn(78)

        # Setup a margin to hold fold markers
        #self.SetFoldFlags(16)  ###  WHAT IS THIS VALUE?  WHAT ARE THE OTHER FLAGS?  DOES IT MATTER?
        STC_Object.SetMarginType(2, stc.STC_MARGIN_SYMBOL)
        STC_Object.SetMarginMask(2, stc.STC_MASK_FOLDERS)
        STC_Object.SetMarginSensitive(2, True)
        STC_Object.SetMarginWidth(2, 12)
        
        
        if STC_Object.fold_symbols == 0:
            # Arrow pointing right for contracted folders, arrow pointing down for expanded
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_ARROWDOWN, "black", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_ARROW, "black", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_EMPTY, "black", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_EMPTY, "black", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_EMPTY,     "white", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_EMPTY,     "white", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_EMPTY,     "white", "black")

        elif STC_Object.fold_symbols == 1:
            # Plus for contracted folders, minus for expanded
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_MINUS, "white", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_PLUS,  "white", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_EMPTY, "white", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_EMPTY, "white", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_EMPTY, "white", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_EMPTY, "white", "black")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_EMPTY, "white", "black")

        elif STC_Object.fold_symbols == 2:
            # Like a flattened tree control using circular headers and curved joins
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_CIRCLEMINUS,          "white", "#404040")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_CIRCLEPLUS,           "white", "#404040")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_VLINE,                "white", "#404040")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_LCORNERCURVE,         "white", "#404040")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_CIRCLEPLUSCONNECTED,  "white", "#404040")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_CIRCLEMINUSCONNECTED, "white", "#404040")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_TCORNERCURVE,         "white", "#404040")

        elif STC_Object.fold_symbols == 3:
            # Like a flattened tree control using square headers
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_BOXMINUS,          "white", "#808080")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_BOXPLUS,           "white", "#808080")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_VLINE,             "white", "#808080")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_LCORNER,           "white", "#808080")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_BOXPLUSCONNECTED,  "white", "#808080")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_BOXMINUSCONNECTED, "white", "#808080")
            STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_TCORNER,           "white", "#808080")


        #self.Bind(stc.EVT_STC_UPDATEUI, self.OnUpdateUI)
        #self.Bind(stc.EVT_STC_MARGINCLICK, self.OnMarginClick)
        #self.Bind(wx.EVT_KEY_DOWN, self.OnKeyPressed)

        # Make some styles,  The lexer defines what each style is used for, we
        # just have to define what each style looks like.  This set is adapted from
        # Scintilla sample property files.

        # Global default styles for all languages
        STC_Object.StyleSetSpec(stc.STC_STYLE_DEFAULT,     "face:%(helv)s,size:%(size)d" % faces)
        STC_Object.StyleClearAll()  # Reset all to be like the default

        # Global default styles for all languages
        STC_Object.StyleSetSpec(stc.STC_STYLE_DEFAULT,     "face:%(helv)s,size:%(size)d" % faces)
        STC_Object.StyleSetSpec(stc.STC_STYLE_LINENUMBER,  "back:#C0C0C0,face:%(helv)s,size:%(size2)d" % faces)
        STC_Object.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, "face:%(other)s" % faces)
        STC_Object.StyleSetSpec(stc.STC_STYLE_BRACELIGHT,  "fore:#FFFFFF,back:#0000FF,bold")
        STC_Object.StyleSetSpec(stc.STC_STYLE_BRACEBAD,    "fore:#000000,back:#FF0000,bold")

        # Python styles
        # Default
        STC_Object.StyleSetSpec(stc.STC_P_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        # Comments
        STC_Object.StyleSetSpec(stc.STC_P_COMMENTLINE, "fore:#007F00,face:%(other)s,size:%(size)d" % faces)
        # Number
        STC_Object.StyleSetSpec(stc.STC_P_NUMBER, "fore:#007F7F,size:%(size)d" % faces)
        # String
        STC_Object.StyleSetSpec(stc.STC_P_STRING, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        # Single quoted string
        STC_Object.StyleSetSpec(stc.STC_P_CHARACTER, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
        # Keyword
        STC_Object.StyleSetSpec(stc.STC_P_WORD, "fore:#00007F,bold,size:%(size)d" % faces)
        # Triple quotes
        STC_Object.StyleSetSpec(stc.STC_P_TRIPLE, "fore:#7F0000,size:%(size)d" % faces)
        # Triple double quotes
        STC_Object.StyleSetSpec(stc.STC_P_TRIPLEDOUBLE, "fore:#7F0000,size:%(size)d" % faces)
        # Class name definition
        STC_Object.StyleSetSpec(stc.STC_P_CLASSNAME, "fore:#0000FF,bold,underline,size:%(size)d" % faces)
        # Function or method name definition
        STC_Object.StyleSetSpec(stc.STC_P_DEFNAME, "fore:#007F7F,bold,size:%(size)d" % faces)
        # Operators
        STC_Object.StyleSetSpec(stc.STC_P_OPERATOR, "bold,size:%(size)d" % faces)
        # Identifiers
        STC_Object.StyleSetSpec(stc.STC_P_IDENTIFIER, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
        # Comment-blocks
        STC_Object.StyleSetSpec(stc.STC_P_COMMENTBLOCK, "fore:#7F7F7F,size:%(size)d" % faces)
        # End of line where string is not closed
        STC_Object.StyleSetSpec(stc.STC_P_STRINGEOL, "fore:#000000,face:%(mono)s,back:#E0C0E0,eol,size:%(size)d" % faces)

        STC_Object.SetCaretForeground("BLUE")
        STC_Object.Bind(stc.EVT_STC_UPDATEUI, self.OnUpdateUI)
        
        #STC_Object.Bind(stc.EVT_STC_UPDATEUI, self.OnUpdateUI)
        STC_Object.Bind(stc.EVT_STC_MARGINCLICK, self.OnMarginClick)
        STC_Object.Bind(wx.EVT_KEY_DOWN, self.OnKeyPressed)
        
        '''
        # register some images for use in the AutoComplete box.
        STC_Object.RegisterImage(1, images.Smiles.GetBitmap())
        STC_Object.RegisterImage(2,
            wx.ArtProvider.GetBitmap(wx.ART_NEW, size=(16,16)))
        STC_Object.RegisterImage(3,
            wx.ArtProvider.GetBitmap(wx.ART_COPY, size=(16,16)))
        
        '''
     
     
    
    
    
    
    def SetUpEditor(self):
        self.STC_Object.SetProperty("fold", "1" )

        # Highlight tab/space mixing (shouldn't be any)
        self.STC_Object.SetProperty("tab.timmy.whinge.level", "1")

        # Set left and right margins
        self.STC_Object.SetMargins(2,2)

        # Set up the numbers in the margin for margin #1
        self.STC_Object.SetMarginType(1, wx.stc.STC_MARGIN_NUMBER)
        # Reasonable value for, say, 4-5 digits using a mono font (40 pix)
        self.STC_Object.SetMarginWidth(1, 40)

        # Indentation and tab stuff
        self.STC_Object.SetIndent(4)               # Proscribed indent size for wx
        self.STC_Object.SetIndentationGuides(True) # Show indent guides
        self.STC_Object.SetBackSpaceUnIndents(True)# Backspace unindents rather than delete 1 space
        self.STC_Object.SetTabIndents(True)        # Tab key indents
        self.STC_Object.SetTabWidth(4)             # Proscribed tab size for wx
        self.STC_Object.SetUseTabs(False)          # Use spaces rather than tabs, or
                                            # TabTimmy will complain!
        # White space
        self.STC_Object.SetViewWhiteSpace(False)   # Don't view white space

        # EOL: Since we are loading/saving ourselves, and the
        # strings will always have \n's in them, set the STC to
        # edit them that way.
        self.STC_Object.SetEOLMode(wx.stc.STC_EOL_LF)
        self.STC_Object.SetViewEOL(False)

        # No right-edge mode indicator
        self.STC_Object.SetEdgeMode(stc.STC_EDGE_NONE)

        # Setup a margin to hold fold markers
        self.STC_Object.SetMarginType(2, stc.STC_MARGIN_SYMBOL)
        self.STC_Object.SetMarginMask(2, stc.STC_MASK_FOLDERS)
        self.STC_Object.SetMarginSensitive(2, True)
        self.STC_Object.SetMarginWidth(2, 12)

        # and now set up the fold markers
        self.STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_BOXPLUSCONNECTED,  "white", "black")
        self.STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_BOXMINUSCONNECTED, "white", "black")
        self.STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_TCORNER,  "white", "black")
        self.STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_LCORNER,  "white", "black")
        self.STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_VLINE,    "white", "black")
        self.STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_BOXPLUS,  "white", "black")
        self.STC_Object.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_BOXMINUS, "white", "black")

        # Global default style
        if wx.Platform == '__WXMSW__':
            self.STC_Object.StyleSetSpec(stc.STC_STYLE_DEFAULT,
                                  'fore:#000000,back:#FFFFFF,face:Courier New')
        elif wx.Platform == '__WXMAC__':
            # TODO: if this looks fine on Linux too, remove the Mac-specific case
            # and use this whenever OS != MSW.
            self.STC_Object.StyleSetSpec(stc.STC_STYLE_DEFAULT,
                                  'fore:#000000,back:#FFFFFF,face:Monaco')
        else:
            defsize = wx.SystemSettings.GetFont(wx.SYS_ANSI_FIXED_FONT).GetPointSize()
            self.STC_Object.StyleSetSpec(stc.STC_STYLE_DEFAULT,
                                  'fore:#000000,back:#FFFFFF,face:Courier,size:%d'%defsize)

        # Clear styles and revert to default.
        self.STC_Object.StyleClearAll()

        # Following style specs only indicate differences from default.
        # The rest remains unchanged.

        # Line numbers in margin
        self.STC_Object.StyleSetSpec(wx.stc.STC_STYLE_LINENUMBER,'fore:#000000,back:#99A9C2')
        # Highlighted brace
        self.STC_Object.StyleSetSpec(wx.stc.STC_STYLE_BRACELIGHT,'fore:#00009D,back:#FFFF00')
        # Unmatched brace
        self.STC_Object.StyleSetSpec(wx.stc.STC_STYLE_BRACEBAD,'fore:#00009D,back:#FF0000')
        # Indentation guide
        self.STC_Object.StyleSetSpec(wx.stc.STC_STYLE_INDENTGUIDE, "fore:#CDCDCD")

        # Python styles
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_DEFAULT, 'fore:#000000')
        # Comments
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_COMMENTLINE,  'fore:#008000,back:#F0FFF0')
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_COMMENTBLOCK, 'fore:#008000,back:#F0FFF0')
        # Numbers
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_NUMBER, 'fore:#008080')
        # Strings and characters
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_STRING, 'fore:#800080')
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_CHARACTER, 'fore:#800080')
        # Keywords
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_WORD, 'fore:#000080,bold')
        # Triple quotes
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_TRIPLE, 'fore:#800080,back:#FFFFEA')
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_TRIPLEDOUBLE, 'fore:#800080,back:#FFFFEA')
        # Class names
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_CLASSNAME, 'fore:#0000FF,bold')
        # Function names
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_DEFNAME, 'fore:#008080,bold')
        # Operators
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_OPERATOR, 'fore:#800000,bold')
        # Identifiers. I leave this as not bold because everything seems
        # to be an identifier if it doesn't match the above criterae
        self.STC_Object.StyleSetSpec(wx.stc.STC_P_IDENTIFIER, 'fore:#000000')

        # Caret color
        self.STC_Object.SetCaretForeground("BLUE")
        # Selection background
        self.STC_Object.SetSelBackground(1, '#66CCFF')

        self.STC_Object.SetSelBackground(True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.STC_Object.SetSelForeground(True, wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

    def RegisterModifiedEvent(self, eventHandler):
        self.Bind(wx.stc.EVT_STC_CHANGE, eventHandler)
    
    
        
    def OnUpdateUI(self, evt):
        # check for matching braces
        braceAtCaret = -1
        braceOpposite = -1
        charBefore = None
        caretPos = self.STC_Object.GetCurrentPos()

        if caretPos > 0:
            charBefore = self.STC_Object.GetCharAt(caretPos - 1)
            styleBefore = self.STC_Object.GetStyleAt(caretPos - 1)

        # check before
        if charBefore and chr(charBefore) in "[]{}()" and styleBefore == stc.STC_P_OPERATOR:
            braceAtCaret = caretPos - 1

        # check after
        if braceAtCaret < 0:
            charAfter = self.STC_Object.GetCharAt(caretPos)
            styleAfter = self.STC_Object.GetStyleAt(caretPos)

            if charAfter and chr(charAfter) in "[]{}()" and styleAfter == stc.STC_P_OPERATOR:
                braceAtCaret = caretPos

        if braceAtCaret >= 0:
            braceOpposite = self.STC_Object.BraceMatch(braceAtCaret)

        if braceAtCaret != -1  and braceOpposite == -1:
            self.STC_Object.BraceBadLight(braceAtCaret)
        else:
            self.STC_Object.BraceHighlight(braceAtCaret, braceOpposite)
            #pt = self.PointFromPosition(braceOpposite)
            #self.Refresh(True, wxRect(pt.x, pt.y, 5,5))
            #print(pt)
            #self.Refresh(False)    
            
            
    def OnMarginClick(self, evt):
        # fold and unfold as needed
        if evt.GetMargin() == 2:
            if evt.GetShift() and evt.GetControl():
                self.STC_Object.FoldAll()
            else:
                lineClicked = self.STC_Object.LineFromPosition(evt.GetPosition())

                if self.STC_Object.GetFoldLevel(lineClicked) & stc.STC_FOLDLEVELHEADERFLAG:
                    if evt.GetShift():
                        self.STC_Object.SetFoldExpanded(lineClicked, True)
                        self.STC_Object.Expand(lineClicked, True, True, 1)
                    elif evt.GetControl():
                        if self.STC_Object.GetFoldExpanded(lineClicked):
                            self.STC_Object.SetFoldExpanded(lineClicked, False)
                            self.STC_Object.Expand(lineClicked, False, True, 0)
                        else:
                            self.STC_Object.SetFoldExpanded(lineClicked, True)
                            self.STC_Object.Expand(lineClicked, True, True, 100)
                    else:
                        self.STC_Object.ToggleFold(lineClicked)


    def FoldAll(self):
        lineCount = self.STC_Object.GetLineCount()
        expanding = True

        # find out if we are folding or unfolding
        for lineNum in range(lineCount):
            if self.STC_Object.GetFoldLevel(lineNum) & stc.STC_FOLDLEVELHEADERFLAG:
                expanding = not self.STC_Object.GetFoldExpanded(lineNum)
                break

        lineNum = 0

        while lineNum < lineCount:
            level = self.STC_Object.GetFoldLevel(lineNum)
            if level & stc.STC_FOLDLEVELHEADERFLAG and \
               (level & stc.STC_FOLDLEVELNUMBERMASK) == stc.STC_FOLDLEVELBASE:

                if expanding:
                    self.STC_Object.SetFoldExpanded(lineNum, True)
                    lineNum = self.STC_Object.Expand(lineNum, True)
                    lineNum = lineNum - 1
                else:
                    lastChild = self.STC_Object.GetLastChild(lineNum, -1)
                    self.STC_Object.SetFoldExpanded(lineNum, False)

                    if lastChild > lineNum:
                        self.STC_Object.HideLines(lineNum+1, lastChild)

            lineNum = lineNum + 1



    def Expand(self, line, doExpand, force=False, visLevels=0, level=-1):
        lastChild = self.STC_Object.GetLastChild(line, level)
        line = line + 1

        while line <= lastChild:
            if force:
                if visLevels > 0:
                    self.STC_Object.ShowLines(line, line)
                else:
                    self.STC_Object.HideLines(line, line)
            else:
                if doExpand:
                    self.STC_Object.ShowLines(line, line)

            if level == -1:
                level = self.STC_Object.GetFoldLevel(line)

            if level & stc.STC_FOLDLEVELHEADERFLAG:
                if force:
                    if visLevels > 1:
                        self.STC_Object.SetFoldExpanded(line, True)
                    else:
                        self.STC_Object.SetFoldExpanded(line, False)

                    line = self.STC_Object.Expand(line, doExpand, force, visLevels-1)

                else:
                    if doExpand and self.STC_Object.GetFoldExpanded(line):
                        line = self.STC_Object.Expand(line, True, force, visLevels-1)
                    else:
                        line = self.STC_Object.Expand(line, False, force, visLevels-1)
            else:
                line = line + 1

        return line
    
    
    def OnKeyPressed(self, event):
        if self.STC_Object.CallTipActive():
            self.STC_Object.CallTipCancel()
        key = event.GetKeyCode()

        if key == 32 and event.ControlDown():
            pos = self.STC_Object.GetCurrentPos()

            # Tips
            if event.ShiftDown():
                self.STC_Object.CallTipSetBackground("yellow")
                self.STC_Object.CallTipShow(pos, 'lots of of text: blah, blah, blah\n\n'
                                 'show some suff, maybe parameters..\n\n'
                                 'fubar(param1, param2)')
            # Code completion
            else:
                #lst = []
                #for x in range(50000):
                #    lst.append('%05d' % x)
                #st = " ".join(lst)
                #print(len(st))
                #self.STC_Object.AutoCompShow(0, st)

                kw = keyword.kwlist[:]
                #kw.append("zzzzzz?2")
                #kw.append("aaaaa?2")
                kw.append("__init__")
                kw.append("zzaaaaa?2")
                #kw.append("zzbaaaa?2")
                #kw.append("this_is_a_longer_value")
                #kw.append("this_is_a_much_much_much_much_much_much_much_longer_value")

                kw.sort()  # Python sorts are case sensitive
                self.STC_Object.AutoCompSetIgnoreCase(False)  # so this needs to match

                # Images are specified with a appended "?type"
                for i in range(len(kw)):
                    if kw[i] in keyword.kwlist:
                        kw[i] = kw[i] + "?1"

                self.STC_Object.AutoCompShow(0, " ".join(kw))
        else:
            event.Skip()
        