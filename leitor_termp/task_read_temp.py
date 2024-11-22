import json
from datetime import datetime
import asyncio
from manager_placa import ManagerPlacaSlave
from factory.factory_placa_master import FactoryPlacaMaster
from factory.factory_placa_slave import FactoryPlacaSlave

class ManagerObjectPlaca:
    def __init__(self):
        self._list_placa = []
        self.placa_slave = ManagerPlacaSlave()

    def manager_object(self):
        self.cod = self.placa_slave._cod_placa
        self.ip = self.placa_slave._ip_placa

        # Se não houver placas slaves, retorna sem adicionar nada à lista
        if not self.cod or not self.ip:
            return

        for indice, cod in enumerate(self.placa_slave._cod_placa):
            _factory_placa = FactoryPlacaSlave()
            ip = self.ip[indice]
            placa = _factory_placa.create_placa(ip, cod)
            self._list_placa.append(placa)

        self.placa_slave = None

    @property
    def get_list(self):
        return self._list_placa

class ManagerThreads:
    def __init__(self):
        self.manager_object_slave = ManagerObjectPlaca()
        self.tasks = []
        self.factory_master = FactoryPlacaMaster()
        self.placa_master = self.factory_master.create_placa()

    async def _init_threads(self):
        self.manager_object_slave.manager_object()

        # Executa leitura da placa master diretamente
        self.placa_master.read_temp()

        # Verifica se há placas slave
        if self.manager_object_slave.get_list:
            # Cria tasks assíncronas para cada placa slave
            for placa in self.manager_object_slave.get_list:
                th = asyncio.create_task(placa.read_temp())
                self.tasks.append(th)

            # Aguarda a conclusão de todas as tasks das slaves
            await asyncio.gather(*self.tasks)

        # Coleta os resultados
        leituras_master = self.placa_master.result_placa_master
        self.placa_master.result_placa_master = None
        leituras_slaves = {}

        for pl in self.manager_object_slave.get_list:
            leituras_slaves.update(pl.result_placa_secund)

        print('LEITURAS MASTER::::: ', leituras_master)
        print('LEITURAS SLAVE::::: ', leituras_slaves)
        leituras_completas = {**leituras_master, **leituras_slaves}
        print('COMPLETAS::::: ', leituras_completas)
        self.placa_master.save(leituras_completas)

        leituras_completas = None
        self.placa_master.result_placa_master = None
        self.factory_master = None

        return leituras_completas

class App:
    async def run(self):
        threads = ManagerThreads()
        result = await threads._init_threads()
        return result

enable = True

async def main_loop():
    app = App()

    while True:
        now = datetime.now()
        global enable
        if now.minute == 0 and now.second < 30:
            enable = True
        
        if enable == True:
            result = await app.run()
            enable = False
        print(f"Leituras completadas: {result}")
        await asyncio.sleep(20)  # Evita múltiplas execuções dentro do mesmo minuto
       
if __name__ == "__main__":
    asyncio.run(main_loop())
