import json
from utils.random_hex import key_gen

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

random_user_data = {'username': 'pardus{}'.format(key_gen())}


def test_create_user(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.post('/users/', data=json.dumps(random_user_data), headers=headers)
    assert response.status_code == 201

def test_login(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.post('/login/', data=json.dumps(random_user_data), headers=headers)
    assert response.status_code == 201



def test_create_report(test_client):
    data = [{
        "checkup_type": "BLOOD PRESSURE",
        "checkup_report": "ALL FINE. 20.90",
        "checkup_for": "bholanath",
        "machine": "BP PRESSURE CHECK MACH",
        "taken_by": "Ayush",
        "disease": "BP"
    }, {
        "checkup_type": "BLOOD PRESSURE",
        "checkup_report": "ALL FINE. 20.90",
        "checkup_for": "bholanath",
        "machine": "BP PRESSURE CHECK MACH",
        "taken_by": "Ayush",
        "disease": "BP"
    }, {
        "checkup_type": "BLOOD PRESSURE",
        "checkup_report": "ALL FINE. 20.90",
        "checkup_for": "bholanath",
        "machine": "BP PRESSURE CHECK MACH",
        "taken_by": "Ayush",
        "disease": "BP"
    }
    ]
    response = test_client.post('/users/{}/checkups/'.format(random_user_data.get('username')),
                                data=json.dumps(data), headers=headers)
    assert 'User checkup created' in response.json().get('details')
    assert response.status_code == 201

# TODO : API TESTING AND UNIT TEST


# def test_user(test_client):
#     response = test_client.get('/users/{}/'.format(random_user_data))
#     assert response.status_code == 200


# def test_reports(test_client):
#     response = test_client.get('/reports/')
#     assert response.status_code == 200


# def test_users_reports(test_client):
#     response = test_client.get('users/{}/reports/'.format(random_user_data.get('username')))
#     assert response.status_code == 200
