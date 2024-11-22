from .base import Base
class ManagerPlacaSlave(Base):

    _cod_placa  =   []
    _ip_placa   =   []
    
    def execute(self):
        with self.lock:
            self.result_placa_secund    =       self.conn.select_placa_secund()
            print('Dados da Placa Secundária ::: ',self.result_placa_secund)
        cod_placa       =   [cod['cod_placa'] for cod in self.result_placa_secund]
        ip_placa        =   [ip['ip'] for ip in self.result_placa_secund]

        self._cod_placa =   cod_placa
        self._ip_placa  =   ip_placa