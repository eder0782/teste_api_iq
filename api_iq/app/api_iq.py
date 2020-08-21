#from app.models import tabelas
from api_iq.iqoptionapi.stable_api import IQ_Option
import time
from datetime import datetime

API = None

def conectar(email,senha):
    global API
    API = IQ_Option(email,senha)
    API.connect()
    retorno = None
    while True:    
        if API.check_connect() == False:
                   		
            API.connect()
            retorno = False
        else:
           
            retorno = True
            break
        
        time.sleep(1)
    
    return retorno


def alterar_conta(tipo_conta):
    try:
        global API
        API.change_balance(tipo_conta)
        return True
    except :
        return False
    

def pegar_balanco():
    try:
        return API.get_balance()
    except :
        return 'FALHA NA CONEXÃO'

def desconectar():
    try:
        API.api.close()
        return True
    except :
        return False
    
    
    



