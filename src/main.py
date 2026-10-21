from tkinter import *
import requests

window = Tk()
window.geometry("420x560")

# window.mainloop()
# 6767a2203fc970df2d47b6076f3fc9a3
r = requests.get("https://api.openweathermap.org/data/4.0/weather?q=barcelona&units=metric&lang=en&appid=2d1c6ba9e8931bf4b4619943ef920958")
print(r.json())