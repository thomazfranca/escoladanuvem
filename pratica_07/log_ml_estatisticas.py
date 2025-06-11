
def ler_log_e_calcular_estatisticas(caminho_arquivo):
    tempos = []

    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            if "tempo_execucao" in linha:
                partes = linha.strip().split("=")
                if len(partes) == 2:
                    try:
                        tempo = float(partes[1])
                        tempos.append(tempo)
                    except ValueError:
                        continue

    if tempos:
        media = sum(tempos) / len(tempos)
        variancia = sum((x - media) ** 2 for x in tempos) / len(tempos)
        desvio_padrao = variancia ** 0.5
        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão: {desvio_padrao:.2f}")
    else:
        print("Nenhum dado de tempo de execução encontrado.")

# Exemplo de uso
if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo de log: ")
    ler_log_e_calcular_estatisticas(caminho)
