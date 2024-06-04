# formas de declarar uma tupla

# lembrando que diferente das listas, as tuplas são imutáveis, ou seja, depois de criada, não pode ser alterada

frutas = ("laranja", "uva", "morango",)

letras = tuple("Python")

numeros = tuple([1, 2, 3, 4, 5]) # convertendo lista para tupla

pais = ("Brasil", "Canadá",)

print(frutas)
print(letras)
print(numeros)
print(pais)

# como acessar um objeto? do mesmo jeito q a lista
print(frutas[1])

# tuplas aninhadas / matriz bidimensional
matriz = (
    ("João", "Maria", "Pedro",),
    (7, 10, 6,),
    (8, 10, 5,), 
    (True, True, False)
)

# como chamar e retornar as posições (igual como se chama uma lista)
print(f"Todos os alunos: {matriz[0][::]}")
print(f"Notas de Av1: {matriz[1][::]}")
print(f"Notas de Av2: {matriz[2][::]}")
print(f"Aprovações: {matriz[-1][::]}")

# usando for para percorrer os dados da TUPLA
print()
for aluno in matriz[0][::]:
    print(aluno)

print()
# usando o enumerate para passar o indice/enumerar os itens
for indice, aluno in  enumerate(matriz[0][::]):
    print(f"{indice}: {aluno}")
    
    
# Métodos utilizáveis com a tupla

# Count

# como o nome sugere, permite contar quantas vezes um elemento aparece na tupla
cursos = ("kotlin", "java", "c", "python", "c", "c")

print(cursos.count("c")) # exibindo quantas vezes esse elemento aparece na tupla

# Index

# o uso do método Index em tuplas funciona de maneira semelhante ao das listas
print(cursos.index("c")) # exibindo o índice do (primeiro) elemento "c"

# len

# retorna a quantidade de elementos que a tupla contém
print(len(cursos)) # exibindo quantidade de elementos contidos dentro da tupla