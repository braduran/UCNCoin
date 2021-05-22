import datetime
import collections
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
import binascii

class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()

    def sign_transaction(self):
        signer = self.sender._signer
        tx = SHA.new(str(self.to_dict()).encode('utf-8'))
        return binascii.hexlify(signer.sign(tx)).decode('ascii')

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({
            'sender': identity,
            'recipient': self.recipient,
            'value': self.value,
            'time': self.time
        })

    def display_transaction(self):
        dict = self.to_dict()
        print ("------------")
        print ("sender: " + dict['sender'])
        print ("recipient: " + dict['recipient'])
        print ("value: " + str(dict['value']))
        print ("time: " + str(dict['time']))
        print ("------------")
