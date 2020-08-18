from iqoptionapi.stable_api import IQ_Option
import json

API = IQ_Option('eder0782@hotmail.com','iqo473pti116')

API.connect()

paridade = 'EURUSD'

timeframe = 5

indicador = API.get_technical_indicators(paridade)



for ind in indicador:
    if ind['candle_size']==timeframe*60 and ind['group']=='MOVING AVERAGES' and 'Simple' in ind['name']:
        print(ind)
    # print(json.dumps(ind['candle_size']==timeframe *60))
