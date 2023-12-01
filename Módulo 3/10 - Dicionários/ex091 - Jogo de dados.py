# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador 1': randint(1, 6),
             'jogador 2': randint(1, 6),
             'jogador 3': randint(1, 6),
             'jogador 4': randint(1, 6)}
ranking = list
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)
print('-=' * 12)
print('RANKING DOS JOGADORES')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} no dado.')
