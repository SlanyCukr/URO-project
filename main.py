# -*- coding: utf-8 -*-
from tkinter import *

from app import App

if __name__ == '__main__':
    root = Tk()
    root.wm_title("Záznamový a vysílací program")
    root.minsize(1100, 800)
    app = App(root)
    root.mainloop()
