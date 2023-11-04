def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {comp:.2f}m x {larg:.2f}m é {a:.2f}m².')


print('Controle de Terrenos')
print('-' * 20)
l = float(input(f'LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.
