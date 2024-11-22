 


def consulta_receita():
    return  "SELECT * FROM receita_aeracao WHERE codigo ORDER BY codigo DESC LIMIT 1;"


def data_envio():
    return  "UPDATE receita_aeracao SET data_atualizacao = NOW() WHERE data_atualizacao is null ORDER BY codigo DESC LIMIT 1;"
    


def error_status404():
    return "INSERT INTO log_erros (TIPO_ERRO, MSG_ERRO,ID_ERRO) VALUES ('falha ao enviar dados receita.', 'Erro 404: Recurso não encontrado. Verifique se a URL ou a rota está correta.',1);"

def error_http_exception():
     return "INSERT INTO log_erros (TIPO_ERRO, MSG_ERRO,ID_ERRO) VALUES ('falha ao enviar dados receita.', 'ERRO: Ocorreu um erro de HTTP',2);"

def error_connection():
    return "INSERT INTO log_erros (TIPO_ERRO, MSG_ERRO,ID_ERRO) VALUES ('falha ao enviar dados receita.', 'ERRO: falha na conexão.',3);"
#erro de timeout

def error_timeout():
    return "INSERT INTO  log_erros (TIPO_ERRO, MSG_ERRO,ID_ERRO) VALUES ('falha ao enviar dados da receita.', 'ERROR:500 Houve um erro de tempo limite.',4);"
#erro decodificação do Json

def error_json_decode():
    return "INSERT INTO log_erros (TIPO_ERRO, MSG_ERRO, ID_ERRO) VALUES ('falha ao enviar dados da receita.', 'ERROR: Houve um erro na decodificação do Json no corpo na requisição.',5)"
#erro indefino trata erros de maneira genérica

def error():
     return "INSERT INTO log_erros (TIPO_ERRO, MSG_ERRO,ID_ERRO) VALUES ('falha ao enviar dados receita.','ERROR: Houve um erro.',6);"

def error_status500():
    return "INSERT INTO log_erros (TIPO_ERRO, MSG_ERRO, ID_ERRO) VALUES ('Falha ao enviar dados receita.', 'ERROR: Erro 500 encontrado, possivel erro no JSON.', 7);"

def failure_record_integration():
    return "INSERT INTO log_erros (TIPO_ERRO, MSG_ERRO , ID_ERRO) VALUES ('Falha ao enviar dados receita', 'FALHA: essa menssagem é para quando o endpoint retorna um Json vazio indicando uma possivel falha , proxima tentativa em 1 minuto!', 8)"

def error_Except():
    return "INSERT INTO log_erros (TIPO_ERRO, MSG_ERRO, ID_ERRO) VALUES ('Falha ao enviar dados receita.', 'ERROR: houve uma exceção', 9);"