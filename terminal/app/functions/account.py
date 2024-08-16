import json

from app import TerminalColor, PATH
from app.functions.cache import save_cache, check_logged_in, get_auth_header
from app.api.calls import (
    get_auth_token,
    get_current_user,
    post_new_user,
    delete_user,
    get_user_settings,
    put_user_settings,
)


def login(args):
    username, password = args.login
    response = get_auth_token(username, password)
    token = response.json()
    token = json.dumps(token)

    try:
        save_cache(f"{PATH}/user.json", token)
    except:
        raise ValueError("Cache error")

    print(TerminalColor.BOLD + f"Logged into {username}" + TerminalColor.END)


def settings():
    check_logged_in()
    headersAuth = get_auth_header()
    response = get_user_settings(headersAuth)
    print(TerminalColor.BOLD + "---Settings---" + TerminalColor.END)
    for setting in response.json().items():
        print(setting)


def toggle_japanese_titles():
    check_logged_in()
    headersAuth = get_auth_header()
    response = get_user_settings(headersAuth)
    japanese_titles = response.json()["japanese_titles"]
    response = put_user_settings(not japanese_titles, headersAuth)
    print(
        TerminalColor.BOLD
        + f"Japanese Titles changed to {not japanese_titles}"
        + TerminalColor.END
    )


def user():
    headersAuth = get_auth_header()
    response = get_current_user(headersAuth)
    print(
        TerminalColor.BOLD
        + f"Logged in as {response.json()["username"]}"
        + TerminalColor.END
    )


def logout():
    check_logged_in()
    save_cache(f"{PATH}/user.json", json.dumps({}))
    print(TerminalColor.BOLD + f"Logged out" + TerminalColor.END)


def register(args):
    username, password = args.register
    response = post_new_user(username, password)
    print(TerminalColor.BOLD + f"{username} Registered" + TerminalColor.END)


def delete_account():
    check_logged_in()
    if not confirm_delete():
        return

    headersAuth = get_auth_header()
    response = delete_user(headersAuth)
    save_cache(f"{PATH}/user.json", json.dumps({}))
    print(TerminalColor.BOLD + f"Account Deleted" + TerminalColor.END)


def confirm_delete():
    result = input("Are you sure?(y,n):")
    if result.lower() != "y":
        print(TerminalColor.BOLD + f"Cancelled" + TerminalColor.END)
        return False

    return True
