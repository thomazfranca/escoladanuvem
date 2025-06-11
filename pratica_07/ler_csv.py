
import csv

def ler_dados_csv(caminho_arquivo):
    with open(caminho_arquivo, newline="") as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            print(", ".join(linha))

if __name__ == "__main__":
    caminho = "dados_pessoas.csv"
    ler_dados_csv(caminho)
