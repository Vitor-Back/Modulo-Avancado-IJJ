frutas = ['Abacaxi', 'Pera', 'Pessego', 'Uva', 'Limão', 'Goiaba', 'Maçã', 'Melancia', 'Cacau', 'Pitaia',]
alergicos = ['Pitaia', 'Cacau', 'Pessego', 'Pera']

for frutas in frutas:
    if frutas in alergicos:
        print(frutas)