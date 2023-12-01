#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
#usando a estrutura while.

termo = int(input('Digite um número: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
while cont < 10:
    print(f'{termo}', end=' -> ')
    termo += razao
    cont += 1
print(f'{termo}')
