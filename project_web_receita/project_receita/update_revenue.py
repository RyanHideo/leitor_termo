from datetime import datetime
import json
from .database import MysqlConnection


def validar(data,data_embarcado,dados_receita):
    global create_web,atualizado_web

    data                =       data
    data_embarcado      =       data_embarcado
    criado_embarcado    =       data_embarcado[0]['dados_receita']['criado_em']      
    create_web          =       data[0]['criado_em']
    atualizado_web      =       data[0]['atualizado_em']



    if criado_embarcado < atualizado_web:
        print(dados_receita)
        atualizar_dias_habilita(data,dados_receita)
        return True
    
    elif criado_embarcado > atualizado_web:
        return False
    
    else:
        return "integrações atualizadas"


def atualizar_dias_habilita(jsons,dados_receita):
    dias_semana_habilita        =       ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

    # Assuming create_web is a list of items, and you want to check the presence of days in each item
    for item in jsons:
        if 'dias_semana' in item:
            condicoes_dias_semana       =       {dia: 1 if dia in item['dias_semana'] else 0 for dia in dias_semana_habilita}
            dom                         =        condicoes_dias_semana['Domingo']
            seg                         =        condicoes_dias_semana['Segunda']
            ter                         =        condicoes_dias_semana['Terça']
            quar                        =        condicoes_dias_semana['Quarta']
            quin                        =        condicoes_dias_semana['Quinta']
            sex                         =        condicoes_dias_semana['Sexta']
            sab                         =        condicoes_dias_semana['Sábado']
            db                          =        MysqlConnection()
           


        if 'temperatura_minima' in item and item['temperatura_minima'] is not None:
            temp_min                =       float(jsons[0]['temperatura_minima'])
            intervaloTemp_habilita  =       1
        else:
            temp_min                =       0
            intervaloTemp_habilita  =       0


        if 'temperatura_maxima' in item and item['temperatura_maxima'] is not None:
            temp_max                =       float(jsons[0]['temperatura_maxima'])
            intervaloTemp_habilita  =       1
        else:
            temp_max                =       0
            intervaloTemp_habilita  =       0



        if 'hora_inicial' in item and item['hora_inicial'] is not None:
            hora_inicial_str            =       jsons[0]['hora_inicial']
            hora_inicial                =       int(datetime.strptime(hora_inicial_str, "%H:%M:%S").strftime("%H"))
            intervaloHorario_habilita   =       1
        else:
            hora_inicial = 0
            intervaloHorario_habilita = 0


        if 'hora_inicial' in item and item['hora_inicial'] is not None:
            min_inicial_str             =       jsons[0]['hora_inicial']
            min_inicial                 =       int(datetime.strptime(min_inicial_str, "%H:%M:%S").strftime("%M"))
            intervaloHorario_habilita   =       1
        else:
            min_inicial                 =       0
            intervaloHorario_habilita   =       0



        if 'hora_final' in item and item['hora_final'] is not None:
            hora_final_str              =       jsons[0]['hora_final']
            hora_final                  =       int(datetime.strptime(hora_final_str, "%H:%M:%S").strftime("%H"))
            intervaloHorario_habilita   =       1
        else:
            hora_final                  =       0
            intervaloHorario_habilita   =       0



        if 'hora_final' in item and item['hora_final'] is not None:
            hora_final_str              =       jsons[0]['hora_final']
            min_final                   =       int(datetime.strptime(hora_final_str, "%H:%M:%S").strftime("%M"))
            intervaloHorario_habilita   =       1
        else:
            min_final                   =       0
            intervaloHorario_habilita   =       0



        if 'considerar_chuva' in item and item['considerar_chuva'] is not None:
            considerar_chuva            =       jsons[0]['considerar_chuva']
            chuva_habilita              =       1
        else:
            considerar_chuva            =       0
            chuva_habilita              =       0



        if 'umidade_minima' in item and item['umidade_minima'] is not None:
            umidade_minima              =       float(jsons[0]['umidade_minima'])
            umidade_habilita            =       1
        else:
            umidade_minima              =       0
            umidade_habilita            =       0



        if 'umidade_maxima' in item and item['umidade_maxima'] is not None:
                umidade_maxima          =       jsons[0]['umidade_maxima']
                umidade_habilita        =       1
        else:
            umidade_maxima              =       0
            umidade_habilita            =       0

        if 'ponto_orvalho' in item and item['ponto_orvalho'] is not None:
            ponto_orvalho               =       jsons[0]['ponto_orvalho']
            pontoOrvalho_habilita       =       0
        else:   
            ponto_orvalho               =       0
            pontoOrvalho_habilita       =       0
        

        if 'tempsilo_habilita' in item and item['tempsilo_habilita'] is not None:
            tempsilo_habilita = item['tempsilo_habilita']
            print('tempsilo_habilita', tempsilo_habilita)
        else:
            tempsilo_habilita = dados_receita['dados']['tempSilos_habilita']
       
        if 'tempsilo_tipo_set_point' in item is not None:
            tempsilo_tipo_set_point = 0 if  item['tempsilo_tipo_set_point'] == None else item['tempsilo_tipo_set_point']
            print('tempsilo_tipo_set_point', tempsilo_tipo_set_point)
            
        else:
            tempsilo_tipo_set_point = dados_receita['dados']['tempSilos_tipo_set_point']


        if 'tempsilo_limite' in item is not None:
            tempsilo_limite = 0 if item['tempsilo_limite'] == None else item['tempsilo_limite']
            
        else:
            tempsilo_limite = 0

        if 'tempsilo_set_point' in item and item['tempsilo_set_point'] is not None:
           print('aqui tempsilo')
           tempSilos_temp_set_point = float(item['tempsilo_set_point'])
           tempSilos_temp_set_point_decimal = f'{tempSilos_temp_set_point:.1f}'
           tempSilos_temp_set_point_str = str(tempSilos_temp_set_point_decimal)

        else:
        
            tempSilos_temp_set_point_str = dados_receita['dados']['tempSilos_temp_set_point']

    db.set_query_receita_web(atualizado_web,
                             intervaloTemp_habilita,
                             intervaloHorario_habilita,
                             chuva_habilita,
                             umidade_habilita,
                             pontoOrvalho_habilita,
                             temp_min,
                             temp_max,
                             hora_inicial,
                             min_inicial,
                             hora_final,
                             min_final,
                             dom,
                             seg,
                             ter,
                             quar,
                             quin,
                             sex,
                             sab,
                             considerar_chuva,
                             umidade_minima,
                             umidade_maxima,
                             ponto_orvalho,
                             tempsilo_habilita,
                             tempsilo_tipo_set_point,
                             tempsilo_limite,
                             tempSilos_temp_set_point_str
                            )

