menu = '''
[d] Depositar
[S] Sacar
[e] Extrato
[q] Sair

'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(f"{menu}Digite a opção desejada: ")

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: R$"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado e invalido")

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: R$"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficinte.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")

        elif excedeu_saque:
            print("Operação falhou! Numero maximo de saques excedido.")

        elif valor > 0:
          
          saldo -= valor
          extrato += f"Saque: R$ {valor:.2f}\n"
          numero_saques += 1
        else:
          print("Operação falhou! O valor informado e invalido")
    elif opcao == "e":
        print("\n================EXTRATO================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:R$ {saldo:.2f}")
        print("=========================================")
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")