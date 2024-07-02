


def par_ou_impar(matricula: int, lista: int ) -> int:
    resto = matricula % 2

    for posicao in lista:
     if posicao > 4:
          print("O numero informado possui mais que 5 numeros, informe uma amtricula de 5 numeros")
     if posicao < 4:
         print("O numero informado possui menos que 5 numeros, informe uma amtricula de 5 numeros")
    
    if resto == 0:
         print("VOCÊ ESTA NO TIME DOS MENINES")
    else: 
         print("VOCÊ É DO TIME DAS MENINES")

matricula = int(input('informe a matricula: '))
lista = [matricula]


par_ou_impar(matricula)