import random

numeros = '0123456789'
letras = 'abcdefghijklmnopqrstuvwxyz'
letras_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
soma = numeros + letras + letras_upper

quantidade = int(input('Quantas senhas?'))
lenght = int(input('Quantos caracteres?'))

def gera_cpf():
    embaralha = ''.join(random.sample(soma, lenght))
    print(embaralha)


for c in range(quantidade):
    gera_cpf()


