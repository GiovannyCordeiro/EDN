notas = []

while True:
    entrada = input("Digite a nota do aluno (0 a 10) ou 'fim' para encerrar: ")

    if entrada.lower() == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite uma nota numérica ou 'fim'.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"\nQuantidade de notas registradas: {len(notas)}")
    print(f"Média da turma: {media:.2f}")
else:
    print("\nNenhuma nota válida foi registrada.")
