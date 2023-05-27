# Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua area e a quantidade de tinta necessária para pintá-la
# nota: cada ltro de tinta pinta uma área de 2m^2

width = int(input('Enter the width: '))
height = int(input('Enter the height: '))
qnt_ink = 2**2

# A = w * h
Area = width * height

print(Area / qnt_ink)