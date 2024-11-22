import mysql.connector
# Parâmetros de conexão com o banco de dados
config = {
    'user': 'root',
    'password': 'termometria',
    'host': 'localhost',
    'database': 'Termometria'
}

# Cria a conexão com o banco de dados
conn = mysql.connector.connect(**config)
cursor = conn.cursor()
c = 32

# Loop para gerar e executar as consultas SQL
for canal in range(1, 17):
    c += 1
    for sensor in range(1, 17):
        cordao_fisico = f"Ch{c}S{sensor}"
        sql = f"INSERT INTO registro_cordoes (cod_placa,cordao_fisico, canal_placa, sensor_placa) VALUES (2,'{cordao_fisico}', {canal}, {sensor});"
        
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")

# Fecha a conexão com o banco de dados
cursor.close()
conn.close()

