numero = str(input('Digite um número de 0 a 9999: '))
print('Analisando o número {}...'.format(numero))
print('Sua milhar é {}.'.format(numero[0]))
print('Sua centena é {}.'.format(numero[1]))
print('Sua dezena é {}.'.format(numero[2]))
print('Sua unidade é {}.'.format(numero[3]))
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Só aceita se digitar 4 números.

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Sua milhar é {}.'.format(m))
print('Sua centena é {}.'.format(c))
print('Sua dezena é {}.'.format(d))
print('Sua unidade é {}.'.format(u))
#O mesmo programa, mas aceita números de 1, 2 e 3 dígitos.
