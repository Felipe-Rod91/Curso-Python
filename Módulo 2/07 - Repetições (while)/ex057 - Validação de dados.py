#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça
#a digitação novamente até ter um valor correto.

genero = str(input('Informe o seu gênero [M/F]: ').strip().upper())
while genero not in 'FM':
    genero = str(input('Informação inválida, informe o seu gênero [M/F]: '))
if genero in 'Mm':
    print('Ok, você é um rapaz.')
if genero in 'Ff':
    print('Ok, você é uma garota.')
