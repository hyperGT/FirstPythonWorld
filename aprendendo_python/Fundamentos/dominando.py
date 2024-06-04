# principais metodos usados da classe string

curso = "PythoN"

print(curso.upper())
#>>>> PYTHON

print(curso.lower())
#>>>> python

print(curso.title())
#>>>> Python

curso = "   Python   3.1   "

print(curso.strip())
#>>>> "Python   3.1"

print(curso.lstrip())
#>>>> "Python   3.1   "

print(curso.rstrip())
#>>>> "   Python   3.1"

curso = "Python"

print(curso)

print(curso.center(10, '#'))
#>>> ##Python##

print(curso.center(12, '-'))
#>>> ---Python---

print(".".join(curso))
#>>> P.y.t.h.o.n


# interpolação de variáveis
nome = "Juan"
idade = 18


print()
# Old Style:
print("Olá, meu nome é %s e tenho %d anos" % (nome, idade))
print()
# Modo (horrível) format: (você pode passar o indice dentro de {} para não repetir a var ali no format)
print("Olá, meu nome é {} e tenho {} anos".format(idade, nome))
print()
# Mais recomendado e moderno:
print(f"Olá, meu nome é {nome} e tenho {idade} anos")
print()


# Outros exemplos:

PI = 3.14159                                                     

print(f"Valor de PI: {PI:.2f}") 
print()

# fatiamento de string (0)(:9)(10:)

nome = "Gabriel Teixeira Charles da Silva"

print(nome[0])
#>>> "G"

print(nome[:7])
#>>> "Gabriel"

print(nome[8:])
#>>> "Teixeira Charles da Silva"

print(nome[0:3]) # ele vai de 0 a 3-1
#>>> "Gab"

print(nome[0:8:2]) # o parametro final (atualmente setado como 2) é o step.
#>>> "Gbil"

print(nome[:])
#>>> "Gabriel Teixeira Charles da Silva"

print(nome[:: -1])
#>>> "avliS ad selrahC ariexieT leirbaG"


# string com múltiplas linhas

nome = "Gabriel"

mensagem = f"""Olá, meu nome é {nome},
Eu estou aprendendo python. 
Este aqui é um exemplo de string com múltiplas linhas"""

print()
print(mensagem)
print()