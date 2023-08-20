import requests
import pytest




token = '580d251819ff04f74a4b8db20eb153a7'
url = 'https://api.pokemonbattle.me:9104'


def test_status_code():
    response = requests.get(f'{url}/trainers', params = {'trainer_id' : 1252}, headers = {'Content-Type': 'application/json',
                  'trainer_token': token} )
    assert response.status_code == 200
   