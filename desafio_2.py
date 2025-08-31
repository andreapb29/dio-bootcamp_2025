def depositar(valor, conta, /):
    """Depósito - argumentos somente posicionais"""
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")


def sacar(*, conta, valor, limite, limite_saques):
    """Saque - argumentos somente nomeados"""
    if conta["numero_saques"] >= limite_saques:
        print("Limite de saques atingido!")
    elif valor > limite:
        print("O valor do saque excede o limite")
    elif valor > conta["saldo"]:
        print(f"Saldo insuficiente\nSaldo: R$ {conta['saldo']:.2f}")
    elif valor <= 0:
        print("O valor informado é inválido")
    else:
        conta["saldo"] -= valor
        conta["extrato"] += f"Saque: R$ {valor:.2f}\n"
        conta["numero_saques"] += 1
        print("Saque realizado com sucesso!")


def exibir_extrato(conta, /, *, extrato=None):
    """Extrato - saldo posicional, extrato nomeado"""
    extrato = conta["extrato"] if extrato is None else extrato
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")


def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    if any(u["cpf"] == cpf for u in usuarios):
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ").strip()

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário cadastrado com sucesso!")


def cadastrar_conta(usuarios, contas, numero_conta, agencia="0001"):
    cpf = input("Informe o CPF do usuário para vincular a conta: ").strip()
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário antes da conta.")
        return None

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0
    }
    contas.append(conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    return conta


def listar_contas(contas):
    print("\n======= CONTAS =======")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for c in contas:
            u = c["usuario"]
            print(f"Agência: {c['agencia']} | Conta: {c['numero_conta']} | Titular: {u['nome']} | CPF: {u['cpf']}")
    print("=======================")


def selecionar_conta(contas):
    cpf = input("Informe o CPF do titular: ").strip()
    numero = int(input("Informe o número da conta: "))
    conta = next((c for c in contas if c["numero_conta"] == numero and c["usuario"]["cpf"] == cpf), None)
    if not conta:
        print("Conta não encontrada ou CPF não confere.")
    return conta


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair
=> """

LIMITE_SAQUES = 3
LIMITE_SAQUE = 500
usuarios = []
contas = []
numero_conta = 1

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        conta = selecionar_conta(contas)
        if conta:
            valor = float(input("Insira o valor do depósito: "))
            depositar(valor, conta)

    elif opcao == "s":
        conta = selecionar_conta(contas)
        if conta:
            valor = float(input("Digite o valor do saque: "))
            sacar(conta=conta, valor=valor, limite=LIMITE_SAQUE, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        conta = selecionar_conta(contas)
        if conta:
            exibir_extrato(conta)

    elif opcao == "nu":
        cadastrar_usuario(usuarios)

    elif opcao == "nc":
        conta = cadastrar_conta(usuarios, contas, numero_conta)
        if conta:
            numero_conta += 1

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
