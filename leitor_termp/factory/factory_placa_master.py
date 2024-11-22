from .factory_abs import FactoryPlacaAbstract
from placa import PlacaMaster



class FactoryPlacaMaster(FactoryPlacaAbstract):

    def create_placa(self):
        return PlacaMaster()