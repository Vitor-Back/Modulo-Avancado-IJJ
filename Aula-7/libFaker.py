from faker import Faker 
from random import Random
faker = Faker('pt_BR')

persona = {
    'Nome:': faker.name(),
    'Cidade': faker.city(),
    'Idade': faker.random_int(min=0, max=101)
}

print(persona)