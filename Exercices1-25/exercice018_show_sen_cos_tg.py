"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan

angle = float(input("Insira o ângulo: "))

sen = sin(radians(angle))
cos = cos(radians(angle))
tg = tan(radians(angle))

print(f"Ângulo: {angle}")
print("seno: {:.2f}".format(sen))
print("cosseno: {:.2f}".format(cos))
print("tangente: {:.2f}".format(tg))



