import webbrowser

from app import TerminalColor
from app.functions.cache import get_auth_header
from app.api.calls import (
    get_watchlist_airing,
    get_user_settings,
    get_watchlist,
    get_season,
)


def show_anime_list(japanese_titles, anime_list):
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


def lists(args):
    sort_type = get_sort_type(args)
    headersAuth = get_auth_header()
    settings = get_user_settings(headersAuth)
    japanese_titles = settings.json()["japanese_titles"]

    if "today" in args.lists or "t" in args.lists:
        list_today(headersAuth, sort_type, japanese_titles)
    elif "watchlist" in args.lists or "wl" in args.lists:
        list_watchlist(headersAuth, sort_type, japanese_titles)
    else:
        list_all(sort_type, japanese_titles)


def list_today(headersAuth, sort_type, japanese_titles):
    response = get_watchlist_airing(headersAuth)
    print(TerminalColor.BOLD + "---Watchlist Airing Today---" + TerminalColor.END)
    anime_list = sort_list(response.json(), sort_type)
    show_anime_list(japanese_titles, anime_list)


def list_watchlist(headersAuth, sort_type, japanese_titles):
    response = get_watchlist(headersAuth)
    print(TerminalColor.BOLD + "---Watchlist---" + TerminalColor.END)
    anime_list = sort_list(response.json(), sort_type)
    show_anime_list(japanese_titles, anime_list)


def list_all(sort_type, japanese_titles):
    response = get_season()
    print(TerminalColor.BOLD + "---Season---" + TerminalColor.END)
    anime_list = make_season_list(response.json())
    anime_list = sort_list(anime_list, sort_type)
    show_anime_list(japanese_titles, anime_list)


def make_season_list(anime_list):
    result = []
    for anime in anime_list:
        mal_id = anime
        title = anime_list[anime]["title"]
        japanese_title = anime_list[anime]["japanese_title"]
        image = anime_list[anime]["image"]
        result.append(
            {
                "mal_id": mal_id,
                "title": title,
                "japanese_title": japanese_title,
                "image": image,
            }
        )
    return result


def nyaa():
    headersAuth = get_auth_header()
    response = get_watchlist_airing(headersAuth)
    print(TerminalColor.BOLD + "---Opened Nyaa Links---" + TerminalColor.END)
    open_nyaa(response.json())


def open_nyaa(anime_list):
    for anime in anime_list:
        title = anime["title"].lower()
        title = title.replace(" ", "+")
        webbrowser.open(f"https://nyaa.si/?f=0&c=0_0&q={title}&s=seeders&o=desc")


def sort_list(anime_list, sort):
    if sort == "name":
        anime_list.sort(key=lambda x: x["title"])
    elif sort == "id":
        anime_list.sort(key=lambda x: x["mal_id"])
    else:
        anime_list.reverse()

    return anime_list


def get_sort_type(args):
    if not args.sort:
        return "recent"
    if "i" in args.sort or "id" in args.sort:
        return "id"
    elif "n" in args.sort or "name" in args.sort:
        return "name"
    else:
        return "recent"
