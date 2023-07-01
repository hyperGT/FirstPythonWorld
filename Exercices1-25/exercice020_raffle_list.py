"""
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.    
"""

from random import shuffle

nomes = []

for _ in range(4):
    nome_alunos = input("Insira o nome do aluno {}: ".format(_))
    nomes.append(nome_alunos)


shuffle(nomes)

print("\nOrdem de apresentação: ")

for i, nome in enumerate(nomes, start=1): 
    print(f"{i}. {nome}")
    


