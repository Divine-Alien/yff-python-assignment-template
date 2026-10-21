import requests

def get_weather (API_KEY, place):
    # r = requests.get(f"https://pro.openweathermap.org/data/2.5/forecast/hourly?q={place}&appid={API_KEY}")
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}&units=metric&lang=en")

    a = r.json()

    return a