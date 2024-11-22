from .config_call_api import ConfigCallApi
import http.client
import json


class CallAPi(ConfigCallApi):
           
    def Post(self, dados):
                    global conn
                    conn                =       http.client.HTTPSConnection(self.host)
                    dados_enviar        =       json.dumps(dados)
                    conn.request('POST', self.endpoint, dados_enviar, headers={'Content-Type':'application/json'})
                    return conn.getresponse()