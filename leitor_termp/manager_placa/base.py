import json
from datetime import datetime
from model import registro_instalacao
import threading
from model import Db_information
import data_base
from abc import ABC, abstractmethod
from leitor_termo import Leitor_temp

class Base:

    
    def __init__(self) -> None:
        self.db                         =       Db_information("Termometria",3306,"localhost","leitor_termo","termometria")
        self.conn                       =       data_base.Connector(self.db)
        self.conf                       =       self.conn.get_informaton_instal()
        self.data_instal                =       json.loads(self.conf.dados)
        self.dt                         =       datetime
        self.registro_instal            =       registro_instalacao(0, self.conf.nome, self.conf.configuracao_fisica, self.dt.now(), "")
        self.result_placa_slave         =       None
        self.lock                       =       threading.RLock()
        self.result_placa_master        =       None
        self.leitor                     =       Leitor_temp()
        self.chave_cordoes              =       []
        self.lista_canal                =       []
        self.lista_sensor               =       []
        self.execute()

    
    @abstractmethod
    def execute(self):
        pass