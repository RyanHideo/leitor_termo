import json
from datetime import date
from datetime import datetime
import threading
from manager_placa import ManagerPlacaSlave
from factory.factory_placa_master import  FactoryPlacaMaster
from factory.factory_placa_slave import  FactoryPlacaSlave

class ManagerObjectPlaca:

    _list_placa = []
    placa_slave = ManagerPlacaSlave()
    def manager_object(self):    
        self.cod    =   self.placa_slave._cod_placa
        self.ip     =   self.placa_slave._ip_placa

        for indice , cod in  enumerate(self.placa_slave._cod_placa):

            _factory_placa = FactoryPlacaSlave()
            ip      =   self.ip[indice]
            placa   =   _factory_placa.create_placa(ip, cod)
            self._list_placa.append(placa)  

    @property
    def get_list(self):
        return self._list_placa


class ManagerThreads:

    manager_object_slave    =   ManagerObjectPlaca()
    tasks                   =   []
    factory_master          =   FactoryPlacaMaster()
    placa_master            =   factory_master.create_placa()
    th_master               =   threading.Thread(target=placa_master.read_temp)

    def _init_threds(self):
        self.manager_object_slave.manager_object()
        for placa in self.manager_object_slave._list_placa:
            th = threading.Thread(target=placa.read_temp)
            self.tasks.append(th)

        self.th_master.start()
        [th.start() for th in self.tasks]
        [th.join() for th in self.tasks]
        self.th_master.join()
    
        
        leituras_master     =   self.placa_master.result_placa_master
        leituras_slaves     =   {}

        placas              =   self.manager_object_slave.get_list

        for pl in placas:
            leituras_slaves.update(pl.result_placa_secund)

        leituras_completas = {**leituras_master,**leituras_slaves }

        self.placa_master.save(leituras_completas)

        return leituras_completas


class App:
    def run(self):

        threads = ManagerThreads()
        result = threads._init_threds()
        return result


if __name__ == "__main__":
    dt = datetime
    while True:
        #if dt.now().minute == 0 and dt.now().second < 30:
        app     =   App()
        app.run()



 
