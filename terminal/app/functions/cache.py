import json
from app import PATH


def read_cache(file):
    try:
        with open(file, "r") as f:
            cache = json.load(f)
        return cache

    except:
        raise ValueError("Cache error")


def save_cache(file, data):
    try:
        with open(file, "w") as f:
            f.write(data)
    except:
        raise ValueError("Cache error")


def check_logged_in():
    cache = read_cache(f"{PATH}/user.json")
    if "access_token" not in cache:
        raise ValueError("Not Logged In")
