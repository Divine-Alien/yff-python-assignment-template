from tkinter import *
from tkinter import ttk

def pop_error_window():
    error_window = Tk()
    error_window.geometry("120x80")
    error_window.resizable(False, False)
    error_window.title("The Weather Forcast")
    mainframe = ttk.Frame(error_window, padding=(1, 1, 2, 2))
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    def close_windos():
        error_window.destroy()

    ttk.Label(mainframe, text="City not found!", foreground="red").grid(column=1, row=1, sticky=(W, E))
    ttk.Button(mainframe, text="Close", command=close_windos).grid(column=1, row=2, sticky=E)

    error_window.columnconfigure(0, weight=1)
    error_window.rowconfigure(0, weight=1)
    mainframe.columnconfigure(2, weight=1)
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)

    error_window.mainloop()