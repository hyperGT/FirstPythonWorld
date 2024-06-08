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

#  # Operações entre conjuntos  
# 
#  #  # Union
conjunto_a = {1, 3}
conjunto_b = {2, 4}

print(conjunto_a.union(conjunto_b)) # {1, 2, 3, 4}


# 
#  #  # Intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b)) # {2, 3}


# 
#  #  # difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b)) # retornando elementos que estão em A mas não em B: 1 
print(conjunto_b.difference(conjunto_a)) # retornando elementos que estão em B mas não em A: 4

# 
#  #  # symmetric difference
print(conjunto_a.symmetric_difference(conjunto_b)) # retornando um novo conjunto com a diferença simétrica de dois conjuntos, isto é, elementos que estão em a mas não em b e vice e versa.

print()

# 
#  #  # issubset (está contido)
conjunto_a = {1, 2, 3}
conjunto_b = {2, 1, 3, 6, 4, 5}

print("está contido\n")
print(conjunto_a.issubset(conjunto_b)) # Retorna Verdadeiro se o conjunto a for estiver contido em b e falso caso contrário
print(conjunto_b.issubset(conjunto_a)) # conjunto b não está contido em a


# 
#  #  # issuperset (contém)
#  # (é o contrário do anterior, ou seja, verifica se um é o "super" conjunto do outro)
print("contém\n")
print(conjunto_a.issuperset(conjunto_b)) # conjunto a contém b? True:False (nesse caso é falso)
print(conjunto_b.issuperset(conjunto_a)) # True


# 
#  #  # isdisjoint  (disjunto)
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 9, 8}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b)) # a e b são disjuntos pois não existe nenhum número em comum entre eles
print(conjunto_a.isdisjoint(conjunto_c)) # vai retornar True pois existe elementos em comum (existe intersecção entre ambos os conjuntos)



# método Add: serve pra adicionar um novo elemento ao conjunto
valores = {10, 22}
print(valores) # {10, 22}
print()
valores.add(30)
print(valores) # {10, 22, 30}
print()

# OBS: se um elemento novo adicionado porém já existir dentro do conjunto, ele simplesmente será ignorado, isso porque conjuntos não guardam valores igual dentro.
valores.add(22) # {10, 22, 30}
print(valores)
print()

# método Clear: limpa todo o conjunto

valores.clear()
print(valores)
print()

# método Copy: copia os elementos de um conjunto em um outro, criando uma nova instância deste conjunto já existente.
valores = {1, 22, 13}
valores.copy()
print(valores)
print()

# método Discard: Passamos um valor existente dentro do conjunto como parâmetro para descartá-lo, removê-lo desse conjunto.

valores.discard(13)
print(valores)
print()

# método Pop: Remove o primeiro elemento da lista e assim por diante
numeros = {1, 2, 3, 4, 5}
numeros.pop() # elimina o elemento 17 (último elemento)
print(numeros)
print()

# método Remove: Remove o valor passado como parâmetro, porém, diferente do discard, se esse elemento não existir, ele retorna um erro na execução

numeros.remove(2) # {1, 3, 4, 5}
print(numeros) 
print()

# numeros.remove(7) # retorna um erro

# método Len: retorna o tamanho do conjunto
print(len(numeros))


# In: Retorna true se o valor existir e false caso contrário
print(numeros)
valor = 3
print(valor in numeros)