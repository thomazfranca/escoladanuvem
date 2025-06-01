
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

if __name__ == "__main__":
    valor = float(input("Digite o valor total da conta: "))
    porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))
    gorjeta = calcular_gorjeta(valor, porcentagem)
    print(f"Gorjeta a ser deixada: R$ {gorjeta:.2f}")
