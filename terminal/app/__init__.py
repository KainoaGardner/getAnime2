import argparse
import os

msg = "Terminal verison to checking daily airing anime"
parser = argparse.ArgumentParser(description=msg)

APIBASE = "http://10.0.0.64/api"
# APIBASE = "http://54.176.88.48"
PATH = os.path.dirname(__file__)


class TerminalColor:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


import app.arguments
import app.main
