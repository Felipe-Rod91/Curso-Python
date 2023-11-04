lista_completa = list()
lista_individual = dict()
soma = media = 0
while True:
    lista_individual['nome'] = str(input('Nome: '))
    lista_individual['sexo'] = str(input('Sexo: ').upper())
    while lista_individual['sexo'] not in 'MF':
        print('Valor inválido! Digite apenas M ou F.')
        lista_individual['sexo'] = str(input('Sexo: ').upper())
    lista_individual['idade'] = int(input('Idade: '))
    soma += lista_individual['idade']
    lista_completa.append(lista_individual.copy())
    cont = str(input('Deseja continuar?[S / N] ').upper())
    while cont not in 'SN':
        print('Valor inválido! Digite o valor S ou N.')
        cont = str(input('Deseja continuar?[S / N] ').upper())
    if cont in 'N':
        break
media = soma / len(lista_completa)
print('-=' * 20)
for p in lista_completa:
    print(p)
print('-=' * 20)
print(f'Foram cadastradas {len(lista_completa)} pessoas.')
print(f'A média de idade entre elas é {media:.0f} anos.')
print('-=' * 20)
print(f'As mulheres do grupo são:')
for m in lista_completa:
    if m['sexo'] == 'F':
        print(m['nome'])
print('-=' * 20)
print(f'As pessoas mais velhas que a média de idade do grupo ({media:.0f} anos) são:')
for v in lista_completa:
    if v['idade'] > media:
        for k, i in v.items():
            print(f'{k}: {i}', end=', ')
        print()
print('-=' * 20)
print('PROGRAMA ENCERRADO!')
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas;
# B) A média de idade;
# C) Uma lista com as mulheres;
# D) Uma lista de pessoas com idade acima da média.
