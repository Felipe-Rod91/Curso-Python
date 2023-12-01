# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    c = int(input('Digite um valor: '))
    if c < 0:
        break
    print('-' * 20)
    for n in range(1, 11):
        print(f'{c} x {n} = {c * n}')
    print('-' * 20)
print('-' * 20)
print('FINALIZANDO...')
print('Programa encerrado.')
