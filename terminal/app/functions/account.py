from app import APIBASE, TerminalColor, PATH
from app.functions.cache import read_cache, save_cache, check_logged_in
from app.api.calls import get_auth_token, get_current_user
import requests
import json


def login(args):
    username, password = args.login
    response = get_auth_token(username, password)
    token = json.dumps(response.json())
    try:
        save_cache(f"{PATH}/user.json", token)
    except:
        raise ValueError("Cache error")

    print(TerminalColor.BOLD + f"Logged into {username}" + TerminalColor.END)


def user():
    check_logged_in()
    cache = read_cache(f"{PATH}/user.json")
    response = get_current_user(cache["access_token"])
    print(
        TerminalColor.BOLD
        + f"Logged in as {response.json()["username"]}"
        + TerminalColor.END
    )


def logout():
    with open(
        "/home/cowie/programming/python/restGetAnime/terminal/app/user.json", "r"
    ) as f:
        json_object = json.load(f)
        if "token" in json_object:
            with open(
                "/home/cowie/programming/python/restGetAnime/terminal/app/user.json",
                "w",
            ) as file:
                user_object = json.dumps({})
                file.write(user_object)

                print(TerminalColor.BOLD + f"Logged out" + TerminalColor.END)
        else:
            print(TerminalColor.BOLD + "Not logged in" + TerminalColor.END)


def register(args):
    username, password = args.register
    user_response = requests.post(
        APIBASE + "users/account",
        json={"register": {"username": username, "password": password}},
    ).json()

    print(TerminalColor.BOLD + user_response["result"] + TerminalColor.END)


def delete_account(args):
    username, password = args.removeaccount
    user_response = requests.delete(
        APIBASE + "users/account",
        json={"delete": {"username": username, "password": password}},
    )

    print(TerminalColor.BOLD + user_response.json()["result"] + TerminalColor.END)
