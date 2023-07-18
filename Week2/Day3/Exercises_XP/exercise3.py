brand = {}

#2.
brand['name'] = 'Zara'
brand['creation_date'] = 1975
brand['creator_name'] = 'Amancio Ortega Gaona'
brand['type_of_clothes'] = ['men', 'women', 'children', 'home']
brand['international_competitors'] = ['Gap', 'H&M', 'Benetton']
brand['number_stores'] = 7000
brand['major_color'] = dict(zip(['France', 'Spain', 'USA'], ['blue', 'red', ['pink', 'green']]))

for key, value in brand.items():
    print(f"{key}: {value}")

#3.
brand['number_stores'] = 2

#4.
type_of_clothes = 's, '.join(brand['type_of_clothes'])
print(f"Zara's clients are {type_of_clothes}")

#5.
brand['country_creation'] = 'Spain'

#6.
brand.setdefault('international_competitors', []).append('Desigual')

#7. Delete the information about the date of creation
del brand['creation_date']

#8. Print the last international competitor.
print(brand.get('international_competitors')[-1])

#9.
print('Major clothes colors in the US:',', '.join(brand.get('major_color').get('USA')))

#10.
print('Length of the dictionary:', len(brand))

#11
print(brand.keys())

#12
more_on_zara = {'creation_date': 1975, 'number_stores': 10000}

#13
brand.update(more_on_zara)
print(brand)

#14
#after update the value from the source dictionary will overwrite the value in the target dictionary
print(brand.get('number_stores')) 