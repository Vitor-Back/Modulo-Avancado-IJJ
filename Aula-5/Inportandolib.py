import requests

cep = input('Informe um CEP: ') 
response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

data = response.json()

print(f':\n', 'Localidade:', data['localidade'], data['cep'], data['logradouro'])

