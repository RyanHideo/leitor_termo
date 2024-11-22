from model import Db_information

class db_information:
    def __init__ (self):
        self.get_data_base_information

    def get_data_base_information(self):
        db_i = Db_information("Termometria",3306,"localhost","leitor_termo","termometria")
        return db_i
