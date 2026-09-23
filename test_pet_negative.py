import pytest
import requests
import random

base_url = 'https://petstore.swagger.io/v2'

#response = requests.get(base_url)
#print(f'ОТВЕТ ОТ СЕРВЕРА - {response.status_code}')
uncorrect_id = 'five'
uncorrect_name = 25

@pytest.fixture(scope='module')
def pet_payload():

    return {
            "id": uncorrect_id,
            "category": {
            "id": 0,
            "name": "Pet"
            },
            "name": uncorrect_name,
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

def test_post_pet_uncorrect_id_name(pet_payload):
    #POST/pet
    get_response = requests.get(f'{base_url}/pet', json = pet_payload)
    assert get_response.status_code == 405

def test_update_pet_uncorrect_id(pet_payload):
    #PUT/pet
    update_pet_payload = pet_payload.copy()
    update_pet_payload['id'] = 'one'
    update_pet_payload['name'] = 'Zhychka'

    update_response = requests.put(f'{base_url}/pet', json = update_pet_payload)
    assert update_response.status_code == 500


def test_get_pet_by_new_id(pet_payload):
    #PUT/pet
    update_pet_payload = pet_payload.copy()
    update_pet_payload['id'] = 92567027
    update_pet_payload['name'] = 'Zhychka'

    get_response = requests.get(f'{base_url}/pet', json = update_pet_payload)
    assert get_response.status_code == 405

def test_delete_pet(pet_payload):
    #DELETE/pet
    del_response = requests.delete(f'{base_url}/pet/{pet_payload['id']}')
    assert del_response.status_code == 404, 'Ошибка при удалении питомца'
