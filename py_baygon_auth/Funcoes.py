import requests
from faker import Faker

faker = Faker('pt_BR')

def dados_cadastro() -> dict: 
    data= {
   "username": faker.user_name(),
    "email": faker.email(),
    "password": faker.password(digits=8 ) ,
    "phone": faker.phone_number(),
    "address": faker.address(),
    "cpf": faker.cpf()  
    }
    return data

def cadastra(dados):
    response = requests.post(f'https://desafiopython.jogajuntoinstituto.org/api/users/', json=dados)
    return response


def login(dados):
    responser = requests.post(f'http://desafiopython.jogajuntoinstituto.org/api/users/login/', json=dados)
    return responser

def status(resp):
    
    return resp.json, resp.text

def main():
    dados = dados_cadastro()

    print("Dados enviados:", dados)

    print(status(cadastra(dados)))
    
    print(status(login(dados)))

    
   
if __name__ == "__main__": 

    main()

