#!/usr/bin/env python
import hashlib

class Block():
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def  hash_block(self):
        sha = hashlib.sha256()
        hash_data = "{}{}{}{}".format(self.index,
                                      self.timestamp,
                                      self.data,
                                      self.previous_hash).encode("utf-8")
        sha.update(bytes(hash_data))
        return sha.hexdigest()
