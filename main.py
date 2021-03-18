# -*- coding: utf-8 -*-
from tkinter import *

from app import App

if __name__ == '__main__':
    root = Tk()
    root.wm_title("Záznamový a vysílací program")
    root.minsize(1024, 768)
    app = App(root)
    root.mainloop()
