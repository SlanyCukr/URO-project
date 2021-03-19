from tkinter import *
from tkinter import simpledialog

from PIL import ImageTk, Image


def add_item(listbox: Listbox):
    name = simpledialog.askstring(title="Prosím napište odpověď", prompt="Jaké je jméno přidávané položky?")
    listbox.insert(listbox.size() + 1, name)


def remove_item(listbox: Listbox):
    listbox.delete(listbox.curselection())


def create_listbox(root, name):
    frame = Frame(root)
    label = Label(frame, text=name)
    listbox = Listbox(frame, bg='white')

    plus = Image.open("pictures/plus.png")
    plus = plus.resize((20, 20), Image.ANTIALIAS)
    plus = ImageTk.PhotoImage(plus)
    add_button = Button(frame, image=plus, command=lambda: add_item(listbox))
    add_button.image = plus

    minus = Image.open("pictures/minus.png")
    minus = minus.resize((20, 20), Image.ANTIALIAS)
    minus = ImageTk.PhotoImage(minus)
    remove_button = Button(frame, image=minus, command=lambda: remove_item(listbox))
    remove_button.image = minus

    label.pack()
    listbox.pack()
    remove_button.pack(side=RIGHT)
    add_button.pack(side=RIGHT)

    frame.pack(side=LEFT, padx=25, pady=10)

    return listbox


def create_sound_slider(root, name):
    frame = Frame(root)
    scale = Scale(frame, from_=0, to=100, orient=HORIZONTAL)

    im = Image.open("pictures/mute.png")
    im = im.resize((25, 25), Image.ANTIALIAS)
    ph = ImageTk.PhotoImage(im)
    mute_button = Button(frame, image=ph)
    mute_button.image = ph
    label = Label(frame, text=name)

    scale.grid(row=0)
    mute_button.grid(row=0, column=1, pady=(15, 0))
    label.grid(row=1, columnspan=1)

    frame.pack()

