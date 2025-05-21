# Esse código tem como objetivo ler valores inteiros inputados pelo usuário, e cacular a diferença

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

# Calculo da diferença
Diferenca   = (A * B) - (C * D)

# Exibir resultado
print(f"O valor de A é: {A}")
print(f"O valor de B é: {B}")
print(f"O valor de C é: {C}")
print(f"O valor de D é: {D}")

# Exibir resultado
print("A fórmula para a difereça é: (A * B) - (C * D)")
print(f"Substituindo os valores fornecidos: ({A} * {B}) - ({C} * {D})")
print(f"O Valor da diferença é: {Diferenca}")