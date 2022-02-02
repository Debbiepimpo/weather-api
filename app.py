import os
import requests
from datetime import datetime

def check_weather_by_ip():
    ip = "24.48.0.1"
    ip_url= f"http://ip-api.com/json/{ip}"
    ipData = requests.get(ip_url).json()
    lat = ipData["lat"]
    lon = ipData["lon"]

    key = os.getenv("API_KEY")
    key = "b97aac961b6899d1caf2b26a2b88e534"

    weather_url= f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}'
    weatherData = requests.get(weather_url).json()
    weather_list = weatherData["list"]
    today = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    mydate = datetime.strptime(today, "%Y-%m-%d %H:%M:%S")

    forecast_weather = [item["weather"] for item in weather_list if datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S").date() == mydate.date()]
    
    return forecast_weather
        
if __name__ == "__main__":
    print(check_weather_by_ip())


