from app import parser

account = parser.add_argument_group("Account")
settings = parser.add_argument_group("Settings")
watchlist = parser.add_argument_group("Lists")
add_delete = parser.add_argument_group("Add_delete")
nyaa = parser.add_argument_group("Nyaa")

account.add_argument(
    "-li",
    "--login",
    nargs=2,
    metavar=("username", "password"),
    help="login into account",
)
account.add_argument(
    "-lo", "--logout", action="store_true", help="logout out of account"
)


settings.add_argument(
    "-s",
    "--settings",
    action="store_true",
    help="Toggle Japanese Title setting",
)

settings.add_argument(
    "-jt",
    "--japanese_titles",
    action="store_true",
    help="Toggle Japanese Title setting",
)


account.add_argument(
    "-r",
    "--register",
    nargs=2,
    metavar=("username", "password"),
    help="register account",
)
account.add_argument(
    "-u",
    "--user",
    action="store_true",
    help="show logged in user",
)
account.add_argument(
    "-da",
    "--deleteaccount",
    action="store_true",
    help="delete account",
)


watchlist.add_argument(
    "-l",
    "--lists",
    nargs="?",
    const="t",
    type=str,
    choices=["today", "t", "watchlist", "wl", "all", "a"],
    metavar=("today, t, watchlist, wl, all, a"),
    help="list shows in list",
)

watchlist.add_argument(
    "-so",
    "--sort",
    nargs="?",
    const="r",
    type=str,
    choices=["recent", "r", "name", "n", "id", "i"],
    metavar=("recent, r, name, n, id, i"),
    help="sort showed list",
)

add_delete.add_argument(
    "-a",
    "--add",
    nargs="+",
    help="add shows to list by id",
)

add_delete.add_argument(
    "-d",
    "--delete",
    nargs="+",
    help="delete shows from list by id",
)

add_delete.add_argument(
    "-c",
    "--clear",
    action="store_true",
    help="clear all shows in watchlist",
)

nyaa.add_argument(
    "-n",
    "--nyaa",
    action="store_true",
    help="open nyaa links for each show",
)
