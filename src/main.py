from tkinter import *
from tkinter import ttk

from dotenv import load_dotenv
import os

from get_weather import get_weather
from get_time import get_time

load_dotenv()

API_KEY = os.getenv("API_KEY")
cur_page = 0


def get_info ():
    global cur_page
    if cur_page != 0:
        ttk.Button(mainframe, text="Prev", command=prev_page).grid(column=1, row=1, sticky=W)

    info = get_weather(API_KEY, city.get())
    cur_time = get_time(info["list"][cur_page]["dt_txt"])
    description = info["list"][cur_page]["weather"][0]["description"]
    wind = int(round(info["list"][cur_page]["wind"]["speed"]))
    ttk.Label(mainframe, text=f"{cur_time["hour"]}:{cur_time["minute"]}").grid(column=3, row=2, sticky=(W, E))
    ttk.Label(mainframe, text=round(info["list"][cur_page]["main"]["temp"])).grid(column=3, row=3, sticky=(W, E))
    ttk.Label(mainframe, text=round(info["list"][cur_page]["main"]["feels_like"])).grid(column=3, row=4, sticky=(W, E))
    ttk.Label(mainframe, text=round(info["list"][cur_page]["main"]["temp_min"])).grid(column=3, row=5, sticky=(W, E))
    ttk.Label(mainframe, text=round(info["list"][cur_page]["main"]["temp_max"])).grid(column=3, row=6, sticky=(W, E))
    ttk.Label(mainframe, text=f"There is/are {description}.\nThe wind speed is {wind}m/s").grid(column=1, row=7, sticky=(W, E))

def prev_page():
    global cur_page
    cur_page = cur_page - 1
    get_info()

def next_page():
    global cur_page
    cur_page = cur_page + 1
    get_info()
    
window = Tk()
window.geometry("420x360")
window.title("The Weather Forcast")
mainframe = ttk.Frame(window, padding=(4, 4, 8, 8))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

city = Variable()
cityLine = ttk.Entry(mainframe, text="Enter the city", width=7, textvariable=city)
cityLine.grid(column=3, row=1, sticky=(W, E))

ttk.Button(mainframe, text="Search", command=get_info).grid(column=4, row=1, sticky=W)
ttk.Button(mainframe, text="Next", command=next_page).grid(column=2, row=1, sticky=W)


ttk.Label(mainframe, text="Temperatur(AVG)").grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Feels like").grid(column=1, row=4, sticky=(W, E))
ttk.Label(mainframe, text="Temperatur(min)").grid(column=1, row=5, sticky=(W, E))
ttk.Label(mainframe, text="Temperatur(max)").grid(column=1, row=6, sticky=(W, E))

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

window.mainloop()