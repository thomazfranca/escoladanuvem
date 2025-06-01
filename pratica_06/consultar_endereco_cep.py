
import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200 and 'erro' not in resposta.json():
        dados = resposta.json()
        return dados['logradouro'], dados['bairro'], dados['localidade'], dados['uf']
    else:
        return None

if __name__ == "__main__":
    cep = input("Digite o CEP: ")
    resultado = consultar_cep(cep)
    if resultado:
        logradouro, bairro, cidade, estado = resultado
        print(f"Logradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}")
    else:
        print("CEP inválido ou não encontrado.")
