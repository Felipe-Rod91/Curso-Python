dist = int(input('Qual a distância da viagem em km? '))
if dist <= 200:
    print('Sua viagem de {}km vai custar {:.2f} reais'.format(dist, dist * 0.50))
else:
    print('Sua viagem de {}km vai custar {:.2f} reais'.format(dist, dist * 0.45))
print('BOA VIAGEM!')
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
#por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
