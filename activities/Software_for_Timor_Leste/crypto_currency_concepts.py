import hashlib
import time
import random

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.transactions}{self.timestamp}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []
        self.mining_reward = 10

    def create_genesis_block(self):
        return Block(0, [], int(time.time()), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, miner_address):
        block = Block(len(self.chain), self.pending_transactions, int(time.time()), self.get_latest_block().hash)
        block.mine_block(self.difficulty)

        print("Block mined!")
        self.chain.append(block)

        self.pending_transactions = [
            {"from": "network", "to": miner_address, "amount": self.mining_reward}
        ]

    def create_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            "from": sender,
            "to": recipient,
            "amount": amount
        })

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction['from'] == address:
                    balance -= transaction['amount']
                if transaction['to'] == address:
                    balance += transaction['amount']
        return balance

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.transactions}{self.timestamp}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

# Demonstration
print("Welcome to the Cryptocurrency Concepts Demonstration!")

# Create a new blockchain
timor_coin = Blockchain()

print("\nCreating some transactions...")
timor_coin.create_transaction("Alice", "Bob", 50)
timor_coin.create_transaction("Bob", "Charlie", 25)

print("Mining the block...")
timor_coin.mine_pending_transactions("Miner1")

print("\nCreating more transactions...")
timor_coin.create_transaction("Charlie", "David", 10)
timor_coin.create_transaction("David", "Alice", 5)

print("Mining the block...")
timor_coin.mine_pending_transactions("Miner2")

print("\nBlockchain:")
for block in timor_coin.chain:
    print(f"Block #{block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {block.transactions}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print()

print("Balances:")
print(f"Alice: {timor_coin.get_balance('Alice')}")
print(f"Bob: {timor_coin.get_balance('Bob')}")
print(f"Charlie: {timor_coin.get_balance('Charlie')}")
print(f"David: {timor_coin.get_balance('David')}")
print(f"Miner1: {timor_coin.get_balance('Miner1')}")
print(f"Miner2: {timor_coin.get_balance('Miner2')}")