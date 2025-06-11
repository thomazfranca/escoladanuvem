
import csv

def escrever_dados_csv(caminho_arquivo, dados):
    with open(caminho_arquivo, "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Nome", "Idade", "Cidade"])
        writer.writerows(dados)

if __name__ == "__main__":
    dados = [
        ["Ana", 30, "São Paulo"],
        ["Bruno", 25, "Rio de Janeiro"],
        ["Carla", 28, "Belo Horizonte"]
    ]
    caminho = "dados_pessoas.csv"
    escrever_dados_csv(caminho, dados)
    print(f"Arquivo {caminho} criado com sucesso.")
