from tkinter import *
from tkinter import ttk

from dotenv import load_dotenv
import os

from get_weather import get_weather
from get_time import get_time
# from test_info import weather # TODO

load_dotenv()

API_KEY = os.getenv("API_KEY")

cur_page = 0
weather = {}  
cur_city = ""

def search_city ():
    global weather
    global cur_city
    weather = get_weather(API_KEY, city.get()) 
    cur_city = city.get()

def show_prev_next_buttons():
    ttk.Button(mainframe, text="Prev", command=prev_page).grid(column=1, row=1, sticky=W)
    ttk.Button(mainframe, text="Next", command=next_page).grid(column=2, row=1, sticky=W)


def show_info():
    global cur_page
    global weather
    global cur_city

    if cur_city != city.get():
        search_city()
        if weather["cod"] == "404":
            ttk.Label(mainframe, text="City not found!", foreground="red").grid(column=3, row=2, sticky=(W, E))
            return

    show_prev_next_buttons()

    cur_time = get_time(weather["list"][cur_page]["dt_txt"])
    ttk.Label(mainframe, text=f"{cur_time["hour"]}:{cur_time["minute"]}").grid(column=3, row=2, sticky=(W, E))

    temp_info = weather["list"][cur_page]["main"]
    req_list = ["temp", "feels_like", "temp_min", "temp_max"]
    for i in range(0, 4):
        value = round(temp_info[req_list[i]])
        row = i + 3
        ttk.Label(mainframe, text=value).grid(column=3, row=row, sticky=(W, E))

    description = weather["list"][cur_page]["weather"][0]["description"]
    wind = int(round(weather["list"][cur_page]["wind"]["speed"]))
    ttk.Label(mainframe, text=f"There is/are {description}.\nThe wind speed is {wind}m/s").grid(column=1, row=7, sticky=(W, E))

def show_info_key (event):
    show_info()

def prev_page():
    global cur_page
    if cur_page > 0:
        cur_page = cur_page - 1
        show_info()
    print(cur_page)

def next_page():
    global cur_page
    if cur_page < 7:
        cur_page = cur_page + 1
        show_info()
    print(cur_page)



window = Tk()
window.geometry("420x360")
window.resizable(False, False)
window.title("The Weather Forcast")
mainframe = ttk.Frame(window, padding=(4, 4, 8, 8))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

city = Variable()
cityLine = ttk.Entry(mainframe, width=7, textvariable=city)
cityLine.grid(column=3, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Search", command=show_info).grid(column=4, row=1, sticky=W)
window.bind("<Return>", show_info_key)

text_list = ["Temperatur(AVG)", "Feels like", "Temperatur(min)", "Temperatur(max)"]

for i in range(0, 4):
    row = i + 3
    ttk.Label(mainframe, text=text_list[i]).grid(column=1, row=row, sticky=(W, E))

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

window.mainloop()