import requests, psycopg2
from random import choices
from connection import manage_connection
from IPython.display import display, Image

def create_table():
    response = requests.get('https://restcountries.com/v3.1/all')
    if response.status_code == 200:
        countries_data = response.json()
        countries_data = choices(countries_data, k=10)

    query = f'''
    create table countries(
    id serial primary key,
    	name varchar(100),
    	capital varchar(100),
    	flag varchar(5),
        flag_image varchar(100),
    	subregion varchar(100),
    	population int
    )
    '''

    manage_connection(query, 'create')    

    countries_info = [
        {
            'name': country['name']['official'],
            'capital': country['capital'][0] if country.get('capital') is not None else 'null',
            'flag': country['flag'],
            'flag_image': country['flags']['png'] if country['flags'] is not None else 'https://www.svgrepo.com/show/519862/trexrunner.svg',
            'subregion': country['subregion'] if country.get('subregion') is not None else 'null',
            'population': country['population']
        } for country in countries_data
    ]
    return countries_info

def random_10_countries(countries_info):
    query = f'''
    insert into countries(name, capital, flag, flag_image, subregion, population)
    values (%s,%s,%s,%s,%s,%s)
    '''

    for country in countries_info:
        # image_response = requests.get(country['flag_image'])
        # image_data = image_response.content
        
        values = (
            country['name'],
            country['capital'],
            country['flag'],
            # psycopg2.Binary(image_data),
            country['flag_image'],
            country['subregion'],
            country['population']
        ) 
        manage_connection(query, 'insert', values=values)                                  