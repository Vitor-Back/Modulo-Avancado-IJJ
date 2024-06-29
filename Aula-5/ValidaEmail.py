print(f"\033[1m###################################\nOlá, Bem-vindo ao contador de e-mail BAYGON QUALITY \n###################################\033[0m")
print("-------------------------------")

ijj = "@jogajuntoinstituto.org"
qtdEmail = 0
email = input("Digite o e-mail ou 'sair': ").lower()

for dominio in email:
    if dominio in ijj:
        qtdEmail += 1
        