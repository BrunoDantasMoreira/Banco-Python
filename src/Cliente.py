from Conta import Conta
from Transacao import Transacao

class Cliente:

    def __init__(self, endereco, contas):
        self.endereco = endereco
        self.contas = contas

    def realizar_trasacao(self, conta: Conta, transacao: Transacao):
        trasacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)
