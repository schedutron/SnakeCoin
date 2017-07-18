import datetime
from snakecoin_block import *

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    return Block(this_index, this_timestamp, this_data, last_block.hash)
