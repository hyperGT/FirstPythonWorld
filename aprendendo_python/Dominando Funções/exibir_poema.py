# treinando funções


# Alerta: *args = passar uma tupla  |  **kwargs = passar um dicionário

print()

# data_extenso = recebe data escrita por extenso, *args = recebe os versos, **kwargs = recebe os meta dados -> ex: autor: XXX, ano: XXX, livro: XXX
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args) # A cada verso pula uma linha 
    meta_dados = "\n".join([f"{chave.title()}:{valor}" for chave, valor in kwargs.items()]) # para cada meta dado escrito pula uma linha
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}" # formato do texto que será exibido
    print(mensagem) # exibindo os textos

# a primeira string é a data por extenso
# exibir_poema("O mar é lindo", "As estrelas também", autor="Teixeira-Gabriel", ano=2024)
exibir_poema("Terça-feira, 18 de Junho de 2024", "O mar é lindo", "As estrelas também", autor="Teixeira-Gabriel", ano=2024)