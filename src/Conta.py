class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, clinte, numero):
        return cls(numero, clinte)

    @property
    def saldo():
        return self._saldo

    @property
    def numero(self):
        """The numero property."""
        return self._numero

    @property
    def agencia(self):
        """The agencia property."""
        return self._agencia

    @property
    def clinte(self):
        """The clinte property."""
        return self._clinte

    @property
    def historico(self):
        """The historico property."""
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")

