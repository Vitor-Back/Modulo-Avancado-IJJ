import pandas as pd

dados = {
    "Nome": ["Valter", "Valéria", "Vanessa", "Vitor", "Vinicius", "Jeferson", "Zulmira"],
    'Idade': [12, 18, 24, 15, 36, 42, 102],
    'Cidade': ["Recife", "Recife", "Recife", "Salvador", "Salvador", "São Paulo", "Manaus",]

}

df = pd.DataFrame(data=dados)
 

print(df[df['Cidade'] == 'Recife'])
