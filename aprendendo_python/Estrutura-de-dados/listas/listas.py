
# lista com valores inteiros
num_lists = [1, 3, 5, 7]

# declarando uma lista vazia
void_list = []

# variável do tipo lista que vai guardar uma string convertida em um vetor de caracteres
letras = list("python")

# guardando valores num range aleatório de 0 a 10 em uma lista
numeros = list(range(10))

# uma lista pode guardar dentro de si vários valores de diversos tipos distintos entre si
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

print()
print(carro)
print(letras)
print(numeros)
print(num_lists)

# exemplo de formas de acesso às informações dentro das listas:

# acesso direto

frutas = ["Maçã", "Laranja", "Uva", "Manga"]
print(frutas[-1]) # Independente do tamanho, vai pegar o último item da lista
print(frutas[0]) # O índice sempre começa em 0, logo o primeiro item guardado será retornado
print(frutas[1]) # laranja // o índice positivo conta e busca tradicionalmente o valor dentro da lista
print(frutas[-3]) # laranja // o índice negativo conta do último valor da lista para o primeiro.


# fatiamento 
print()
curso = list("python")

print(curso[2:])
print(curso[:2])
print(curso[1:3])
print(curso[0:3:2])
print(curso[::])
print(curso[::-1])
print()

# lista: Matriz de listas/ listas aninhadas

# como declarar uma matriz de listas
matriz = [
    ["João", "Maria", "Pedro",],
    [7, 10, 6,],
    [8, 10, 5,], 
    [True, True, False]    
]

# como chamar e retornar as posições
print(f"Nome: {matriz[0][0]}")
print(f"Nota Av1: {matriz[1][0]}")
print(f"Nota Av2: {matriz[-2][0]}")
print(f"Aprovado?: {matriz[-1][0]}")

# utilizando o fatiamento
print(f"Todos os alunos: {matriz[0][::]}")
print(f"Notas de Av1: {matriz[1][::]}")
print(f"Notas de Av2: {matriz[2][::]}")
print(f"Aprovações: {matriz[-1][::]}")


# usando for para percorrer os dados da lista
print()
for aluno in matriz[0][::]:
    print()
    print(aluno)

# usando o enumerate para passar o indice/enumerar os itens
for indice, aluno in  enumerate(matriz[0][::]):
    print(f"{indice}: {aluno}")


# list comprehension: Contando a quantidade de numeros pares de 0 a 100 e guardando esses valores em uma nova lista
numeros = list(range(100))
pares = []
qnt_pares = 0

# filtrando valores
for numero in numeros:
    if numero % 2 == 0:
        qnt_pares+=1
        pares.append(numero)
        
print(pares)
print()
print(qnt_pares)

# muito mais confuso, porém funciona
pares2 = [numero for numero in numeros if numero % 2 == 0]

print()
print(pares)

# segundo exemplo: todos os valores ao quadrado
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
    
print()
print(quadrado)

# ou

quadrado2 = [numero ** 2 for numero in numeros]

print("XXX")
print(quadrado)


# Métodos

# Append para armazenar um novo valor no FINAL da lista
nomes = ["Jotapê", "Victor"]

print()
print(nomes)
print("Matriculando aluno...")

print()
nomes.append("Luan Santana")
print(nomes)

print()
print("Lista de matrícula atualizada")


# Novo metodo: limpar()

print("Turma 008 se formou, nova turma vai entrar...")
print()
nomes.clear()

print(nomes)

# New Method: Copy

lista_alunos = ["Jotapê", "Victor", "Luana"]

lista_alunos_intercambio = lista_alunos.copy() # copiando a lista original e retornando uma instância dela

print(lista_alunos_intercambio)
print()
print("Matriculando alunos de intercâmbio...")
lista_alunos_intercambio.append("Andrew Snows")
print()
print(lista_alunos_intercambio)

print(f"Lista de alunos nativos: {lista_alunos}")
print()
print(id(lista_alunos_intercambio), id(lista_alunos)) # retornando o endereço de memória(que identifica uma variável) de cada lista || ferramenta CPython 


# Nuevo método: Extensor()

turma_001 = lista_alunos_intercambio
turma_002 = ["Fernando", "Alvarez", "Diego Torres"]
turma_mandarim = []

print("Ambas turmas vão precisar fazer uma disciplina extra, preciso juntá-las à turma desta disciplina...")
print(turma_001)
print(turma_002)
print(turma_mandarim)

turma_mandarim.extend(turma_001) # esse método só aceita uma lista como argumento de vez
turma_mandarim.extend(turma_002) # por isso para juntar ambas deve-se fazer isso com uma de cada vez

print()
print(turma_mandarim)


# Neue Methode: index()
linguagens = ["kotlin", "java", "c", "python"]

# Esse método retorna o índice no qual está o objeto referenciado
print(linguagens.index("kotlin"))
print(linguagens.index("java"))

# e se não existir o objeto?
# print(linguagens.index("csharp")) # ele retorna um erro pois não existe

linguagens.append("java")
print(linguagens) # ["kotlin", "java", "c", "python", "java"]
print(linguagens.index("java")) # é possível notar que ele retorna apenas o índice da primeira aparição do objeto 

print()

# Nouvelle méthode : pop()

# enquanto o método append acrescenta um novo objeto no FINAL/TOPO da lista, o método pop REMOVE o ÚLTIMO objeto da lista
print(linguagens) # ["kotlin", "java", "c", "python", "java"]
linguagens.pop()
print(linguagens) # ["kotlin", "java", "c", "python"]

print()

# segunda forma de utilizar o método pop: passando o índice do objeto a ser removido.
linguagens.pop(0) # vai remover "kotlin" o objeto que está no índice 0 da lista
print(linguagens) # ["java", "c", "python"]



# Nieuwe methode: verwijderen()
linguagens.append("c")
# o método remover serve para remover um elemento da lista, assim como o método pop, a única diferença é que a referência passada como parâmetro para remover o objeto não é o índice, e sim o próprio valor/string etc.

print(linguagens) # ["java", "c", "python", "c"]
linguagens.remove("c")
print(linguagens) # ["java", "python", "c"] aqui também é possível notar que apenas a primeira ocorrência de "c" foi removida, sendo assim, tome cuidado. 


# Método reverse()
linguagens.reverse() # basicamente reorganiza a lista para que fique ao contrário, último elemento primeiro etc.
print(linguagens) # ["c", "python", "java"]

print()


# Ny metode: sort()
linguagens.sort() # ordena a lista em ordem alfabética || ordenação padrão do método sort
print(linguagens) # ["c", "java", "python"]

linguagens.sort(reverse=True) 
print(linguagens) # ['python', 'java', 'c']

linguagens.sort(key=lambda x: len(x)) # ordena em ordem crescente, nesse caso vai pegar a menor string primeiro e vai colocar a maior por último
print(linguagens) # ['c', 'java', 'python']

linguagens.sort(key=lambda x: len(x), reverse=True) 
print(linguagens) # ['python', 'java', 'c']


print()
print()


# Método len()

# basicamente retorna o tamanho da lista
print(len(linguagens)) # tamanho da minha atual lista de linguagens: 3




# função SORTED = método SORT
lista_alunos_intercambio.sort()
print(lista_alunos_intercambio)
sorted(lista_alunos_intercambio, key=lambda x: len(x))
print(lista_alunos_intercambio)

sorted(lista_alunos_intercambio, key=lambda x: len(x), reverse=True)
print(lista_alunos_intercambio)
