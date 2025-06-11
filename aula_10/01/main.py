import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    try:
        tamanho = int(input("Informe a quantidade de caracteres da senha: "))
        if tamanho <= 0:
            print("A quantidade de caracteres deve ser maior que zero.")
        else:
            senha = gerar_senha(tamanho)
            print(f"Senha gerada: {senha}")
    except ValueError:
        print("Por favor, informe um número inteiro válido.")

if __name__ == "__main__":
    main()
