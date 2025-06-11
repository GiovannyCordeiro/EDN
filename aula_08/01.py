while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Erro: entrada inválida. Por favor, digite um número válido.")

while True:
    try:
        num2 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Erro: entrada inválida. Por favor, digite um número válido.")

while True:
    operacao = input("Digite a operação (+, -, *, /): ")

    try:
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida.")

        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
        break  # operação bem-sucedida, sai do loop
    except ZeroDivisionError as e:
        print(f"Erro: {e}")
        num2 = float(input("Digite um novo segundo número diferente de zero: "))
    except ValueError as e:
        print(f"Erro: {e}")
