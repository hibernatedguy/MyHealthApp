import json
import base64
from .generate_hex import key_gen

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

random_user_data = {'username': 'pardus{}'.format(key_gen()), 'password': 'password'}


def test_registration_api(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.post('/registration/', data=json.dumps(random_user_data), headers=headers)
    assert response.status_code == 201


def test_login_api(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    username = random_user_data.get('username')
    password = random_user_data.get('password')
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(bytes(username + ":" + password, 'ascii')).decode('ascii')
    }
    response = test_client.get('/login/', headers=headers)
    assert 'token' in json.loads(response.data).keys()
    assert response.status_code == 200


def test_create_report_api(test_client):

    username = random_user_data.get('username')
    password = random_user_data.get('password')
    headers = {
        'Authorization': 'Basic ' + base64.b64encode(bytes(username + ":" + password, 'ascii')).decode('ascii')
    }
    response = test_client.get('/login/', headers=headers)
    token = json.loads(response.data).get('token')

    data = [{
        "checkup_type": "BLOOD PRESSURE",
        "checkup_report": "ALL FINE. 20.90",
        "checkup_for": random_user_data.get('username'),
        "machine": "BP PRESSURE CHECK MACH",
        "taken_by": "Ayush",
        "disease": "BP"
    }, {
        "checkup_type": "BLOOD PRESSURE",
        "checkup_report": "ALL FINE. 20.90",
        "checkup_for": random_user_data.get('username'),
        "machine": "BP PRESSURE CHECK MACH",
        "taken_by": "Ayush",
        "disease": "BP"
    }, {
        "checkup_type": "BLOOD PRESSURE",
        "checkup_report": "ALL FINE. 20.90",
        "checkup_for": random_user_data.get('username'),
        "machine": "BP PRESSURE CHECK MACH",
        "taken_by": "Ayush",
        "disease": "BP"
    }
    ]

    request_headers = {
        'Content-Type': mimetype,
        'x-access-token': token
    }
    response = test_client.post('/users/{}/checkups/'.format(random_user_data.get('username')),
                                data=json.dumps(data), headers=request_headers)
    print(response)
    assert 'User checkup created' in json.loads(response.data).get('details')
    assert response.status_code == 201
