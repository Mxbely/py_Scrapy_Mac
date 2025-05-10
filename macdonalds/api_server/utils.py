import json

FILE_PATH = "data.json"


def read_file():
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
