import os.path
import time
import bitsv
import requests


filepath = os.path.dirname(__file__)


def status_api_bsv():

    """ Checks the status of the API """

    url = 'https://api.whatsonchain.com/v1/bsv/test/woc'

    response = requests.get(url)
    status_url = response.status_code

    if status_url == 200:
        api_bsv = 1
    else:
        api_bsv = 0

    return api_bsv


def transaction_details():

    hex_data = open_bsv_file()
    txid = hex_data

    url = "https://api.whatsonchain.com/v1/bsv/test/tx/hash/" + txid
    response = requests.get(url)
    data = response.json()
    vout = data['vout']
    vout_x = vout[0]
    scriptPubKey = vout_x['scriptPubKey']
    hex_x = scriptPubKey['hex']
    first_list_save = bytes.fromhex(str(hex_x)).decode('latin-1')
    bsv_data_x = first_list_save[7:]

    return bsv_data_x


def pk_file():

    """ Check pk.txt file """

    pk_list_file = os.listdir(os.path.join(filepath, "data\\bitcoinkey\\"))

    return pk_list_file


def open_bsv_file():

    """ Open bsv_save file """

    file_bsv = open(os.path.join(filepath, "data\\save\\bsv_save.txt"), "r")
    hex_data = file_bsv.read()
    file_bsv.close()

    return hex_data


def private_key(pk_list_file):

    file = open(os.path.join(filepath, "data\\bitcoinkey\\" + pk_list_file[0]))
    pk_key = file.read()

    return pk_key


def check_bsv(pk_key):

    my_key = pk_key
    try:
        key = bitsv.Key.from_hex(my_key, network="test")
        balance_bsv = key.get_balance('bsv')
        if balance_bsv == 0:
            key = "Error"
            balance_bsv = "Error"
    except ValueError:
        key = "Error"
        balance_bsv = "Error"

    return key, balance_bsv


def send_save(key, save_list):

    list_of_pushdata = [bytes.fromhex('6d01'), save_list.encode('utf-8')]
    key.send_op_return(list_of_pushdata, fee=0)
    time.sleep(5)
    unspend = key.get_unspents()
    if not unspend:
        unspend = "Error"

    return unspend


def save(one_id):

    save_file = open(os.path.join(filepath, "data\\save\\bsv_save.txt"), "w")
    save_file.write(one_id)
    save_file.close()
