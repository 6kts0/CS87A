import python_weather
from datetime import datetime
import time
from zoneinfo import ZoneInfo
import pytz
import asyncio

"""
Domestic Weather Forecaster
"""

async def main():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:

        print('=' * 65 + '\n')
        print("                 --- TODAYS FORECAST ---\n")
        print('=' * 65)

        # Input city to forcast
        usr_map = input("Enter a city to fetch the current weather: ").strip()
        usr_map_formed = usr_map.replace(" ", "_").title()
        weather = await client.get(usr_map_formed)

        # Fetching location time
        map_time = "America/" + usr_map_formed
        city_tz = ZoneInfo(map_time)
        city_datetime = datetime.now(tz=city_tz)
        city_datetime = city_datetime.strftime("%I:%M%p")

        # Current forecast at formatte time
        print('=' * 65)
        print(f"The weather in {usr_map_formed.replace('_', ' ')} today is {weather.temperature} degrees fahrenheit at {city_datetime}.") 
        
        # Three day future weather forecast
        print('=' * 65 + '\n')
        print("               --- Near Future Forecast ---\n")
        print('=' * 65 )

        for daily in weather:
            daily_time_format = daily.date.strftime("%Y/%m/%d")
            print(f"On {daily_time_format} the temperature will be {daily.temperature} degrees fahrenheit")
            if daily.temperature > 76:
                print("ADVISORY: The current temperature is above the global average, apply sunscreen before sun exposure and stay hydrated")
            elif daily.temperature <= 76 and daily.temperature >= 70:
                print("ADVISORY: Its pretty warm out, shorts or a t-shirt along with sunscreen is highly recommended")
            elif daily.temperature <= 70 and daily.temperature >= 65:
                print("ADVISORY: A hoodie or light jacket is recommended for this temperature range")
            elif daily.temperature <= 65 and daily.temperature >= 60:
                print("ADVISORY: This temperature calls for a sufficiently warm jacket and/or multiple layers with pants")
            elif daily.temperature <= 60 and daily.temperature >= 55:
                print("ADVISORY: Wear multiple layers and/or a jacket")
            elif daily.temperature <= 55 and daily.temperature >= 40:
                print("ADVISORY: Its cold as fuuuck!")
            elif daily.temperature <= 40:
                print("ADVISORY: The current temperature can cause vulnerability to viral sickness unless your equipped with proper outer layers")
            elif daily.temperature <= 30:
                print("ADVISORY: Its freezing...")
                time.sleep(0.5)
                print("Literally")
            print('-' * 60)


if __name__ == '__main__':
    asyncio.run(main())