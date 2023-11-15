# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite um número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and b < c:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a or c > b:
    maior = c

print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')
