# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja continuar? [S / N] '))
    while cont not in 'SsNn':
        cont = str(input('Comando inválido! Deseja continuar? [S / N] '))
    if cont in "Nn":
        break
print(f'Você digitou {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print(f'Essa lista possui o número 5 nela.')
else:
    print('Essa lista não possui o número 5 nela.')
