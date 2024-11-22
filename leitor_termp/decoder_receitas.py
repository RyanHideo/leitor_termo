import model

class decoder:
    def __init__(self):
        self.decoder_dados_usuario
        self.decoder_dados_on_line
        
    def decoder_dados_usuario(self, obj):
        return model.dados_usuario_receita_aeracao(obj['intervaloTemp_habilita'], 
            obj['intervaloTemp_temp_min'], obj['intervaloTemp_temp_max'],
            obj['tempSilos_habilita'], obj['tempSilos_tipo_set_point'],
            obj['tempSilos_num_sensores_laterais'], obj['tempSilos_num_sensores_centro'],
            obj['tempSilos_temp_set_point'], obj['tempSilos_limite_temperatura'],
            obj['intervaloHorario_habilita'], obj['intervaloHorario_hora_inicial'],
            obj['intervaloHorario_minuto_inicial'], obj['intervaloHorario_hora_final'],
            obj['intervaloHorario_minuto_final'], obj['intervaloHorario_habilita_domingo'],
            obj['intervaloHorario_habilita_segunda'], obj['intervaloHorario_habilita_terca'],
            obj['intervaloHorario_habilita_quarta'], obj['intervaloHorario_habilita_quinta'],
            obj['intervaloHorario_habilita_sexta'], obj['intervaloHorario_habilita_sabado'],
            obj['chuva_habilita'], obj['umidade_habilita'], obj['umidade_min_valor'],
            obj['umidade_max_valor'], obj['pontoOrvalho_habilita'],
            obj['pontoOrvalho_temp_ponto_orvalho'])

    def decoder_dados_on_line(self, obj):
        return model.dados_on_line_receia_aeracao(obj['result_temp_silos'],
            obj['result_temp_ambiente'], obj['result_media_calculada'],
            obj['result_valor_media_calculada'], obj['result_horario'],
            obj['result_chuva'], obj['result_umidade'], obj['result_ponto_orvalho'],
            obj['var_temp_ambiente'], obj['var_umidade_relativa'], obj['var_sensor_chuva'],
            obj['var_date_time_cpu'], obj['var_temp_ponto_orvalho'])


