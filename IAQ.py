class IAQ():
    # https://github.com/G6EJD/BME680-Example/blob/master/ - helpful
    def __init__(self) -> None:
        self.total_gas = 0
        self.total_gas_counter = 0
        self.gases = []


    def calculate_humidity_score(self, humidity) -> float:
        humidity_reference = 40
        current_humidity = humidity
        if current_humidity >= 38 and current_humidity <= 42:
            humidity_score = 0.25 * 100
        elif current_humidity < 38:
            humidity_score = 0.25 / humidity_reference * current_humidity * 100
        else:
            humidity_score = ((-0.25 / (100 - humidity_reference) * current_humidity) + 0.40) * 100
        return humidity_score


    def calculate_gas_score(self, gas) -> float:
        gas_lower_limit = 10000
        gas_upper_limit = 300000
        # gas_reference = 2500
        self.gases.append(gas)
        if len(self.gases) > 10:
            del self.gases[0]
        gas_reference = sum(self.gases) / len(self.gases)
        # self.total_gas += gas
        # self.total_gas_counter += 1
        # gas_reference = self.total_gas / self.total_gas_counter


        gas_score = (0.75 / (gas_upper_limit - gas_lower_limit) * gas_reference - (gas_lower_limit * (0.75 / (gas_upper_limit - gas_lower_limit)))) * 100

        gas_score = 75 if gas_score > 75 else gas_score
        gas_score = 0 if gas_score < 0 else gas_score

        return gas_score


    def calculate_air_quality_score(self, humidity, gas) -> float:
        score = self.calculate_humidity_score(humidity) + self.calculate_gas_score(gas)
        print('Calculated air quality score is', score)
        return score


    def calculate_IAQ(self, air_quality_score) -> str:
        score = (100 - air_quality_score) * 5
        iaq = None
        if score > 301:
            iaq = 'Hazardous'
        elif score > 201:
            iaq = 'Very unhealthy'
        elif score > 176:
            iaq = 'Unhealthy'
        elif score > 151:
            iaq = 'Bad'
        elif score > 51:
            iaq = 'Moderate'
        else:
            iaq = 'Good'
        return iaq