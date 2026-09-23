import pytest
import requests
import random

base_url = 'https://petstore.swagger.io/v2'
pet_id = random.randint(1, 300)

#response = requests.get(base_url)
#print(f'ОТВЕТ ОТ СЕРВЕРА - {response.status_code}')

@pytest.fixture(scope='module')
def pet_payload():

    return {
            "id": pet_id,
            "category": {
            "id": 0,
            "name": f"Pet with ID {pet_id}"
            },
            "name": "DOG",
            "photoUrls": [
            "string"
            ],
            "tags": [
            {
            "id": 0,
            "name": "string"
            }
            ],
            "status": "available"
            }

def test_post_pet(pet_payload):
    #POST/pet
    post_response = requests.post(f'{base_url}/pet', json=pet_payload)
    assert post_response.status_code == 200, 'Ошибка создания питомца'
    assert post_response.json()['id'] == pet_payload['id']
    assert post_response.json()['name'] == pet_payload['name']

def test_update_pet(pet_payload):
    #PUT/pet
    update_payload = pet_payload.copy()
    update_payload['name'] == 'FOX'
    update_payload['status'] == 'sold'

    update_response = requests.put(f'{base_url}/pet', json = update_payload)
    assert update_response.status_code == 200, 'Ошибка при изменении данных питомца'
    assert update_response.json()['name'] == update_payload['name']
    assert update_response.json()['status'] == update_payload['status']

def test_get_pet_by_id(pet_payload):
    #GET/pet/{petid}
    get_response = requests.get(f'{base_url}/pet/{pet_id}')
    assert get_response.status_code == 200, f'Питомец с ID {pet_id} не найден'
    assert get_response.json()['id'] == pet_payload["id"]

@pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
#GET/pet/findBYStatus
def test_get_pet_by_status(status):
    get_response = requests.get(f'{base_url}/pet/findByStatus', params={'status': status})
    assert get_response.status_code == 200
    assert isinstance(get_response.json(), list)
    if len(get_response.json()) > 0:
        for pet in get_response.json():
            assert pet['status'] == status


def test_delete_pet(pet_payload):
    #DELETE/pet
    del_response = requests.delete(f'{base_url}/pet/{pet_payload['id']}')
    assert del_response.status_code == 200, 'Ошибка при удалении питомца'

def test_check_delete_pet(pet_payload):
    check_response = requests.get(f'{base_url}/pet/{pet_payload['id']}')
    assert check_response.status_code == 404



