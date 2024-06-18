# Passagem de parametros por posição (apenas)

# até a '/', todos os parametros devem ser passados de acordo com as posições dadas das variáveis. 
def criar_carro_position_only(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_position_only("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gás e Gasolina") # válido

#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gás e Gasolina") # inválido


# Passagem somente por Palavras chaves

# não se usa barra, porém, deve-se colocar o '*' antes dos parametros a serem passados através das palavras chaves (nomes das variáveis)
def criar_carro_keyword_only(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_keyword_only(modelo="Siena", ano=2012, placa="AXC-5544", marca="Fiat", motor="1.4", combustivel="Flex") # válido

#criar_carro_position_only("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gás e Gasolina") # inválido


# Passagem somente por palavras chaves + posição

# até placa, todos os parametros serão passados por POSIÇÃO, e, a partir do '*', todos serão passados por NOME (plavra chave tanto faz)
def criar_carro_ambas(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_ambas("Grand Siena", 2012, "AZX-9988", marca="Fiat", motor="1.4 aspirado", combustivel="Flex") # válido

#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gás e Gasolina") # inválido