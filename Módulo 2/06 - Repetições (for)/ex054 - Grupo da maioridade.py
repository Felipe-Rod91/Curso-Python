from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?'.format(pessoa)))
    idade = atual - nasc
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Dessas pessoas, {} são MAIORES de idade e {} são MENORES.'.format(maior, menor))
#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
#a maioridade e quantas já são maiores.
