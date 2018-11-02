import yaml
from pprint import pprint
import sys
import json
from peerplays import PeerPlays
from peerplays.account import Account
from peerplays.blockchain import Blockchain

config = yaml.load(open("config.yml").read())

instance = PeerPlays(
    config["witness_url"],
    keys=[config["wif"]],
    nobroadcast=config["nobroadcast"]
)

def run(begin=None, end=None):

    blockchain = Blockchain(
        mode="head",
        blockchain_instance=instance
    )

    for op in blockchain.stream(
        opNames=["account_create"],
        start=int(begin) if begin else None,
        stop=int(end) if end else None,
    ):
        blockid = op.get("block_num")
        timestamp = op.get("timestamp")

        print("Blockid: %d (%s)" % (blockid, timestamp), flush=True)

        pprint(instance.transfer(
            op["name"],
            config["donation_amount"], config["donation_asset"],
            account=config["registrar"]
        ))


if __name__ == '__main__':
    run()
