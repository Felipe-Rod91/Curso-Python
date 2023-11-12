# programa para sortear qual dos 4 alunos começará apresentando os trabalhos

import random

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno sorteado para apresentar primeiro é o(a) {random.choice(lista)}.')
