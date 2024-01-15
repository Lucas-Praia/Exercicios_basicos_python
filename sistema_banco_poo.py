class ContaCorrente:

    #se quisesse criar um atributo para quando a pessoa fosse abrir a conta dela com um saldo,
    # aí colocaria o atributo saldo no self...mas como nao é requisito, nao colocamos.

    #primeiro construiu o primeiro metodo - innit - nome, cpf
    #depois construiu o metodo consultar_saldo, depositar, sacar_saldo

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None

    def consultar_saldo(self):
        print(f'O saldo atual é de R$ {self.saldo :,.2f}')

    def depositar(self,valor):
        self.saldo += valor

    def limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self,valor):
        if self.saldo - valor < self.limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor


#programa
conta_lucas = ContaCorrente('Lucas', '555.555.432-12')

print(f'Nome: {conta_lucas.nome}. CPF: {conta_lucas.cpf}')
conta_lucas.consultar_saldo()
#depositando dinheiro na conta
conta_lucas.depositar(8000)
conta_lucas.consultar_saldo()

#sacando um dinheiro da conta
conta_lucas.sacar_dinheiro(10000)

print(f'Saldo Final:{conta_lucas.consultar_saldo()}')
