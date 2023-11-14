# Faça um programa que leia o aumento salarial de um funcionário. Se for acima de 1250 reais, terá um aumento de 10%.
# Se for abaixo disso, 15%.

sal = float(input('Qual o salário do funcionário? '))

if sal > 1250:
    print('O seu salário de {:.2f} reais terá um aumento de 10%, ou seja, {:.2f} reais, e será um total de {:.2f} reais.'.format(sal, sal * 0.1, sal + (sal * 0.1)))
else:
    print('O seu salário de {:.2f} reais terá um aumento de 15%, ou seja, {:.2f} reais, e será um total de {:.2f} reais.'.format(sal, sal * 0.15, sal + (sal * 0.15)))
print('Parabéns pelo aumento, continue o bom trabalho!')
