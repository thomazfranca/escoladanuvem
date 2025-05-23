nome = input("Nome do vendedor: ")
salario_fixo = float(input("Salário fixo: "))
vendas = float(input("Total de vendas: "))

comissao = vendas * 0.15
total = salario_fixo + comissao

print(f"TOTAL = R$ {total:.2f}")