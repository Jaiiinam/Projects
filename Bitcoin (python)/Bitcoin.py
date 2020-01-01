
# Jeet Desai
# Yash Patel
import time
import hashlib
import os
import binascii
import copy
import random
from random import randrange
from flask import Flask, jsonify, request, json, Response

app = Flask(__name__)


# ---------------------------------------- BLOCKCHAIN CLASS ---------------------------------------- #


class Blockchain:


    def __init__(self):
        self.chain = []
        self.difficulty_target = 4

        #### NEW ####
        self.wallets = {}
        self.mempool = {}
        #############

        self.mine_block('Genesis block!')


# ---------------------------------- NEW BLOCKCHAIN CLASS FUNCTIONS --------------------------------- #

    def create_wallet(self):

        # define wallet with fields: public_key, private_key, balance
        wallet = {
            binascii.b2a_hex(os.urandom(8)).decode('utf-8'): {
                'private_key': binascii.b2a_hex(os.urandom(8)).decode('utf-8'),
                'balance': 10
            }
        }

        # add new wallet to self.wallets
        self.wallets.update(wallet)

        # return the wallet to caller
        return wallet

    def hash_transaction(self, transaction):
        hashId = hashlib.sha256()
        hashId.update(repr(transaction).encode('utf-8'))
        return str(hashId.hexdigest())


    def add_transaction_to_mempool(self, transaction_id, transaction):

        # validate transaction
        if (blockchain.hash_transaction(transaction) == transaction_id):

            pending_transaction = {
                transaction_id: transaction
            }

            # add transaction to self.mempool
            self.mempool.update(pending_transaction)

        # return OK or BAD
            return True

        else:
            return False


    def choose_transactions_from_mempool(self):

        total_transaction = {}

        # Check if mempool has more than 10 avaiable transaction
        if len(self.mempool) > 10:


            # choose 10 random transactions
            for x in range(random.randrange(1,11)):

                random_transaction = str(random.choice(list(self.mempool.keys())))

                # check if the balances allow spending the amount
                if((self.mempool[random_transaction]['amount'] > 0) and (self.wallets[self.mempool[random_transaction]['from']]['balance'] > self.mempool[random_transaction]['amount'])):
                    # change the balance for the sender
                    sub_balance = self.wallets[self.mempool[random_transaction]['from']]['balance'] - self.mempool[random_transaction]['amount']
                    self.wallets[self.mempool[random_transaction]['from']]['balance'] = sub_balance

                    # change the balance for the recipient
                    add_balance = self.wallets[self.mempool[random_transaction]['to']]['balance'] + self.mempool[random_transaction]['amount']
                    self.wallets[self.mempool[random_transaction]['to']]['balance'] = add_balance

                    # Adding transaction into a new dictionary
                    total_transaction.update({random_transaction: self.mempool[random_transaction]})

                    # remove transaction from mempool
                    del self.mempool[random_transaction]

                else:
                    del self.mempool[random_transaction]

        #pass if mempool does not have more than 10 transaction avaliable
        else:
            pass

        # return transactions to caller
        return total_transaction



    def calculate_merkle_root(self, block):
        all_transaction_hashes = []

        # hash all transactions ids and append to a list
        for index in sorted(block['transactions']):
            all_transaction_hashes.append(index)
            print(index)

        return self.helper_calculate_merkle_root(all_transaction_hashes)


    def helper_calculate_merkle_root(self, input):
        tempHashList = []
        tempHashList2 = []
        tempOddHash = ''

        # if there are no transactions in the block, set the merkle root as null (for genesis block)
        if len(input) == 0:
            return None

        # odd numbered transactions will have the last transaction exluded till the end
        if len(input) % 2 == 1:
            if tempOddHash == '':
                tempOddHash = input.pop()
            else:
                input.append(tempOddHash)

        for hash in (input):
            tempHashList.append(hash)

            # each time 2 hashes have been found, append them to new list with their hash and reset current list
            if len(tempHashList) % 2 == 0:
                tempHashList2.append(self.hash_transaction(tempHashList[0] + tempHashList[1]))
                tempHashList = []

        # recursion will continue until only 1 true hash of all transactions are made (merkle root)
        if len(tempHashList2) == 1:
            return tempHashList2[0]
        else:
            return self.helper_calculate_merkle_root(tempHashList2)



    def check_merkle_root(self, block):
        # check merkle root
        if block['header']['merkle_root'] == self.calculate_merkle_root(block):

            # return OK or BAD
            return True
        else:
            return False


# --------------------------------------------------------------------------------------------------- #


    def create_block(self, data = None):

        block = {
            'header' : {
                'block_number': len(self.chain),
                'block_time': str(time.time()),
                'block_nonce': None,
                'previous_block_hash': self.get_last_block_hash(),
                #### NEW ####
                'merkle_root': None
                #############
            },
            #### NEW ####
            'transactions': {},
            #############
            'hash' : None
        }
        return block


    def mine_block(self, data):

        block = self.create_block(data)

        while True:

            #### NEW ####
            if ((not block['transactions']) and (block['header']['merkle_root'] == None)):
                block['transactions'] = self.choose_transactions_from_mempool()
                block['header']['merkle_root'] = self.calculate_merkle_root(block)
            #############

            block['header']['block_nonce'] = binascii.b2a_hex(os.urandom(8)).decode('utf-8')
            block['hash'] = self.hash_block_header(block)

            if block['hash'][:self.difficulty_target] == '0' * self.difficulty_target:
                break

        self.chain.append(block)
        return block


    def get_last_block_hash(self):
        return (self.chain[-1]['hash'] if len(self.chain) > 0 else None)


    def hash_block_header(self, block):
        hashId = hashlib.sha256()
        hashId.update(repr(block['header']).encode('utf-8'))
        return str(hashId.hexdigest())


    def check(self):

        for block_number in reversed(range(len(self.chain))):

            block = self.chain[block_number]

            if not block['hash'] == self.hash_block_header(block):
                return 'invalid block hash for block ' + str(block_number)

            if block_number > 0 and not block['header']['previous_block_hash'] == self.chain[block_number - 1]['hash']:
                return 'invalid block pointer from block ' + str(block_number) + ' back to block ' + str(block_number - 1)

            ##### NEW #####
            if not self.check_merkle_root(block):
                return 'invalid merkle root for block ' + str(block_number)
            ###############

        return 'ok'

# ------------- *New* FLASK ROUTES - AUTOMATE CREATE WALLET AND TRANSACTIONS ------------------- #

# test a change in the merkle root for block #1
@app.route('/change_merkle', methods = ['GET'])
def change_merkle():

    blockchain.chain[1]['header']['merkle_root'] = '12345'
    response = Response(
            response = json.dumps(blockchain.chain[1]),
            status = 200,
            mimetype = 'application/json'
    )
    return response

# creates 25 new wallets - seen using /show_balances
@app.route('/create_wallets', methods = ['GET'])
def create_wallets():

    for x in range(25):
        response = Response(
            response = json.dumps(blockchain.create_wallet()),
            status = 200,
            mimetype = 'application/json'
        )
    return response

#randomly generates 20 new transactions each time when called
@app.route('/create_transactions', methods = ['GET'])
def create_transactions():

    for x in range(20):
        try:

            transaction = {
                'time': int(time.time()),
                'from': str(random.choice(list(blockchain.wallets.keys()))),
                'to': str(random.choice(list(blockchain.wallets.keys()))),
                'amount': float(random.randrange(1,4))
            }

            private_key = blockchain.wallets[transaction['from']]['private_key']
            assert private_key == blockchain.wallets[transaction['from']]['private_key']

            if(transaction['amount'] > blockchain.wallets[transaction['from']]['balance']):

                response = Response(
                    response = json.dumps({'Error': 'Invalid transaction'}),
                    status = 400,
                    mimetype = 'application/json'
                )
                return response


        except:

            response = Response(
                response = json.dumps({'Error': 'Invalid transaction'}),
                status = 400,
                mimetype = 'application/json'
            )
            return response

        transaction_id = blockchain.hash_transaction(transaction)

        if blockchain.add_transaction_to_mempool(transaction_id, transaction):
            response = Response(
                response = json.dumps({'result': transaction_id}),
                status = 200,
                mimetype = 'application/json'
            )
        else:
            response = Response(
                response = json.dumps({'error': 'invalid transaction'}),
                status = 400,
                mimetype = 'application/json'
            )

    return response

# ---------------------------------------- New FLASK ROUTES ------------------------------------ #


@app.route('/create_wallet', methods = ['GET'])
def create_wallet():

    response = Response(
        response = json.dumps(blockchain.create_wallet()),
        status = 200,
        mimetype = 'application/json'
    )
    return response


@app.route('/show_balances', methods = ['GET'])
def show_balances():

    # To Do: Clean wallets of private_keys here.
    total_wallets = {}
    total_wallets = copy.deepcopy(blockchain.wallets)

    for id, info in total_wallets.items():
        del info['private_key']

    response = Response(
        response = json.dumps(total_wallets),
        status = 200,
        mimetype = 'application/json'
    )
    return response


@app.route('/show_mempool', methods = ['GET'])
def show_mempool():

    response = Response(
        response = json.dumps(blockchain.mempool),
        status = 200,
        mimetype = 'application/json'
    )
    return response


@app.route('/create_transaction', methods = ['GET'])
def create_transaction():

    try:

        transaction = {
            'time': int(time.time()),
            'from': request.args.get('from', type=str),
            'to': request.args.get('to', type=str),
            'amount': request.args.get('amount', type=float)
        }


        private_key = request.args.get('private_key', type=str)
        assert private_key == blockchain.wallets[transaction['from']]['private_key']

        if(transaction['amount'] > blockchain.wallets[transaction['from']]['balance']):

            response = Response(
                response = json.dumps({'Error': 'Invalid transaction'}),
                status = 400,
                mimetype = 'application/json'
            )
            return response

    except:

        response = Response(
            response = json.dumps({'Error': 'Invalid transaction'}),
            status = 400,
            mimetype = 'application/json'
        )
        return response

    transaction_id = blockchain.hash_transaction(transaction)

    if blockchain.add_transaction_to_mempool(transaction_id, transaction):
        response = Response(
            response = json.dumps({'result': transaction_id}),
            status = 200,
            mimetype = 'application/json'
        )
    else:
        response = Response(
            response = json.dumps({'error': 'invalid transaction'}),
            status = 400,
            mimetype = 'application/json'
        )

    return response


# ---------------------------------------- FLASK ROUTES ---------------------------------------- #
# No need to modify anything below!


@app.route('/mine_block', methods = ['GET'])
def mine_block():

    block_data = request.args.get('data', default='', type=str)

    response = Response(
        response = json.dumps(blockchain.mine_block(block_data)),
        status = 200,
        mimetype = 'application/json'
    )
    return response


@app.route('/check_blockchain', methods = ['GET'])
def check_blockchain():

    response = Response(
        response = json.dumps({'result': blockchain.check()}),
        status = 200,
        mimetype = 'application/json'
    )
    return response


@app.route('/get_blocks', methods = ['GET'])
def get_blocks():

    response = Response(
        response = json.dumps(blockchain.chain),
        status = 200,
        mimetype = 'application/json'
    )
    return response


@app.route('/get_block', methods = ['GET'])
def get_block():

    try:

        block_number = request.args.get('number', default=0, type=int)
        response = Response(
            response = json.dumps(blockchain.chain[block_number]),
            status = 200,
            mimetype = 'application/json'
        )

    except IndexError:

        response = Response(
            response = json.dumps({'error': 'invald block number'}),
            status = 400,
            mimetype = 'application/json'
        )

    return response


blockchain = Blockchain()
app.run(host = '0.0.0.0', port = 8080, debug=1)
