
"""
A Blockchain is a sequential chain of records, similar to a linked list.

Each block contains some information and how it is connected related to the other blocks
in the chain. Each block contains a cryptographic hash of the previous block, a timestamp,
and transaction data. For our blockchain we will be using a SHA-256 hash,
the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

We can break the blockchain down into three main parts.

"""

import hashlib
import time
# import json


class Block:

    """
    We do this for the information we want to store in the block chain such as transaction time,
    data, and information like the previous chain.

    The next main component is the block on the blockchain:

    """

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, text):
        sha = hashlib.sha256()
        hash_str = text.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

    def __str__(self):
        return '[Block] ==> timestamp: {}, previous_hash: {}, hash: {}, data: {}'.format(self.timestamp, self.hash, self.previous_hash, self.data)


class BlockChain(object):
    def __init__(self):
        self.tail = None

    def append(self, data):
        # data_text = json.dumps(data)
        tail = None if self.tail is None else self.tail
        self.tail = Block(time.time(), data, tail)

    def search(self, data):

        if self.tail is None:
            return None
        else:
            current = self.tail

            while current:
                if current.data == data:
                    return current
                current = current.previous_hash

    def __str__(self):

        result = ""
        element = self.tail

        while element:
            result += str(element) + "\n\n"
            element = element.previous_hash
        return result

    def __len__(self):
        size = 0
        element = self.tail
        while element:
            size += 1
            element = element.previous_hash

        return size


def test():
    my_blockchain = BlockChain()
    ############################################################################
    ###################### ADD ELEMENTS TO THE BLOCKCHAIN ######################
    ############################################################################
    transaction_data_1 = {
        "my_balance":  1000,
        "my_currency": "EUR",
        "type": "transfer_out",
        "amount": 100,
        "operation_currency": "EUR"
    }
    transaction_data_1 = "Transaction 1"
    my_blockchain.append(transaction_data_1)

    transaction_data_2 = {
        "my_balance":  900,
        "my_currency": "EUR",
        "type": "transfer_out",
        "amount": 375,
        "operation_currency": "EUR"
    }
    transaction_data_2 = "Transaction 2"
    my_blockchain.append(transaction_data_2)

    transaction_data_3 = {
        "my_balance":  525,
        "my_currency": "EUR",
        "type": "transfer_in",
        "amount": 99,
        "operation_currency": "EUR"
    }
    transaction_data_3 = "Transaction 3"
    my_blockchain.append(transaction_data_3)  # 624

    # # Uncomment next 4 lines to see the whole chain
    # print("\nFor testing purposes print the blockchain created: ")
    # print("\n\n#####################################################################")
    # print(my_blockchain)
    # print("#####################################################################\n\n")

    ############################################################################
    #################### SEARCH ELEMENTS IN THE BLOCKCHAIN #####################
    ############################################################################

    element_1 = my_blockchain.search(transaction_data_1)
    print(element_1)
    # [Block] ==> timestamp: 1569904402.3503675, previous_hash: dff3b30655dc240deca00ed22fae68fdf8cf465bbe99bb2b2e24259cc1daac3a, hash: None, data: Transaction 1
    assert element_1.data == transaction_data_1

    element_2 = my_blockchain.search(transaction_data_2)
    assert element_2.data == transaction_data_2
    assert element_2.previous_hash.data == transaction_data_1

    element_3 = my_blockchain.search(transaction_data_3)
    assert element_3.data == transaction_data_3
    assert element_3.previous_hash.data == transaction_data_2

    element_not_found = my_blockchain.search("some dummydata")
    assert element_not_found == None
    print("-> Search tests passed")

    ############################################################################
    ######################### SIZE OF THE BLOCKCHAIN ###########################
    ############################################################################
    assert len(my_blockchain) == 3
    print("-> len() method testing")

    #  Edge cases

    element_1 = my_blockchain.search("no data")
    print(element_1)
    # None

    blockchain = BlockChain()
    print(blockchain.search('some other data'))
    # None


test()
