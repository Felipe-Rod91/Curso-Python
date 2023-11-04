dados = list()
pessoas = list()
maior = menor = 0
pesados = list()
leves = list()
while True:
    pessoas.append(str(input('Digite o nome: ')))
    pessoas.append(float(input('Digite o peso: ')))
    if len(dados) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    cont = str(input('Deseja continuar? [S / N] '))
    while cont not in 'SsNn':
        cont = str(input('Comando inválido! Deseja continuar? [S / N] '))
    if cont in 'Nn':
        break
print('-=' * 30)
for n in dados:
    print(n)
print('-=' * 30)
for p in dados:
    if p[1] == maior:
        pesados.append(p[0])
    elif p[1] == menor:
        leves.append(p[0])
print(f'Foram cadastradas {len(dados)} pessoas.')
print(f'As pessoas mais pesadas são {pesados} e pesam {maior}kg.')
print(f'As pessoas mais leves são {leves} e pesam {menor}kg.')
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
