# Faça um programa que leia o aumento salarial de um funcionário. Se for acima de 1250 reais, terá um aumento de 10%.
# Se for abaixo disso, 15%.

sal = float(input('Qual o salário do funcionário? '))

if sal > 1250:
    print(f'O seu salário de {sal:.2f} reais terá um aumento de 10%, ou seja, {sal * 0.1:.2f} reais, e será um total '
          f'de {sal + (sal * 0.1):.2f} reais.')
else:
    print(f'O seu salário de {sal:.2f} reais terá um aumento de 15%, ou seja, {sal * 0.15:.2f} reais, e será um total '
          f'de {sal + (sal * 0.15):.2f} reais.')

print('Parabéns pelo aumento, continue o bom trabalho!')
