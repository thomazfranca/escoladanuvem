
import requests

def gerar_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return nome, email, pais
    else:
        return None

if __name__ == "__main__":
    resultado = gerar_usuario_aleatorio()
    if resultado:
        nome, email, pais = resultado
        print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")
    else:
        print("Não foi possível obter os dados do usuário.")
