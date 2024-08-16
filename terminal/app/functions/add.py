from app import TerminalColor
from app.functions.cache import get_auth_header
from app.api.calls import (
    clear_watchlist,
    add_entries,
    delete_entries,
    get_user_settings,
)


def show_add_remove_list(japanese_titles, anime_list):
    for count, anime in enumerate(anime_list):
        print(
            TerminalColor.BOLD
            + f"{count + 1} ID: {anime["mal_id"]}"
            + TerminalColor.END,
            end=" ",
        )
        if japanese_titles:
            print(anime["japanese_title"])
        else:
            print(anime["title"])


def add(args):
    headersAuth = get_auth_header()
    settings = get_user_settings(headersAuth)
    japanese_titles = settings.json()["japanese_titles"]

    entries = [int(x) for x in args.add]
    response = add_entries(entries, headersAuth)
    print(TerminalColor.BOLD + "---Adding---" + TerminalColor.END)
    show_add_remove_list(japanese_titles, response.json())


def delete(args):
    headersAuth = get_auth_header()
    settings = get_user_settings(headersAuth)
    japanese_titles = settings.json()["japanese_titles"]

    entries = [int(x) for x in args.delete]
    response = delete_entries(entries, headersAuth)
    print(TerminalColor.BOLD + "---Deleting---" + TerminalColor.END)
    show_add_remove_list(japanese_titles, response.json())


def clear():
    headersAuth = get_auth_header()
    response = clear_watchlist(headersAuth)
    print(TerminalColor.BOLD + "---Watchlist cleared---" + TerminalColor.END)
