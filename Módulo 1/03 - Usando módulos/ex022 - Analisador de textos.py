nome = str(input('Digite um nome: ')).strip()
print('Analisando o seu nome...')
print('O seu nome em maiúsculas é {}.'.format(nome.upper()))
print('O seu nome em minúsculas é {}.'.format(nome.lower()))
print('O seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome é {} e tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))
#crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, minúsculas,
#quantas letras tem sem os espaços e quantas letras tem o primeiro nome
