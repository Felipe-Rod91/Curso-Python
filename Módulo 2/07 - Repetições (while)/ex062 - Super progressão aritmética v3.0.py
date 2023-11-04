termo = int(input('Digite um número: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont < total:
        termo += razao
        print('{}'.format(termo), end=' -> ' if cont < total - 1 else '\n')
        cont += 1
    mais = int(input('Quantos termos você quer a mais? '))
print('FINALIZANDO...')
print('FIM DO PROGRAMA.')
print('O programa foi finalizado com {} termos mostrados.'.format(total))
#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando
#ele disser que quer mostrar 0 termos.
