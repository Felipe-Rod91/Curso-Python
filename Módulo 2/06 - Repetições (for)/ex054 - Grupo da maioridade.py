#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
#a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoa}ª pessoa nasceu?'))
    idade = atual - nasc
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'Dessas pessoas, {maior} são MAIORES de idade e {menor} são MENORES.')
