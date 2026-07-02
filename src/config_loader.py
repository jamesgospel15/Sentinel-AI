import json


def load_feeds():

    with open("config/feeds.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data["feeds"]