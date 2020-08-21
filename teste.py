from api_iq.iqoptionapi.stable_api import IQ_Option
import multiprocessing, threading
import time
import sys, os
from datetime import datetime, timedelta

API = IQ_Option('eder0782@hotmail.com','iqo473pti116')



var = True


def ativar():

    API.connect()
    API.change_balance('PRACTICE')
    
    
    while True:
        print('ativo')
        global var
        if not var:
            API.api.close()       
            sys.exit()
        time.sleep(1)

def conectar():
    global var
    proc = threading.Thread(target=ativar)
    proc.start()


def balanco():
    try:
        return  API.get_balance()
    except:
        return 'falha na conexão'
def muda_var(valor):
    global var
    var = valor


API.connect()

print(API.get_server_timestamp())

print(datetime.fromtimestamp(API.get_server_timestamp()))


    
    