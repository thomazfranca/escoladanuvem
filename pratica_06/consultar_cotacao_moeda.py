
import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave in dados:
            info = dados[chave]
            return {
                'moeda': info['name'],
                'valor_atual': info['bid'],
                'valor_maximo': info['high'],
                'valor_minimo': info['low'],
                'ultima_atualizacao': info['create_date']
            }
    return None

if __name__ == "__main__":
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
    resultado = consultar_cotacao(moeda)
    if resultado:
        print(f"Moeda: {resultado['moeda']}")
        print(f"Valor atual: R$ {resultado['valor_atual']}")
        print(f"Valor máximo: R$ {resultado['valor_maximo']}")
        print(f"Valor mínimo: R$ {resultado['valor_minimo']}")
        print(f"Última atualização: {resultado['ultima_atualizacao']}")
    else:
        print("Não foi possível obter a cotação.")
