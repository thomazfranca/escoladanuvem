
import json

def escrever_json(caminho_arquivo, pessoa):
    with open(caminho_arquivo, "w") as arquivo:
        json.dump(pessoa, arquivo)

def ler_json(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        dados = json.load(arquivo)
        print(f"Nome: {dados['nome']}")
        print(f"Idade: {dados['idade']}")
        print(f"Cidade: {dados['cidade']}")

if __name__ == "__main__":
    pessoa = {
        "nome": "Daniela",
        "idade": 35,
        "cidade": "Curitiba"
    }
    caminho = "pessoa.json"
    escrever_json(caminho, pessoa)
    ler_json(caminho)
