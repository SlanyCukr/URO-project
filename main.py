# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk, colorchooser, filedialog, messagebox

from app import App

if __name__ == '__main__':
    root = Tk()
    root.wm_title("Recording and streaming software")
    root.attributes('-zoomed', True)
    root.minsize(720, 480)
    app = App(root)
    root.mainloop()
