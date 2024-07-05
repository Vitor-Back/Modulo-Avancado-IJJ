from faker import Faker 
import pandas as pd

faker = Faker('pt_BR')

def persona() -> dict:    
    dados = {
    "Nome": faker.name(),
    "Cidade": faker.city(),
    "Idade": faker.random_int(18, 100)
    }

    return dados

def gerar_qtd_personas(num_personas: int) -> list:
    return [persona() for _ in range(num_personas)]



lista_personas = gerar_qtd_personas(20)


def criando_df(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data)
    return df

df_lista_personas = criando_df(lista_personas)

print(df_lista_personas)

def salvar_csv(nomearquivo: str, dataframe: pd.DataFrame) -> None:
    dataframe.to_csv(nomearquivo, index=False)

df_lista_personas.to_csv('lista_de_personas.csv', index=False)

salvar_csv(nomearquivo='lista_de_personas.csv', dataframe=df_lista_personas)

