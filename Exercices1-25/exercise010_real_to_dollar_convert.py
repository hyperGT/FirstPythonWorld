# Make an algorithm that reads a value in reals and converts it to dollars

valor = float(input('Insira o valor que deseja converter para dólar: '))
dollar = 4.99

real = valor / dollar

print(' Valor do dólar: US${} \n Valor inserido: R${} \n Conversão: US${:.2f}'.format(dollar, valor, real))



