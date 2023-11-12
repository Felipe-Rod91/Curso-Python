#crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, minúsculas,
#quantas letras tem sem os espaços e quantas letras tem o primeiro nome

nome = str(input('Digite um nome: ')).strip()

print('Analisando o seu nome...')
print(f'O seu nome em maiúsculas é {nome.upper()}.')
print(f'O seu nome em minúsculas é {nome.lower()}.')
print(f'O seu nome tem {len(nome) - nome.count(" ")} letras.')
print(f'O seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras.')
