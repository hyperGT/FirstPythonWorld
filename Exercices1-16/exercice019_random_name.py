"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""

import random

#Criando a lista com 4 alunos
nomes = ["Larissa", "João", "Daniel", "Geovanna"]

#Sorteando nome aleatório
nome_sorteado = random.choice(nomes)

print("O aluno a apagar o quadro hoje é {}".format(nome_sorteado))
