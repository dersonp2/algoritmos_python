opcao = 0

while opcao != 3:
    print("1 - Somar")
    print("2 - Dividir")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"A soma de {num1} e {num2} é {resultado}")
    elif opcao == 2:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"A divisão de {num1} por {num2} é {resultado}")
        else:
            print("Divisão por zero não é permitida.")
    elif opcao == 3:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")