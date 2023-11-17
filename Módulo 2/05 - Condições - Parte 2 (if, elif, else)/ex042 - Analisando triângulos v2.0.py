#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

lado1 = float(input('Digite a medida do primeiro lado: '))
lado2 = float(input('Digite a medida do segundo lado: '))
lado3 = float(input('Digite a medida do terceiro lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('O triângulo formado é um triângulo EQUILÁTERO.')
    elif lado1 != lado2 != lado3 != lado1:
        print('O triângulo formado é um triângulo ESCALENO.')
    else:
        print('O triângulo formado é um triângulo ISÓSCELES.')
else:
    print('As três linhas NÃO FORMAM um triângulo.')
