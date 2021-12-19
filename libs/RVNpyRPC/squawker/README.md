# Squawker 
- Very Alpha Standard Edition

 Squawker is a decentralized messaging standard for use on the Ravencoin blockchain. 

 The sending of a Kaw can be done with any asset. 

 POLITICOIN is the currently the working default. Development and early adopters can currently get some from BadGuyTy upon request in the Ravencoin Discord Server

 This code currently needs access to a full Ravencoin node. A standalone client may be available in the future to operate against a standardized API.

# Installation
Squawker currently requires
- being run on a full node 
- being run on an ipfs server

For security reasons only Python3.9 is currently supported

Download Git repo

Edit the config.json - Remove all values that you currently don't have and leave as empty strings. For profile timestamp set it to 0 unless you have manually configured a profile.

Create a credentials.py file with 

USER = "\<rpc user>" 

PASSWORD = "\<rpc password>"

# Message types
These values represent how to tell what type of Kaw an IPFS hash is.

- 1 coin to self = regular kaw
- 0.5 coins to self = profile update
- 0.3 coins to someone = private encrypted message attached
- 0.2 coins to self = Market listing
- 0.1 coins to someone = Follow
- 0.001 coins to someone = Unfollow
- 0.01 coins to someone = Tag
- 0.01 coins to PHA (publicly listed address) (maintained list at PMHA) = hashtag

# Hashtag management and tracking
- 1 RVN to PMHA (Public Maintained Hashtag Address) to create and list a new hashtag
- 1 coin from PMHA to PMHA address to show latest hashtags
    
# Standards
Message Standard

- Sender address
- Sender profile hash and profile timestamp #this removes some RPC calls to a node. 
The profile and timestamp are cached locally and the profile is updated upon seeing a newer timestamp
- Message timestamp
- Message contents
- Multimedia IPFS hash(es)

Profile Standard
- Name
- pgp public key
- Profile Picture IPFS hash
- Bio
- Website
- Social Medias

Marketplace Listing
- Item name
- Atomic transaction 
- Price
- Item description


