#Modulos
#Data Base
import model
import data_base
import json
import decoder_receitas
from time import sleep
from model import dados_on_line_receia_aeracao
from calc_medias import calc
import calc_medias
from datetime import datetime

#date time
import time
from datetime import datetime
from datetime import time
c_horario_hr_inicial = time()
c_horario_hr_final = time()
c_horario_hr_cpu = time()
c_horario_meio_dia = time(12,00,00)

#Conexao com o banco de dados
db = model.Db_information("Termometria",3306,"localhost","leitor_termo","termometria")
conn = data_base.Connector(db)

#Carrega o ultimo registro de temperaturas
reg_instalacao = conn.select_ultimo_registro_instalacao()

#Carrega os dados da Receia de aeracao
receita_aer = conn.get_atual_receita()

#Carrega dos dados do usuario para controle da receita
decoder_data = decoder_receitas.decoder()
dados_receita_usuario = json.loads(receita_aer.dados_usuario, object_hook = decoder_data.decoder_dados_usuario)

#dados da estação mt
dados_estacao_mt = conn.select_estacao_mt()

#dados online da receita a partir do banco
receita_on_line = json.loads(receita_aer.dados_on_line, object_hook = decoder_data.decoder_dados_on_line)

calcula_medias = calc()

#status final da receita
status_receita = False

#Monitoramento da receita
while True:

    #Carrega o ultimo registro de temperaturas
    reg_instalacao = conn.select_ultimo_registro_instalacao()

    #Carrega os dados da Receia de aeracao
    receita_aer = conn.get_atual_receita()

    #Carrega dos dados do usuario para controle da receita
    decoder_data = decoder_receitas.decoder()
    dados_receita_usuario = json.loads(receita_aer.dados_usuario, object_hook = decoder_data.decoder_dados_usuario)

    #dados da estação mt
    dados_estacao_mt = conn.select_estacao_mt()

    #dados online da receita a partir do banco
    receita_on_line = json.loads(receita_aer.dados_on_line, object_hook = decoder_data.decoder_dados_on_line)

    calcula_medias = calc()

    #temperatura ambiente
    if(dados_receita_usuario.intervaloTemp_habilita):
        if( dados_estacao_mt.temp_ambiente > dados_receita_usuario.intervaloTemp_temp_min and
        dados_estacao_mt.temp_ambiente < dados_receita_usuario.intervaloTemp_temp_max):
            receita_on_line.result_temp_ambiente = True
        else:
            receita_on_line.result_temp_ambiente = False
   
    #temperatura silos
    if(dados_receita_usuario.tempSilos_habilita):
        valor_temp_comparar = 0
        #print(dados_receita_usuario.tempSilos_limite_temperatura)
        if(dados_receita_usuario.tempSilos_limite_temperatura == 0): #valor minimo
            valor_temp_comparar = calcula_medias.min_valor(reg_instalacao.registros_temperaturas)
        elif(dados_receita_usuario.tempSilos_limite_temperatura == 1): #valor maximo
            valor_temp_comparar = calcula_medias.max_valor(reg_instalacao.registros_temperaturas)
        else:
            valor_temp_comparar = calcula_medias.media(reg_instalacao.registros_temperaturas)

        receita_on_line.result_valor_media_calculada = valor_temp_comparar
        #print(valor_temp_comparar)

        #comparador 0 = ">", 1 = "<", 2 = "=", 3 = ">=", 4 = "<="
        #print(dados_receita_usuario.tempSilo,_tipo_set_point
        if(dados_receita_usuario.tempSilos_tipo_set_point == 0):
            if((float(dados_estacao_mt.temp_ambiente)+ 
            float(dados_receita_usuario.tempSilos_temp_set_point)) >
            float(valor_temp_comparar)):
                receita_on_line.result_temp_silos = True
            else:
                receita_on_line.result_temp_silos = False 
               
        elif(dados_receita_usuario.tempSilos_tipo_set_point == 1):
            if(float(dados_estacao_mt.temp_ambiente) < 
            (float(valor_temp_comparar) -
            float(dados_receita_usuario.tempSilos_temp_set_point))):
                receita_on_line.result_temp_silos = True
            else:
                receita_on_line.result_temp_silos = False          
       
        elif(dados_receita_usuario.tempSilos_tipo_set_point == 2):
            if(float(dados_estacao_mt.temp_ambiente) ==
            (float(valor_temp_comparar))):
                receita_on_line.result_temp_silos = True
            else:
                receita_on_line.result_temp_silos = False 
     
        elif(dados_receita_usuario.tempSilos_tipo_set_point == 3):
            if(float(dados_estacao_mt.temp_ambiente) >=
            (float(valor_temp_comparar))):
                receita_on_line.result_temp_silos = True
            else:
                receita_on_line.result_temp_silos = False 
        
        elif(dados_receita_usuario.tempSilos_tipo_set_point == 4):
            if(float(dados_estacao_mt.temp_ambiente) <=
            (float(valor_temp_comparar))):
                receita_on_line.result_temp_silos = True
            else:
                receita_on_line.result_temp_silos = False 
     

    #horario
    if(dados_receita_usuario.intervaloHorario_habilita):
        dia_semana = datetime.today().weekday()
        #print(dia_semana)
        hora_atual = datetime.now().hour
        minuto_atual = datetime.now().minute
        if((dados_receita_usuario.intervaloHorario_habilita_segunda and dia_semana == 0) or
        (dados_receita_usuario.intervaloHorario_habilita_terca and dia_semana == 1) or
        (dados_receita_usuario.intervaloHorario_habilita_quarta and dia_semana == 2) or
        (dados_receita_usuario.intervaloHorario_habilita_quinta and dia_semana == 3) or
        (dados_receita_usuario.intervaloHorario_habilita_sexta and dia_semana == 4) or
        (dados_receita_usuario.intervaloHorario_habilita_sabado and dia_semana == 5) or
        (dados_receita_usuario.intervaloHorario_habilita_domingo and dia_semana == 6)):
            #transforma os valores da receita em variavies time
            c_horario_hr_cpu = datetime.now().time()
            c_horario_hr_inicial = time(dados_receita_usuario.intervaloHorario_hora_inicial,
                                        dados_receita_usuario.intervaloHorario_minuto_inicial,00)
            c_horario_hr_final = time(dados_receita_usuario.intervaloHorario_hora_final,
                                      dados_receita_usuario.intervaloHorario_minuto_final,00)
            """
            #debug
            print(f"horario da cpu: {c_horario_hr_cpu}")
            print(f"horario inicial da receita: {c_horario_hr_inicial}")
            print(f"horario final da receita: {c_horario_hr_final}")
            """
            #condição para ligar em intervalos no mesmo dia
            if(c_horario_hr_final > c_horario_hr_inicial):
                #print("1")
                if(c_horario_hr_cpu > c_horario_hr_inicial  and
                   c_horario_hr_cpu < c_horario_hr_final):
                    receita_on_line.result_horario = True
                    #print("ok")
                else:
                    receita_on_line.result_horario = False
                    #print("none")
            
            else:
                #print("2")
                if(c_horario_hr_cpu > c_horario_hr_inicial):
                    receita_on_line.result_horario = True
                elif(c_horario_hr_cpu < c_horario_hr_final):
                    receita_on_line.result_horario = True
                else:
                   receita_on_line.result_horario = False             

            #debug
            #print(f"horario da cpu > horario inicial: {(c_horario_hr_cpu > c_horario_hr_inicial)}")
            #print(f"horario da cpu < horario final: {(c_horario_hr_cpu < c_horario_hr_final)}")

        else:
            receita_on_line.result_horario = False


    #umidade
    if(dados_receita_usuario.umidade_habilita):
        #print("habilita")
        if(float(dados_estacao_mt.umidade_rel) > float(dados_receita_usuario.umidade_min_valor) and
        float(dados_estacao_mt.umidade_rel) < float(dados_receita_usuario.umidade_max_valor)):
            receita_on_line.result_umidade = True
        else:
            receita_on_line.result_umidade = False
    #print(f"if {dados_estacao_mt.umidade_rel} > {dados_receita_usuario.umidade_min_valor} and < {dados_receita_usuario.umidade_max_valor} = {receita_on_line.result_umidade}")
    
    #chuva corrigido status chuva para bascula
    if(dados_receita_usuario.chuva_habilita):
        if(dados_estacao_mt.chuva == 1):
             receita_on_line.result_chuva = 0
        else:
            receita_on_line.result_chuva = 1


    #status final
    if(((dados_receita_usuario.intervaloTemp_habilita and #temperatura ambiente
    receita_on_line.result_temp_ambiente) or 
    not dados_receita_usuario.intervaloTemp_habilita) and
    #temperatura silos
    ((dados_receita_usuario.tempSilos_habilita and 
    receita_on_line.result_temp_silos) or 
    not dados_receita_usuario.tempSilos_habilita) and
    #horario
    ((dados_receita_usuario.intervaloHorario_habilita and 
    receita_on_line.result_horario) or 
    not dados_receita_usuario.intervaloHorario_habilita) and
    #umidade
    ((dados_receita_usuario.umidade_habilita and
    receita_on_line.result_umidade) or
    not dados_receita_usuario.umidade_habilita) and
    #chuva
    ((dados_receita_usuario.chuva_habilita and
    receita_on_line.result_chuva) or
    not dados_receita_usuario.chuva_habilita)):
        status_receita = True
    else:
        status_receita = False

    #todos controles desablilitados
    if(not dados_receita_usuario.intervaloTemp_habilita and
    not dados_receita_usuario.tempSilos_habilita and
    not dados_receita_usuario.intervaloHorario_habilita and
    not dados_receita_usuario.umidade_habilita and
    not dados_receita_usuario.umidade_habilita and
    not dados_receita_usuario.chuva_habilita):
        status_receita = False
    

    #Variaveis da receita online
    receita_on_line.var_temp_ambiente = dados_estacao_mt.temp_ambiente
    receita_on_line.var_umidade_relativa = dados_estacao_mt.umidade_rel
    receita_on_line.var_sensor_chuva = dados_estacao_mt.chuva
    receita_on_line.var_date_time_cpu = datetime.now()

    #pausa de 3 segundos
    sleep(3.0)

    receita_on_line.var_temp_ambiente = float(receita_on_line.var_temp_ambiente)
    receita_on_line.var_umidade_relativa = float(receita_on_line.var_umidade_relativa)
    receita_on_line.var_temp_ponto_orvalho = float(receita_on_line.var_temp_ponto_orvalho)
    receita_on_line.var_date_time_cpu = str(datetime.now())
    dados = vars(receita_on_line)
    #print(json.dumps(dados))
    #print(dados)
    conn.update_receita_on_line(json.dumps(dados), receita_aer.codigo,
        datetime.now(), status_receita)
    




    





