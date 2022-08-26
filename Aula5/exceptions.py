class SaldoInsuficienteError(Exception):
    def __init__(self, message='', saldo=None, valor=None, *args):
        self.saldo = saldo
        self.valor = valor
        msg = f'Saldo insuficiente para efetuar a transação... Seu saldo atual :{self.saldo}... Valor a ser sacado: {self.valor}'
        super(SaldoInsuficienteError, self).__init__(message or msg, self.saldo, self.valor, *args)
