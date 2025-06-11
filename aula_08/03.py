def senha_forte(senha):
    return len(senha) >= 8 and any(char.isdigit() for char in senha)

while True:
    senha = input("Digite uma senha forte ou 'sair' para encerrar: ")

    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    if senha_forte(senha):
        print("Senha válida e forte!")
        break
    else:
        print("Senha fraca. Ela deve ter pelo menos 8 caracteres e conter pelo menos um número.")
