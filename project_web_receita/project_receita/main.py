import http.client 
import json
from .query import Formatador
from .query_database import *
import time
from .database import MysqlConnection
from datetime import datetime
from .update_revenue import validar

erros = 0
class Request:
    def __init__(self, host,endpoint):
        self.host       =       host
        self.endpoint   =       endpoint
        
    def Post(self, dados_receita):
        global conn
        conn                =       http.client.HTTPSConnection(self.host)
        DadosJsonReceita    =       json.dumps(dados_receita)
        conn.request('POST', self.endpoint, DadosJsonReceita, headers={'Content-Type':'application/json'})
        return conn.getresponse()

class TreatingResponses:
 
    def tratar_resposta(self, response):
        global response_api
        content_type            =       response.headers.get('Content-Type', '')

        if 'application/json' in content_type:
            response_json       =       json.loads(response.read().decode('utf-8'))
            response_api        =       response_json
            print("API::::" , response_api)
            result              =       validar(response_api,dados_enviar,dados_receita)

            if result == True:
                #print("web mais atual , atualiando embarcado")
                time.sleep(5)
                #print("embarcado atualizado.")
                content = response.read()
                return True
            
            if result == False:
                #print("embarcado mais atual")
                return False
            
            if result == "integrações atualizadas":
                #print("EMBARCADO E WEB ESTÃO SINCRONIZADOS COM A MESTA RECEITA REFERENTE A DATA/HORA")
                return True
            #print(content)
        
           
        if response.status == 500:
            # time.sleep(30)
            #print("Erro 500 encontrado . Obtendo o conteúdo do erro...")
            content = response.read()
            #print(content)
            db = MysqlConnection()
            db.set_query(error_status500())
            
            return content_type
        elif response.status == 404:
            # time.sleep(30)
            db = MysqlConnection()
            db.set_query(error_status404())
            #print("Erro 404: recurso não encontrado . Verifique se a URL ou a rota está corre.")
            
            return content_type
class Main:
    
    def enviar_dados_receita(self):
        global dados_enviar,dados_receita
        self.request        =       Request('api.sinapsesolucoes.com','/publico/integracao/unidade-armazenamento/configuracao-receita')
        tentativas          =       5
        tratamento          =       TreatingResponses()
        formatador          =       Formatador()
        db                  =       MysqlConnection()
        dados_receita       =       db.get_query_receita()
        dados_equipamento   =       db.get_query_id_equipamento()
        dados_receita       =       formatador.dados_receita(dados_receita)
        dados_equipamento   =       formatador.dados_cliente(dados_equipamento)
        dados_enviar        =       [{'dados_receita':dados_receita , 'id_quipamento':dados_equipamento}]
  
        while erros < tentativas:
            try:
                response    =       self.request.Post(dados_enviar)
                print(dados_enviar)
                content     =       tratamento.tratar_resposta(response)
                #print('enviando')
                break
                
            except http.client.HTTPException as e :
                time.sleep(30)
                db.set_query(error_http_exception())
            except ConnectionError as e:
                time.sleep(30)
                db.set_query(error_connection())
            except TimeoutError as e:
                time.sleep(30)
                db.set_query(error_timeout())
            except json.JSONDecodeError as e:
                time.sleep(30)
                db.set_query(error_json_decode())
               
            except Exception as e:
                #print(e)
                time.sleep(30)
                db.set_query(error_Except())

    
    def run(self):
        while True:
            self.enviar_dados_receita()

 
    
class App:

    def __init__(self) -> None:
        self.app = Main()

    @classmethod
    def execute(cls):
        cls().app.run()