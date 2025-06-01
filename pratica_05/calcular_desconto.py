
def calcular_preco_final(preco_original, percentual_desconto):
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return preco_final

# Exemplo de uso:
if __name__ == "__main__":
    preco = float(input("Digite o preço original do produto: "))
    desconto = float(input("Digite o percentual de desconto: "))
    final = calcular_preco_final(preco, desconto)
    print(f"Preço final com desconto: R$ {final:.2f}")
