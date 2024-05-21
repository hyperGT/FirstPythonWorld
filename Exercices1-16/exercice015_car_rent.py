# car rent
"""
Escreva um programa
que pergunte a quantidade de km percorridos por
um carro alugado e a quantidade de dias pelos
quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por km rodado.
"""

km = float(input('Quantos km rodados? '))
days = int(input('Quantidade de dias que foi alugado: '))

per_day = 60
per_km = 0.15

total_price = (km * per_km) + (days * per_day)

print('O total a pagar é: {:.2f}'.format(total_price))
