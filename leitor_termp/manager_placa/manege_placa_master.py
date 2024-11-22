from model import Db_information
import json
from datetime import datetime
from model import registro_instalacao
import threading
import data_base

from .base import Base

class ManagerPlacaMaster(Base):
        
        def execute(self):
                with self.lock:
                        data_placa                      =       self.conn.select_placa_main()
               
                
                for item in data_placa:
                        self.lista_canal.append(item['canal_placa'])
                        self.lista_sensor.append(item['sensor_placa'])
                        self.chave_cordoes.append(item['cordao_fisico'])

                        
                