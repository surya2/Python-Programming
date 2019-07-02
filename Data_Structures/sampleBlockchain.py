#Program is a Blockchain version on a Linked List using SHA 356
import datetime
import hashlib

class Block:
    blockNo = 0
    amount = None
    user = None
    sale = None
    recipient = None
    hash = None
    date = datetime.datetime.now()
    next_hash = None
    prev_hash = None

    def __init__(self, amount, user, sale, recipient):
        self.amount = amount
        self.user = user
        self.sale = sale
        self.recipient = recipient
        print("Start of Blockchain; Genesis Block: ")

    def hash(self):
        hash = hashlib.sha3_256()
        hash.update(
            str(self.amount).encode('utf-8') +
            str(self.user).encode('utf-8') +
            str(self.recipient).encode('utf-8') +
            str(self.date).encode('utf-8') +
            str(self.prev_hash).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        return hash.hexdigest()

    def __str__(self):
        return "Block: " + str(self.blockNo) + " by " + str(self.user) + "/nTo: " + str(self.recipient) + "/nTransaction Amount: " + str(self.amount) + "/nSale/Good Quantity: " + str(self.sale) + "/n1-Hash: " + str(self.hash) + "/n2-Previous Hash: " + str(self.prev_hash)

class Blockchain:
    maxNonce = 2**32
    target = 2**(256-20)
    block = Block("Genesis")
    dummy = head = block

    def compileBlock(self, amount):
        self.amount = amount

        self.addBlock(self.amount)
    def addBlock(self, block):
        block.prev_hash = self.block.hash()
        block.blockNo = self.block.blockNo() + 1
        self.block.next = self.block
        self.block = self.block.next

    def mine(self, amount, user, sale, recipient):
        for i in ranger (0, maxNonce):
            if((block.hash(), 16) <= self.target):
                self.addBlock(block)
                print(block)







username = input("Name of user: ")
transaction_amount = input("Transaction Amount: ")
sale = input("Quantity of sale: ")
recipient = input("Recipient: ")

b = Blockchain()
b.compileBlock(transaction_amount)

while b.head != None:
    print(b.head)
