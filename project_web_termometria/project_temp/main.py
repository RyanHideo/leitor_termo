import json
import time
from callapi import CallAPi
from .query_database import *
from .database import MysqlConnector
from .search_data import SearchData
from .response_api import ResponseApi
import http.client

tentativas = 5
erros = 0

error_mapping = {
     
                    http.client.HTTPException: error_http_exception(),
                    ConnectionError: error_connection(),
                    TimeoutError: error_timeout(),
                    json.JSONDecodeError: error_json_decode(),
                    # Add more mappings as needed
                }



class App:

    def __init__(self):
                        self.search_data        =    SearchData()
                        self.request            =    CallAPi()
                        self.response           =    ResponseApi()
                        self.erros              =    0
                        self.dados_temperatura  =    []
                        self.datas              =    []
                        ##print("selferro = 0")


    def do_call_to_api(self): 
        db                                  =       MysqlConnector()
        tentativas                          =       5
        dados_temperatura, dados_cliente    =       self.search_data.search()

        if len(dados_temperatura) != 0:
                dados_enviar                =       [{'Leituras': dados_temperatura}, {'Dados_cliente': dados_cliente}]
                self.datas                  =       [item['Data'] for item in dados_enviar[0]["Leituras"]]
               
                if dados_temperatura is not None:
                    while self.erros < tentativas:
                        try:
                            response        =           self.request.Post(dados_enviar)
                            result          =           self.response.treat_response(response, self.datas)
  
                            break

                        except ( 
                                http.client.HTTPException, 
                                ConnectionError, TimeoutError, 
                                json.JSONDecodeError
                                ) as e:
                            
                            time.sleep(30)
                            db.set_query(error_mapping.get(type(e)))
                            self.erros += 1

                        except Exception as e:
                            db.set_query(error_except_exception())
                            
                            time.sleep(30)
                            self.erros += 1
                            # Log the exception or handle it appropriately

                    if self.erros == tentativas:
                        self.erros = 0
                        
                        time.sleep(300)

        elif len(dados_temperatura) == 0:
            
            pass

    @staticmethod
    def run():
        while True:
            try:
                app_instance = App()
                app_instance.do_call_to_api()
                time.sleep(2)

            except Exception as e:
                print(e)
            
            

