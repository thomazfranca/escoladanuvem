
def verificar_palindromo(texto):
    texto = ''.join(c.lower() for c in texto if c.isalnum())
    return texto == texto[::-1]

# Exemplo de uso:
if __name__ == "__main__":
    frase = input("Digite uma palavra ou frase: ")
    if verificar_palindromo(frase):
        print("Sim")
    else:
        print("Não")
