# Vamos criar um menu em python, usando modularização

from lib.interface.funções_interface import *
from lib.arquivo.funções_arquivo import *
from time import sleep

arquivo = 'Pessoas Cadastradas.txt'
if not arquivo_existe(arquivo):
    criar_arquivo('Pessoas Cadastradas.txt')

while True:
    opção = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if opção == 1:
        ler_arquivo(arquivo)
    elif opção == 2:
        título('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastro(arquivo, nome, idade)
    elif opção == 3:
        título('SAINDO DO PROGRAMA... ATÉ LOGO!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
