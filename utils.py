from tkinter import *

from PIL import ImageTk, Image


def create_listbox(root, name):
    frame = Frame(root)
    label = Label(frame, text=name)
    listbox = Listbox(frame, bg='white')
    label.pack()
    listbox.pack()

    frame.pack(side=LEFT, padx=25, pady=10)

    return listbox


def create_sound_slider(root, name):
    frame = Frame(root)
    scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL)

    im = Image.open("mute.png")
    im = im.resize((25, 25), Image.ANTIALIAS)
    ph = ImageTk.PhotoImage(im)
    mute_button = Button(frame, image=ph)
    mute_button.image = ph
    label = Label(frame, text=name)

    scale.grid(row=0)
    mute_button.grid(row=0, column=1, pady=(15, 0))
    label.grid(row=1, columnspan=1)

    frame.pack()

