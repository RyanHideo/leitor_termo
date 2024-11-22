import json 

class Formatter:
    
    def data_temperature(self, temperature):
        
        self.temperature            =       temperature
        temperatura                 =       []
        
        for item in temperature:
                self.sensores               =       json.loads(item['temperaturas'])
                data_hora_string            =       item['data'].strftime("%Y-%m-%d %H:%M:%S")
                dados_temperatura           =   {
                                                        'Temperaturas': json.loads(item['temperaturas']),
                                                        'Nome_Silo' : item['nome'],
                                                        'Data': data_hora_string,
                                                        'Config_fisica':json.loads(item['config_fisica'])
                                                }
                
                data_dump           =       json.dumps(dados_temperatura)
                data_load           =       json.loads(data_dump)
              
                temperatura.append(data_load)
        return temperatura
        

    def data_client(self, dados_cliente):
        # TOTAL_ARMAZENAMENTO = 300000
        # SACA_KG = 60

        # temp_sensores = [valor for chave , valor in self.sensores.items() if self.sensores != None else None]
        # print(temp_sensores)




        
        # total_sensor = [valor for chave,valor in self.sensores.items()]
        # temp_silo = sum(float(valor) for chave,valor in self.sensores.items())
        # media_silo = temp_silo / len(total_sensor)
        # print(f'{media_silo:.0f}')

        
        # filtrado = {chave: valor for chave,valor in self.sensores.items() if chave.startswith("Ch1S")}
        # tem_grao = {chave: valor for chave , valor in filtrado.items() if valor < '29.00'}

        # total_sensores = len(filtrado)
        # qntd_sensor = len(tem_grao) * 100

        # percentual_silo = (total_sensores * qntd_sensor) / 100
        # qnt_armazenamento = (percentual_silo * TOTAL_ARMAZENAMENTO) / 100

        # total_saca = qnt_armazenamento / SACA_KG
        
        # saca_por_ton  =  (SACA_KG * total_saca) / 1000

        # print(f'TOTAL_TON: {saca_por_ton:.0f} TONELADAS')
        # print(f'PERCENTUAL_SACA: {total_saca:.0f} MIL')
        # print(f'porcentual_armazenamento: {percentual_silo:.0f} MIL')
       
        for dado_cliente in dados_cliente:
            date_client       =     {
                                        'ID_cliente'              :   dado_cliente['id_cliente'],
                                        'ID_planta'               :   dado_cliente['id_planta'],
                                        'ID_equipamento'          :   dado_cliente['id_equipamento'],
                                        'ID_placa'                :   dado_cliente['id_placa'],
                                        'superaquecimento'        :   0,
                                        'nivel_percentual_silo'   :   0,
                                        'total_armazenado_ton'    :   0,
                                        'Total_armazenado_sacas'  :   0
                                    }

            data_dumps          =       json.dumps(date_client)
            data_load           =       json.loads(data_dumps)

            return data_load
        


