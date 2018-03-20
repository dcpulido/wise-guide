import sys
sys.path.insert(0, './')
import json
import time
from weather import WeatherHandler


class Controller:
    def __init__(self,
                 general,
                 tokens,
                 client):
        self.conf = general
        self.tokens = tokens
        self.weather = WeatherHandler(tokens["weather_token"])
        self.members = client.get_all_members()

    def parse_message(self,
                      message,
                      client):
        print(client)
        msg = message.content
        author = message.author
        print(msg)
        if msg.startswith("!weather"):
            return json.dumps(self.weather.place(msg.split(" ")[1]),
                              indent=2)
        if msg.startswith("!hello"):
            return author.mention + "\'s ass is so wet"

        if msg.startswith("!date"):
            return time.strftime("%H:%M:%S %d/%m/%Y")

        if msg.startswith("!pubg"):
            toret = []
            self.members = client.get_all_members()
            for m in self.members:
                if m.game != None:
                    if m.game.name == "PLAYERUNKNOWN'S BATTLEGROUNDS":
                        print(dir(m.status))
                        toret.append(dict(name=m.display_name,
                                          status=m.status.value,
                                          server=m.server.name))
            return json.dumps(toret,
                              indent=2)

        if msg.startswith("!info"):
            try:
                for m in self.members:
                    print(m.game)
                    print(m.nick)
                    print(dir(m.game))
                return " "
            except Exception as e:
                return "pa k kieres saber eso jaja saludos"
                raise e


if __name__ == '__main__':
    cont = Controller(
        {},
        {"weather_token": "ff9800322cfaf4c6cb9fd025ed74b2e2"})
    cont.parse_message("!weather ourense")
