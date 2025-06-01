
import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    try:
        qtd = int(input("Digite a quantidade de caracteres para a senha: "))
        senha = gerar_senha(qtd)
        print(f"Senha gerada: {senha}")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
