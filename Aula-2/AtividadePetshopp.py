nomeCachorro = input("Informe o nome do cachorro:")
idadeAnimal= int(input("Idade do animal:"))
porteCachorro=input("Informe o porte do cachorro('Grande', 'Médio', 'Pequeno'):").lower()
totalAnual=0
portes=['grande', 'médio', 'pequeno']

if porteCachorro in portes:

    totalBanho=int (input("Informe o total de banhos até agora:"))
    custoGrande= 20
    custoMedio=15
    custoPequeno=3
    valorBanhoGrande=75
    valorBanhoMedio=60
    valorBanhoPequeno=50

    idadeDeCachorro = idadeAnimal * 7

    if porteCachorro == "grande":
        totalAnual = (valorBanhoGrande * totalBanho) - (custoGrande  * totalBanho)

    elif porteCachorro == "médio":
        totalAnual = (valorBanhoMedio * totalBanho) - (custoMedio  * totalBanho)

    elif porteCachorro == "pequeno":
        totalAnual = (valorBanhoPequeno * totalBanho) - (custoPequeno  * totalBanho)
     
 
    print(f"Olá, {nomeCachorro} tem {idadeDeCachorro} anos e nos últimos 12 meses o lucro com este animal foi de {totalAnual}")
else:
    print("Porte não existente!")
