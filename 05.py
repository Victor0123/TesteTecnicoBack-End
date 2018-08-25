class Conta:


    def __init__(self, nome:str, numero:str):
        self.__nome = nome
        self.__numero_conta = numero
        self.__saldo = 0


    def saque(self, valor_saque):
        if self.__saldo >= valor_saque:
            self.__saldo -= valor_saque
        else:
            print('Operação Invalida')


    def deposito(self, valor_deposito):
        if valor_deposito > 0:
            self.__saldo += valor_deposito
        else:
            print('Operação Invalida')


    def alterar_nome(self, nome:str):
        if not nome or len(nome.strip()) == 0:
            print('Nome invalido')
        else:
            self.__nome = nome

    def __repr__(self):
        return f'{self.__nome} conta: {self.__numero_conta} saldo {self.__saldo}'


conta = Conta('João', '2085-3')
conta.deposito(20)
conta.saque(10)
conta.alterar_nome('Victor')

print(conta)