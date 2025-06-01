
def calcular_idade_em_dias(ano_nascimento):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade * 365

# Exemplo de uso:
if __name__ == "__main__":
    ano = int(input("Digite seu ano de nascimento: "))
    idade_dias = calcular_idade_em_dias(ano)
    print(f"Sua idade em dias é aproximadamente: {idade_dias}")
