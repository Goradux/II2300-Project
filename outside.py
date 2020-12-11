import requests
import json


class Outside():
    API_KEY = 'NRV0H71x4loDRQWuJFg4gRt7cCFuz4i5'
    ENDPOINT = "https://api.climacell.co/v3/weather/realtime"
    querystring = {
        "lat": "59.404",
        "lon": "17.951",
        "apikey": API_KEY,
        "unit_system":"si",
        "fields":"pm25,pm10,temp,humidity",
    }


    def __init__(self) -> None:
        self.name = ['PM2.5', 'PM10', 'temp.', 'humidity']
        self.value = []
        self.unit = ['μg/m3', 'μg/m3' ,'C', '%']
        self.size = 4
        self.refresh_data()


    def refresh_data(self):
        try:
            response = requests.request("GET", self.ENDPOINT, params=self.querystring)
            data = json.loads(response.text)
            # self.pm25 = {"name": "PM2.5", "value": data['pm25']['value']}
            # self.pm10 = {"name": "PM10", "value": data['pm10']['value']}
            # self.temp = {"name": "temp.", "value": data['temp']['value']}
            # self.humidity = {"name": "humidity", "value": data['humidity']['value']}
            self.value = [
                data['pm25']['value'],
                data['pm10']['value'],
                data['temp']['value'],
                data['humidity']['value']
            ]
        except Exception as e:
            print(e)


# outside = Outside()
# for property, value in vars(outside).items():
#     print(property, value)