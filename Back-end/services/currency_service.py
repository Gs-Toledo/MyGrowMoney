import requests

API_KEY = 'api_key=d6452dc4d8-b4e8be90bb-spuqyc'
BASE_URL = f'https://api.fastforex.io/'

def listar_moedas():
    response = requests.get(f'{BASE_URL}/currencies?{API_KEY}').json()
    return response['currencies']

def converter(moeda_origem, moeda_destino, valor):
    url = f'{BASE_URL}convert?from={moeda_origem}&to={moeda_destino}&amount={valor}&precision=2&{API_KEY}'
    print(url)
    response = requests.get(url).json()
    print(response)

    if not response or 'result' not in response or not isinstance(response['result'], dict):
        raise Exception(f"Erro ao converter as moedas: {response.get('message', 'Resposta inválida da API')}")

    valor_convertido = response['result'].get(moeda_destino)
    taxa = response['result'].get('rate')

    # Valida se os valores foram encontrados
    if valor_convertido is None or taxa is None:
        raise Exception(f"Erro ao converter as moedas: Valor convertido ou taxa não encontrados na resposta: {response['result']}")

    return {'valor_convertido': valor_convertido, 'taxa': taxa}