from blockchain import Blockchain

difficulty = 6 #you can try to modify the difficulty (amount of prefix zeros) to see how it affects the calculation time

block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}

local_blockchain = Blockchain()
local_blockchain.add_block(block_one_transactions, difficulty)
local_blockchain.add_block(block_two_transactions, difficulty)
local_blockchain.add_block(block_three_transactions, difficulty)
local_blockchain.print_blocks()
