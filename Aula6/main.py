from optparse import _parse_int
from pprint import pprint
from exceptions import SaldoInsuficienteError, OperacoesFinanceiraError

class Cliente:

    def __init__(self,nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.__agencia = 0
        self.__numero = 0
        self.saques_nao_permitidos = 0
        self.transferencias_nao_permitidos = 0
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas

    @property
    def agencia(self):
        return self.__agencia


    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo agencia deve ser um numero inteiro", value)

        if value <= 0:
            raise ValueError("O atributo agencia deve ser um valor positivo")

        self.__agencia = value

    @property
    def numero(self):
        return self.__numero


    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo numero deve ser um numero inteiro", value)

        if value <= 0:
            raise ValueError("O atributo numero deve ser um valor positivo")
        self.__numero  = value

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo saldo deve ser um numero inteiro", value)

        self.__saldo = value

    def transferir(self, valor, favorecido):
        if valor <= 0:
            raise ValueError("O valor a ser transferido não pode ser menor que zero")
        try:
            self.sacar(valor)
        except SaldoInsuficienteError as E:
            self.transferencias_nao_permitidos += 1
            E.args = ()
            raise OperacoesFinanceiraError("Operação não finalizada") from E
            raise E
        favorecido.depositar(valor)

    def sacar(self, valor):
        if self.saldo < valor:
            raise SaldoInsuficienteError('', self.saldo, valor)
        if valor <= 0:
            self.saques_nao_permitidos += 1
            raise ValueError("O valor a ser sacado não pode ser menor que zero")
        self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

def main():
    import sys

    contas = []
    while True:
        try:
            nome = input('Digite o nome do cliente: ')
            agencia = input('Digite o número da agencia: ')
            numero = input("Digite o número da conta corrente: ")
            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)
        except ValueError as E:
            print(type(E.args))
            sys.exit()
        except KeyboardInterrupt:
            print(f'{len(contas)} (s) contas criadas')
            sys.exit()



conta_corrente1 = ContaCorrente(None, 400, 123456)
conta_corrente2 = ContaCorrente(None, 401, 11231)

try:
    conta_corrente1.sacar(1000)
    print("Saldo da conta 1: ", conta_corrente1.saldo)
    print("Saldo da conta 2: ", conta_corrente2.saldo)
except OperacoesFinanceiraError as E:
    breakpoint()
    pass