# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
# valor monetário formatado.

import moeda

valor = float(input('Digite um valor: '))
porcent = int(input('Digite uma porcentagem: '))
print(f'O valor de {moeda.moeda(valor)} aumentado em {porcent}% é {moeda.moeda(moeda.aumentar(valor, porcent))}.')
print(f'O valor de {moeda.moeda(valor)} diminuído em {porcent}% é {moeda.moeda(moeda.diminuir(valor, porcent))}.')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}.')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}.')
