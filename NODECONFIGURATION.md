About
-----

Configuration of ravencore is recommended in NODE MODE with the following options :
( Wallet Menu > Configuration > Open configuration )





```
#Accept cli/json RPC
server=1
#Maintains the full transaction index on your node. Needed if you call getrawtransaction. Default is 0.
txindex=1
#Maintains the full Address index on your node. Needed if you call getaddress* calls. Default is 0.
addressindex=1
#Maintains the full Asset index on your node. Needed if you call getassetdata. Default is 0.
assetindex=1
#Maintains the full Timestamp index on your node. Default is 0.
timestampindex=1
#Maintains the full Spent index on your node. Default is 0.
spentindex=1

rpcconnect=127.0.0.1
rpcallowip=127.0.0.1

#Username and password - You can make this whatever you want.
rpcuser=yourusername
rpcpassword=yourpassword
```


Restart Ravencore, rebuilt index and go !