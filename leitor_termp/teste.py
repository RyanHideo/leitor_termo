import asyncio
import json

async def send_request(ip_placa, lista_final):
    """
    Envia uma solicitação ao servidor de forma assíncrona.
    """
    try:
        reader, writer = await asyncio.open_connection(ip_placa, 8080)
        print(f"Conectado ao servidor {ip_placa}")

        request = json.dumps(lista_final).encode('utf-8')
        writer.write(request)
        await writer.drain()

        data = await reader.read(4096)
        leitura_list = json.loads(data.decode('utf-8'))
        print(leitura_list)
        print('ola')

        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print(f"Erro ao enviar solicitação: {e}")

if __name__ == "__main__":
    ip_placa = '192.168.100.141'
    lista_final = [{1:[1,2,3,4,5]},{2:[1,2,3,4,5]},{4:[1,2,3,4,5]}]

    asyncio.run(send_request(ip_placa, lista_final))

