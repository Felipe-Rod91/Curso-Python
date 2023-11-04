n1 = 0
n2 = 1
n3 = 0
cont = 2
print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
seq = int(input('Quantos termos você quer mostrar? '))
print('~' * 30)
if seq == 1:
    print('{}'.format(n1))
elif seq == 2:
    print('{} -> {}'.format(n1, n2))
elif seq >= 3:
    print('{} -> {}'.format(n1, n2), end=' ')
    n3 = n1 + n2
    while cont < seq:
        print('-> {}'.format(n3), end=' ')
        cont += 1
        n1 = n2
        n2 = n3
        n3 = n1 + n2
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
# de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8
