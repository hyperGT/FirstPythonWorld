# Entrar no modo interativo: python -i nome_arquivo.py


# printar coisas na tela

print("Hello world")

# inicializando variaveis
idade = 18 # ele automaticamente já reconhece o tipo de dado adicionado

# input e output
print("============Entrada e saída de dados===========")
nome = input('Informe seu nome: ') # string
idade = int(input('Informe sua idade: '))

# formatação de saida
print(f'Ola {nome}, seja bem-vindo.')
# ou 
print("Ola " + nome + ", como vai?") # concatenando strings, como a var nome tbm é uma string, nao vai dar conflito


print("Você possui", idade,"anos, confirma?") # sem concatenar
print() # quebra linha
resp = int(input('[1 - sim/2 - nao]: '))

# estruturas de condição: if/else/elif

# preste atenção na identação
if resp == 1: # inicia bloco if
    resp = int(input('Ótimo! você pode abrir uma conta! deseja? [1 - sim/2 - nao]: '))
    if resp == 1: 
        print('Abrindo conta...')
    elif resp == 2: 
        print("Okay, prosseguindo sem uma conta")
    else:
        print('Comando inválido digitado')
elif resp == 2:
    print("Você não possui idade pra usar o app")
else:
    print('Comando inválido digitado')

# estruturas de repetição: for(com buit-in function e sem) e while


