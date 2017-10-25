from flask import Flask, jsonify, request
from uuid import uuid4
import json

from blockchain import Blockchain

app = Flask(__name__)

node_identifier = str(uuid4()).replace('-', '')

blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "We'll make a new Block"

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    print(values)
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    index = blockcahin.new_transaction(values['sender'], values['recipient'], values=['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}
    return "We'll add a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    PORT = 5000
    app.run(host='0.0.0.0', port=PORT)
