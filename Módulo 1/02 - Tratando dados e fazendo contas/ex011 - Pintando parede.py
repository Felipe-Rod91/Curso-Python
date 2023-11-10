#programa para calcular a área de uma parede e quantos litros de tinta serão necessários para pintá-la inteira

larg = float(input('Qual a largura da parede em metros?'))
alt = float(input('E qual a altura dela em metros?'))
print(f'Se a largura é de {larg} metros e a altura é de {alt} metros, então a área dela é {larg * alt}m², então '
      f'precisamos de {(larg * alt) / 2} litros de tinta para pintá-la inteira.')
