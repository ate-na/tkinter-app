import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

"""
  This module includes functions to render frames corresponding to each three tasks of admin panel.
1. Buying airplanes
2. Adding a new user
3. Registering airlines
"""

plane_list = [
    'Airbus A310',
    'Boeing 727',
    'Convair 880',
    'Irkut MC-21',
    'Airbus A318',
    'Boeing 757',
    'Dassault Mercure',
    'Lockheed L-1011',
    'Airbus A380',
    'Boeing 767',
    'Douglas DC-8',
    'Vickers VC10',
    'BAC One-Eleven',
    'Comac C919',
    'Ilyushin Il-86',
    'Airbus A321'
]



root = tk.Tk()


def render_root(root):
    # Set window size
    root.geometry("800x900")
    # root.geometry("530x600")
    # Set title
    root.title("Reserve Flight")
    # Make window size fixed
    root.resizable(False, False)
    # Set root window color
    root.config(background="#c4d1de")
    # root.config(background="#d9d9da")
    # root.config(background="#c9f1ed")
    # root.config(background="#9eedfa")


def render_plane_shop(root):
    frame_shop = Frame(root)
    frame_shop.pack(fill=BOTH)
    for plane in plane_list:
        img = ImageTk.PhotoImage(Image.open("/home/hm/PycharmProjects/airport_acounting_app/planes/{}.jpeg".format(plane)))
        l = ttk.Label(frame_shop)
        l.config(image=img)
        l.pack()
        # radiobtn = Radiobutton(frame_shop)
        # radiobtn.config(image=img)
        # radiobtn.pack()

def render_user_register(root):
    frame_user = Frame(root)
    frame_user.pack(fill=BOTH)

def render_airline_register(root):
    frame_airline = Frame(root)
    frame_airline.pack(fill=BOTH)


def run(root=root):
    render_root(root)
    render_plane_shop(root)
    render_user_register(root)
    render_airline_register(root)

    root.mainloop()

if __name__ == "__main__":
    run()