from time import sleep
opcao = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opcao != 5:
    print('''--[ 1 ] Somar
--[ 2 ] Multiplicar
--[ 3 ] Valor maior
--[ 4 ] Novos números
--[ 5 ] Sair do programa''')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('A soma entre os dois números é {}.'.format(n1 + n2))
    if opcao == 2:
        print('A multiplicação entre os dois números é {}.'.format(n1 * n2))
    if opcao == 3:
        if n1 > n2:
            print('O primeiro valor é maior que o segundo.')
        elif n2 > n1:
            print('O segundo valor é maior que o primeiro.')
        elif n1 == n2:
            print('Os dois valores são iguais.')
    if opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    if opcao >= 6:
        print('Opção inválida! Tente novamente.')
print('Finalizando...')
sleep(3)
print('Programa encerrado.')
#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
