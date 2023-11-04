times = ('Botafogo', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Fluminense',
         'Fortaleza', 'Bragantino', 'Atlético-PR', 'Santos', 'Internacional', 'Corinthians', 'Cuiabá', 'Bahia', 'Goiás',
         'Vasco', 'América-MG', 'Coritiba')
print(f'Tabela do Brasileirão em maio/2023:')
for posicao, t in enumerate(times):
    print(f'{posicao}º {t}')
print('-=' * 15)
print(f'Os cinco primeiros colocados são {times[:5]}.')
print(f'Os últimos quatro colocados são {times[-4:]}.')
print(f'Os times em ordem alfabética são {sorted(times)}')
print(f'O time do Corinthians está em {times.index("Corinthians") + 1}º lugar.')
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Corinthians.
