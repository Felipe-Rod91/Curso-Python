from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        print('ERRO! O PASSO NÃO PODE SER ZERO! O PASSO SERÁ CONSIDERADO 1.')
        passo = 1
    print(f'Contagem de {inicio} até {fim} contando de {passo} em {passo}:')
    sleep(0.5)
    if inicio > fim:
        if passo < 0:
            passo *= -1
        passo *= -1
        fim -= 1
    else:
        fim += 1
    for n in range(inicio, fim, passo):
        print(n, end=' ')
        sleep(0.3)
    print('FIM!')
    print('-=' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem.')
while True:
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    contador(i, f, p)
    cont = str(input('Deseja continuar?[S/N] ').upper())
    while cont not in 'SN':
        print('COMANDO INVÁLIDO!')
        cont = str(input('Deseja continuar?[S/N] ').upper())
    if cont == 'N':
        break
    print('-=' * 30)
print('PROGRAMA FINALIZADO!')
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu
# programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
