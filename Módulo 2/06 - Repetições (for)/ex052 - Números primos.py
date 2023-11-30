#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

tot = 0
num = int(input('Digite um número: '))
for n in range(1, num + 1):
    if num % n == 0:
        tot = tot + 1
print(f'O número {num} foi divisível, entre 1 e {num}, {tot} vezes.')
if tot <= 2:
    print('Esse número É PRIMO.')
else:
    print('Esse número NÃO É PRIMO!')
