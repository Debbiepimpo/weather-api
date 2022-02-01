import requests

def check_weather_by_ip():
    ip = "24.48.0.1"
    ip_url= f"http://ip-api.com/json/{ip}"
    ipData = requests.get(ip_url).json()
    lat = ipData["lat"]
    lon = ipData["lon"]

    API_KEY= "b97aac961b6899d1caf2b26a2b88e534"
    weather_url= f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}'
    weatherData = requests.get(weather_url).json()
    weather_list = weatherData["list"]
    mydate = "2022-03-02 00:00:00"

    forecast_temp = [item["main"] for item in weather_list if item["dt_txt"] == mydate]
    forecast_weather = [item["weather"] for item in weather_list if item["dt_txt"] == mydate]

    total_forecast = sum(forecast_temp,forecast_weather)
    return total_forecast
        
if __name__ == "__main__":
    print(check_weather_by_ip())


