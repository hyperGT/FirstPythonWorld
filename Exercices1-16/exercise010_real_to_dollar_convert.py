# Make an algorithm that reads a value in reals and converts it to dollars

real = float(input('Insira o valor que deseja converter para dólar: '))
dollar_value = 4.99

valor = real / dollar_value

print(' Valor do dólar: US${} \n Valor inserido: R${} \n Conversão: US${:.2f}'.format(dollar_value, real, valor))



