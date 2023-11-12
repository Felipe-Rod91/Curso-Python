# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Só aceita se digitar
# 4 números.

numero = str(input('Digite um número de 0 a 9999: '))

print(f'Analisando o número {numero}...')
print(f'Sua milhar é {numero[0]}.')
print(f'Sua centena é {numero[1]}.')
print(f'Sua dezena é {numero[2]}.')
print(f'Sua unidade é {numero[3]}.')

# O mesmo programa, mas aceita números de 1, 2 e 3 dígitos.

num = int(input('Digite um número de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Sua milhar é {m}.')
print(f'Sua centena é {c}.')
print(f'Sua dezena é {d}.')
print(f'Sua unidade é {u}.')
