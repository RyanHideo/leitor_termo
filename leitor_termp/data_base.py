import mariadb
import sys
from model import Db_information
from model import Config_install
from model import Registro
from model import Registro_sensor
from model import registro_instalacao
from model import receita_aeracao
from model import estacao_mt

class Connector:
    def __init__(self, Db_information):
        self.user = Db_information.user
        self.password = Db_information.password
        self.host = Db_information.host
        self.port = Db_information.port
        self.database = Db_information.database
        self.conn = mariadb.connect()

    def connect(self):
        try:
            self.conn = mariadb.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.database
            )
        except mariadb.Error as e:
            #print(f"Error connection to MariaDB Plataform: {e}")
            sys.exit(1)

    def command_sql(self, command):
        #Connect to database
        self.connect()
        #Get Cursor
        cur = self.conn.cursor()
        cur.execute(command)
        self.conn.close()
        return cur


    def get_informaton_instal(self):
        #Connect to database
        self.connect()
        #Get Cursor
        cur = self.conn.cursor()
        cur.execute("SELECT nome, tipo, dados, configuracao_fisica, ip FROM ConfigInstalacao")
        #Exract information
        for (nome, tipo, dados, configuracao_fisica, ip) in cur:
            config = Config_install(nome, tipo, dados,configuracao_fisica, ip)
        self.conn.close()
        return config


    def get_ip_instal(self):
        try:
            #Connect to database
            self.connect()
            _ip_install = ""
            #Get Cursor
            cur = self.conn.cursor()
            cur.execute("SELECT ip FROM ConfigInstalacao")
            #Exract information
            for (ip) in cur:
                _ip_install = ip
        except mariadb.Error as e:
            ...
            #print(f"Error: {e}")
        self.conn.close()
        new_ip = ''.join( x for x in _ip_install if x not in "(),")
        ##print(new_ip)
        return new_ip


    def insert_record(self, Registro):
        try:
            #Connect to database
            self.connect()
            record = Registro
            #Get Cursor
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO RegistroTemperaturas (nome, data, horario, tipo_instal, registros) VALUES (?, ?, ?, ?, ?)", (record.nome, record.data, record.horario, record.tipo, record.registros))
           # cur.execute(comand)
        except mariadb.Error as e:
            ...
            #print(f"Error: {e}")
        self.conn.commit()
        #print(f"Last Inserted ID: {cur.lastrowid}")
        self.conn.close()
        ##print(comand)


    def insert_record_sensor(self, Registro_sensor):
        try:
            #Connect to database
            self.connect()
            record = Registro_sensor
            #Get Cursor
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO registros (created_at, data_hora,tag, tipo, valor) VALUES (?, ?, ?, ?, ?)",
                    (record.created_at, record.data_hora, record.tag, record.tipo, record.valor))
           # cur.execute(comand)
        except mariadb.Error as e:
            ...
            #print(f"Error: {e}")
        self.conn.commit()
        ##print(f"Last Inserted ID: {cur.lastrowid}")
        self.conn.close()
        ##print(comand)

    def insert_registro_instalacao(self, registro_instalacao):
        try:
            #connect to database
            self.connect()
            record = registro_instalacao
            #Get Cursor
            cur = self.conn.cursor()
            cur.execute(
                "INSERT INTO registro_instalacao (config_fisica, data, nome, temperaturas) VALUES (?, ?, ?, ?)",
                    (record.configuracao_fisica, record.data, record.nome, record.registros_temperaturas))
        except mariadb.Error as e:
            ...
            #print(f"Error: {e}")
        self.conn.commit()
        #print(f"Last Inserted ID: {cur.lastrowid}")
        self.conn.close()


    def get_atual_receita(self):
        try:
            #Connect to database
            self.connect()
            #Get Cursor
            cur = self.conn.cursor()
            cur.execute("SELECT codigo, criada_em, team_id, usuario, dados_usuario, atualizada_em, dados_on_line, status FROM `receita_aeracao` WHERE codigo = (SELECT MAX(codigo) FROM receita_aeracao)")
            #Extract information
            for (codigo, criada_em, team_id, usuario, dados_usuario, atualizada_em, dados_on_line, status) in cur:
                receita_aer = receita_aeracao(codigo, criada_em, team_id, usuario, dados_usuario, dados_on_line, atualizada_em, status)
        except mariadb.Error as e:
            ...
            #print(f"Error: {e}")
        self.conn.close()
        return receita_aer

    def select_ultimo_registro_instalacao(self):
        try:
            #Connect to database
            self.connect()
            #Get Cursor
            cur = self.conn.cursor()
            cur.execute("SELECT codigo, nome, config_fisica, data, temperaturas FROM `registro_instalacao` WHERE codigo = (SELECT MAX(codigo) FROM registro_instalacao)")
            #Extract information
            for (codigo, nome, config_fisica, data, temperaturas) in cur:
                reg_instalacao = registro_instalacao(codigo, nome, config_fisica, data, temperaturas)
        except mariadb.Error as e:
            ...
            #print(f"Error: {e}")
        self.conn.close()
        return reg_instalacao


    def update_estacao_mt(self, estacao_mt):
        try:
            #Connect to database
            self.connect()
            dados_est_mt = estacao_mt
            #Get Cursor
            cur = self.conn.cursor()
            cur.execute(
                f"UPDATE estacao_mt SET temp_ambiente = {dados_est_mt.temp_ambiente}," +
                f"umidade_rel = {dados_est_mt.umidade_rel}, chuva = {dados_est_mt.chuva}," +
                f"data_atualizacao = '{dados_est_mt.data_atualizacao}', " +
                f"status = {dados_est_mt.status} WHERE 1")
        except mariadb.Error as e:
            ...
            #print(f"Error: {e}")
        ##print(f"UPDATE estacao_mt SET temp_ambiente = {dados_est_mt.temp_ambiente}," +
        #        f"umidade_rel = {dados_est_mt.umidade_rel}, chuva = {dados_est_mt.chuva}," +
        #        f"data_atualizacao = '{dados_est_mt.data_atualizacao}', " +
        #        f"status = {dados_est_mt.status} WHERE 1")
        self.conn.commit()
        self.conn.close()

    def select_estacao_mt(self):
        try:
            #Connect to database
            self.connect()
            #Get Cursor
            cur = self.conn.cursor()
            cur.execute("SELECT temp_ambiente, umidade_rel, chuva, data_atualizacao, status FROM estacao_mt")
            #Extract information
            for (temp_ambiente, umidade_rel, chuva, data_atualizacao, status) in cur:
                dados_estacao = estacao_mt(temp_ambiente, umidade_rel, chuva, data_atualizacao, status)
        except mariadb.Error as e:
            #print(f"Error: {e}")
            ...
        self.conn.close()
        return dados_estacao

    def update_receita_on_line(self, receita_on_line, codigo, data_atualizacao, status):
        try:
            #connect to database
            self.connect()
            record = registro_instalacao
            #Get Cursor
            cur = self.conn.cursor()
            cur.execute(
                f"UPDATE receita_aeracao SET dados_on_line = '{receita_on_line}', " +
                f" atualizada_em = '{data_atualizacao}', status = {status} WHERE codigo = {codigo}")
        except mariadb.Error as e:
            #print(f"Error: {e}")
            #print(f"UPDATE receita_aeracao SET dados_on_line = '{receita_on_line}', " +
                f" atualizada_em = '{data_atualizacao}', status = {status} WHERE codigo = {codigo}"
        self.conn.commit()
        self.conn.close()

    def get_status_receita(self):
        try:
            #Connect to database
            self.connect()
            #Get Cursor
            cur = self.conn.cursor()
            cur.execute("SELECT status FROM `receita_aeracao` WHERE codigo = (SELECT MAX(codigo) FROM receita_aeracao)")
            #Extract information
            for ( status) in cur:
                status_receita =  status
        except mariadb.Error as e:
            #print(f"Error: {e}")
            ...
        self.conn.close()
        return status_receita


    def select_placa_main(self):
        
        try:
            self.connect()
            cur = self.conn.cursor(dictionary=True)
            cur.execute(f'select * from registro_cordoes where cod_placa = 1')
            result = cur.fetchall()
            return result
        except mariadb.Error as e:
            #print(e)
            ...

    def select_placa_secund(self):      
        try:    
            self.connect()
            cur = self.conn.cursor(dictionary = True)
            cur.execute(f'select * from registro_placas where cod_placa != 1')
            result = cur.fetchall()
            return result
        except mariadb.Error as e:
            print(e)
            ...
    
    def select_data_placa_secun(self, cod_placa):
        try:
            self.connect()
            cur = self.conn.cursor(dictionary=True)
            cur.execute(f'select * from registro_cordoes where cod_placa = {cod_placa}')
            result = cur.fetchall()
            return result
        except mariadb.Error as e:
            ...

    
   
