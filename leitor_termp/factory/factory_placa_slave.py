from .factory_abs import FactoryPlacaAbstract
from placa import PlacaSlave


class FactoryPlacaSlave(FactoryPlacaAbstract):

    def create_placa(self,ip_placa, cod_placa):
        return PlacaSlave(ip_placa, cod_placa)