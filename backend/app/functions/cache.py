import json
from typing import Dict


def read_cache(file: str):
    try:
        with open(file, "r") as f:
            season_cache = json.load(f)
        return season_cache

    except:
        raise FileNotFoundError("Cache error")


def save_cache(file: str, data: Dict):
    try:
        with open(file, "w") as f:
            season_cache = json.dumps(data)
            f.write(season_cache)
    except:
        raise FileNotFoundError("Cache error")
