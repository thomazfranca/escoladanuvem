def calculadora():
    """ Calculadora que realiza as quatro operações básicas entre dois números,
    tratando erros de entrada e operação. """

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == '+':
                resultado = num1 + num2
                print(f"Resultado: {resultado}")
                break  # Encerra o loop após o sucesso
            elif operacao == '-':
                resultado = num1 - num2
                print(f"Resultado: {resultado}")
                break  # Encerra o loop após o sucesso
            elif operacao == '*':
                resultado = num1 * num2
                print(f"Resultado: {resultado}")
                break  # Encerra o loop após o sucesso
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero!")
                else:
                    resultado = num1 / num2
                    print(f"Resultado: {resultado}")
                    break  # Encerra o loop após o sucesso
            else:
                print("Erro: Operação inválida!")

        except ValueError:
            print("Erro: Entrada inválida! Por favor, digite números.")
        except Exception as errosinexperados:
            print(f"Erro inesperado: {errosinexperados}") # Para capturar outros erros inesperados
            print("Por favor, tente novamente.")
    # Inicia a calculadora
    calculadora()

