while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break

    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break

    if len(senha) >= 8 and tem_numero:
        print("Senha forte cadastrada com sucesso!")
        break
    else:
        print("Senha fraca. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
