import json
import time
from .query_database import *
from .database import MysqlConnector


tentativas = 5
erros = 0

class ResponseApi:
    
    def __init__(self) -> None:
        self.conection_database = MysqlConnector()

    def treat_response(self,response, datas):
        global erros
        while erros <= tentativas:
            if response.status      ==      202:

                self.datas          =       datas
                objeto_resposta     =       json.loads(response.read().decode('utf-8'))
                data_formatada      =       [' '.join(item) for item in objeto_resposta]
                datas               =       [data for data in datas if data in data_formatada]
                datas_atualizar     =       str(datas)[1:-1]

                if len(datas_atualizar) != 0:
                    self.conection_database.set_query(update(datas_atualizar))
                    break
                
                else:
                    self.conection_database.set_query(update_if_erro())
                    break
                
            elif response.status == 500:
                time.sleep(30)
                content = response.read()
                self.conection_database.set_query(error_status500())
               
                
            elif response.status == 404:
               
                time.sleep(30)
                self.conection_database.set_query(error_status404())
                erros += 1

            if erros == tentativas:
                erros = 0
                break