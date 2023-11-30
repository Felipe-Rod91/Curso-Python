#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input(f'Quantos quilos a {pessoa}ª pessoa pesa? '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'A pessoa com maior peso tem {maior:.1f}kg, e a com menor peso tem {menor:.1f}kg.')
