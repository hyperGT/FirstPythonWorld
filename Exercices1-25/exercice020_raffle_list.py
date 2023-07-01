"""
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.    
"""

import random


nomes = ["Ahri", "Fiora", "Veigar", "Miss Fortune"]

random.shuffle(nomes)

print("Ordem de apresentação: ")

for i, nome in enumerate(nomes, start=1): 
    print(f"{i}. {nome}")
    


