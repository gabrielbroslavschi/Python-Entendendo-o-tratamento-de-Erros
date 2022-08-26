def dividir (dividendo, divisor):
    return dividendo / divisor

def testa_divisao(divisor):
    try:
        teste = 'teste'
        teste.ola()
        resultado = dividir(10, divisor)
        print(f'o valor da divisão é: {resultado}')
    except ZeroDivisionError:
        print(f"não é possivel fazer a divisão com o valor {divisor}")


try:
    testa_divisao(1)
except AttributeError:
    print('Tem um erro de Atributo')