from tkinter import *
from dotenv import load_dotenv
import os
from get_weather import get_weather

load_dotenv()

API_KEY = os.getenv("API_KEY")

window = Tk()
window.geometry("420x560")

# window.mainloop()


print(get_weather(API_KEY, "london"))