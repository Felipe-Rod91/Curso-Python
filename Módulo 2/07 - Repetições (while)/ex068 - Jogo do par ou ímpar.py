from random import randint
cont = 0
print('-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('-' * 30)
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um valor: '))
    palpite = ' '
    res = jogador + computador
    while palpite not in 'PpIi':
        palpite = str(input('Você escolhe PAR ou ÍMPAR? [ P / I ] ').upper().strip())
    print(f'Você escolheu {jogador} e o computador escolheu {computador}. O total é {res}.')
    print(f'Então é PAR!' if res % 2 == 0 else 'Então é ÍMPAR!')
    print('-' * 20)
    if res % 2 == 0:
        if palpite == 'P':
            print('Você GANHOU! VAMOS JOGAR NOVAMENTE...')
            cont += 1
        elif palpite == 'I':
            print('Você PERDEU!')
            print('-' * 20)
            break
    else:
        if palpite == 'P':
            print('Você PERDEU!')
            print('-' * 20)
            break
        elif palpite == 'I':
            print('Você GANHOU! VAMOS JOGAR NOVAMENTE...')
            cont += 1
    print('-' * 20)
print(f'Você ganhou {cont} vezes.')
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
