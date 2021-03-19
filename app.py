from tkinter import Menu, Label, Frame
from tkinter import ttk, colorchooser, filedialog, messagebox
from PIL import ImageTk, Image

from about import about


class App:
    def __init__(self, root):
        self.root = root
        self.maximized = False

        # menu
        self.menubar = Menu(root)

        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Nastavení", command=self.settings)
        self.filemenu.add_command(label="Konec", command=self.quit)

        self.view_menu = Menu(self.menubar, tearoff=0)
        self.view_menu.add_command(label="Zobrazit na celou obrazovku", command=self.maximize)

        self.menubar.add_cascade(label="Soubor", menu=self.filemenu)
        self.menubar.add_cascade(label="Zobrazit", menu=self.view_menu)
        self.menubar.add_command(label="Informace", command=about)
        root.config(menu=self.menubar)

        # picture in middle
        image = Image.open("desktop.png")
        image = image.resize((900, 505), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        label_image = Label(root, image=image)
        label_image.image = image
        label_image.pack(padx=100, pady=50)

        # bottom
        bottom_frame = Frame(root)


    def quit(self):
        end = messagebox.askyesno('Zavřít', 'Opravdu?')
        if end:
            self.root.quit()

    def settings(self):
        pass

    def maximize(self):
        self.maximized = not self.maximized
        self.root.attributes('-zoomed', self.maximized)
