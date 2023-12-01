# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar (supondo que seja 65 anos).

from datetime import date

trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - nascimento
trabalhador['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['CTPS'] == 0:
    for k, v in trabalhador.items():
        print(f'{k.title()}: {v}.')
    print('Essa pessoa ainda não trabalha.')
else:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['aposentadoria'] = 65 - (date.today().year - trabalhador['contratacao'])
    trabalhador['salário'] = float(input(f'Salário: R$'))
    for k, v in trabalhador.items():
        print(f'{k.title()}: {v}.')
