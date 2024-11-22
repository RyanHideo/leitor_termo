import json
class Formatador:
    def dados_receita(self, dados_receita):
        dados = dados_receita

        for dado in dados:
            dados_receita = {

                                'criado_em'         :       str(dado[1]) if dado [1] is not None else None,
                                'team_id'           :       dado[2],
                                'usuario'           :       dado[3],
                                'dados'             :       json.loads(dado[4]), 
                                'dados_online'      :       json.loads(dado[6]),
                                'status'            :       dado[7]

                            }
            
            dados_json          =       json.dumps(dados_receita)
            leitura_json        =       json.loads(dados_json)
            result              =       leitura_json
            return result


    def dados_cliente(self, dados_cliente):
        for item in dados_cliente:
            dados_cliente = {

                                'ID_equipamento'    :       item[0],

                            }
            
            dados_json          =       json.dumps(dados_cliente)
            dados_json2         =       json.loads(dados_json)
            return dados_json2
        
#'atualizado_em':str(dado[5]) if dado[5] is not None else None,