lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cont = str(input('Deseja continuar? [S / N] '))
    while cont not in 'SsNn':
        cont = str(input('Comando inválido! Deseja continuar? [S / N] '))
    if cont in 'Nn':
        break
for i, n in enumerate(lista):
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'A lista completa dos números digitados é {lista}.')
print(f'Os números pares são {pares}.')
print(f'Os números ímpares são {impares}.')
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
# listas geradas.
