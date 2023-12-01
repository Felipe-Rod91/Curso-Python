# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

lista_numerica = list()
n = 0
while True:
    n = (int(input('Digite um número: ')))
    while n in lista_numerica:
        n = int(input('Valor repetido, digite um número diferente: '))
    lista_numerica.append(n)
    cont = str(input('Deseja continuar? [S / N] '))
    while cont not in 'SsNn':
        cont = str(input('Comando inválido! Deseja continuar? [S / N] '))
    if cont in 'Nn':
        break
lista_numerica.sort()
print(f'Os valores digitados e organizados em ordem crescente foram {lista_numerica}.')
