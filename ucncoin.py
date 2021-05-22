class UCNCoin:
    def __init__(self):
        self.blocks = []

    def dump_blockchain(self):
        print ("Number of blocks in the chain: " + str(len(self.blocks)))
        print ("===================")
        for x in range (len(self.blocks)):
            block_temp = self.blocks[x]
            print ("block # " + str(x))
            print ("Hash prev -> " + str(block_temp.previous_block_hash))
            print ("Hash last -> " + str(block_temp.last_block_hash))
            for tx in block_temp.verified_transactions:
                tx.display_transaction()
            print ("===================")