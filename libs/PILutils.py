
# ImgConv.py

"""
Based on pyWiki 'Working With Images' @  http://wiki.wxpython.org/index.cgi/WorkingWithImages
Modified to properly copy, create or remove any alpha in all conversion permutations.
A wx.App must be created in order for the various wx functions to work.

Win32IconImagePlugin  
Alternate PIL plugin for dealing with Microsoft .ico files.
http://code.google.com/p/casadebender/wiki/Win32IconImagePlugin

Notes:  
    - The terms "plane", "band", "layer" and "channel" are used interchangibly.
    - When the phrase "{argument name} is given" is used, it means 
      this optional argument is specified in the function call's argument list.

Tested on Win7 64-bit (6.1.7600) and Win XP SP3 (5.1.2600) using Python unicode 32-bit.

Platform  Windows 6.1.7600
Python    2.5.4 (r254:67916, Dec 23 2008, 15:10:54) [MSC v.1310 32 bit (Intel) (x86)]
Python wx 2.8.10.1
Pil       1.1.7

Ray Pasco      
pascor(at)verizon(dot)net

Last modification:      2012-12-25      
                        Documentation fixes and clarifications
                        Deleted line [ import WxImageFromPilImage ].

This code may be freely modified and distributed for any purpose whatsoever.

"""

import wx       # WxBmap <==> wxImage
    # wxImage <==> PilImage.  Used when converting to or from Pil images.
from PIL import Image
#------------------------------------------------------------------------------

#   image type         image type       image type
#       1                  2                3
#   wx.Bitmap   <==>   wx.Image  <==>   pilImage

#----------------------------

def WxBitmapFromPilImage( pilImage, addAlphaLayer=False, delAlphaLayer=False ) :
    """
    3 ==> 1
    
    The default parameter values preserve any existing transparency,
      but does not create any kind of transparency layer if none already exists.
   
    If the given pilImage mode is RGB, this function can optionally create
      a new wxImage alpha transparency plane (layer) by calling with the
      argument [ addAlphaLayer=True ].
     
    If the given pilImage mode is RGBA, this function can optionally delete
      any transparency plane by calling with the argument [ delAlphaLayer=True ].
     
    If given *both* addAlphaLayer=True *and* delAlphaLayer=True,
        which is nonsensical, [ addAlphaLayer=True ] will take precedence.
     
    """
   
    # Pass on the given parameters.
    wxImage = WxImageFromPilImage( pilImage, addAlphaLayer, delAlphaLayer )
    wxBitmap = wxImage.ConvertToBitmap()
      
   
    
    # Pass on the given parameters.
    wxImage = WxImageFromPilImage( pilImage, addAlphaLayer, delAlphaLayer )
    wxBitmap = wxImage.ConvertToBitmap()
    
    return wxBitmap
    
#end def

#----------------------------

def WxImageFromPilImage( pilImage, addAlphaLayer=False, delAlphaLayer=False ) :
    """
    3 ==> 2
    
    The default parameter values preserve any existing transparency, 
      but do not add one if it none exists in the source image.
    
    If the given source has no alpha, a new image with alpha transparency 
      can be returned by calling with addAlphaLayer=True.
      
    If the given source image has alpha, a new image without alpha
      can be returned by calling with delAlphaLayer=True.
      
    """
    
    wxImage = wx.EmptyImage( *pilImage.size  )      # Has no transparency plane.
    
    pilMode = pilImage.mode
    hasAlpha = pilImage.mode[-1] == 'A'
    
    if hasAlpha or (not hasAlpha and addAlphaLayer) :
        
        pilImageRGBA = pilImage.copy()  # Image mode might now be RGB, not RGBA.
        if pilImage.mode != 'RGBA' :
            pilImageRGBA = pilImageRGBA.convert( 'RGBA' )
        #end if
        # The image mode is now gauranteed to be RGBA.
        
        pilImageStr = pilImageRGBA.tostring()    # Convert all 4 image planes.
        
        # Extract just the RGB data
        pilRgbStr = pilImageRGBA.copy().convert( 'RGB').tostring()
        wxImage.SetData( pilRgbStr )
        
        # Extract just the existing pilImage alpha plane data.
        pilAlphaStr = pilImageStr[3::4]      # start at index 3 with a stride (skip) of 4.
        wxImage.SetAlphaData( pilAlphaStr )
        
    elif delAlphaLayer or ((not hasAlpha) and (not addAlphaLayer)) :
        
        pilImageRGB = pilImage.copy().convert( 'RGB' )
        
        wxImage.SetData( pilImageRGB.tostring() )     
        
    #end if
    
    return wxImage
    
#end def

#----------------------------

def WxBitmapFromWxImage( wxImage, threshold=128 ) :    
    """
    2 ==> 1
    
    Any transparency mask or alpha transparency will be copied, to0.
    """
    
    wxBmap = wxImage.ConvertToBitmap()
    
    return wxBmap
    
#end def

#----------------------------

def WxImageFromWxBitmap( wxBmap ) :              
    """
    1 ==> 2
    
    Any transparency mask or alpha transparency will be copied, to0.
    """
    return wx.ImageFromBitmap( wxBmap )
#end def

#------------------------------------------------------------------------------

def PilImageFromWxBitmap( wxBmap, keepTransp=True, createTransp=False, debug=False ) :
    """
    1 ==> 3
    
    The default parameter values preserve any existing transparency, 
      but do not add one if it none exists in the source image.
    
    If the given source has no alpha, a new image with alpha transparency 
      can be returned by calling with addAlphaLayer=True.
      
    If the given source image has alpha, a new image without alpha
      can be returned by calling with delAlphaLayer=True.
      
    """
    
    wxImage = WxImageFromWxBitmap( wxBmap )
    
    return PilImageFromWxImage( wxImage )   # Always preserves any transparency.
#end def

#----------------------------

def PilImageFromWxImage( wxImage, keepTransp=True, createTransp=False, debug=False ) :
    """
    2 ==> 3  
    
    Default preserves any transparency.
    """
    
    # These can never be simultaneous.
    hasMask  = wxImage.HasMask()
    hasAlpha = wxImage.HasAlpha()
    if debug :
        print('>>>>  PilImageFromWxImage():  Input Image has Alpha')
    
    # Always convert a mask into an aplha layer.
    # Deal with keeping or discarding this alpha later on.
    if hasMask :    # Is always mutually exclusive with hasAlpha.
        
        if debug :
            print('>>>>  PilImageFromWxImage():  Converting Input Image Mask to Alpha')
        
        wxImage.InitAlpha()     # Covert the separate mask to a 4th alpha layer.
        hasAlpha = True
            
    #end if 
    
    image_size = wxImage.GetSize()      # All images here have the same size.
    
    # Create an RGB pilImage and stuff it with RGB data from the wxImage.
    pilImage = Image.new( 'RGB', image_size )
    pilImage.fromstring( wxImage.GetData() )
    
    # May need the separated planes if an RGBA image is needed. later.
    r_pilImage, g_pilImage, b_pilImage = pilImage.split()
        
    if hasAlpha :
        
        if keepTransp : # Ignore createTransp - has no meaning
            
            if debug :
                print('>>>>  PilImageFromWxImage():  Keeping Transparency')

            # Must recompose the pilImage from 4 layers.
            r_pilImage, g_pilImage, b_pilImage = pilImage.split()

            # Create a Black L pilImage and stuff it with the alpha data 
            #   extracted from the alpha layer of the wxImage.
            pilImage_L = Image.new( 'L', image_size )
            pilImage_L.fromstring( wxImage.GetAlphaData() )

            # Create an RGBA PIL image from the 4 layers.
            pilImage = Image.merge( 'RGBA', (r_pilImage, g_pilImage, b_pilImage, pilImage_L) )
        
        elif (not keepTransp) :
            
            # The RGB pilImage can be returned as it is now.
            if debug :
                print('>>>>  PilImageFromWxImage():  Returning an RGB PIL Image.')
            
        #end if
        
    elif (not hasAlpha) and createTransp :      # Ignore keepTransp - has no meaning
        
        if debug :
            print('>>>>  PilImageFromWxImage():  Creating a New Transparency Layer')
        
        # Create a Black L mode pilImage. The resulting image will still
        #  look the same, but will allow future transparency modification.
        pilImage_L = Image.new( 'L', image_size )
        
        # Create an RGBA pil image from the 4 bands.
        pilImage = Image.merge( 'RGBA', (r_pilImage, g_pilImage, b_pilImage, pilImage_L) )
        
    #end if
    
    return pilImage
    
#end PilImageFromWxImage def

#------------------------------------------------------------------------------