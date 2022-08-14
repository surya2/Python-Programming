import datetime
import hashlib

class Block:
    blockNo = 0
    hash = None
    nextHash = None
    previousHash = 0x0
    data = None
    nonce = 0
    date = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def createHash(self):
        m = hashlib.sha3_256()
        m.update(
            str(self.nonce).encode('utf-8') +
            str(self.previousHash).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.blockNo).encode('utf-8') +
            str(self.date).encode('utf-8')
        )
        return m.hexdigest()

    def __str__(self):
        return "Block Number: " + str(self.blockNo) + "/nBlock Hash: " + str(self.hash) + "/nPrevious Hash Link: " + str(self.previousHash) +  "/nData: " + str(self.data) + "/nTimestamp: " + str(self.date)


class Blockchain:
    diff = 20
    maxNonce = 2**32
    target = 2**(256-diff)

    block = Block("Genesis")
    """dummy block: """
    dummy = head = block

    def add(self, block):
        block.previousHash = self.block.hash()
        block.blockNo = self.block.blockNo() + 1
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for i in range(self.maxNonce):
            if(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                self.target += 1

blockchain = Blockchain()

for n in range(10):
    blockchain.mine(Block("Block: " + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next