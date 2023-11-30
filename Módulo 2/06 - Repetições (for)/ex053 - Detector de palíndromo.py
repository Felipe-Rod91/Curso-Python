#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
#Exemplos de palíndromos:
#APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Insira uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

#ou inverso = junto[::-1] e tira o for, é o macete do fatiamento

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('UAU! ISSO É UM PALÍNDROMO!')
else:
    print('Isso não é palíndromo nem aqui e nem na China.')
