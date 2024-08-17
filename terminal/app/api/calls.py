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


def get_current_user(headersAuth):
    response = requests.get(APIBASE + f"/users/current", headers=headersAuth)
    return check_response(response)


def get_user_settings(headersAuth):
    response = requests.get(APIBASE + f"/users/settings", headers=headersAuth)
    return check_response(response)


def put_user_settings(japanese_titles, headersAuth):
    data = {"japanese_titles": japanese_titles}
    response = requests.put(
        APIBASE + f"/users/settings", json=data, headers=headersAuth
    )
    return check_response(response)


def post_new_user(username, password):
    data = {"username": username, "password": password}
    response = requests.post(APIBASE + "/users/create", json=data)
    return check_response(response)


def delete_user(headersAuth):
    response = requests.delete(APIBASE + "/users/delete", headers=headersAuth)
    return check_response(response)


def add_entries(entries, headersAuth):
    data = {"entries": entries}
    response = requests.post(APIBASE + "/entries/add", json=data, headers=headersAuth)
    return check_response(response)


def delete_entries(entries, headersAuth):
    data = {"entries": entries}
    response = requests.delete(
        APIBASE + "/entries/remove", json=data, headers=headersAuth
    )
    return check_response(response)


def clear_watchlist(headersAuth):
    response = requests.delete(APIBASE + "/entries/clear", headers=headersAuth)
    return check_response(response)


def get_watchlist(headersAuth):
    response = requests.get(APIBASE + "/entries/all", headers=headersAuth)
    return check_response(response)


def get_watchlist_airing(headersAuth):
    response = requests.get(APIBASE + "/entries/watchlist/airing", headers=headersAuth)
    return check_response(response)


def get_season():
    response = requests.get(APIBASE + "/lists/season")
    return check_response(response)
