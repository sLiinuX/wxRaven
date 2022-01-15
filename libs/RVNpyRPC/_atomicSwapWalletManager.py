'''
Created on 10 janv. 2022

@author: slinux
'''




import requests
from libs.RVNpyRPC import RVNpyRPC
import json
#from jsonrpcclient.requests import Request
from requests import post, get
from decimal import *

import base64
import logging
import os

from ._atomicSwapTradeAndTransactions import TransactionUtils,  SwapTransaction, SwapTrade

try:
    from ._atomicSwap import AtomicSwapManager
except ImportError:
    pass

from datetime import datetime
import time

def call_if_set(fn_call, *args):
    if fn_call != None:
        fn_call(*args)





class AtomicSwapCacheStorage:

    def __init__(self, AtomicSwapMgr, _timeStampIt=False):
        super()
        self.swaps = []
        self.locks = []
        self.history = []
        self.addresses = []
        
        
        self.savepath = os.getcwd() + f"/userdata/atomicswap_session.cache"   
        if _timeStampIt:
            self._timestamp = round(time.time() * 1000) 
            self.savepath = os.getcwd() + f"/userdata/atomicswap_session_{self._timestamp}.cache"
            
            
        self.settings = {
               "data_path": self.get_path(),
              "fee_rate": 0.0125,
              "default_destination": "",
              "locking_mode": True,
              "active_rpc": 0,
              "update_interval": 5000,
              "server_url": "https://raventrader.net",
              "preview_timeout": 3,
              "protocol_handler_enabled": False
            }
        
        
        
        
        self.AtomicSwapMgr = AtomicSwapMgr
        
        self.RPCconnexion = AtomicSwapMgr.RPCconnexion
        self.RVNpyRPC = AtomicSwapMgr.RVNpyRPC
        
        

    def on_load(self):
        self.load_data()

    def on_close(self):
        #try:
        self.save_data()
        #except Exception as e:
        #    print("on_close Wallet error.")
        
    def ensure_directory(self,dir):
        if not os.path.exists(dir):
            os.makedirs(dir)


    def load_json(self, path, hook, title, default=[]):
        if not os.path.isfile(path):
            #logging.info("No {} records.".format(title))
            return default
        fSwap = open(path, mode="r")
        swapJson = fSwap.read()
        fSwap.close()
        data = json.loads(swapJson, object_hook=hook)
        #logging.info("Loaded {} {} records from disk".format(len(data), title))
        return data
    
    
    def save_json(self, path, data):
        #dataJson = json.dumps(data)#, default=lambda o: o.__dict__, indent=2)
        dataJson = json.dumps(data, default=lambda o: o.__dict__, indent=2)
        fSwap = open(path, mode="w")
        fSwap.truncate()
        fSwap.write(dataJson)
        fSwap.flush()
        fSwap.close()
    
    
    def init_list(self, items, hook):
        return [hook(item ) for item in items]
    
    def init_list_cast(self, items, hook):
        return [hook(item, self.AtomicSwapMgr ) for item in items]
#
# File I/O
#
    def load_data(self):
        loaded_data = self.load_json(self.get_path(), dict, "Storage")
        self.swaps = self.init_list_cast(
            loaded_data["trades"],         SwapTrade) if "trades" in loaded_data else []
        self.locks = self.init_list(
            loaded_data["locks"],               dict) if "locks" in loaded_data else []
        self.history = self.init_list_cast(
            loaded_data["history"],  SwapTransaction) if "history" in loaded_data else []
        self.addresses = self.init_list(loaded_data["addresses"],           dict) if "addresses" in loaded_data else [
            {"name": "default", "addresses": []}]

    def save_data(self):
        
        _swapsJsons = []
        
        for s in self.swaps:
            _swapsJsons.append(s.Export())
        
        save_payload = {
            "trades": _swapsJsons,
            "locks": self.locks,
            "history": self.history,
            "addresses": self.addresses
        }
        self.save_json(self.get_path(), save_payload)

    def get_path(self):
        #self.savepath = os.getcwd() + "/userdata/atomicswap_cache.cache"
        #base_path = os.path.expanduser(AppInstance.settings.read("data_path"))
        #self.ensure_directory(base_path)
        #print(f' saving atomic swap cache data in : {self.savepath}')
        return self.savepath#os.path.join(base_path, AppInstance.settings.rpc_save_path())



    
    
    def protocol_enabled(self):
        return self.settings["protocol_handler_enabled"]

    def protocol_path(self):
        return "rvnswap" if self.rpc_mainnet() else "rvntswap"

    def lock_mode(self):
        return self.settings["locking_mode"]

    def fee_rate(self):
        return self.settings["fee_rate"]











class WalletAddresses:

    RPCconnexion = None
    _walletPassphrase = ""
    
    def __init__(self,connexion, parent:RVNpyRPC, addresses=[]):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.RPCconnexion = connexion
        self.RVNpyRPC = parent
        
        
        
        super()
        self.address_pools = addresses
        
            
    
    def on_load(self, AppCacheStorage):
        self.address_pools = AppCacheStorage.addresses

    def on_close(self, AppCacheStorage):
        AppCacheStorage.addresses = self.address_pools
   
    
    
    def create_new_address(self):
        return self.RVNpyRPC.do_rpc("getnewaddress")

    def get_pool(self, pool_name="default", create=False):
        for pool in self.address_pools:
            if pool["name"] == pool_name:
                return pool
        if create:
            pool = {"name": pool_name, "addresses": []}
            self.address_pools.append(pool)
            return pool
        return None

    def add_to_pool(self, address, pool_name="default"):
        pool = self.get_pool(pool_name, create=True)
        if address in pool["addresses"]:
            return
        pool["addresses"].append(address)
        logging.info("Adding new address {} to pool [{}]".format(
            address, pool_name))

    def get_single_address(self, pool_name="default", avoid=[]):
        return self.get_address_set(1, pool_name, avoid)[0]

    def get_address_set(self, num_addresses=1, pool_name="default", avoid=[]):
        pool = self.get_pool(pool_name, create=True)
        valid_addrs = [addr for addr in pool["addresses"] if addr not in avoid]
        missing_addrs = num_addresses - len(valid_addrs)
        if missing_addrs > 0:
            for i in range(0, missing_addrs):
                new_addr = self.create_new_address()
                self.add_to_pool(new_addr, pool_name)
        # Re-Get latest list
        valid_addrs = [addr for addr in pool["addresses"] if addr not in avoid]
        return valid_addrs[:num_addresses]






class WalletManager:

    RPCconnexion = None
    RVNpyRPC = None 
    
    
    def __init__(self, AtomicSwapMgr):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        
        self.AtomicSwapMgr = AtomicSwapMgr
        
        self.RPCconnexion = AtomicSwapMgr.RPCconnexion
        self.RVNpyRPC = AtomicSwapMgr.RVNpyRPC
        
        
        
        self.txUtils = AtomicSwapMgr.txUtils#TransactionUtils(connexion, parent)
        
        super()
        self.waiting = []  # Waiting on confirmation
        self.addresses = WalletAddresses(AtomicSwapMgr.RPCconnexion, self.RVNpyRPC)
        self.trigger_cache = []
        self.on_swap_mempool = None
        self.on_swap_confirmed = None
        self.on_completed_mempool = None
        self.on_completed_confirmed = None

    def on_load(self):
        logging.info("Loading Virtual Wallet Datas")
        self.load_data()
        self.update_wallet()
        self.wallet_unlock_all()
        self.refresh_locks()

    def on_close(self):
        logging.info("Closing Virtual Wallet, saving...")
        self.save_data()

#
# File I/O
#
    def load_data(self):
        # TODO: Replace all local member access with app_storage directly?
        self.swaps = self.AtomicSwapMgr.CacheStorage.swaps
        self.locks = self.AtomicSwapMgr.CacheStorage.locks
        self.history = self.AtomicSwapMgr.CacheStorage.history
        self.addresses.on_load(self.AtomicSwapMgr.CacheStorage)
        # TODO: Better way to handle post-wallet-load events
        self.check_missed_history()
        logging.info("Wallet data loaded !")

    def save_data(self):
        # Needed?
        self.AtomicSwapMgr.CacheStorage.swaps = self.swaps
        self.AtomicSwapMgr.CacheStorage.locks = self.locks
        self.AtomicSwapMgr.CacheStorage.history = self.history
        self.addresses.on_close(self.AtomicSwapMgr.CacheStorage)
        logging.info("Wallet data saved !")
        
        

#
# Basic Operations
#

    def add_swap(self, swap_trade):
        self.swaps.append(swap_trade)
        logging.info("swap data added in virtual wallet !")

    def remove_swap(self, swap_trade):
        self.swaps.remove(swap_trade)
        for utxo in swap_trade.order_utxos:
            self.remove_lock(utxo=utxo)

    def add_completed(self, swap_transaction):
        if swap_transaction in self.history:
            logging.info("Duplicate order add")
            return
        logging.info("Adding to history...")
        self.history.append(swap_transaction)
        if swap_transaction.own:
            self.remove_lock(utxo=swap_transaction.utxo)

    def remove_completed(self, swap_transaction):
        self.history.remove(swap_transaction)

#
# Balance Calculation
#

    def calculate_balance(self):
        bal_total = [0, 0, 0]  # RVN, Unique Assets, Asset Total
        for utxo in self.utxos:
            bal_total[0] += utxo["amount"]
        # Take the distinct set of names
        lock_asset_names = [lock["asset"]
                            for lock in self.locks if "asset" in lock]
        self.my_asset_names = [name for name in set(
            [*self.assets.keys()] + lock_asset_names)]
        for asset in self.my_asset_names:
            bal_total[1] += 1
            asset_total = 0
            for outpoint in self.assets[asset]["outpoints"]:
                asset_total += outpoint["amount"]
            self.assets[asset]["balance"] = self.assets[asset]["available_balance"] = asset_total
            bal_total[2] += asset_total
        bal_avail = bal_total[:]

        for my_lock in self.locks:
            if my_lock["type"] == "rvn":
                bal_avail[0] -= my_lock["amount"]
            elif my_lock["type"] == "asset":
                asset_name = my_lock["asset"]
                asset_amt = my_lock["amount"]
                bal_avail[2] -= asset_amt
                if asset_name not in self.assets:
                    # This is almost certainly a stale order, just ignore it
                    continue
                self.assets[asset_name]["available_balance"] -= asset_amt

        self.available_balance = tuple(bal_avail)
        self.total_balance = tuple(bal_total)

    def rvn_balance(self):
        return self.available_balance[0]

    def asset_balance(self):
        return self.available_balance[2]

#
# Callbacks
#

    def __on_swap_mempool(self, transaction, trade):
        # TODO: Re-scan transaction to verify details of chain-executed trade
        trade.txid = transaction["txid"]
        trade.state = "pending"
        self.add_completed(trade)
        call_if_set(self.on_swap_mempool, transaction, trade)

    def __on_swap_confirmed(self, transaction, trade):
        trade.txid = transaction["txid"]
        trade.state = "completed"
        call_if_set(self.on_swap_confirmed, transaction, trade)

    def __on_completed_mempool(self, transaction, swap):
        swap.txid = transaction["txid"]
        swap.state = "pending"
        self.add_completed(swap)
        call_if_set(self.on_completed_mempool, transaction, swap)

    def __on_completed_confirmed(self, transaction, swap):
        swap.txid = transaction["txid"]
        swap.state = "completed"
        call_if_set(self.on_completed_confirmed, transaction, swap)

#
# Wallet Interaction
#

    def wallet_prepare_transaction(self):
        logging.info("Preparing for a transaction")
        if self.AtomicSwapMgr.CacheStorage.lock_mode():
            logging.info("Locking")
        else:
            logging.info("Non-Locking")

    def wallet_completed_transaction(self):
        logging.info("Completed a transaction")
        if self.AtomicSwapMgr.CacheStorage.lock_mode():
            logging.info("Locking")
        else:
            logging.info("Non-Locking")

    def swap_executed(self, swap, txid):
        self.add_waiting(txid, self.__on_completed_mempool,
                         self.__on_completed_confirmed, callback_data=swap)

    def num_waiting(self):
        return len(self.waiting)

    def add_waiting(self, txid, fnOnSeen=None, fnOnConfirm=None, callback_data=None):
        logging.info("Waiting on txid: {}".format(txid))
        self.waiting.append((txid, fnOnSeen, fnOnConfirm, callback_data))

    def clear_waiting(self):
        self.waiting.clear()

    def check_waiting(self):
        for waiting in self.waiting:
            (txid, seen, confirm, callback_data) = waiting
            tx_data = self.RVNpyRPC.do_rpc("getrawtransaction", txid=txid, verbose=True)
            if not tx_data:
                continue
            # TODO: Adjustable confirmations
            tx_confirmed = "confirmations" in tx_data and tx_data["confirmations"] >= 1

            if not tx_confirmed and txid not in self.trigger_cache:
                logging.info(
                    "Waiting txid {} confirmed in mempool.".format(txid))
                self.trigger_cache.append(txid)
                call_if_set(seen, tx_data, callback_data)
            elif tx_confirmed and txid in self.trigger_cache:
                logging.info("Waiting txid {} fully confirmed.".format(txid))
                self.trigger_cache.remove(txid)
                self.waiting.remove(waiting)
                call_if_set(confirm, tx_data, callback_data)
            elif tx_confirmed and txid not in self.trigger_cache:
                logging.info(
                    "Missed memcache for txid {}, direct to confirm.".format(txid))
                self.waiting.remove(waiting)
                call_if_set(seen, tx_data, callback_data)
                call_if_set(confirm, tx_data, callback_data)

    def wallet_lock_all_swaps(self):
        # first unlock everything
        self.wallet_unlock_all()
        # now build all orders and send it in one go
        locked_utxos = []
        for swap in self.swaps:
            for utxo in swap.order_utxos:
                locked_utxos.append(utxo)
        logging.info("Locking {} UTXO's from orders".format(len(locked_utxos)))
        self.wallet_lock_utxos(locked_utxos)

    def wallet_lock_utxos(self, utxos=[], lock=True):
        txs = []
        for utxo in utxos:
            (txid, vout) = self.txUtils.split_utxo(utxo)
            txs.append({"txid": txid, "vout": vout})
        self.RVNpyRPC.do_rpc("lockunspent", unlock=not lock, transactions=txs)

    def wallet_lock_single(self, txid=None, vout=None, utxo=None, lock=True):
        if utxo != None and txid == None and vout == None:
            (txid, vout) = self.txUtils.split_utxo(utxo)
        self.RVNpyRPC.do_rpc("lockunspent", unlock=not lock,
               transactions=[{"txid": txid, "vout": vout}])

    def load_wallet_locked(self):
        if self.AtomicSwapMgr.CacheStorage.lock_mode():
            wallet_locks = self.RVNpyRPC.do_rpc("listlockunspent")
            wallet_utxos = []
            for lock in wallet_locks:
                utxo_str = self.txUtils.make_utxo(lock)
                txout = self.RVNpyRPC.do_rpc("gettxout", txid=lock["txid"], n=int(
                    lock["vout"]), include_mempool=True)
                if txout:
                    utxo = self.txUtils.vout_to_utxo(txout, lock["txid"], int(lock["vout"]))
                    wallet_utxos.append(utxo_str)
                    if utxo["type"] == "rvn":
                        self.utxos.append(utxo)
                    elif utxo["type"] == "asset":
                        asset_name = utxo["asset"]
                        if asset_name not in self.assets:
                            self.assets[asset_name] = {"outpoints": []}
                        self.assets[asset_name]["outpoints"].append(utxo)
                else:
                    # If we don't get a txout from a lock, it's no longer valid (wallet keeps them around for some reason.....)
                    logging.info(
                        "Removing Stale Wallet lock: {}".format(utxo_str))
                    self.wallet_lock_single(utxo=utxo_str, lock=False)

    def wallet_unlock_all(self):
        self.RVNpyRPC.do_rpc("lockunspent", unlock=True)

    def invalidate_all(self):
        self.utxos = []
        self.assets = {}
        self.trigger_cache = []
        self.my_asset_names = []
        self.total_balance = (0, 0, 0)
        self.available_balance = (0, 0, 0)
        self.clear_waiting()

    def update_wallet(self):
        self.check_waiting()
        # Locked UTXO's are excluded from the list command
        utxos = self.RVNpyRPC.do_rpc("listunspent")
        # only include spendable UTXOs
        self.utxos = [utxo for utxo in utxos if utxo["spendable"]]

        # Pull list of assets for selecting
        self.assets = self.RVNpyRPC.do_rpc("listmyassets", asset="", verbose=True)

        # Load details of wallet-locked transactions, inserted into self.utxos/assets
        self.load_wallet_locked()

        removed_orders = self.search_completed()
        for (trade, utxo) in removed_orders:
            finished_order = trade.order_completed(utxo)
            transaction = self.txUtils.search_swap_tx(utxo)
            if transaction:
                txid = transaction["txid"]
                logging.info("Order Completed: TXID {}".format(txid))
                self.add_waiting(txid, self.__on_swap_mempool,
                                 self.__on_swap_confirmed, callback_data=finished_order)
            else:
                logging.info("Order executed on unknown transaction")

        # Remove any locks we can't find with the gettxout command
        self.clear_stale_locks()

        # Actual balance calculation
        self.calculate_balance()

        # Cheat a bit and embed the asset name in it's metadata. This simplified things later
        for name in self.my_asset_names:
            self.assets[name]["name"] = name

#
# Lock Management
#

    def add_lock(self, txid=None, vout=None, utxo=None):
        if utxo != None and txid == None and vout == None:
            (txid, vout) = self.txUtils.split_utxo(utxo)
        for lock in self.locks:
            if txid == lock["txid"] and vout == lock["vout"]:
                return  # Already added
        logging.info("Locking UTXO {}-{}".format(txid, vout))
        # True means this will be None when spent in mempool
        txout = self.RVNpyRPC.do_rpc("gettxout", txid=txid, n=vout, include_mempool=True)
        if txout:
            utxo = self.txUtils.vout_to_utxo(txout, txid, vout)
            self.locks.append(utxo)
            if self.AtomicSwapMgr.CacheStorage.lock_mode():
                self.wallet_lock_single(txid, vout)

    def remove_lock(self, txid=None, vout=None, utxo=None):
        if utxo != None and txid == None and vout == None:
            (txid, vout) = self.txUtils.split_utxo(utxo)
        found = False
        for lock in self.locks:
            if txid == lock["txid"] and int(vout) == int(lock["vout"]):
                self.locks.remove(lock)
                found = True
        if not found:
            return
        logging.info("Unlocking UTXO {}-{}".format(txid, vout))
        # in wallet-lock mode we need to return these to the wallet
        if self.AtomicSwapMgr.CacheStorage.lock_mode():
            self.wallet_lock_single(txid, vout, lock=False)

    def refresh_locks(self, clear=False):
        if clear:
            self.wallet_unlock_all()
            self.locks = []
        for swap in self.swaps:
            for utxo in swap.order_utxos:
                self.add_lock(utxo=utxo)
        if self.AtomicSwapMgr.CacheStorage.lock_mode():
            self.wallet_lock_all_swaps()

    def lock_quantity(self, type):
        if type == "rvn":
            return sum([float(lock["amount"]) for lock in self.locks if lock["type"] == "rvn"])
        else:
            return sum([float(lock["amount"]) for lock in self.locks if lock["type"] == "asset" and lock["name"] == type])

    def check_missed_history(self):
        # Re-Add listeners for incomplete orders, should be fully posted, but add events so full sequence can happen
        for pending_order in [hist_order for hist_order in self.history if hist_order.state != "completed"]:
            if pending_order.utxo not in self.trigger_cache:
                swap_tx = self.txUtils.search_swap_tx(pending_order.utxo)
                if swap_tx:
                    if pending_order.own:
                        self.add_waiting(
                            swap_tx["txid"], self.__on_swap_mempool, self.__on_swap_confirmed, pending_order)
                    else:
                        self.add_waiting(
                            swap_tx["txid"], self.__on_completed_mempool, self.__on_completed_confirmed, pending_order)
                else:
                    logging.info("Failed to find transaction for presumably completed UTXO {}".format(
                        pending_order.utxo))

    def search_completed(self, include_mempool=True):
        all_found = []
        for trade in self.swaps:
            for utxo in trade.order_utxos:
                if self.swap_utxo_spent(utxo, in_mempool=include_mempool, check_cache=False):
                    all_found.append((trade, utxo))
        return all_found

    def clear_stale_locks(self):
        for lock in self.locks:
            if not self.RVNpyRPC.do_rpc("gettxout", txid=lock["txid"], n=lock["vout"], include_mempool=True):
                logging.info("Removing Stale Lock: {}".format(lock))
                self.remove_lock(utxo=self.txUtils.make_utxo(lock))

#
# UTXO Searching
#

    def find_utxo(self, type, quantity, name=None, exact=True, include_locked=False, skip_rounded=True, sort_utxo=False):
        logging.info("Find {} UTXO: {} Exact: {} Include Locks: {}".format(
            type, quantity, exact, include_locked))
        available = self.get_utxos(type, name, include_locked=include_locked)
        for utxo in available:
            if(float(utxo["amount"]) == float(quantity) and exact) or (float(utxo["amount"]) >= float(quantity) and not exact):
                return utxo
        return None

    def find_utxo_multiple_exact(self, type, quantity, name=None, include_locked=False):
        logging.info("Find UTXO Multiple Exact: {} {} {} Include Locks: {}".format(
            quantity, type, name, include_locked))
        return [utxo for utxo in self.get_utxos(type, name=name, include_locked=include_locked) if utxo["amount"] == quantity]

    def get_utxos(self, type, name=None, include_locked=False):
        results = []
        if type == "rvn":
            results = [utxo for utxo in self.utxos]
        elif type == "asset":
            results = [utxo for utxo in self.assets[name]["outpoints"]]
        else:  # Use the type name itself
            results = [utxo for utxo in self.assets[type]["outpoints"]]
        if include_locked:
            return results
        else:
            return [utxo for utxo in results if not self.is_locked(utxo)]

    def find_utxo_set(self, type, quantity, mode="combine", name=None, include_locked=False):
        found_set = None
        total = 0

        sorted_set = sorted(self.get_utxos(
            type, name, include_locked=include_locked), key=lambda utxo: utxo["amount"])

        if mode == "combine":
            # Try to combine as many UTXO's as possible into a single Transaction
            # This raises your transaction fees slighty (more data) but is ultimately a good thing for the network
            # Don't need to do anything actualy b/c default behavior is to go smallest-to-largest
            # However, if we have a single, unrounded UTXO that is big enough. it's always more efficient to use that instead
            quick_check = self.find_utxo(
                type, quantity, name=name, include_locked=include_locked, exact=False, sort_utxo=True)
            if quick_check:
                # If we have a single UTXO big enough, just use it and get change. sort_utxo ensures we find the smallest first
                found_set = [quick_check]
                total = quick_check["amount"]
        elif mode == "minimize":
            # Minimize the number of UTXO's used, to reduce transaction fees
            # This minimizes transaction fees but
            quick_check = self.find_utxo(
                type, quantity, name=name, include_locked=include_locked, exact=False, sort_utxo=True)
            quick_check_2 = self.find_utxo(
                type, quantity, name=name, include_locked=include_locked, exact=False, skip_rounded=False, sort_utxo=True)
            if quick_check:
                # If we have a single UTXO big enough, just use it and get change. sort_utxo ensures we find the smallest first
                found_set = [quick_check]
                total = quick_check["amount"]
            elif quick_check_2:
                # In this case we had a large enough single UTXO but it was an evenly rounded one (and no un-rounded ones existed)
                found_set = [quick_check_2]
                total = quick_check_2["amount"]
            else:
                # Just need to reverse the search to make it build from the fewest UTXO's
                sorted_set.reverse()

        if found_set == None:
            found_set = []
            while total < quantity and len(sorted_set) > 0:
                removed = sorted_set.pop(0)
                total += removed["amount"]
                found_set.append(removed)

        if float(total) >= float(quantity):
            logging.info("{} UTXOs: {} Requested: {:.8g} Total: {:.8g} Change: {:.8g}".format(
                type, len(found_set), quantity, total, total - quantity))
            return (total, found_set)
        else:
            logging.info("Not enough {} funds found. Requested: {:.8g} Total: {:.8g} Missing: {:.8g}".format(
                type, quantity, total, total-quantity))
            return (None, None)

    # check if a swap's utxo has been spent
    # if so then the swap has been executed!
    def swap_utxo_spent(self, utxo, in_mempool=True, check_cache=True):
        if check_cache:
            # This will always go away immediately w/ mempool. so in_mempool doesnt work here
            return self.search_utxo(utxo) == None
        else:
            (txid, vout) = self.txUtils.split_utxo(utxo)
            txout = self.RVNpyRPC.do_rpc("gettxout", txid=txid, n=vout,
                           include_mempool=in_mempool)
            return txout == None

    # return ({type, utxo}, amount)
    def search_utxo(self, utxo_str):
        (txid, vout) = self.txUtils.split_utxo(utxo_str)
        for utxo in self.utxos:
            if utxo["txid"] == txid and utxo["vout"] == vout:
                return utxo
        for asset_name in self.my_asset_names:
            for a_utxo in self.assets[asset_name]["outpoints"]:
                if a_utxo["txid"] == txid and a_utxo["vout"] == vout:
                    return a_utxo
        return None

    def is_locked(self, utxo):
        for lock in self.locks:
            if lock["txid"] == utxo["txid"] and lock["vout"] == utxo["vout"]:
                return True
        return False

    def is_taken(self, utxo, ignore_locks=False):
        expected = self.txUtils.join_utxo(utxo["txid"], utxo["vout"])
        if not ignore_locks:
            if self.is_locked(utxo):
                return True
        for swap in self.swaps:
            if expected in swap.order_utxos:
                return True
        return False
    
    
    
    
    
    def fund_asset_transaction_raw(self, fn_rpc, asset_name, quantity, vins, vouts, asset_change_addr=None):
        # Search for enough asset UTXOs
        (asset_utxo_total, asset_utxo_set) = self.find_utxo_set(
            "asset", quantity, name=asset_name, include_locked=True)
        # Add our asset input(s)
        for asset_utxo in asset_utxo_set:
            vins.append({"txid": asset_utxo["txid"], "vout": asset_utxo["vout"]})
    
        if not asset_change_addr:
            asset_change_addr = self.addresses.get_single_address(
                "asset_change")
    
        # Add asset change if needed
        if(asset_utxo_total > quantity):
            # TODO: Send change to address the asset UTXO was originally sent to
            logging.info("Asset change being sent to {}".format(asset_change_addr))
            vouts[asset_change_addr] = self.txUtils.make_transfer(
                asset_name, asset_utxo_total - quantity)
    
    
    def fund_transaction_final(self, fn_rpc, send_rvn, recv_rvn, target_addr, vins, vouts, original_txs):
        # Cost represents rvn sent to the counterparty, since we adjust send_rvn later
        cost = send_rvn
    
        # If this is a swap, we need to add pseduo-funds for fee calc
        if recv_rvn == 0 and send_rvn == 0:
            # Add dummy output for fee calc
            vouts[target_addr] = round(
                sum([self.txUtils.calculate_fee(tx) for tx in original_txs]) * 4, 8)
    
        if recv_rvn > 0 and send_rvn == 0:
            # If we are not supplying rvn, but expecting it, we need to subtract fees from that only
            # So add our output at full value first
            vouts[target_addr] = round(recv_rvn, 8)
    
        # Make an initial guess on fees, quadruple should be enough to estimate actual fee post-sign
        fee_guess = self.txUtils.calculated_fee_from_size(self.txUtils.calculate_size(vins, vouts)) * 4
        send_rvn=float(send_rvn)
        send_rvn += float(fee_guess ) # add it to the amount required in the UTXO set
    
        logging.info("Funding Raw Transaction. Send: {:.8g} RVN. Get: {:.8g} RVN".format(
            send_rvn, recv_rvn))
    
        if send_rvn > 0:
            # Determine a valid UTXO set that completes this transaction
            (utxo_total, utxo_set) = self.find_utxo_set("rvn", send_rvn)
            if utxo_set is None:
                #show_error("Not enough UTXOs", "Unable to find a valid UTXO set for {:.8g} RVN".format(send_rvn))
                print("Not enough UTXOs", "Unable to find a valid UTXO set for {:.8g} RVN".format(send_rvn))
                return False
            send_rvn = utxo_total  # Update for the amount we actually supplied
            for utxo in utxo_set:
                vins.append({"txid": utxo["txid"], "vout": utxo["vout"]})
    
        # Then build and sign raw to estimate fees
        sizing_raw = fn_rpc("createrawtransaction", inputs=vins, outputs=vouts)
        sizing_raw = fn_rpc("combinerawtransaction", txs=[
                            sizing_raw] + original_txs)
        # Need to calculate fees against signed message
        sizing_signed = fn_rpc("signrawtransaction", hexstring=sizing_raw)
        fee_rvn = self.txUtils.calculate_fee(sizing_signed["hex"])
        out_rvn = (float(send_rvn) + float(recv_rvn)) - float(cost) - float(fee_rvn)
        vouts[target_addr] = round(out_rvn, 8)
    
        logging.info("Funding result: Send: {:.8g} Recv: {:.8g} Fee: {:.8g} Change: {:.8g}".format(
            send_rvn, recv_rvn, fee_rvn, out_rvn))
    
        return True
    
    
    
    