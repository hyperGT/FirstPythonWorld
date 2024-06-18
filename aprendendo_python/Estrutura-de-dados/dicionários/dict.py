# dicionários 

# Criação/Declaração: sempre guarda uma chave e um valor atrelado (guarda vários)
dados = {"nome": "Gabriel", "idade": 19} # cria um dicionário de forma direta

dados = dict(nome="Gabriel", idade=19) # utilizando o construtor dict (o resultado é o mesmo do de cima)
print(dados)
print()

dados["telefone"] = "3333-1234" # adiciona um elemento a um dicionario existente
print(dados)


# exemplo de dicionários aninhados
contatos = {
    "guilherme@gmail.com": {"nome": "Guilerme", "telefone": "2222-2313"},
    "andrewsnows111@gmail.com": {"nome": "Andrew", "telefone": "2222-3234"},
    "bishopclaude966@gmail.com": {"nome": "Claude", "telefone": "2222-8989"},    
    "massilovski0101@gmail.com": {"nome": "Paul", "telefone": "2222-0101"}
}

print(contatos["massilovski0101@gmail.com"]["telefone"])


# Iterar dicionários (mostrando a melhor forma)
for key, value in contatos.items():
    print(key, value)


# método Clear: limpa todo o conteúdo do dicionário

dados_contatos = dict(nome="Gabriel", idade="19", cargo="Desenvolvedor De Software Júnior")
print(dados_contatos)
print()
dados_contatos.clear() # limpando o dicionário dic
print(dados_contatos)
print()


# método Copy

dados_contatos = {"gabrielch@gmail": {"nome":"Gabriel", "telefone": "2222-1234"}}

backup_dados_pessoais = dados_contatos.copy()
print(dados_contatos)
print()
#dic.clear()
#print(dic)
#print()
print(backup_dados_pessoais)


# método fromkeys: serve para criar chaves
dados_pessoais = {}

dados_pessoais = dict.fromkeys(["nome", "telefone"]) # {"nome": none, "telefone": none}

print(dados_pessoais)

# atribuindo um valor ás chaves
dados_pessoais = dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}

print(dados_pessoais)



# método get: obter retorno de algum dado do dicionário caso ele exista

# cuidado: a forma tradicional pode acusar erro caso a chave não existe e interromper a execução

dados_contatos = {"gabrielch@gmail": {"nome":"Gabriel", "telefone": "2222-3456"}}

# método tradicional: deve-se tomar cuidado, pois se a chave não existir ou for digitada errado, o programa dará erro.
# print(dados_contatos["cargo"]) # keyerror (a chave não existe)

# get
print()
resp = dados_contatos.get("nome")
print(resp) # None

# nota: esse {} depois de uma virgula serve como retorno default. Caso não seja encontrada a chave em questão, é retornado esse "{}" no cmd
resp = dados_contatos.get("nome", {})
print(resp) # {}

resp = dados_contatos.get("gabrielch@gmail", {})
print(resp) # {'nome': 'Gabriel', 'telefone': '2222-3456'}


# método item: retorna tudo dentro do dicionário (chaves + valores)

resp = dados_contatos.items()
print(resp)

# método keys: retorna somente as chaves existentes do dicionário 

resp = dados_contatos.keys()
print(resp)


# método pop: remove uma chave no dicionário e retorna o valor removido

resp = dados_contatos.pop("gabrielch@gmail", {}) # esse {} é o retorno default caso não encontre a chave
print()
print(resp) # {'nome': 'Gabriel', 'telefone': '2222-3456'} (chave encontrada e removida, retornando o valor...)

resp = dados_contatos.pop("gabrielch@gmail", {}) 

print() 
print(resp) # {} (chave já removida)


# método *popitem*: não precisa informar chave, ele remove os valores em sequencia

contatos = {
    "guilherme@gmail.com": {"nome": "Guilerme", "telefone": "2222-2313"},
    "andrewsnows111@gmail.com": {"nome": "Andrew", "telefone": "2222-3234"},
    "bishopclaude966@gmail.com": {"nome": "Claude", "telefone": "2222-8989"},    
    "massilovski0101@gmail.com": {"nome": "Paul", "telefone": "2222-0101"}
}

print()
i=1
for key, value in contatos.items():
    print(i, key, value)
    i+=1

resp = contatos.popitem()

print(resp) # ('massilovski0101@gmail.com', {'nome': 'Paul', 'telefone': '2222-0101'})  (retorna o item removido)
print()

i=1
for key, value in contatos.items():
    print(i, key, value) 
    i+=1


# método setdefault: cria uma chave e atribui um valor como default, porém, se a chave já existir e tiver valor dentro, não alterará nada

dados_contatos = {"nome":"Gabriel", "telefone": "2222-3456"}

print()
resp = dados_contatos.setdefault("nome", "Giovanna")
print(resp) # Gabriel (não mudou nada pois já existe)

resp = dados_contatos.setdefault("idade", 19)

print(resp)


# método update: permite atualizar o dicionário (com outro dicionário inclusive)

dados_contatos.update({"gabrielch@gmail.com": {"nome":"Gabriel", "telefone": "2222-3456"}})

print(dados_contatos) # {'nome': 'Gabriel', 'telefone': '2222-3456', 'idade': 19, 'gabrielch@gmail.com': {'nome': 'Gabriel', 'telefone': '2222-3456'}}


dados_contatos = {"gabrielch@gmail.com": {"nome":"Gabriel", "telefone": "2222-3456"}}
dados_contatos.update({"gabrielch@gmail.com":{"nome":"Gabriel", "idade":19}}) # atualiza a chave

print(dados_contatos)


# método values: retorna apenas os VALORES das chaves existentes no dicionário

dados_contatos = {"gabrielch@gmail.com": {"nome":"Gabriel", "telefone": "2222-3456"}}
print(dados_contatos.values()) # dict_values([{'nome': 'Gabriel', 'idade': 19}]) (nesse caso o valor é um dicionário)

dados_contatos = {"nome": "Luana", "idade": 28}
print(dados_contatos.values()) # dict_values(['Luana', 28])


# método in: retorna verdadeiro ou falso para a verificação da existência de uma chave dentro de um dicionário

contatos = {
    "guilherme@gmail.com": {"nome": "Guilerme", "telefone": "2222-2313"},
    "andrewsnows111@gmail.com": {"nome": "Andrew", "telefone": "2222-3234"},
    "bishopclaude966@gmail.com": {"nome": "Claude", "telefone": "2222-8989"},    
    "massilovski0101@gmail.com": {"nome": "Paul", "telefone": "2222-0101"}
}

print()
exist = "guilherme@gmail.com" in contatos
print(exist) # True

print()
exist = "nome" in contatos["andrewsnows111@gmail.com"]
print(exist) # True

print()
exist = "idade" in contatos["massilovski0101@gmail.com"]
print(exist) # False (dinossauros possuem email?) 


# método del: remove um item do dicionário

contatos = {
    "guilherme@gmail.com": {"nome": "Guilerme", "telefone": "2222-2313"},
    "andrewsnows111@gmail.com": {"nome": "Andrew", "telefone": "2222-3234"},
    "bishopclaude966@gmail.com": {"nome": "Claude", "telefone": "2222-8989"},    
    "massilovski0101@gmail.com": {"nome": "Paul", "telefone": "2222-0101"}
}

del contatos["guilherme@gmail.com"]
print(contatos) # {'nome': 'Andrew', 'telefone': '2222-3234'}, 'bishopclaude966@gmail.com': {'nome': 'Claude', 'telefone': '2222-8989'}, 'massilovski0101@gmail.com': {'nome': 'Paul', 'telefone': '2222-0101'}}

del contatos["bishopclaude966@gmail.com"]["telefone"]
print(contatos) # {'andrewsnows111@gmail.com': {'nome': 'Andrew', 'telefone': '2222-3234'}, 'bishopclaude966@gmail.com': {'nome': 'Claude'}, 'massilovski0101@gmail.com': {'nome': 'Paul', 'telefone': '2222-0101'}}

del contatos # apaga o dicionário todo
print(contatos)