from snakecoin_genesis import *
from snakecoin_new_block import *

# Create the blockchain and add genesis block.
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks to add after the genesis block?
num_of_blocks_to_add = 20

# Add blocks to the chain.
for i in range(num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    # Tell everyone about it!
    print "Block #{} has been added to blockchain!".format(block_to_add.index)
    print "Hash: {}".format(block_to_add.hash)
    print "Timestamp: {}\n".format(block_to_add.timestamp)
