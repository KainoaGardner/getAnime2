from app import parser
from app.functions.account import *
from app.functions.lists import *
from app.functions.add import *

args = parser.parse_args()

if args.login:
    login(args)
elif args.logout:
    logout()
elif args.settings:
    settings()
elif args.japanese_titles:
    toggle_japanese_titles()
elif args.user:
    user()
elif args.register:
    register(args)
elif args.deleteaccount:
    delete_account()
elif args.lists:
    lists(args)
elif args.clear:
    clear()
elif args.add:
    add(args)
elif args.delete:
    delete(args)
elif args.nyaa:
    nyaa()
