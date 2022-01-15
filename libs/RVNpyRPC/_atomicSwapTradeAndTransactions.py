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


import time

try:
    from ._atomicSwap import AtomicSwapManager
except ImportError:
    pass


class TransactionUtils():
    
    RPCconnexion = None
    _walletPassphrase = ""
    
    def __init__(self, AtomicSwapMgr , walletPassphrase=""):
        '''
        Constructor
        '''
        #super().__init__(self,connexion)
        self.AtomicSwapMgr = AtomicSwapMgr
        
        self.RPCconnexion = AtomicSwapMgr.RPCconnexion
        self.RVNpyRPC = AtomicSwapMgr.RVNpyRPC
        
        
        self._walletPassphrase = walletPassphrase
        
        
    def setWalletPassphrase(self, _walletPassphrase):
        self._walletPassphrase = _walletPassphrase
    
    def b64_to_hex(self,b64_str):
        d = base64.b64decode(b64_str)
        return ''.join(['{:02x}'.format(i) for i in d])
    
    def make_transfer(self,name, quantity):
        return {"transfer": {name: round(float(quantity), 8)}}


    def join_utxo(self,txid, n):
        return "{}-{}".format(txid, n)
    
    
    def make_utxo(self,order):
        return "{}-{}".format(order["txid"], order["vout"])
    
    
    def split_utxo(self,utxo):
        (txid, n) = utxo.split("-")
        return (txid, int(n))
    
    
    def utxo_copy(self,vin):
        if "sequence" in vin:
            return {"txid": vin["txid"], "vout": int(vin["vout"]), "sequence": int(vin["sequence"])}
        else:
            return {"txid": vin["txid"], "vout": int(vin["vout"])}
    
    
    def vout_to_utxo(self,vout, txid, n):
        if "scriptPubKey" in vout:
            if "asset" in vout["scriptPubKey"]:
                return {"txid": txid, "vout": n, "type": "asset", "amount": vout["scriptPubKey"]["asset"]["amount"], "asset": vout["scriptPubKey"]["asset"]["name"]}
            else:
                return {"txid": txid, "vout": n, "type": "rvn", "amount": vout["value"]}
        else:
            return {"txid": txid, "vout": n, "type": "unknown"}
    
    
    def make_prefill(self,asset, quantity=1, unit_price=1):
        return {"asset": asset["name"], "quantity": quantity, "unit_price": unit_price}
    
    
    def dup_transaction(self, tx, vins=[], vouts={}):
        for old_vin in tx["vin"]:
            vins.append(
                {"txid": old_vin["txid"], "vout": old_vin["vout"], "sequence": old_vin["sequence"]})
        for old_vout in sorted(tx["vout"], key=lambda vo: vo["n"]):
            vout_script = old_vout["scriptPubKey"]
            vout_addr = vout_script["addresses"][0]
            if("asset" in vout_script):
                vouts[vout_addr] = self.make_transfer(
                    vout_script["asset"]["name"], vout_script["asset"]["amount"])
            else:
                vouts[vout_addr] = old_vout["value"]
        return vins, vouts


    def search_swap_tx(self, utxo):
        (txid, vout) = self.split_utxo(utxo)
        wallet_tx = self.RVNpyRPC.do_rpc("listtransactions", account="", count=10)
        for tx in wallet_tx:
            details = self.RVNpyRPC.do_rpc("getrawtransaction", txid=tx["txid"], verbose=True)
            for tx_vin in details["vin"]:
                if ("txid" in tx_vin and "vout" in tx_vin) and \
                        (tx_vin["txid"] == txid and tx_vin["vout"] == vout):
                    return tx
        logging.info("Unable to find transaction for completed swap")
        return None  # If we don't find it 10 blocks back, who KNOWS what happened to it    
    
    
    
    def decode_full(self,txid, isTestNet=False):
        local_decode = self.RVNpyRPC.do_rpc("getrawtransaction",
                              log_error=False, txid=txid, verbose=True)
        if local_decode and "error" not in local_decode:
            result = local_decode
        else:
            #rpc = AppInstance.settings.rpc_details()
            # TODO: Better way of handling full decode
            tx_url = "https://rvnt.cryptoscope.io/api/getrawtransaction/?txid={}&decode=1" if isTestNet\
                else "https://rvn.cryptoscope.io/api/getrawtransaction/?txid={}&decode=1"
            logging.info("Query Full: {}".format(tx_url.format(txid)))
            resp = get(tx_url.format(txid))
            if resp.status_code != 200:
                logging.info("Error fetching raw transaction")
            result = json.loads(resp.text)
        return result
    
    
    def calculate_fee(self,transaction_hex):
        return self.calculated_fee_from_size(len(transaction_hex) / 2)


    def calculated_fee_from_size(self,size):
        return self.AtomicSwapMgr.CacheStorage.fee_rate() * (size / 1024)

    def calculate_size(self, vins, vouts):
        return 12 + (len(vins) * 148) + (len(vouts) * (9 + 25))
    


    #Remapped in _wallet Class
    def requires_unlock(self):
        # returns None if no password set
        phrase_test = self.RVNpyRPC.do_rpc("help", command="walletpassphrase")
        return phrase_test and phrase_test.startswith("walletpassphrase")
    
    #Remapped in _wallet Class
    def check_unlock(self, timeout=10):
        #rpc = AppInstance.settings.rpc_details()
        if self.requires_unlock():
            logging.info("Unlocking Wallet for {}s".format(timeout))
            self.RVNpyRPC.do_rpc("walletpassphrase", passphrase=self._walletPassphrase, timeout=timeout)






class SwapTransaction():

    
    def __init__(self, dict, AtomicSwapMgr, decoded=None):
        
        
        self.decoded = decoded
        #self.RPCconnexion = connexion
        #self.RVNpyRPC = parent
        
        #self.txUtils = TransactionUtils(connexion, parent)
        vars(self).update(dict)
        self.AtomicSwapMgr = AtomicSwapMgr
        
        self.RPCconnexion = AtomicSwapMgr.RPCconnexion
        self.RVNpyRPC = AtomicSwapMgr.RVNpyRPC
        self.txUtils = AtomicSwapMgr.txUtils
        self.WalletMgr = AtomicSwapMgr.WalletMgr
        
        

    #def __repr__(self):
    #    return str(self.raw)
    
    def __repr__(self):
        return str(self.Export())
    
    def toJSON(self):
        #return json.dumps(self.Export())
        return json.dumps(self.Export(), default=lambda o: '<not serializable>')
        #return json.dumps(self,
        #  default = lambda o: o.__dict__,
        #  sort_keys = True, indent = 2)
        
        
    def Export(self):
        #data = {
        #        '__class__': self.__class__.__name__,
        #        '__module__': self.__module__
        #       }
        data={}
        data.update(self.__dict__)
        try:
            data.pop('RPCconnexion')
            data.pop('RVNpyRPC')
            data.pop('AtomicSwapMgr')
            data.pop('txUtils')
            data.pop('WalletMgr')
        except :
            pass    
        return data

    def total_price(self):
        # Don't need to multiply
        if self.type == "buy":
            return float(self.in_quantity)
        elif self.type == "sell":
            return float(self.out_quantity)
        elif self.type == "trade":
            # In the case of a trade, consider the quantity of our asset, to be the "price"
            return float(self.in_quantity)
        else:
            return 0

    def quantity(self):
        if self.type == "buy":
            return float(self.out_quantity)
        elif self.type == "sell":
            return float(self.in_quantity)
        elif self.type == "trade":
            # In the case of a trade, consider the desired asset to be the quantity
            return float(self.out_quantity)
        else:
            return 0

    def unit_price(self):
        qty = self.quantity()
        return (0 if qty == 0 else self.total_price() / qty)

    def set_unit_price(self, new_price):
        qty = self.quantity()
        if self.type == "buy":
            self.in_quantity = new_price * qty
        elif self.type == "sell":
            self.out_quantity = new_price * qty
        elif self.type == "trade":
            self.in_quantity = new_price * qty

    def asset(self):
        if self.type == "buy":
            return self.out_type
        elif self.type == "sell":
            return self.in_type
        elif self.type == "trade":
            # In the case of a trade, consider the desired asset to be the "asset" of the trade
            return self.out_type
        else:
            return "N/A"

    # This is run by Alice when she wants to create an order
    def sign_partial(self):
        (txid, vout) = self.txUtils.split_utxo(self.utxo)
        vin = {"txid": txid, "vout": vout, "sequence": 0}
        if self.type == "buy":
            vout = {self.destination: self.txUtils.make_transfer(
                self.out_type, self.out_quantity)}
        elif self.type == "sell":
            vout = {self.destination: self.total_price()}
        elif self.type == "trade":
            vout = {self.destination: self.txUtils.make_transfer(
                self.out_type, self.out_quantity)}

        self.txUtils.check_unlock()

        raw_tx = self.RVNpyRPC.do_rpc("createrawtransaction", inputs=[vin], outputs=vout)

        # TODO: Better user interaction here
        signed_raw = self.RVNpyRPC.do_rpc("signrawtransaction", hexstring=raw_tx,
                            prevtxs=None, privkeys=None, sighashtype="SINGLE|ANYONECANPAY")

        self.raw = signed_raw["hex"]
        return self.raw

    # This is run by Bob when he wants to complete an order
    def complete_order(self):
        final_vin = [{"txid": self.decoded["vin"]["txid"], "vout":self.decoded["vin"]
                      ["vout"], "sequence":self.decoded["vin"]["sequence"]}]
        final_vout = {self.destination: self.decoded["vout_data"]}

        tx_allowed = False
        tx_final = None

        send_rvn = 0
        recv_rvn = 0

        # Create our destination for assets
        # NOTE: self.destination is where our raven is going, not our destination for assets
        target_addr = self.WalletMgr.addresses.get_single_address(
            "order_destination")
        logging.info("Output is being sent to {}".format(target_addr))

        # Unlock for signing during fee calc + sending
        self.txUtils.check_unlock(10)

        ##
        # Complete sell Orders (we are buying an asset with rvn)
        ##
        if self.type == "sell":
            logging.info("You are purchasing {} x [{}] for {} RVN".format(
                self.in_quantity, self.asset(), self.total_price()))

            # Send output assets to target_addr
            final_vout[target_addr] = self.txUtils.make_transfer(
                self.asset(), self.quantity())
            # This much rvn must be supplied at the end
            send_rvn = self.total_price()

        ##
        # Complete buy orders (we are selling an asset for rvn)
        ##
        elif self.type == "buy":
            # Buy order means WE are selling, We need to provide assets
            logging.info("You are selling {} x [{}] for {} RVN"
                         .format(self.out_quantity, self.asset(), self.total_price()))

            # Add needed asset inputs
            self.WalletMgr.fund_asset_transaction_raw(
                self.RVNpyRPC.do_rpc, self.out_type, self.out_quantity, final_vin, final_vout)
            # Designate how much rvn we expect to get
            recv_rvn = self.total_price()

        ##
        # Complete trade orders (We are exchange assets for assets)
        ##
        elif self.type == "trade":
            # Trade order means WE are providing and reciving assets
            logging.info("You are trading {}x of YOUR [{}] for {}x of THEIR [{}]"
                         .format(self.out_quantity, self.out_type, self.in_quantity, self.in_type))

            # Send output assets to target_addr
            final_vout[target_addr] = self.txUtils.make_transfer(
                self.in_type, self.in_quantity)
            # Add needed asset inputs
            self.WalletMgr.fund_asset_transaction_raw(
                self.RVNpyRPC.do_rpc, self.out_type, self.out_quantity, final_vin, final_vout)

        # Unkown order type
        else:
            raise Exception("Unkown swap type {}".format(self.type))

        # We only have a single output when buying (the rvn) so no need to generate an addr in that case.
        # Just use the supplied one
        rvn_addr = target_addr if self.type == "buy" else self.WalletMgr.addresses.get_single_address(
            "change")

        # Add needed ins/outs needed to handle the rvn disbalance in the transaction
        funded_finale = self.WalletMgr.fund_transaction_final(
            self.RVNpyRPC.do_rpc, send_rvn, recv_rvn, rvn_addr, final_vin, final_vout, [self.raw])
        if not funded_finale:
            raise Exception("Funding raw transaction failed")

        # Build final funded raw transaction
        final_raw = self.RVNpyRPC.do_rpc("createrawtransaction",
                           inputs=final_vin, outputs=final_vout)
        # Merge the signed tx from the original order
        combined_raw = self.RVNpyRPC.do_rpc("combinerawtransaction",
                              txs=[final_raw, self.raw])
        # Sign our inputs/outputs
        signed_hex = self.RVNpyRPC.do_rpc("signrawtransaction",
                            hexstring=combined_raw)["hex"]
        # Finally, Test mempool acceptance
        mem_accept = self.RVNpyRPC.do_rpc("testmempoolaccept", rawtxs=[signed_hex])

        if(mem_accept and mem_accept[0]["allowed"]):
            logging.info("Accepted to mempool!")
            tx_allowed = True
            tx_final = signed_hex
        elif(mem_accept and mem_accept[0]["reject-reason"] == "66: min relay fee not met"):
            logging.info("Min fee not met")
            #raise Exception("Fee Error")
            tx_allowed = True
            tx_final = signed_hex
        else:
            logging.info(mem_accept)
            logging.info("Final Raw")
            logging.info(final_raw)
            if final_raw:
                logging.info("Decoded")
                logging.info(
                    self.RVNpyRPC.do_rpc("decoderawtransaction", hexstring=final_raw))
            logging.info("!!Error!!")
            print('error in TX, retry')
            raise Exception("Error Building TX")

        # remove this so it doesn't get encoded to json later
        del(self.decoded)
        return tx_final


    def composite_transactions(self,swaps):
        total_inputs = {}
        total_outputs = {}
        canceled_assets = {}
        for swap in swaps:
            total_inputs[swap.in_type] = (
                total_inputs[swap.in_type] if swap.in_type in total_inputs else 0) + swap.in_quantity
            total_outputs[swap.out_type] = (
                total_outputs[swap.out_type] if swap.out_type in total_outputs else 0) + swap.out_quantity
        logging.info(
            "Sub-Total: In {} - Out {}".format(total_inputs, total_outputs))
        # These assets need to be supplied by us (outputs) but were also supplied (inputs)
        for dup_asset in [asset for asset in total_outputs.keys() if asset in total_inputs]:
            if total_inputs[dup_asset] >= total_outputs[dup_asset]:
                # More was provided than we need to supply, net credit
                total_inputs[dup_asset] -= total_outputs[dup_asset]
                canceled_assets[dup_asset] = total_outputs[dup_asset]
                del total_outputs[dup_asset]
                logging.info("Net Credit {}x [{}]".format(
                    total_inputs[dup_asset], dup_asset))
            elif total_inputs[dup_asset] < total_outputs[dup_asset]:
                # More was requested than supplied in inputs, net debit
                total_outputs[dup_asset] -= total_inputs[dup_asset]
                canceled_assets[dup_asset] = total_inputs[dup_asset]
                del total_inputs[dup_asset]
                logging.info("Net Debit {}x [{}]".format(
                    total_outputs[dup_asset], dup_asset))
        logging.info("Total: In {} - Out {} (Cancelled: {})".format(total_inputs,
                     total_outputs, canceled_assets))

        mega_tx_vins = []
        mega_tx_vouts = {}

        for swap in swaps:
            swap_decoded = self.RVNpyRPC.do_rpc("decoderawtransaction",
                                  log_error=False, hexstring=swap.raw)
            if "SINGLE|ANYONECANPAY" not in swap_decoded["vin"][0]["scriptSig"]["asm"]:
                logging.info("Transaction not signed with SINGLE|ANYONECANPAY")
                return None
            self.txUtils.dup_transaction(swap_decoded, mega_tx_vins, mega_tx_vouts)

        logging.info("Un-Funded Inputs: {}".format(mega_tx_vins))
        logging.info("Un-Funded Outputs: {}".format(mega_tx_vouts))

        send_rvn = 0
        recv_rvn = 0

        # Fund all requested assets in the transaction
        for supply_asset in total_outputs.keys():
            if supply_asset == "rvn":
                send_rvn = total_outputs["rvn"]
            else:
                self.WalletMgr.fund_asset_transaction_raw(
                    self.RVNpyRPC.do_rpc, supply_asset, total_outputs[supply_asset], mega_tx_vins, mega_tx_vouts)

        for recieve_asset in total_inputs.keys():
            if recieve_asset == "rvn":
                recv_rvn = total_inputs["rvn"]
            else:
                asset_addr = self.WalletMgr.addresses.get_single_address(
                    "change")
                mega_tx_vouts[asset_addr] = self.txUtils.make_transfer(
                    recieve_asset, total_inputs[recieve_asset])

        logging.info("Asset-Funded Inputs: {}".format(mega_tx_vins))
        logging.info("Asset-Funded Outputs: {}".format(mega_tx_vouts))

        original_hexs = [swap.raw for swap in swaps]

        final_addr = self.WalletMgr.addresses.get_single_address(
            "order_destination")
        funded = self.WalletMgr.fund_transaction_final(
            self.RVNpyRPC.do_rpc, send_rvn, recv_rvn, final_addr, mega_tx_vins, mega_tx_vouts, original_hexs)

        if not funded:
            raise Exception("Funding error")

        # Build final funded raw transaction
        final_raw = self.RVNpyRPC.do_rpc("createrawtransaction",
                           inputs=mega_tx_vins, outputs=mega_tx_vouts)
        # Merge the signed tx from the original order
        combined_raw = final_raw
        for hex in original_hexs:
            logging.info(hex)
            combined_raw = self.RVNpyRPC.do_rpc("combinerawtransaction",
                                  txs=[combined_raw, hex])
            logging.info(combined_raw)
        # Sign our inputs/outputs
        signed_res = self.RVNpyRPC.do_rpc("signrawtransaction", hexstring=combined_raw)
        signed_hex = signed_res["hex"]
        # Finally, Test mempool acceptance
        mem_accept = self.RVNpyRPC.do_rpc("testmempoolaccept", rawtxs=[signed_hex])

        if(mem_accept and mem_accept[0]["allowed"]):
            logging.info("Accepted to mempool!")
            tx_allowed = True
            tx_final = signed_hex
        elif(mem_accept and mem_accept[0]["reject-reason"] == "66: min relay fee not met"):
            logging.info("Min fee not met")
            #raise Exception("Fee Error")
            tx_allowed = True
            tx_final = signed_hex
        else:
            logging.info(mem_accept)
            logging.info("Final Raw")
            logging.info(combined_raw)
            logging.info("Signed Raw")
            logging.info(signed_res)
            # if combined_raw:
            #  logging.info("Decoded")
            #  logging.info(self.RavenpyRPC.do_rpc("decoderawtransaction", hexstring=combined_raw))
            logging.info("!!Error!!")
            raise Exception("Error Building TX")


    def decode_swap(self, raw_swap):
        parsed = self.RVNpyRPC.do_rpc("decoderawtransaction",
                        log_error=False, hexstring=raw_swap)
        if parsed and "error" not in parsed:
            if len(parsed["vin"]) != 1 or len(parsed["vout"]) != 1:
                return (False, "Invalid Transaction. Has more than one vin/vout")
            if "SINGLE|ANYONECANPAY" not in parsed["vin"][0]["scriptSig"]["asm"]:
                return (False, "Transaction not signed with SINGLE|ANYONECANPAY")

            swap_vin = parsed["vin"][0]
            swap_vout = parsed["vout"][0]

            # Decode full here because we liekly don't have this transaction in our mempool
            # And we probably aren't runnin a full node
            vin_tx = self.txUtils.decode_full(swap_vin["txid"])
            
            
            

            # If nothing comes back this is likely a testnet tx on mainnet of vice-versa
            if not vin_tx:
                return (False, "Unable to find transaction. Is this for the correct network?")

            src_vout = vin_tx["vout"][swap_vin["vout"]]
            in_asset = "asset" in src_vout["scriptPubKey"]
            out_asset = "asset" in swap_vout["scriptPubKey"]
            order_type = "unknown"

            if in_asset and out_asset:
                order_type = "trade"
            elif in_asset:
                order_type = "sell"
            elif out_asset:
                order_type = "buy"

            if order_type == "unknown":
                return (False, "Uknonwn trade type")
            
            test_vout = self.RVNpyRPC.do_rpc("gettxout", txid=swap_vin["txid"], n=swap_vin["vout"])
            if not test_vout:
                return (False, "Unable to find UTXO, this transaction may have been executed already.")
            '''
            if src_vout.__contains__('spentTxId'):
                if src_vout['spentTxId'] != None:
                    return (False, "Atomic Transaction already done.")
            '''

            in_type = ""
            out_type = ""
            in_qty = 0
            out_qty = 0

            # Pull asset data based on order type
            if order_type == "buy":
                asset_data = swap_vout["scriptPubKey"]["asset"]
                vout_data = self.txUtils.make_transfer(
                    asset_data["name"], asset_data["amount"])

                in_type = "rvn"
                in_qty = src_vout["value"]
                out_type = asset_data["name"]
                out_qty = asset_data["amount"]
            elif order_type == "sell":
                asset_data = src_vout["scriptPubKey"]["asset"]
                vout_data = swap_vout["value"]

                in_type = asset_data["name"]
                in_qty = asset_data["amount"]
                out_type = "rvn"
                out_qty = swap_vout["value"]
            elif order_type == "trade":
                asset_data = swap_vout["scriptPubKey"]["asset"]
                vout_data = self.txUtils.make_transfer(
                    asset_data["name"], asset_data["amount"])

                in_type = src_vout["scriptPubKey"]["asset"]["name"]
                in_qty = src_vout["scriptPubKey"]["asset"]["amount"]
                out_type = swap_vout["scriptPubKey"]["asset"]["name"]
                out_qty = swap_vout["scriptPubKey"]["asset"]["amount"]

            return (True, SwapTransaction({
                "in_type": in_type,
                "out_type": out_type,
                "in_quantity": in_qty,
                "out_quantity": out_qty,
                "own": False,
                "utxo": self.txUtils.join_utxo(swap_vin["txid"], str(swap_vin["vout"])),
                "destination": swap_vout["scriptPubKey"]["addresses"][0],
                "state": "new",
                "type": order_type,
                "raw": raw_swap,
                "txid": ""
            },
                self.AtomicSwapMgr,
                 {
                "vin": swap_vin,
                "vout": swap_vout,
                "src_vout": src_vout,
                "vout_data": vout_data,
                "from_tx": vin_tx
            }))

        else:
            return (False, "Invalid TX") 
        
        
        
        
        
        

        

class SwapTrade():
    def __init__(self, dict, AtomicSwapMgr ):
        if dict != None:
            vars(self).update(dict)
        
        self.AtomicSwapMgr = AtomicSwapMgr
        
        self.RPCconnexion = AtomicSwapMgr.RPCconnexion
        self.RVNpyRPC = AtomicSwapMgr.RVNpyRPC
        self.txUtils = AtomicSwapMgr.txUtils
        self.WalletMgr = AtomicSwapMgr.WalletMgr
        
        # Recreate types if we load simply from json
        if self.transactions:
            self.transactions = [SwapTransaction(
                tx, AtomicSwapMgr) for tx in self.transactions]

    def __repr__(self):
        return str(self.transactions.__repr__())
    """
    def toJSON(self):
        txall = []
        for _t in self.transactions:
            txall.append(_t.toJSON())
    """
    
            
    def toJSON(self):
        #return json.dumps(self.Export())
        return json.dumps(self.Export(), default=lambda o: '<not serializable>')
        #return json.dumps(self,
        #  default = lambda o: o.__dict__,
        #  sort_keys = True, indent = 2)
        
        
    def Export(self):
        #data = {
        #        '__class__': self.__class__.__name__,
        #        '__module__': self.__module__
        #       }
        data={}
        data.update(self.__dict__)
        try:
            data.pop('RPCconnexion')
            data.pop('RVNpyRPC')
            data.pop('AtomicSwapMgr')
            data.pop('txUtils')
            data.pop('WalletMgr')
        except :
            pass  
        
        
        data['transactions'] = []
        for _t in self.transactions:
            data['transactions'].append(_t.Export())
        
        return data        
    

    def total_price(self):
        # Don't need to multiply
        if self.type == "buy":
            return float(self.in_quantity)
        elif self.type == "sell":
            return float(self.out_quantity)
        elif self.type == "trade":
            # In the case of a trade, consider the quantity of our asset, to be the "price"
            return float(self.in_quantity)
        else:
            return 0

    def quantity(self):
        if self.type == "buy":
            return float(self.out_quantity)
        elif self.type == "sell":
            return float(self.in_quantity)
        elif self.type == "trade":
            # In the case of a trade, consider the desired asset to be the quantity
            return float(self.out_quantity)
        else:
            return 0

    def unit_price(self):
        qty = self.quantity()
        return (0 if qty == 0 else self.total_price() / qty)

    def set_unit_price(self, new_price):
        qty = self.quantity()
        if self.type == "buy":
            self.in_quantity = new_price * qty
        elif self.type == "sell":
            self.out_quantity = new_price * qty
        elif self.type == "trade":
            self.in_quantity = new_price * qty

    def asset(self):
        if self.type == "buy":
            return self.out_type
        elif self.type == "sell":
            return self.in_type
        elif self.type == "trade":
            # In the case of a trade, consider the desired asset to be the "asset" of the trade
            return self.out_type
        else:
            return "N/A"

    def find_pool_trades(self):
        missing_trades = self.missing_trades()
        if missing_trades == 0:
            return []
        ready_utxo = self.WalletMgr.find_utxo_multiple_exact(
            self.in_type, self.in_quantity, include_locked=False)
        available_utxos = len(ready_utxo)
        return ready_utxo

    def pool_available(self):
        available = self.find_pool_trades()
        missing = self.missing_trades()

        if missing == 0:
            return 0
        else:
            return len(available)

    def attempt_fill_trade_pool(self, max_add=None):
        missing_trades = self.missing_trades()
        if missing_trades == 0:
            return True  # Pool is filled

        # Fallback destination address
        if not self.destination:
            self.destination = self.RVNpyRPC.do_rpc("getrawchangeaddress")

        ready_utxo = self.WalletMgr.find_utxo_multiple_exact(
            self.in_type, self.in_quantity, include_locked=False)
        available_utxos = len(ready_utxo)

        if available_utxos < missing_trades:
            # Need to create additional UTXO's to fill the pool
            return False

        if max_add:  # Allow us to only add on-at-a-time if we want
            ready_utxo = ready_utxo[:max_add]

        for utxo_data in ready_utxo[:missing_trades]:
            self.add_utxo_to_pool(utxo_data)

        # Pool now filled (/or there are enough items to fill it otherwise)
        return True

    def add_utxo_to_pool(self, utxo_data):
        if type(utxo_data) is not dict:
            raise Exception("UTXO Data must be dict")
        if round(utxo_data["amount"], 8) != round(self.in_quantity, 8):
            raise Exception("UTXO Size mismatch. Expected {}, Actual {}".format(
                round(self.in_quantity, 8), round(utxo_data["amount"], 8)))

        utxo_str = self.txUtils.make_utxo(utxo_data)
        self.order_utxos.append(utxo_str)
        new_trade = self.create_trade_transaction(
            utxo_str, self.current_number, self.AtomicSwapMgr)
        new_trade.sign_partial()
        self.transactions.append(new_trade)
        self.current_number += 1
        self.WalletMgr.add_lock(utxo=utxo_str)

    def setup_trade(self, max_add=None):
        num_create = self.missing_trades()
        if max_add:
            num_create = min(max_add, num_create)
        quantity_required = self.in_quantity * num_create
        logging.info("Setting up trade for {} missing. Max add: {}. Required Qty: {}".format(
            num_create, max_add, quantity_required))

        # Get a distinct list of addresses to use for deposits
        addr_list = self.WalletMgr.addresses.get_address_set(
            num_create + 2)

        setup_vins = []
        setup_vouts = {}
        asset_total = 0

        for n in range(0, num_create):
            addr = addr_list[n]
            if self.type == "buy":
                # Create rvn vout for buying
                setup_vouts[addr] = round(float(self.in_quantity), 8)
            elif self.type == "sell":
                # Create asset vouts for selling
                setup_vouts[addr] = self.txUtils.make_transfer(
                    self.in_type, self.in_quantity)
            elif self.type == "trade":
                # Create asset vouts for trading
                setup_vouts[addr] = self.txUtils.make_transfer(
                    self.in_type, self.in_quantity)

        asset_change_addr = addr_list[num_create]
        rvn_change_addr = addr_list[num_create + 1]

        # Send any extra assets back to ourselves
        if self.in_type != "rvn":
            (asset_total, asset_vins) = self.WalletMgr.find_utxo_set(
                "asset", quantity_required, name=self.in_type, include_locked=False)
            if not asset_vins:
                return (False, "Not enough assets to fund trade!")

            setup_vins = [self.txUtils.utxo_copy(vin) for vin in asset_vins]
            if asset_total > quantity_required:
                setup_vouts[asset_change_addr] = self.txUtils.make_transfer(
                    self.in_type, asset_total - quantity_required)

        estimated_size = self.txUtils.calculate_size(setup_vins, setup_vouts)
        estimated_fee = self.txUtils.calculated_fee_from_size(estimated_size)

        raw_tx = self.RVNpyRPC.do_rpc("createrawtransaction",
                        inputs=setup_vins, outputs=setup_vouts)

        if self.type == "buy":
            funded_tx = self.WalletMgr.fund_transaction_final(self.RVNpyRPC.do_rpc, quantity_required, 0,
                                               rvn_change_addr, setup_vins, setup_vouts, [raw_tx])
        else:
            funded_tx = self.WalletMgr.fund_transaction_final(self.RVNpyRPC.do_rpc, 0, 0,
                                               rvn_change_addr, setup_vins, setup_vouts, [raw_tx])

        raw_tx = self.RVNpyRPC.do_rpc("createrawtransaction",
                        inputs=setup_vins, outputs=setup_vouts)
        sign_tx = self.RVNpyRPC.do_rpc("signrawtransaction", hexstring=raw_tx)

        return (True, sign_tx["hex"])

    def construct_invalidate_tx(self, combine=False):
        final_vin = []
        final_vout = {}

        # each element is {utxo}
        input_utxos = [self.WalletMgr.search_utxo(
            utxo) for utxo in self.order_utxos]

        # Populate vins with all active UTXO's
        final_vin = [self.txUtils.utxo_copy(utxo) for utxo in input_utxos]

        output_quantities = [utxo["amount"] for utxo in input_utxos]
        if combine:
            output_quantities = [sum(output_quantities)]

        output_addresses = self.WalletMgr.addresses.get_address_set(
            len(output_quantities))

        # Judge all UTXO's based on the first in the list.
        # TODO: Validate all are identical
        trade_type = input_utxos[0]["type"]
        trade_name = "rvn" if trade_type == "rvn" else (
            input_utxos[0]["asset"])

        for index, address in enumerate(output_addresses):
            quantity = output_quantities[index]
            if trade_type == "rvn":
                final_vout[address] = quantity
            elif trade_type == "asset":
                final_vout[address] = self.txUtils.make_transfer(trade_name, quantity)

        self.txUtils.check_unlock()

        new_tx = self.RVNpyRPC.do_rpc("createrawtransaction",
                        inputs=final_vin, outputs=final_vout)
        funded_tx = self.RVNpyRPC.do_rpc("fundrawtransaction", hexstring=new_tx, options={
                           "changePosition": len(final_vout.keys())})
        signed_raw = self.RVNpyRPC.do_rpc("signrawtransaction",
                            hexstring=funded_tx["hex"])["hex"]

        return signed_raw

    def sent_invalidate_tx(self, txid):
        # Don't really need to do much except clear UTXOs and tx list
        for utxo in self.order_utxos:
            self.WalletMgr.remove_lock(utxo=utxo)
        self.order_utxos = []
        self.transactions = []
        self.order_count = 0

    def missing_trades(self):
        return self.order_count - len(self.order_utxos)

    def can_create_single_order(self):
        return self.attempt_fill_trade_pool(max_add=1)

    def order_completed(self, utxo):
        if utxo not in self.order_utxos:
            return None
        self.order_utxos.remove(utxo)
        self.executed_utxos.append(utxo)
        self.executed_count += 1
        self.order_count -= 1

        matching_tx = None
        for tx in self.transactions:
            if tx.utxo == utxo:
                matching_tx = tx
                break
        if matching_tx == None:
            return None

        self.transactions.remove(matching_tx)
        return matching_tx

    def create_trade_transaction(self, utxo, number,AtomicSwapMgr):
        # TODO: Validate utxo is correctly sized
        return SwapTransaction({
            "in_type": self.in_type,
            "out_type": self.out_type,
            "in_quantity": self.in_quantity,
            "out_quantity": self.out_quantity,
            "number": number,
            "own": True,
            "utxo": utxo,
            "destination": self.destination,
            "state": "new",
            "type": self.type,
            "raw": "",
            "txid": ""
        },AtomicSwapMgr)

    @staticmethod
    def create_trade(trade_type, in_type, in_quantity, out_type, out_quantity,AtomicSwapMgr, order_count=1,  destination=None):
        
        
        
        return SwapTrade({
            "in_type": in_type,
            "out_type": out_type,
            "in_quantity": in_quantity,
            "out_quantity": out_quantity,
            "destination": destination,
            "type": trade_type,
            "order_count": order_count,
            "current_number": 0,
            "executed_count": 0,
            "order_utxos": [],
            "executed_utxos": [],
            "transactions": []
        },AtomicSwapMgr)





class SwapTradeManager():
    
    
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
        self.txUtils = AtomicSwapMgr.txUtils
        
        self._LastTrade = None
        
        
    def create_trade(self, trade_type, in_type, in_quantity, out_type, out_quantity, order_count=1,  destination=None):
        
        
        logging.info(f"Creating a {trade_type} order ")
        logging.info(f"IN {in_type}  qt: {in_quantity} ")
        logging.info(f"OUT {out_type}  qt: {out_quantity} ")
        
        _tradeRaw = {}
        #
        # Init trade object
        #
        self._LastTrade = SwapTrade({
            "in_type": in_type,
            "out_type": out_type,
            "in_quantity": in_quantity,
            "out_quantity": out_quantity,
            "destination": destination,
            "type": trade_type,
            "order_count": order_count,
            "current_number": 0,
            "executed_count": 0,
            "order_utxos": [],
            "executed_utxos": [],
            "transactions": []
        },self.AtomicSwapMgr)
        
        
        
        logging.info(f"ORDER CREATED, PROCESSING order ")
        #
        # Do process the trades
        #
        setup_max = 1
        self.txUtils.check_unlock()
        pool_filled = self._LastTrade.attempt_fill_trade_pool(max_add=setup_max)
        logging.info(f"pool_filled = {pool_filled}")
        
        if not pool_filled:
            
            logging.info(f"pool was not filled, setup a trade")
            (setup_success, setup_result) = self._LastTrade.setup_trade(max_add=setup_max)
            
            
            logging.info(f"setup_success = {setup_success}")
            logging.info(f"setup_result = {setup_result}")
            #logging.info(f"self._LastTrade = {self._LastTrade}")
            if setup_result != None:
                _tradeRaw[0]=str(setup_result)
            
            logging.info(f"wait 5 sec and attempt fill trade...")
            time.sleep(5)
            self._LastTrade.attempt_fill_trade_pool(max_add=setup_max)
            logging.info(f"done...")
            
            
            """
            print(f"setup_success = {setup_success}")
            print(f"setup_result = {setup_result}")
            print(f"self._LastTrade = {self._LastTrade}")
            print(f"SWAP TX = {len(self._LastTrade.transactions)}")
            if setup_success and setup_result:
                count = 0
                for _tx in  self._LastTrade.transactions:
                    
                    print(f"SWAP TX = {_tx}")
                    _tradeRaw[count] = _tx.raw
                    count = count+1
                
                if count==0:
                    _tradeRaw[count] = setup_result
                    
                submitted_txid = self.RVNpyRPC.do_rpc("sendrawtransaction", log_error=False, hexstring=setup_result)
                if submitted_txid:
                    pass
            """
                #self.AtomicSwapMgr.WalletMgr.add_waiting(submitted_txid, self.setup_mempool_confirmed, self.setup_network_confirmed, callback_data=self._LastTrade)
                #self.AtomicSwapMgr.WalletMgr.add_swap(self._LastTrade)
                #self.AtomicSwapMgr.WalletMgr.save_data()
                #self.AtomicSwapMgr.WalletMgr.update_wallet()
                #setup_txid = self.preview_complete(setup_result, "Setup Trade Order")
        else:
            pass
            #swap = self._LastTrade.transactions[0]
            #swap_hex = swap.complete_order()
            #logging.info(swap_hex)
            
        
        
        
        logging.info(f"SWAP TX Size = {len(self._LastTrade.transactions)}")    
        available_trades = [tx for tx in self._LastTrade.transactions if tx.state == "new"]
        if len(available_trades) > 0:
            logging.info(available_trades[0].raw)
            _tradeRaw[0]=available_trades[0].raw
            
            
            
        self.AtomicSwapMgr.WalletMgr.add_swap(self._LastTrade)
        self.AtomicSwapMgr.WalletMgr.save_data()
        self.AtomicSwapMgr.WalletMgr.update_wallet()    
        #print(f"SWAP TX = {len(self._LastTrade.transactions)}")    
        #swap = self._LastTrade.transactions[0]
        #swap_hex = swap.complete_order()
        #good_swap = SwapTransaction.decode_swap(swap.raw)
        #swap_hex = good_swap.complete_order()
        #logging.info(swap.raw)
        #logging.info(swap_hex)
        return _tradeRaw
    
    '''
    def decode_swap(self, raw):
        _newAtomicSwap = SwapTransaction({}, self.AtomicSwapMgr)
        return _newAtomicSwap.decode_swap(raw)
    
    '''
    
    