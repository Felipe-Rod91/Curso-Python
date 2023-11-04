soma = 0
count = 0
for num in range (1,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
        count += 1
print('A soma desses {} números pares é {}.'.format(count, soma))
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
#digitado for ímpar, desconsidere-o.
