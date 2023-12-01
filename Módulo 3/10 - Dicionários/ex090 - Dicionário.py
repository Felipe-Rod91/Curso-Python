# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela.

dados = dict()
dados['aluno'] = str(input('Nome: '))
dados['media'] = float(input(f'Média semestral de {dados["aluno"]}: '))
print('-=' * 20)
for k, v in dados.items():
    print(f'- O {k} do aluno é {v}.')
if dados['media'] >= 7:
    dados['situaçao'] = 'APROVADO(A)'
elif 5 <= dados['media'] < 7:
    dados['situaçao'] = 'RECUPERAÇÃO'
else:
    dados['situaçao'] = 'REPROVADO(A)'
print(f'- Situação de {dados["aluno"]} é {dados["situaçao"]}!')
