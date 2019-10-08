" This is a test module for backend "
from django.test import Client
import pytest, json

@pytest.mark.django_db
def test_register():
    ''' Test for 'register/' '''
    client = Client()
    response = client.get('/register/')
    assert response.status_code == 400
    response = client.post('/register/', {'username': 'yangyaru', 'password': 'la123456', 'nickname':'杨雅儒', 'email':'315629555@qq.com'})
    assert response.status_code == 200
    response = client.post('/register/', {'username': 'yangyaru', 'password': 'lla123456', 'nickname':'杨雅儒2', 'email':'3156295552@qq.com'})
    assert response.status_code == 400
    response = client.post('/login/', {'username': 'yangyaru', 'password': 'la123456'})
    assert json.loads(response.content).get('message') == 'The user has not been validated.'
    assert response.status_code == 400
    response = client.post('/login/', {'username': 'yangyaru', 'password': 'lla123456'})
    assert response.status_code == 400
