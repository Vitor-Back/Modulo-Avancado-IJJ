valorDacompra = float(input("Informe o valor da compra para obter desconto:"))

if valorDacompra > 500:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")
    valordesconto = valorDacompra - (valorDacompra * 0.30) 
    print(f"O valor da sua compra é: R${valordesconto:.2f}")
elif valorDacompra >= 250:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
    valordesconto = valorDacompra - (valorDacompra * 0.10) 
    print(f"O valor da sua compra é: R${valordesconto:.2f}")
else:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA.")

