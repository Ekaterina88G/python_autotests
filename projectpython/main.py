import requests

token = '580d251819ff04f74a4b8db20eb153a7'
url = 'https://api.pokemonbattle.me:9104'

response = requests.post (f'{url}/pokemons', json = {
    "name": "Подарок",
    "photo": "https://dolnikov.ru/pokemons/albums/021.png"
    }, headers = {'Content-Type': 'application/json',
                  'trainer_token': token})

print(response.text)
 
response = requests.put (f'{url}/pokemons', json = {
    "pokemon_id": "6296",
    "name": "New Gift",
    "photo": "https://dolnikov.ru/pokemons/albums/035.png"
}, headers = {'Content-Type': 'application/json',
                  'trainer_token': token})
print(response.text)

response = requests.post(f'{url}/trainers/add_pokemonball', json = {
    "pokemon_id": "6338"
}, hesders = {'Content-Type': 'application/json',
                  'trainer_token': token})
print(response.text)
