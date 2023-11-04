import random
aluno01 = str(input('Digite o nome de um aluno:'))
aluno02 = str(input('Digite o nome de outro aluno:'))
aluno03 = str(input('Digite o nome de outro aluno:'))
aluno04 = str(input('Digite o nome de outro aluno:'))
ordem = [aluno01, aluno02, aluno03, aluno04]
random.shuffle(ordem)
print('A ordem dos alunos será:')
print(ordem)
#programa para sortear a ordem em que os 4 alunos apresentarão os trabalhos
