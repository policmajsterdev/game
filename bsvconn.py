import os.path
import time
import bitsv
import sys

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

filepath = os.path.dirname(__file__)


def check_bsv():

    my_key = '32047ac7f8247e2dcaed827bdbf27a7e388a92e47f4935d254966f4dc8035c60'
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

    save_file = open("data\\save\\" + one_id + ".txt", "w")
    save_file.close()
