import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" in dados:
                print("CEP não encontrado.")
            else:
                print(f"\nEndereço encontrado:")
                print(f"Logradouro: {dados.get('logradouro', 'Não informado')}")
                print(f"Bairro: {dados.get('bairro', 'Não informado')}")
                print(f"Cidade: {dados.get('localidade', 'Não informado')}")
                print(f"Estado: {dados.get('uf', 'Não informado')}")
        else:
            print("Erro ao consultar o CEP. Tente novamente mais tarde.")
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")


cep = input("Informe o CEP (somente números): ").strip()
if len(cep) == 8 and cep.isdigit():
    consultar_cep(cep)
else:
    print("CEP inválido. Informe 8 dígitos numéricos.")