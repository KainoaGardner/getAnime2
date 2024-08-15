import requests
from app import APIBASE


def check_response(response):
    if not response.ok:
        raise ValueError(response.json())
    return response


def get_auth_token(username, password):
    data = {"username": username, "password": password}
    response = requests.post(APIBASE + "/auth/token", data=data)
    return check_response(response)


def get_current_user(token):
    headersAuth = {"Authorization": "Bearer " + token}
    response = requests.get(APIBASE + f"/users/current", headers=headersAuth)
    return check_response(response)
