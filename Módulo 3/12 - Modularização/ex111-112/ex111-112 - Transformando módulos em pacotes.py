from UtilidadesCeV import moeda
from UtilidadesCeV import dados

valor = dados.leia_dinheiro('Digite um valor: R$')
print(moeda.resumo(valor, 20, 25))
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções
# utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dados. Crie uma função chamada
# leia_dinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas
# valores que seja monetários.
