def dividir (dividendo, divisor):

    if not ( isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("dividir() deve receber apenas argumentos inteiros")
    try:
        aux = dividendo / divisor

    except:
        print(f'Não foi possivel dividir {dividendo} por {divisor}')
        raise
    return aux


def testa_divisao(divisor):
        resultado = dividir(10, divisor)
        print(f'o valor da divisão é: {resultado}')
"""try:
    testa_divisao(0)
except Exception as E:
    print(E)"""

"""try:
    testa_divisao(0)
except AttributeError as E:
    print(E.__class__.__bases__)
except ZeroDivisionError as E:
    print(E.__class__.__bases__)"""

try:
    testa_divisao(0)
except ZeroDivisionError as E:
    print("Erro de divisão por ZERO")
except Exception as E:
    print('Tratamento de erro generico')

print("Programa encerrado")