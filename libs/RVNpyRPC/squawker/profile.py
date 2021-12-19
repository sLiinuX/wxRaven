from utils import tx_to_self
from serverside import *
import squawker_errors
import json


class Profile():
    def __init__(self, address):
        if isinstance(address, list):
            address = address[0]
        self.address = address
        self.ipfs_hash = self.find_latest_profile()["message"]
        self.picture = None
        self.validate(self.ipfs_hash)

    def validate(self, ipfs_hash):
        try:
            data = json.loads(ipfs.cat(ipfs_hash))
            for key in data:
                self.__dict__[key] = data[key]
        except json.decoder.JSONDecodeError:
            raise squawker_errors.InvalidProfileJSON(f"{ipfs_hash} did not decode")
        try:
            self.picture = ipfs.cat(self.profile_picture)
        except AttributeError:
            # Fails if there is no photo or is doesn't work.
            self.picture = False
            pass

    def find_latest_profile(self):
        latest = []
        messages = dict()
        messages["addresses"] = [self.address]
        messages["assetName"] = ASSETNAME
        deltas = rvn.getaddressdeltas(messages)["result"]
        for tx in deltas:
            if tx["satoshis"] == 50000000 and tx_to_self(tx, 0.5):
                transaction = rvn.decoderawtransaction(rvn.getrawtransaction(tx["txid"])["result"])["result"]
                for vout in transaction["vout"]:
                    vout = vout["scriptPubKey"]
                    if vout["type"] == "transfer_asset" and vout["asset"]["name"] == ASSETNAME and vout["asset"][
                        "amount"] == 0.5:
                        kaw = {"address": vout["addresses"], "message": vout["asset"]["message"],
                               "block": transaction["locktime"]}
                        latest.append(kaw)
        return sorted(latest[:1], key=lambda message: message["block"], reverse=True)[0]

    def basic_xml(self):
        return f"""
        <profile>
            <profile_image>
                {self.picture}
            </profile_image>
            <profile_name>
                {self.name}
            </profile_name>
        </profile>"""



