lista_completa = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    lista_completa.append([nome, [n1, n2], media])
    cont = str(input('Deseja continuar?[S / N] '))
    while cont not in 'SsNn':
        cont = str(input('Comando inválido! Deseja continuar?[S / N] '))
    if cont in 'Nn':
        print('-=' * 13)
        break
print(f'{"Nº":<4} {"ALUNO":<10} {"MÉDIA":>8}')
print('-' * 26)
for i, n in enumerate(lista_completa):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8}')
print('-' * 26)
while True:
    a = int(input('Digite o número do aluno a ser analisado (999 para encerrar): '))
    if a == 999:
        break
    if 0 <= a <= len(lista_completa) - 1:
        print(f'As notas de {lista_completa[a][0]} são {lista_completa[a][1][0]:.1f} e {lista_completa[a][1][1]:.1f}.')
    else:
        print('Aluno inexistente!')
    print('-=' * 30)
print('PROGRAMA ENCERRADO!')
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
