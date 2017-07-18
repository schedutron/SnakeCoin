import datetime
from snakecoin_block import *

def create_genesis_block():
    '''Constructs a block with index 0 and arbitrary previous hash'''
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")
