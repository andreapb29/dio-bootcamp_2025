menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Insira a quantidade a ser depositada: "))
        
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Digite um valor válido")

    elif opcao == "s":

        if numero_saques == LIMITE_SAQUES:
            print("Limite de saque atingido!")

        else:
            valor_saque = float(input("Digite o valor de saque: "))

            if valor_saque > limite_saque:
                print("O valor do saque excede o limite")

            elif valor_saque > saldo:
                print(f"Saldo insuficiente\n Saldo: R$ {saldo:.2f}\n")

            elif valor_saque < 0:
                print("O valor informado é inválido")

            else:
                saldo -= valor_saque
                extrato += f"Saque: R${valor_saque:.2f}\n"
                numero_saques += 1
            
      
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")