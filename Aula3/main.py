from optparse import _parse_int
from pprint import pprint


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

        if value <= 0:
            raise ValueError("O atributo saldo deve ser um valor positivo")
        self.__saldo = value

    def transferir(self, valor, favorecido):
        favorecido.depositar(valor)

    def sacar(self, valor):
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
            breakpoint()
            numero = input("Digite o número da conta corrente: ")
            cliente = Cliente(nome, None, None)
            conta_corrente = ContaCorrente(cliente, agencia, numero)
            contas.append(conta_corrente)
        except KeyboardInterrupt:
            print(f'{len(contas)} (s) contas criadas')
            sys.exit()

if __name__ == '__main__':
    main()