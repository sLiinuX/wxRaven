from ravenrpc import Ravencoin
import ipfshttpclient
from credentials import USER, PASSWORD

rvn = Ravencoin(USER, PASSWORD)
ipfs = ipfshttpclient.connect()
ASSETNAME = "POLITICOIN"
IPFSDIRPATH = "/opt/squawker/ipfs"



