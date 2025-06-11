import requests
from datetime import datetime

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            chave = f"{moeda}BRL"

            if chave in dados:
                info = dados[chave]
                valor_atual = float(info['bid'])
                valor_maximo = float(info['high'])
                valor_minimo = float(info['low'])
                timestamp = int(info['timestamp'])
                data_hora = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

                print(f"\nCotação de {moeda} para BRL:")
                print(f"Valor atual: R$ {valor_atual:.2f}")
                print(f"Valor máximo do dia: R$ {valor_maximo:.2f}")
                print(f"Valor mínimo do dia: R$ {valor_minimo:.2f}")
                print(f"Última atualização: {data_hora}")
            else:
                print("Moeda não encontrada ou código inválido.")
        else:
            print("Erro ao acessar a API. Tente novamente mais tarde.")
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")

codigo = input("Informe o código da moeda (ex: USD, EUR, GBP): ").strip()
consultar_cotacao(codigo)
