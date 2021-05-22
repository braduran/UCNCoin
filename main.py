from client import Client
from transaction import Transaction
from block import Block
from ucncoin import UCNCoin
import miner

Dinesh = Client()
Ramesh = Client()
Seema = Client()
Vijay = Client()

#Bloque Genesis
t0 = Transaction("Genesis", Dinesh.identity, 500.0)

block0 = Block()
block0.verified_transactions.append(t0)

block0.previous_block_hash = None
block0.Nonce = None
block0.last_block_hash = hash(block0)
#Bloque Genesis

#Bloque 2
t1 = Transaction(Dinesh, Ramesh.identity, 5.0)
t1.sign_transaction()
t2 = Transaction(Dinesh, Seema.identity, 6.0)
t2.sign_transaction()
t3 = Transaction(Ramesh, Vijay.identity, 2.0)
t3.sign_transaction()

block1 = Block()
block1.verified_transactions.append(t1)
block1.verified_transactions.append(t2)
block1.verified_transactions.append(t3)

block1.previous_block_hash = block0.last_block_hash
block1.Nonce = miner.mine(block1, 2)
block1.last_block_hash = hash(block1)
#Bloque 2

#Bloque 3
t4 = Transaction(Seema, Ramesh.identity,4.0)
t4.sign_transaction()
t5 = Transaction(Vijay, Seema.identity,7.0)
t5.sign_transaction()
t6 = Transaction(Ramesh, Seema.identity,3.0)
t6.sign_transaction()

block2 = Block()
block2.verified_transactions.append(t4)
block2.verified_transactions.append(t5)
block2.verified_transactions.append(t6)

block2.previous_block_hash = block1.last_block_hash
block2.Nonce = miner.mine(block2, 2)
block2.last_block_hash = hash(block2)
#Bloque 3

#Bloque 4
t7 = Transaction(Seema, Dinesh.identity, 8.0)
t7.sign_transaction()
t8 = Transaction( Seema, Ramesh.identity, 1.0)
t8.sign_transaction()
t9 = Transaction(Vijay, Dinesh.identity, 5.0)
t9.sign_transaction()

block3 = Block()
block3.verified_transactions.append(t7)
block3.verified_transactions.append(t8)
block3.verified_transactions.append(t9)

block3.previous_block_hash = block2.last_block_hash
block3.Nonce = miner.mine(block3, 2)
block3.last_block_hash = hash(block3)
#Bloque 4

#Mostramos la cadena de bloques
blockchain = UCNCoin()
blockchain.blocks.append(block0)
blockchain.blocks.append(block1)
blockchain.blocks.append(block2)
blockchain.blocks.append(block3)
blockchain.dump_blockchain()
