from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

from about import about
from utils import create_listbox, create_sound_slider


class App:
    def __init__(self, root: Tk):
        self.root = root
        self.maximized = False

        # scale the picture when resizing -> IS BUGGY
        self.root.bind("<Configure>", self.scale_picture)

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
        self.ratio = 900 / 505
        image = Image.open("pictures/desktop.png")
        image = image.resize((900, 505), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image)
        self.canvas_image = Canvas(root, width=900, height=505)
        self.canvas_image.create_image(0, 0, image=self.image, anchor="nw")
        self.canvas_image.pack(fill=BOTH, expand=True, padx=50, pady=50)

        # bottom
        bottom_frame = Frame(root)

        # scenes
        scenes_listbox = create_listbox(bottom_frame, "Scény")
        scenes_listbox.insert(1, 'Scéna 1')
        scenes_listbox.insert(2, 'Scéna 2')
        scenes_listbox.insert(3, 'Scéna 3')
        scenes_listbox.insert(4, 'Scéna 4')

        # sources
        sources_listbox = create_listbox(bottom_frame, "Zdroje")
        sources_listbox.insert(1, 'Monitor 1')
        sources_listbox.insert(2, 'Zvukové zařízení')
        sources_listbox.insert(3, 'Webkamera')
        sources_listbox.insert(4, 'Obrázek')

        # sound mixer
        sound_mixer_frame = Frame(bottom_frame)
        sound_mixer_label = Label(sound_mixer_frame, text="Zvukový mixér").pack(side=TOP)
        create_sound_slider(sound_mixer_frame, "Sluchátka")
        create_sound_slider(sound_mixer_frame, "Mikrofon")
        sound_mixer_frame.pack(side=LEFT, padx=25, pady=10, fill=BOTH)

        # control buttons
        control_frame = Frame(bottom_frame)
        control_frame_label = Label(control_frame, text="Ovládací prvky").pack()
        stream_button = Button(control_frame, text="Začít vysílat", width=15).pack(pady=(10, 0))
        record_button = Button(control_frame, text="Začít nahrávat", width=15).pack()
        settings_button = Button(control_frame, text="Nastavení", width=15).pack()
        exit_button = Button(control_frame, text="Ukončit", width=15, command=self.quit).pack()
        control_frame.pack(side=LEFT, padx=25, pady=10, fill=BOTH)

        bottom_frame.pack()

    def scale_picture(self, event):
        basewidth = self.canvas_image.winfo_width()
        image = Image.open("pictures/desktop.png")
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((basewidth, hsize), Image.ANTIALIAS)

        #self.canvas_image.config(width=canvas_width, height=canvas_height)

        self.image = ImageTk.PhotoImage(image)
        self.canvas_image.create_image(0, 0, image=self.image, anchor="nw")

    def quit(self):
        end = messagebox.askyesno('Zavřít', 'Opravdu?')
        if end:
            self.root.quit()

    def settings(self):
        pass

    def maximize(self):
        self.maximized = not self.maximized
        self.root.attributes('-zoomed', self.maximized)
