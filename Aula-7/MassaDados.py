import pandas as pd

dados = {
"Nome": ["João", "Matheus", "Michele", "Carlos", "Pedro"],
"Idade": [12,23,15,20,36]


}

df = pd.DataFrame(data=dados)

print(df)