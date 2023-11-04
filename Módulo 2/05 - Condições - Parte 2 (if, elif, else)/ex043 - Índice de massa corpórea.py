peso = float(input('Qual é o seu peso em kg? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso / (altura ** 2)
print('O seu IMC é igual a {:.2f}'.format(imc), end= ', ')
if imc >= 0 and imc <= 18.5:
    print('ABAIXO DO PESO.')
elif imc > 18.5 and imc <= 25:
    print('PESO IDEAL.')
elif imc > 25 and imc <= 30:
    print('SOBREPESO.')
elif imc > 30 and imc <= 40:
    print('OBESIDADE.')
elif imc > 40:
    print('OBESIDADE MÓRBIDA.')
else:
    print('ESSE VALOR ESTÁ INCORRETO!')
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
#seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
