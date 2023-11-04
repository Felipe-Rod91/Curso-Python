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
print('O total de números foi {} e a média entre eles é {:.1f}.'.format(cont, soma / cont))
print('O maior dos números digitados é {} e o menor é {}.'.format(maior, menor))
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.
