import time
import json


class Account:
    def __init__(self, config_file, asset, rvn, ipfs):
        with open(config_file, 'r') as config_file_handle:
            self.config = json.load(config_file_handle)
        self.rvn = rvn
        self.ipfs = ipfs
        self.asset = asset

    def __getattr__(self, name):
        if name.startswith('__') and name.endswith('__'):
            # Python internal stuff
            raise AttributeError

        if name in self.config:
            return self.config[name]
        elif name in self.__dict__:
            return self.__dict__[name]
        else:
            raise AttributeError

    def send_kaw(self, message):
        hash = self.ipfs.add_json(self.compile_message(message))
        self.ipfs.pin.add(hash)
        # transfer asset_name, qty, to_address, message, expire_time, change_address, asset_change_address
        return self.rvn.transfer(self.asset, 1, self.address, hash, 0, self.address, self.address)

    def compile_message(self, text, multimedia=None):
        message = dict()
        message["sender"] = self.address
        message["profile"] = {"ipfs_hash": self.profile_ipfs_hash, "timestamp": self.profile_timestamp}
        message["timestamp"] = time.time()
        message["message"] = text
        if multimedia:
            message["multimedia"] = [media["ipfs_hash"] for media in multimedia]
        return message

    def update_profile(self):
        message = dict()
        self.config["profile_timestamp"] = time.time()
        for att in self.config:
            if att == "profile_timestamp":
                message["timestamp"] = self.config[att]
            elif att == "profile_hash":
                pass
            else:
                message[att] = self.config[att]

        hash = self.ipfs.add_json(message)
        self.ipfs.pin.add(hash)
        self.config["profile_hash"] = hash
        with open("config.json", 'w') as cf:
            json.dump(self.config, cf)

        return self.rvn.transfer(self.asset, 0.5, self.address, hash, 0, self.address, self.address)
