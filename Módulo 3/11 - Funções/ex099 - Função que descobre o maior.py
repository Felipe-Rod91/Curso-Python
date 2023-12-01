# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa
# tem que analisar todos os valores e dizer qual deles é o maior.


def maior(* num):
    lista = []
    maior_valor = 0
    for i, valor in enumerate(num):
        lista.append(valor)
        if i == 0:
            maior_valor = valor
        else:
            if valor > maior_valor:
                maior_valor = valor
    print('Analisando os valores passados...')
    print(f'Foram informados {len(lista)} valores ao todo: {lista}.')
    print(f'O maior valor informado é {maior_valor}.')
    print('-=' * 30)


maior(7, 2, 6)
maior(6, 4, -2, 99, 56, 12, 110)
maior(5, 2, 6, 4, 6, 2)
maior()
