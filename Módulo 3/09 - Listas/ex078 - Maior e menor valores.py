# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite o valor na posição {v}: ')))
maior = max(valores)
menor = min(valores)
valores_maiores = [i for i, valor in enumerate(valores) if valor == maior]
valores_menores = [i for i, valor in enumerate(valores) if valor == menor]
print(f'Os valores digitados foram {valores}.')
print(f'O maior valor é o {maior} e está na posição {valores_maiores}')
print(f'O menor valor é o {menor} e está na posição {valores_menores}')
