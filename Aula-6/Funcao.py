
def primeiraFuncao(nome):
    print(f"Olá, {nome} Essa é uam função!")

#Boa pratica apra melhor entendimento da Função{ 
def soma(a: int, b:int) -> int:
    resultado = a + b

    return resultado
#}
primeiraFuncao('Vitor')

resultado = soma(1,0)

if resultado >= 10:
    print(f"deu {resultado}")

else:
    print(f'deus mas ta {resultado}')