def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao_somar):
    resultado = funcao_somar(a, b)
    print(f"O resultado da operação de {a} + {b} é: {resultado}")


# Passe dois valores inteiros 
exibir_resultado(15, 10, somar)