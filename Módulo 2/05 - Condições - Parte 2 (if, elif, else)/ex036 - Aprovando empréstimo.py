# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos pretende pagar a casa?'))

parcela = casa / (anos * 12)
cores = {'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'limpa': '\033[m'}

print('O valor da parcela será de R${:.2f}.'.format(parcela))
porcentagem = sal * .3
print('O valor máximo da parcela, de acordo com o seu salário, é de R${:.2f}.'.format(porcentagem))

if porcentagem > parcela:
    print(f'{cores["verde"]}PARABÉNS! O seu financiamento foi aprovado!{cores["limpa"]}')
else:
    print(f'{cores["vermelho"]}Que pena, mas não poderemos oferecer o financiamento.{cores["limpa"]}')
