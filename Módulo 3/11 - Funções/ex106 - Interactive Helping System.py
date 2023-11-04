from time import sleep
color = ('\033[m',  # 0 - sem cor
         '\033[0;30;41m',  # 1 - vermelho
         '\033[0;30;42m',  # 2 - verde
         '\033[0;30;43m',  # 3 - amarelo
         '\033[0;30;44m',  # 4 - azul
         '\033[0;30;45m',  # 5 - roxo
         '\033[7;40m'      # 6 - branco
         )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\':', 4)
    print(color[6], end='')
    help(com)
    print(color[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    print(color[cor], end='')
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))
    print(color[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('  SISTEMA DE AJUDA INTERATIVA pyHELP  ', 1)
    comando = str(input('Comando ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('  OBRIGADO E ATÉ LOGO!  ', 2)
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
