import requests

def get_weather (API_KEY, place):
    r = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric&lang=en&cnt=8")
    return r.json()