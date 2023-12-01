# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
# retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

valor = float(input('Digite um valor: '))
porcent = int(input('Digite uma porcentagem: '))
print(f'O valor de {moeda.moeda(valor)} aumentado em {porcent}% é {moeda.aumentar(valor, porcent, True)}.')
print(f'O valor de {moeda.moeda(valor)} diminuído em {porcent}% é {moeda.diminuir(valor, porcent, True)}.')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}.')
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}.')
