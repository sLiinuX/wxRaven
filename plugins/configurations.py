'''
Created on 15 févr. 2022

@author: slinux
'''

#
# Inlcudes_Only Tables to limit plugins at startup
#


wxraven_standard_edition = ['General', 'ProfileManager',  'Ravencore' ]
wxraven_artist_edition = wxraven_standard_edition + ['IPFS', 'Miscellaneous' ]
wxraven_developer_edition = []


__wxraven_configurations_default__ = 'wxRaven : Standard Edition'

#
#
# Complete configuration list
#
#
__wxraven_configurations_list__ = {
    
    'wxRaven : Standard Edition': wxraven_standard_edition,
    'wxRaven : NFT Artist Edition':wxraven_artist_edition,
    'wxRaven : Developer/Server Edition' : wxraven_developer_edition
    
    }



#
#
# Configuration default Icon and Avatars
#
#

__wxraven_configurations_icons__ = {
    
    'wxRaven : Standard Edition': 'wxraven_standard_edition_icon',
    'wxRaven : NFT Artist Edition':'wxraven_artist_edition_icon',
    'wxRaven : Developer/Server Edition' : 'wxraven_developer_edition_icon'
    
    }

__wxraven_configurations_logos__ = {
    
    'wxRaven : Standard Edition': 'avatar_4',
    'wxRaven : NFT Artist Edition':'avatar_2',
    'wxRaven : Developer/Server Edition' : 'avatar_3'
    
    }

__wxraven_configurations_predefined__ = {
    
    'wxRaven : Standard Edition': 'wxraven_standard_edition',
    'wxRaven : NFT Artist Edition':'wxraven_artist_edition',
    'wxRaven : Developer/Server Edition' : 'wxraven_developer_edition'
    
    }

