#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
#de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

preco = float(input('O preço do produto é R$'))
dinheiro = preco * 0.9
vista = preco * 0.95
x2 = preco
x3 = preco * 1.2

print('Os métodos de pagamento são:')
print('[1] Pagamento à vista no dinheiro ou cheque (10% de desconto): R${:.2f}'.format(dinheiro))
print('[2] À vista no cartão (5% de desconto): R${:.2f}'.format(vista))
print('[3] Em até 2x no cartão: R${:.2f}'.format(x2))
print('[4] De 3 até 12x no cartão (20% de juros): R${:.2f}'.format(x3))

metodo = int(input('Qual o método de pagamento? '))

if metodo == 1:
    print(f'Você selecionou pagamento à vista no dinheiro ou cheque com 10% de desconto, total de R${dinheiro:.2f}.')
elif metodo == 2:
    print(f'Você selecionou pagamento à vista no cartão com 5% de desconto, total de R${vista:.2f}.')
elif metodo == 3:
    print(f'Você selecionou pagamento em 2x, total de R${x2:.2f}, cada parcela de R${x2 / 2:.2f}.')
elif metodo == 4:
    print(f'Você selecionou pagamento em 3x até 12x no cartão, com juros de 20%, total de R${x3:.2f}.')
    parcelas = int(input('Em quantas vezes deseja parcelar? '))
    if parcelas == 3:
        print(f'Você parcelou em {parcelas} vezes, cada parcela no valor de R${x3 / parcelas:.2f}.')
    elif parcelas == 4:
        print(f'Você parcelou em {parcelas} vezes, cada parcela no valor de R${x3 / parcelas:.2f}.')
    elif parcelas == 5:
        print(f'Você parcelou em {parcelas} vezes, cada parcela no valor de R${x3 / parcelas:.2f}.')
    elif parcelas == 6:
        print(f'Você parcelou em {parcelas} vezes, cada parcela no valor de R${x3 / parcelas:.2f}.')
    elif parcelas == 7:
        print(f'Você parcelou em {parcelas} vezes, cada parcela no valor de R${x3 / parcelas:.2f}.')
    elif parcelas == 8:
        print(f'Você parcelou em {parcelas} vezes, cada parcela no valor de R${x3 / parcelas:.2f}.')
    elif parcelas == 9:
        print(f'Você parcelou em {parcelas} vezes, cada parcela no valor de R${x3 / parcelas:.2f}.')
    elif parcelas == 10:
        print(f'Você parcelou em {parcelas} vezes, cada parcela no valor de R${x3 / parcelas:.2f}.')
    elif parcelas == 11:
        print(f'Você parcelou em {parcelas} vezes, cada parcela no valor de R${x3 / parcelas:.2f}.')
    elif parcelas == 12:
        print(f'Você parcelou em {parcelas} vezes, cada parcela no valor de R${x3 / parcelas:.2f}.')
    else:
        print('ERRO! ESSA OPÇÃO NÃO É VÁLIDA!')
else:
    print('ERRO! ESSA OPÇÃO NÃO É VÁLIDA!')
