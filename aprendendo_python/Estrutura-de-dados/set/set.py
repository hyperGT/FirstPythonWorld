# Conjuntos ou "set"

# "build an unordered collection of unique elements"

# Usamos sets para representar conjuntos matemáticos e eliminar objetos duplicados de um iterável

# como criar um conjunto
carros = {"gol", "celta", "palio"}
a = set([1, 2, 3, 4, 3, 5])
print(a)

frutas = set("abacaxi") # também é possível guardar strings
print(frutas) 

# note que a cada execução o print(frutas) vai mostrar os valores em posições aleatórias sempre, isso é uma caracteristica do SET


# Passando uma tupla para o conjunto
cursos_tupla = ("kotlin", "java", "c", "python", "c", "c") # tupla
cursos_conjunto = set(cursos_tupla)

print(cursos_tupla) # ('kotlin', 'java', 'c', 'python', 'c', 'c')
print(cursos_conjunto) # {'c', 'python', 'kotlin', 'java'} || toda execução muda a ordem dos elementos

# para acessar os dados é necessário converter o conjunto (set) para uma lista (list)
cursos_lista = list(cursos_conjunto)

print(cursos_lista[0])  # acessando o elemento guardado no índice 0


# usando for para percorrer os dados da TUPLA
print()
for carro in carros:
    print(carro)

print()
# usando o enumerate para passar o indice/enumerar os itens
for indice, carro in  enumerate(carros):
    print(f"{indice}: {carro}")
    
    
# Métodos 

# Union
