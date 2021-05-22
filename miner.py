import hashlib

def mine(message, difficulty=1):
    assert difficulty >=1
    prefix = '1' * difficulty
    for i in range(1000000):
        digest = sha256(str(hash(message)) + str(i))
        if digest.startswith(prefix):
            print ("After " + str(i) + " iterations found nonce: " + digest)
            return digest

def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()