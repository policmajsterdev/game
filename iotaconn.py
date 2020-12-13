import random
import os
from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import TryteString


filepath = os.path.dirname(__file__)


def check():

    """ Check connection """

    api = Iota('https://nodes.devnet.iota.org:443', testnet=True)
    try:
        response = api.get_node_info()
        status = response['isHealthy']
        if status:
            node = response['appName']
            version = response['appVersion']
        else:
            node = "Error"
            version = "Error"
    except:
        node = "Error"
        version = "Error"

    return node, version
            
             
def function_address(seed_x):

    """ Create new address """

    security_level = 2
    api = Iota('https://nodes.devnet.iota.org:443', seed_x)
    address = api.get_new_addresses(index=0, count=1, security_level=security_level)['addresses'][0]

    is_spent = api.were_addresses_spent_from([address])['states'][0]

    return address


def new_seed():

    """ Create new seed """
    
    alphabet = 'ABCDEFGHIJKLMNOPRQSTUWYZX9'
    seed = ""
    while len(seed) != 81:
        rand = random.randrange(25)
        seed += alphabet[rand]
    return seed


def open_save():

    """ Open save in DLT """

    try:
        list_file = os.listdir(os.path.join(filepath, "data\\save"))
        save_file = list_file[0].replace(".txt", "")

    except (UnboundLocalError, FileNotFoundError):
        pass
    try:
        api = Iota('https://nodes.devnet.iota.org:443', testnet=True)
        tail_transaction_hash = str(save_file)

        bundle = api.get_bundles(tail_transaction_hash)
        message = bundle['bundles'][0].tail_transaction.signature_message_fragment
        list_save = message.decode()
        return list_save
    except:
        pass


def save(save_list):

    """ Save game in DLT """

    seed_x = new_seed()
    address = function_address(seed_x)

    api = Iota('https://nodes.devnet.iota.org:443', testnet=True)
    message = TryteString.from_unicode(save_list)
    tx = ProposedTransaction(
        address=Address(address),
        message=message,
        value=0
    )
    result = api.send_transfer(transfers=[tx])

    hash = result['bundle'].tail_transaction.hash

    save_file = open("data\\save\\" + str(hash) + ".txt", "w")
    save_file.close()

    return hash
