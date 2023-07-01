"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
"""
import math

a = (float(input("Insira o valor do cateto oposto: ")))
b = (float(input("Insira o valor do cateto adjacente: ")))

# c = √(a² + b²)

# Método matemático
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
# Jeito mais funcional
c2 = math.hypot(a, b)

print("O comprimento da hipotenusa é {:.2f}".format(c2))
