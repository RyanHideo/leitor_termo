import asyncio
import json
import time
import traceback
import socket
from .placa_abs import PlacaAbstract
import data_base
from model import Db_information
from manager_placa import ManagerPlacaSlave

class PlacaSlave(PlacaAbstract, ManagerPlacaSlave):

    def __init__(self, ip_placa, cod_placa) -> None:
        self.ip_placa = ip_placa
        self.cod_placa = cod_placa
        self.db = Db_information("Termometria", 3306, "localhost", "leitor_termo", "termometria")
        self.conn = data_base.Connector(self.db)
    
    def __str__(self) -> str:
        return 'Iniciando leitura Placa-Slave' + f'{self.ip_placa}'

    async def read_temp(self):
       
       
        data_temp       =   {}
        data_placa      =   self.conn.select_data_placa_secun(self.cod_placa)
        chave_cordoes   =   []
        lista_canal     =   []
        lista_sensor    =   []



        for item in data_placa:

            lista_canal.append(item['canal_placa'])
            lista_sensor.append(item['sensor_placa'])
            chave_cordoes.append(item['cordao_fisico'])

        lista_final = [{'chave':chave_cordoes, 'lista_canal': lista_canal, 'lista_sensor':lista_sensor}]
        erro = 0

        while erro < 3:
            try:
                reader, writer = await asyncio.open_connection(self.ip_placa, 8080)
                print(f"Conectado ao servidor {self.ip_placa}")

                request = json.dumps(lista_final).encode('utf-8')
                writer.write(request)
                await writer.drain()

                data = await reader.read(4096)
                leitura_list = json.loads(data.decode('utf-8'))
                response_content = dict(zip(chave_cordoes, leitura_list))
                chave_cordoes.clear()
                data_temp.update(response_content)
                self.result_placa_secund = data_temp
                break

            except (ConnectionRefusedError, socket.error) as e:
                erro += 1
                await asyncio.sleep(30)

            except Exception as e:
                erro += 1
                traceback.print_exc()
                await asyncio.sleep(30)

            if erro == 3:
                self.result_placa_secund = {chave: '' for chave in chave_cordoes}
                break
