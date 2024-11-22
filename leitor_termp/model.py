class Config_install:

    def __init__(self,nome,tipo,dados,configuracao_fisica, ip):
        self.nome = nome
        self.tipo = tipo
        self.dados = dados
        self.configuracao_fisica = configuracao_fisica
        self.ip = ip


class Db_information:

    def __init__(self,database,port,host,user,password):
        self.database = database
        self.port = port
        self.host = host
        self.user = user
        self.password = password


class Registro:
    def __init__(self, Config_instal, data, horario, registros):
        self.nome = Config_instal.nome
        self.tipo = Config_instal.tipo
        self.data = data
        self.horario = horario
        self.registros = registros


class Registro_sensor:
    def __init__(self, created_at, data_hora, tag, tipo, valor):
        self.created_at = created_at
        self.data_hora = data_hora
        self.tag = tag
        self.tipo = tipo
        self.valor = valor

class registro_instalacao:
    def __init__(self,codigo, nome, configuracao_fisica, data, registros_temperaturas):
        self.codigo = codigo
        self.nome = nome
        self.configuracao_fisica = configuracao_fisica
        self.data = data
        self.registros_temperaturas = registros_temperaturas

class dados_usuario_receita_aeracao:
    def __init__(self, intervaloTemp_habilita, intervaloTemp_temp_min, 
    intervaloTemp_temp_max, tempSilos_habilita,
    tempSilos_tipo_set_point, tempSilos_num_sensores_laterais,
    tempSilos_num_sensores_centro, tempSilos_temp_set_point,
    tempSilos_limite_temperatura, intervaloHorario_habilita,
    intervaloHorario_hora_inicial, intervaloHorario_minuto_inicial,
    intervaloHorario_hora_final, intervaloHorario_minuto_final,
    intervaloHorario_habilita_domingo,
    intervaloHorario_habilita_segunda,
    intervaloHorario_habilita_terca,
    intervaloHorario_habilita_quarta,
    intervaloHorario_habilita_quinta,
    intervaloHorario_habilita_sexta,
    intervaloHorario_habilita_sabado,
    chuva_habilita, umidade_habilita,
    umidade_min_valor, umidade_max_valor,
    pontoOrvalho_habilita, pontoOrvalho_temp_ponto_orvalho):
        self.intervaloTemp_habilita = intervaloTemp_habilita
        self.intervaloTemp_temp_min = intervaloTemp_temp_min
        self.intervaloTemp_temp_max = intervaloTemp_temp_max
        self.tempSilos_habilita = tempSilos_habilita
        self.tempSilos_tipo_set_point = tempSilos_tipo_set_point
        self.tempSilos_num_sensores_laterais = tempSilos_num_sensores_laterais
        self.tempSilos_num_sensores_centro = tempSilos_num_sensores_centro
        self.tempSilos_temp_set_point = tempSilos_temp_set_point
        self.tempSilos_limite_temperatura = tempSilos_limite_temperatura
        self.intervaloHorario_habilita = intervaloHorario_habilita
        self.intervaloHorario_hora_inicial = intervaloHorario_hora_inicial
        self.intervaloHorario_minuto_inicial = intervaloHorario_minuto_inicial
        self.intervaloHorario_hora_final = intervaloHorario_hora_final
        self.intervaloHorario_minuto_final = intervaloHorario_minuto_final
        self.intervaloHorario_habilita_domingo = intervaloHorario_habilita_domingo
        self.intervaloHorario_habilita_segunda = intervaloHorario_habilita_segunda
        self.intervaloHorario_habilita_terca = intervaloHorario_habilita_terca
        self.intervaloHorario_habilita_quarta = intervaloHorario_habilita_quarta
        self.intervaloHorario_habilita_quinta = intervaloHorario_habilita_quinta
        self.intervaloHorario_habilita_sexta = intervaloHorario_habilita_sexta
        self.intervaloHorario_habilita_sabado = intervaloHorario_habilita_sabado
        self.chuva_habilita = chuva_habilita
        self.umidade_habilita = umidade_habilita
        self.umidade_min_valor = umidade_min_valor
        self.umidade_max_valor = umidade_max_valor
        self.pontoOrvalho_habilita = pontoOrvalho_habilita
        self.pontoOrvalho_temp_ponto_orvalho = pontoOrvalho_temp_ponto_orvalho



class dados_on_line_receia_aeracao:
    def __init__ (self, result_temp_silos, result_temp_ambiente,
    result_media_calculada, result_valor_media_calculada, result_horario,
     result_chuva, result_umidade, result_ponto_orvalho, var_temp_ambiente,
    var_umidade_relativa, var_sensor_chuva, var_date_time_cpu, var_temp_ponto_orvalho):
        self.result_temp_silos = result_temp_silos
        self.result_temp_ambiente = result_temp_ambiente
        self.result_media_calculada = result_media_calculada
        self.result_valor_media_calculada = result_valor_media_calculada
        self.result_horario = result_horario
        self.result_chuva = result_chuva
        self.result_umidade = result_umidade
        self.result_ponto_orvalho = result_ponto_orvalho
        self.var_temp_ambiente = var_temp_ambiente
        self.var_umidade_relativa = var_umidade_relativa
        self.var_sensor_chuva = var_sensor_chuva
        self.var_date_time_cpu = var_date_time_cpu
        self.var_temp_ponto_orvalho = var_temp_ponto_orvalho

class receita_aeracao:
    def __init__ (self, codigo, criada_em, team_id,
    usuario, dados_usuario, dados_on_line, atualizada_em, status):
        self.codigo = codigo
        self.criada_em = criada_em
        self.team_id = team_id
        self.usuario = usuario
        self.dados_usuario = dados_usuario
        self.dados_on_line = dados_on_line
        self.atualizada_em = atualizada_em
        self.status = status


class estacao_mt:
    def __init__ (self, temp_ambiente, umidade_rel, chuva, data_atualizacao, status):
            self.temp_ambiente = temp_ambiente
            self.umidade_rel = umidade_rel
            self.chuva = chuva
            self.data_atualizacao = data_atualizacao
            self.status = status


