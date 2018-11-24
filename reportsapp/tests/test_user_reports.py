"""
This file (test_users.py) contains the functional tests for the users blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the users blueprint.
"""
import json
from utils.random_hex import key_gen

mimetype = 'application/json'
headers = {
    'Content-Type': mimetype,
    'Accept': mimetype
}

random_user_data = {'username': 'pardus{}'.format(key_gen())}
print('USER ',random_user_data)


def test_create_user(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.post('/users/', data=json.dumps(random_user_data), headers=headers)
    assert response.status_code == 201


def test_create_report(test_client):
    data = [{
            "username": random_user_data.get('username'),
            "disease": "BS",
            "machine": "BS_CHECK_MMK",
            "taken_by": "ayush",
            "created_at": "2016-05-18T16:00:00Z"
            },
            {
            "username": random_user_data.get('username'),
            "disease": "BP",
            "machine": "BP_PRESSURE_CHECK_MMK",
            "taken_by": "ayush",
            "created_at": "2016-06-18T16:00:00Z"
            }
            ]
    response = test_client.post('/reports/', data=json.dumps(data), headers=headers)
    assert 'report_ids' in json.loads(response.data).keys()
    assert response.status_code == 201


def test_user(test_client):
    response = test_client.get('/users/{}/'.format(random_user_data))
    assert response.status_code == 200


def test_reports(test_client):
    response = test_client.get('/reports/')
    assert response.status_code == 200


def test_users_reports(test_client):
    response = test_client.get('users/{}/reports/'.format(random_user_data.get('username')))
    assert response.status_code == 200
