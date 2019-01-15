import yaml
from pprint import pprint
import sys
import json
from peerplays import PeerPlays
from peerplays.instance import set_shared_blockchain_instance
from peerplays.account import Account
from peerplays.blockchain import Blockchain

config = yaml.load(open("config.yml").read())
instance = PeerPlays(
    config["witness_url"],
    keys=[config["wif"]],
    nobroadcast=config["nobroadcast"],
    bundle=True,
)
set_shared_blockchain_instance(instance)


def donate(account, amount, symbol):
    tx = instance.transfer(account, amount, symbol, account=config["registrar"])
    pprint(tx)


def run(begin=None, end=None):
    blockchain = Blockchain(mode="head", blockchain_instance=instance)
    for op in blockchain.stream(
        opNames=["account_create"],
        start=int(begin) if begin else None,
        stop=int(end) if end else None,
    ):
        blockid = op.get("block_num")
        timestamp = op.get("timestamp")
        print("Blockid: %d (%s)" % (blockid, timestamp), flush=True)

        # Legacy
        if config.get("donation_amount") and config.get("donation_asset"):
            donate(op["name"], config["donation_amount"], config["donation_asset"])

        if config.get("donations") and isinstance(config["donations"], dict):
            for symbol, amount in config["donations"]:
                donate(op["name"], amount, symbol)

        instance.broadcast()


if __name__ == "__main__":
    run()
