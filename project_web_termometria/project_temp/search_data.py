from .formatter_json import Formatter
from .query_database import *
from .database import MysqlConnector

class SearchData:

    def search(self):
                    
                    conection_dataBase       =        MysqlConnector()
                    formatter                =        Formatter()
                    temperatura              =        conection_dataBase.get_query(get_temperatura())
                    cliente                  =        conection_dataBase.get_query(get_cliente())
                    dados_temperatura        =        formatter.data_temperature(temperatura)
                    dados_cliente            =        formatter.data_client(cliente)
                    
                    return dados_temperatura , dados_cliente