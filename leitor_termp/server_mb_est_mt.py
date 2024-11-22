from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from datetime import datetime
from datetime import date
from db_information import db_information
import data_base
from model import estacao_mt

#connect data base
_db_connect = db_information()
conn = data_base.Connector(_db_connect.get_data_base_information())

ip = conn.get_ip_instal()
#print(ip)

if (ip != ""):
    #Cria uma instância do servidor modbus
    server = ModbusServer(ip, 502, no_block=True)

dt = datetime
count_update = 0

#variaveis da estacao mt
_estacao_mt = estacao_mt(0.0, 0.0, 0, dt.now(), 0)

#status da receita, para o plc poder ler e acionar a aeração
status_receita = [0]
status_receita[0] = conn.get_status_receita()
print(status_receita)

try:
    print("Start server...")
    server.start()
    print("Server is online")
    State = [0]
    #db.set_holding_registers(1, [12,13,14], srv_info=None)
    
    while True:
        _estacao_mt.temp_ambiente = server.data_bank.get_holding_registers(0, srv_info=None)[0]
        
        #print(server.data_bank.get_holding_registers(0, 10, srv_info=None))
        _estacao_mt.umidade_rel = server.data_bank.get_holding_registers(1, 1, srv_info=None)[0]
        _estacao_mt.chuva = server.data_bank.get_holding_registers(2, 1, srv_info=None)[0]
        _estacao_mt.data_atualizacao = dt.now()

        if (_estacao_mt.temp_ambiente > 0):
            _estacao_mt.temp_ambiente = _estacao_mt.temp_ambiente / 10
        if (_estacao_mt.umidade_rel > 0):
            _estacao_mt.umidade_rel = _estacao_mt.umidade_rel / 10

        if(_estacao_mt.temp_ambiente == 0 or _estacao_mt.umidade_rel == 0):
            _estacao_mt.status = 0
        else:
            _estacao_mt.status = 1

        sleep(0.01)
        count_update = count_update + 1
        #_estacao_mt.temp_ambiente = _estacao_mt.temp_ambiente / 10
        #_estacao_mt.umidade_rel = _estacao_mt.umidade_rel / 10

        if (count_update > 500):
            conn.update_estacao_mt(_estacao_mt)
            count_update = 0
            #print(status_receita[0])
            status_receita[0] = conn.get_status_receita()
            server.data_bank.set_holding_registers(3,status_receita[0], srv_info=None)
except:
    #print("Shutdown server ...")
    #server.stop()
    #print("Server is offline")
    print("error on server")

