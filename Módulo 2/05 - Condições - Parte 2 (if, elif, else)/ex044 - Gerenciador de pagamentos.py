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
    print('Você selecionou pagamento à vista no dinheiro ou cheque com 10% de desconto, total de R${:.2f}.'.format(dinheiro))
elif metodo == 2:
    print('Você selecionou pagamento à vista no cartão com 5% de desconto, total de R${:.2f}.'.format(vista))
elif metodo == 3:
    print('Você selecionou pagamento em 2x, total de R${:.2f}, cada parcela de R${:.2f}.'.format(x2, x2 / 2))
elif metodo == 4:
    print('Você selecionou pagamento em 3x até 12x no cartão, com juros de 20%, total de R${:.2f}.'.format(x3))
    parcelas = int(input('Em quantas vezes deseja parcelar? '))
    if parcelas == 3:
        print('Você parcelou em {} vezes, cada parcela no valor de R${:.2f}.'.format(parcelas, x3 / parcelas))
    elif parcelas == 4:
        print('Você parcelou em {} vezes, cada parcela no valor de R${:.2f}.'.format(parcelas, x3 / parcelas))
    elif parcelas == 5:
        print('Você parcelou em {} vezes, cada parcela no valor de R${:.2f}.'.format(parcelas, x3 / parcelas))
    elif parcelas == 6:
        print('Você parcelou em {} vezes, cada parcela no valor de R${:.2f}.'.format(parcelas, x3 / parcelas))
    elif parcelas == 7:
        print('Você parcelou em {} vezes, cada parcela no valor de R${:.2f}.'.format(parcelas, x3 / parcelas))
    elif parcelas == 8:
        print('Você parcelou em {} vezes, cada parcela no valor de R${:.2f}.'.format(parcelas, x3 / parcelas))
    elif parcelas == 9:
        print('Você parcelou em {} vezes, cada parcela no valor de R${:.2f}.'.format(parcelas, x3 / parcelas))
    elif parcelas == 10:
        print('Você parcelou em {} vezes, cada parcela no valor de R${:.2f}.'.format(parcelas, x3 / parcelas))
    elif parcelas == 11:
        print('Você parcelou em {} vezes, cada parcela no valor de R${:.2f}.'.format(parcelas, x3 / parcelas))
    elif parcelas == 12:
        print('Você parcelou em {} vezes, cada parcela no valor de R${:.2f}.'.format(parcelas, x3 / parcelas))
    else:
        print('ERRO! ESSA OPÇÃO NÃO É VÁLIDA!')
else:
    print('ERRO! ESSA OPÇÃO NÃO É VÁLIDA!')
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
#de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros
