import pyowm

class WeatherHandler:
    def __init__(self, token):
        self.owm = pyowm.OWM(token)

    def place(self, place):
        observation = self.owm.weather_at_place(place)
        w = observation.get_weather()
        values = dict(temperature=w.get_temperature("celsius"),
                      humidity=w.get_humidity(),
                      wind=w.get_wind())
        return values
