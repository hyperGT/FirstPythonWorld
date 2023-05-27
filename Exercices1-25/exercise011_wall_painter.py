# Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua area e a quantidade de tinta necessária para pintá-la
# nota: cada ltro de tinta pinta uma área de 2m^2

width = float(input('Enter the width: '))
height = float(input('Enter the height: '))
ink = 2

# A = w * h
Area = width * height

# A / ink
qnt_ink = Area / ink

print(qnt_ink)