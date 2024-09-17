from datetime import datetime

menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [nu] Novo usuário
    [q] sair

    => """

LIMITE_SAQUES = 10
AGENCIA = '0001'

saldo = 10000
limite = 500
extrato = ""
numero_saques = 0
historico = []
formato_data = "%d/%m/%Y %a %H:%M"
usuarios = []
contas = []

def criarUsuario(usuarios):
    cpf = int(input("Digite o seu cpf: "))

    usuario = filtrarUsuario(cpf, usuarios)
    if usuario:
        print('Já existe usuário com esse CPF!')
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informa a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print("Usuário criado com sucesso!")

def filtrarUsuario(cpf, usuario):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criarConta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('Usuário não encontrado, fluxo de criação de conta encerrado!')

def listarContas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        pritn('='*100)
        print(textwrap.dedent(linha))

while True:

    opcao = input(menu)
    
    if opcao == "d":
        print("Desposito")
        valor = float(input("Qual valor para depositar? "))
        if valor <= 0:
            print("Nenhum valor foi depositado!")

        else: 
            saldo += valor
            print("Valor depositado com sucesso!")
            data_atual = datetime.now()
            historico.append(['deposito', valor, data_atual])

    elif opcao == "s":
        print("Saque")
        valor = float(input("Qual valor para sacar? "))

        data_atual = datetime.now()
        for c in range(0, len(historico)):
            numero_saques += historico[c].count(data_atual)

        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diarios atingido")

        elif valor > saldo:
            print("Saldo insuficiente")

        elif valor > 500:
            print("Nao e possivel sacar mais de 500 reais")

        else:
            saldo -= valor
            print("Valor retirado, saldo de ", saldo)
            numero_saques += 1
            data_atual = datetime.now()
            historico.append(['saque', valor, data_atual])

    elif opcao == "e":
        print("Extrato")
        for c in range(0, len(historico)):
            print(f'{historico[c][0]}: R${historico[c][1]:.2f} | {historico[c][2].strftime(formato_data)}')

        print("---"*30)
        print("Saldo total: ", saldo)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.
 
    elif opcao == "nu":
        criarUsuario(usuarios)

    elif opcao == "q":
        break


