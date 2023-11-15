#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
#por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = int(input('Qual a distância da viagem em km? '))

if dist <= 200:
    print(f'Sua viagem de {dist}km vai custar {dist * 50:.2f} reais')
else:
    print(f'Sua viagem de {dist}km vai custar {dist * 0.45:.2f} reais')
print('BOA VIAGEM!')
