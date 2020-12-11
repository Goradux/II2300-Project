import bme680
import traceback
import sys


class Inside():
    def __init__(self) -> None:
        try:
            self.sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
        except Exception as e:
            traceback.print_exc(file=sys.stdout)
            print('Could not configure the sensor. Exiting...')
            exit(1)
        self.name = ['temp.', 'gas res.', 'humidity', 'pressure']
        self.value = []
        self.unit = ['C', '???' ,'%', 'hPa']
        self.size = 4
        self.refresh_data()

        
    def refresh_data(self):
        self.sensor.get_sensor_data()
        # self.temp = {"name": "temp.", "value": self.sensor.data.temperature}
        # self.gas_resistance = {"name": "gas res.", "value": self.sensor.data.gas_resistance}
        # self.humidity = {"name": "humidity", "value": self.sensor.data.humidity}
        # self.pressure = {"name": "pressure", "value": self.sensor.data.pressure}
        self.value = [
            self.sensor.data.temperature,
            self.sensor.data.gas_resistance,
            self.sensor.data.humidity,
            self.sensor.data.pressure
        ]
