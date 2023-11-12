#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip().split()

print(f'Olá {nome}, muito prazer! Analisando o seu nome...'.format(nome))
print(f'Seu primeiro nome é {nome[0]}.')
print(f'Seu último nome é {len(nome)-1}.')
