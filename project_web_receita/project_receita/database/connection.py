import mysql.connector
import time

class QueryError(Exception):
    pass

class MysqlConnection:

    def __init__(self):
        while True:
            try:
                self.__connection = mysql.connector.connect(

                                                                host = "localhost",
                                                                user = "leitor_termo",
                                                                password = "termometria",
                                                                db = "Termometria"
                                                            ) 
                if self.__connection.is_connected():
                    print("conected.")
                    break
            except mysql.connector.Error as e:
                print(f"Exception {e}")
                pass

            print("erro trying in 10 secouds")
            time.sleep(10)
    def __conect(self) -> mysql.connector.connection:
        self.__connection()
                    
    def desconect(self):
        self.__connection.close()

    
    def get_query_receita(self):
        if not self.__connection.is_connected or self.__connection is None:
            self.__connection = self.__conect() 
        cursor = self.__connection.cursor()
        try:
            cursor.execute("SELECT * FROM receita_aeracao ORDER BY codigo DESC LIMIT 1;")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise QueryError(f"Erro in querying{e}")
        finally:
            cursor.close()
    def get_query_id_equipamento(self):
        if not self.__connection.is_connected or self.__connection is None:
            self.__connection = self.__conect()
        cursor = self.__connection.cursor()
        try:
            cursor.execute("SELECT ConfigInstalacao.id_equipamento FROM ConfigInstalacao;")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as e:
            raise QueryError(f"Erro in querying{e}")
        finally:
            cursor.close()
    def set_query(self,query):
        if not self.__connection.is_connected or self.__connection is None:
            self.__connection = self.__conect()
        cursor = self.__connection.cursor(dictionary=True)
        try:
            cursor.execute(query)
            self.__connection.commit()
        except mysql.connector.Error as e:
            raise QueryError(f"erro in query: {e}")
        finally:
            cursor.close()
    def set_query_receita_web(self,
                                atualizada_em,
                                intervaloTemp_habilita,
                                intervaloHorario_habilita,
                                chuva_habilita,
                                umidade_habilita,
                                pontoOrvalho_habilita,
                                temp_min,
                                temp_max,
                                hora_ini,
                                min_inicial,
                                min_fin,
                                hora_fin,dom, 
                                seg, ter, quar, 
                                quin, 
                                sex, 
                                sab,
                                chuva,
                                um_min,
                                um_max,
                                po,
                                tempSilos_habilita,
                                tempSilos_tipo_set_point,tempSilos_limite_temperatura,tempSilos_temp_set_point):
                            
        if not self.__connection.is_connected or self.__connection is None:
            self.__connection = self.__conect()
        cursor  = self.__connection.cursor(dictionary=True)
        
        try:

            query = """
                        UPDATE receita_aeracao
                        SET team_id = 'importado_web', usuario = 'importado_web ', criada_em = %s, dados_usuario = JSON_SET(
                            dados_usuario,
                            '$.intervaloTemp_habilita',%s,
                            '$.intervaloHorario_habilita',%s,
                            '$.chuva_habilita',%s,
                            '$.umidade_habilita',%s,
                            '$.pontoOrvalho_habilita',%s,
                            '$.intervaloTemp_temp_min',%s,
                            '$.intervaloTemp_temp_max',%s,
                            '$.intervaloHorario_hora_inicial',%s,
                            '$.intervaloHorario_minuto_inicial',%s,
                            '$.intervaloHorario_hora_final',%s,
                            '$.intervaloHorario_minuto_final',%s,
                            '$.intervaloHorario_habilita_domingo',%s,
                            '$.intervaloHorario_habilita_segunda',%s,
                            '$.intervaloHorario_habilita_terca',%s,
                            '$.intervaloHorario_habilita_quarta',%s,
                            '$.intervaloHorario_habilita_quinta',%s,
                            '$.intervaloHorario_habilita_sexta',%s,
                            '$.intervaloHorario_habilita_sabado',%s,
                            '$.chuva_habilita',%s,
                            '$.umidade_min_valor',%s,
                            '$.umidade_max_valor',%s,
                            '$.pontoOrvalho_temp_ponto_orvalho',%s,
                            '$.tempSilos_habilita',%s,
                            '$.tempSilos_tipo_set_point',%s,
                            '$.tempSilos_limite_temperatura',%s,
                            '$.tempSilos_temp_set_point',%s
                            
                        )
                        WHERE codigo order by codigo desc limit 1;
                    """
            paremetro =  (atualizada_em,intervaloTemp_habilita,intervaloHorario_habilita,chuva_habilita,umidade_habilita,pontoOrvalho_habilita,temp_min,temp_max,hora_ini,min_inicial,min_fin,hora_fin,dom,seg, ter, quar, quin, sex, sab,chuva,um_min,um_max,po,tempSilos_habilita,tempSilos_tipo_set_point,tempSilos_limite_temperatura,tempSilos_temp_set_point)
            cursor.execute(query,paremetro)
            self.__connection.commit()
            print("Query executada com sucesso")
            
            # Para depuração, se desejar verificar a quantidade de linhas afetadas
            print(f"Linhas afetadas: {cursor.rowcount}")

        except mysql.connector.Error as e:
            # Exibir o erro SQL
            print(f"Erro na execução da query: {e}")
            raise QueryError(f"Erro na execução da query: {e}")

        except Exception as e:
            # Exibir outros erros genéricos
            print(f"Erro inesperado: {e}")
            raise QueryError(f"Erro inesperado: {e}")

        finally:
            cursor.close()


