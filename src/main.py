from tkinter import *
from tkinter import ttk
from dotenv import load_dotenv
import os
from get_weather import get_weather

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_info (city):
    info = get_weather(API_KEY, city)
    print(info)

    return

window = Tk()
window.geometry("420x560")
window.title("The Weather Forcast")

mainframe = ttk.Frame(window, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

feet = StringVar()
city = ttk.Entry(mainframe, width=7, textvariable=feet)
city.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Search", command=get_info(city)).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

city.focus()
# window.bind("<Return>", calculate)






window.mainloop()


# print(get_weather(API_KEY, "london"))