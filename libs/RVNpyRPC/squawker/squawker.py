import squawker_errors
from account import Account
from message import Message
import json
from utils import tx_to_self
from serverside import *

debug = 0


def find_latest_messages(asset=ASSETNAME, count=50):
    latest = []
    messages = dict()
    messages["addresses"] = list(rvn.listaddressesbyasset(asset, False)["result"])
    messages["assetName"] = asset
    deltas = rvn.getaddressdeltas(messages)["result"]
    for tx in deltas:
        if tx["satoshis"] == 100000000 and tx_to_self(tx):
            transaction = rvn.decoderawtransaction(rvn.getrawtransaction(tx["txid"])["result"])["result"]
            for vout in transaction["vout"]:
                vout = vout["scriptPubKey"]
                if vout["type"] == "transfer_asset" and vout["asset"]["name"] == asset and vout["asset"]["amount"] == 1.0:
                    kaw = {"address": vout["addresses"], "message": vout["asset"]["message"], "block": transaction["locktime"]}
                    latest.append(kaw)
    return sorted(latest[:count], key=lambda message: message["block"], reverse=True)


# def get_message(message):
#     ipfs_hash = message["message"]
#     doc = ipfs.cat(ipfs_hash)
#     return doc
#
# def get_message_context(message):
#     profile_ipfs_hash = find_latest_profile(message["sender"])["message"]
#     profile = ipfs.cat(profile_ipfs_hash)
#     return json.loads(profile)


def recursive_print(dictionary, spacing=0):
    if isinstance(dictionary, str):
        print(dictionary)
    elif isinstance(dictionary, list):
        print(dictionary)
    else:
        for part in dictionary:

            if isinstance(dictionary[part], dict):
                recursive_print(dictionary[part], spacing=spacing+1)
            else:
                print("  "*spacing, part)
                print("  "*spacing, "  ", dictionary[part])
                print()




"""
TODOs:

find messages from address
    get asset list for your tracked assets 
    pull messages (sending 1 to oneself)

display message
    get ipfs hash 
    pull profiles of messengers (latest sending 0.5 to oneself)
    get profile pic from profile
    pull profile pic
    locally cache profile/pic hashes
    display message profile picture in gui
    
lookup mentions
    pull address look for 0.01 transactions to the address
    get transactions txid's messages
    get message and display message  

format for tagging in a message
    send small amount of coin to addresses messaging the txid
    used for mentions and hashtags

# use RPC commands for endpoint to generate # addresses.

setup atomic swaps for marketplace sales.
    

"""

if __name__ == "__main__":
    usr = Account("config.json", ASSETNAME, rvn, ipfs)
    while True:
        intent = input("Kaw (1) | Read (2) | Read XML (3) | Update Profile (4) | Exit (5)")
        if str(intent).strip() == "1":
            msg = input("What would you like to kaw?")
            output = usr.send_kaw(msg)
            print(output)
        elif str(intent).strip() == "2":
            latest = find_latest_messages()
            for m in latest:
                try:
                    print(Message(m))
                except squawker_errors.NotMessage:
                    pass
        elif str(intent).strip() == "3":
            latest = find_latest_messages()
            for m in latest:
                try:
                    print(Message(m).xml())
                except squawker_errors.NotMessage:
                    pass
        elif str(intent).strip() == "4":
            msg = input("Are you sure?(y/N)")
            if msg.upper() == "Y":
                print(usr.update_profile())
        else:
            exit(0)



