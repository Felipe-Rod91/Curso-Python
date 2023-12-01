# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

cont = soma = maior = menor = 0
mais = 'S'
while mais != 'N':
    if mais == 'S':
        n = int(input('Digite um valor: '))
        cont += 1
        soma += n
        if cont == 1:
            maior = menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
        mais = str(input('Gostaria de continuar? [ S / N ]: ').upper().strip())
    elif mais not in 'SN':
        print('ERRO! OPÇÃO INVÁLIDA!')
        mais = str(input('Gostaria de continuar? [ S / N ]: ').upper().strip())
print(f'O total de números foi {cont} e a média entre eles é {soma / cont:.1f}.')
print(f'O maior dos números digitados é {maior} e o menor é {menor}.')
