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