menu = """
    [d] Depositar,
    [s] Sacar,
    [e] Extrato,
    [q] sair,

    => """

saldo = 10000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
historico = []

while True:

    opcao = input(menu)
    
    if opcao == "d":
        print("Desposito")
        valor = float(input("Qual valor para depositar? "))
        if valor <= 0:
            print("Nenhum valor foi depositado!")

        elif: 
            saldo += valor
            print("Valor depositado com sucesso!")
            historico.append(['deposito', valor])

    elif opcao == "s":
        print("Saque")
        valor = float(input("Qual valor para sacar? "))
        if valor > saldo:
            print("Saldo insuficiente")

        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diarios atingido")

        elif valor > 500:
            print("Nao e possivel sacar mais de 500 reais")

        else:
            saldo -= valor
            print("Valor retirado, saldo de ", saldo)
            numero_saques += 1
            historico.append(['saque', valor])

    elif opcao == "e":
        print("Extrato")
        for c in range(0, len(historico)):
            print(f'{historico[c][0]}: R${historico[c][1]:.2f}')

        print("---"*30)
        print("Saldo total: ", saldo)

    elif opcao == "q":
        break


