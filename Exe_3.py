import random

NAMES = ['Alvaro', 'Roberto', 'Tom', 'Maverick', 'Heylin', 'Giselle', 'Rogleio', 'Josue', 'Jeymi', 'Alondra', 'Maria', 'Bryhanci']
CITYS = ['Raccoon_City', 'Umbrella', 'Nicaragua', 'U_S_A', 'Silent_Hill', 'San_Andreas', 'Madrid']

def get_diccionary_student():
	students = {}

	for nombre in NAMES:
		students = {
		'Edad': random.randrange(16,30),
		'Anho': random.randrange(1,5),
		'Ciudad': random.choice(CITYS)
		}

		return students


didy={'diccionario': get_diccionary_student()}
print(didy)	
for i in didy:
	print(didy[i])
