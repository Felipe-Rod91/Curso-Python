# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
# ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

mais1000 = menor = total = produtos = 0
continuar = ' '
print('-' * 20)
print('LOJAS FERFAFE')
print('-' * 20)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    produtos += 1
    total += preco
    if produtos == 1 or preco < menor:
        menor = preco
        produtinho = nome
    if preco >= 1000:
        mais1000 += 1
    while continuar not in 'sn':
        continuar = str(input('Deseja continuar? [ S / N ] ').lower().strip())
    if continuar == 'n':
        print('-' * 20)
        break
    else:
        continuar = ' '
        print('-' * 20)
print('Finalizando...')
print(f'O total gasto nas compras é R${total:.2f}.')
print(f'Dentre os produtos, {mais1000} deles custam mais de mil reais.')
print(f'O produto mais barato é o {produtinho}, que custa R${menor:.2f}.')
