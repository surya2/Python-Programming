import hashlib
m = hashlib.sha3_256()
m.update(b'my name is surya')
m.digest()
test_val= m.hexdigest()
print(test_val)

blockchain = []

def get_last_value():
    return blockchain[-1]


def add_value(item, last_transaction=[0]):
    blockchain.append([last_transaction, float(item)])

def user_input():
    return input("Transaction Amount: ")

item = user_input()
add_value(item)
add_value(item, get_last_value())

print(blockchain)
