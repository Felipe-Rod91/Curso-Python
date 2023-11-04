from time import sleep
jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['partidas'] = partidas
    for g in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols fez na partida {g}? ')))
    jogador['gols'] = gols.copy()
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    jogador.clear()
    gols.clear()
    cont = str(input('Deseja continuar?[S / N] ').upper())
    while cont not in 'SN':
        print('Comando inválido! Digite apenas S ou N.')
        cont = str(input('Deseja continuar?[S / N] ').upper())
    if cont == 'N':
        break
    print('-=' * 20)
print('-=' * 20)
print(f'{"Nº":<3} {"NOME":<12} {"PARTIDAS":<8} {"GOLS":>5}')
print('-' * 33)
for i, j in enumerate(jogadores):
    print(f'{i:<3} {j["nome"]:<12} {j["partidas"]:^8} {j["total"]:>5}')
print('-=' * 20)
while True:
    analise = int(input('Digite o número do jogador para análise (999 para terminar): '))
    if analise == 999:
        break
    elif 0 <= analise <= len(jogadores) - 1:
        print(f'Buscando informações de {jogadores[analise]["nome"]}...')
        sleep(2)
        print(f'O jogador {jogadores[analise]["nome"]} jogou {jogadores[analise]["partidas"]} partidas:')
        for i, v in enumerate(jogadores[analise]["gols"]):
            print(f'- Na partida {i + 1} fez {v} gols.')
        print(f'No total, {jogadores[analise]["nome"]} fez {jogadores[analise]["total"]} gols.')
        print('-=' * 20)
    else:
        print('Número inválido!')
        print('-=' * 20)
print('Você digitou 999...')
print('PROGRAMA ENCERRADO!')
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
# aproveitamento de cada jogador.
