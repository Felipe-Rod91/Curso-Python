# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite a cidade na qual você nasceu: ').strip().title()[:5])
print(cidade == 'Santo')
