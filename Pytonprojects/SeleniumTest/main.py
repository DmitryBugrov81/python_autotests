import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'bab92d11ecb955bf50b1e3783accdd94'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}


'''body_create = {
    
    "name": "pipa",
    "photo_id": 7
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''body_putname =  {

    "pokemon_id": "122856",
    "name": "New Name",
    "photo_id": 33
}
response_putname = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_putname)
print(response_putname.text)'''

body_addpokeball = {

    "pokemon_id": "122856"
}
response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_addpokeball)
print(response_addpokeball.text)

