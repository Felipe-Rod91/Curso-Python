prim = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = prim + (10 - 1) * razao
for n in range(0, 10):
    print(prim + (razao * n), end=' -> ')
print('ACABOU!')

for n2 in range(prim, decimo + razao, razao):
    print('{}'.format(n2), end= ' -> ')
print('ACABOU!')
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
#dessa progressão.
