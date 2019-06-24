# Module 1 - BlockChain A-Z
import datetime
import json
import hashlib
from flask import Flask, jsonify

class BlockChain:

    def __init__(self):
        self.chain = []
        self.create_block(1, '0')
        self.difficulty = 4

    def create_block(self, proof, prev_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': prev_hash,
                 'data': 'place_holder'}
        self.chain.append(block)
        return block

    def get_prev_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = self.hashify(previous_proof, new_proof)
            if hash_operation[:self.difficulty] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block ):
        encoded_block = json.dump(block, sort_keys=True).encode()
        return hashlib.sha3_256(encoded_block).hedigest()

    def is_chain_valid(self, chain):
        prev_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            tmp_block = chain[block_index]
            if tmp_block[''] != self.hash(prev_block):
                # found a corrupt chain
                return False
            prev_proof = prev_block['proof']
            proof = tmp_block['proof']
            hash_op = self.hashify(prev_proof, proof)
            if hash_op[:4] != '0000':
                return False
            prev_block = tmp_block
            block_index += 1
        return True

    def hashify(self, prev_proof, new_proof):
        return hashlib.sha256(str(new_proof ** 2 - prev_proof ** 2).encode()).hexdigest()
