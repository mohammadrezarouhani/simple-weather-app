import requests
import json
import pdb
from datetime import datetime


class Weather:
    def __init__(self,city,app_id) -> None:
        self.request=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={app_id}').text
        self.city=city
        self.set_weather_info()

    def set_weather_info(self):
        data=json.loads(self.request)
        weather=data.get("weather")[0]
        main=data.get("main")
        wind=data.get("wind")
        sys=data.get("sys")

        self.updated_at=datetime.fromtimestamp(data.get("dt")).strftime("%H:%M %p")
        self.weather_status=weather['description']
        self.temp=main['temp']
        self.max_temp=main['temp_max']
        self.min_temp=main['temp_min']
        self.pressure=main['pressure']
        self.humidity=main['humidity']
        self.wind_speed=wind['speed']
        self.sunrise=datetime.fromtimestamp(sys['sunrise']).strftime('%H:%M %p')
        self.sunset=datetime.fromtimestamp(sys['sunset']).strftime('%H:%M %p')

    def __str__(self) -> str:
        return f"""
                    ***** {self.city} *****

                    updated at {self.updated_at}
                    status : {self.weather_status}
                    temp : {self.temp}°C
                    max_temp : {self.max_temp}°C , min_temp : {self.min_temp}°C
                    pressure : {self.pressure}
                    humidity : {self.humidity}
                    wind_speed : {self.wind_speed}
                    sunrise : {self.sunrise} , sunset: {self.sunset}
        """




if __name__=='__main__':
    app_id='d1eaa9f005392a6f2a8225051875a6d9'
    city='Tonekabon,ir'

    while True:
        city=input("please enter the name of your city:\n      ")

        try:
            print(Weather(city,app_id))
            break
        except Exception as err:
            print(err)