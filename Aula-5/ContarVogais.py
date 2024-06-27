palavra = input("Informe uma palavra:")
vogais = 'aeiou'
contador = 0
for i in palavra:

    if i in vogais:
        contador += 1
print(f"A {type(vogais)}{palavra} tem {contador} vogais")        
