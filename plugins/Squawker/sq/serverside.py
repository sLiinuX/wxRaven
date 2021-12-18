from ravenrpc import Ravencoin
import ipfshttpclient
from .credentials import USER, PASSWORD

rvn = Ravencoin(USER, PASSWORD)
ipfs = None
try:
    ipfs = ipfshttpclient.connect("gateway.ipfs.io")
except Exception as e:
    print("ipfs :" + str(e))  
    
    
ASSETNAME = "POLITICOIN"
IPFSDIRPATH = "/opt/squawker/ipfs"



