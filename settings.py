from tkinter import *
from scrollable_frame import ScrollableFrame


def create_checkbox(root, text, row):
    variable = IntVar()
    button = Checkbutton(root, text=text, var=variable).grid(row=row, sticky="W", padx=(75, 0))


def create_option_menu(root, text, options: [], row):
    variable = StringVar(root)
    variable.set(options[0])
    label_language = Label(root, text=text).grid(row=row, column=0, padx=(75, 0), sticky="EW")
    language_option_menu = OptionMenu(root, variable, *options)
    language_option_menu.config(width=50)
    language_option_menu.grid(row=row, column=1, sticky="EW")


def general_draw(right_frame):
    # remove old widget items
    for widget in right_frame.winfo_children():
        widget.destroy()

    # general frame
    general_frame = LabelFrame(right_frame, text="Obecné")
    create_option_menu(general_frame, "Jazyk", ["Česky", "English", "Polski"], 0)
    create_option_menu(general_frame, "Styl", ["Klasický", "Temný", "Bílý", "Futuristický"], 1)
    general_frame.pack(fill=X, padx=25, side=TOP, expand=1)

    # output frame
    output_frame = LabelFrame(right_frame, text="Výstup")
    create_checkbox(output_frame, "Zobrazit dialog při startu vysílání", 0)
    create_checkbox(output_frame, "Zobrazit dialog při zastavení vysílání", 1)
    create_checkbox(output_frame, "Zobrazit dialog při zastavení nahrávání", 2)
    create_checkbox(output_frame, "Automaticky nahrávat při vysílání", 3)
    create_checkbox(output_frame, "Nahrávat i po skončení vysílání", 4)
    create_checkbox(output_frame, "Automaticky zapnout přehrávací buffer po vysílání", 5)
    create_checkbox(output_frame, "Udržovat přehrávací buffer aktivní po skončení vysílání", 6)
    create_checkbox(output_frame, "Při startu otevřít statistiky", 7)
    output_frame.pack(fill=X, padx=25, side=TOP)

    # system tray
    tray_frame = LabelFrame(right_frame, text="System tray")
    create_checkbox(tray_frame, "Zapnout", 0)
    create_checkbox(tray_frame, "Schovat při startu", 1)
    create_checkbox(tray_frame, "Vždy minimalizovat to system tray místo task baru", 2)
    tray_frame.pack(fill=X, padx=25, side=TOP)

    # preview frame
    preview_frame = LabelFrame(right_frame, text="Náhled")
    create_checkbox(preview_frame, "Schovat overflow", 0)
    create_checkbox(preview_frame, "Overflow vždy viditelný", 1)
    create_checkbox(preview_frame, "Ukázat overflow i když je zdroj neviditelný", 2)
    preview_frame.pack(fill=X, padx=25, side=TOP)

    # system tray 1
    tray_frame1 = LabelFrame(right_frame, text="System tray")
    create_checkbox(tray_frame1, "Zapnout", 0)
    create_checkbox(tray_frame1, "Schovat při startu", 1)
    create_checkbox(tray_frame1, "Vždy minimalizovat to system tray místo task baru", 2)
    tray_frame1.pack(fill=X, padx=25, side=TOP)

    # preview frame
    preview_frame1 = LabelFrame(right_frame, text="Náhled")
    create_checkbox(preview_frame1, "Schovat overflow", 0)
    create_checkbox(preview_frame1, "Overflow vždy viditelný", 1)
    create_checkbox(preview_frame1, "Ukázat overflow i když je zdroj neviditelný", 2)
    preview_frame1.pack(fill=X, padx=25, side=TOP)

    # output frame
    output_frame1 = LabelFrame(right_frame, text="Výstup")
    create_checkbox(output_frame1, "Zobrazit dialog při startu vysílání", 0)
    create_checkbox(output_frame1, "Zobrazit dialog při zastavení vysílání", 1)
    create_checkbox(output_frame1, "Zobrazit dialog při zastavení nahrávání", 2)
    create_checkbox(output_frame1, "Automaticky nahrávat při vysílání", 3)
    create_checkbox(output_frame1, "Nahrávat i po skončení vysílání", 4)
    create_checkbox(output_frame1, "Automaticky zapnout přehrávací buffer po vysílání", 5)
    create_checkbox(output_frame1, "Udržovat přehrávací buffer aktivní po skončení vysílání", 6)
    create_checkbox(output_frame1, "Při startu otevřít statistiky", 7)
    output_frame1.pack(fill=X, padx=25, side=TOP)


def stream_draw(right_frame):
    # remove old widget items
    for widget in right_frame.winfo_children():
        widget.destroy()

    # general frame
    general_frame = LabelFrame(right_frame, text="Vysílání")
    create_option_menu(general_frame, "Služba", ["Twitch", "Youtube", "Facebook"], 0)
    create_option_menu(general_frame, "Server", ["Evropa", "Amerika", "Austrálie", "Německo"], 1)
    label = Label(general_frame, text="Vysílací klíč").grid(row=2, column=0, padx=(75, 0))
    text = Entry(general_frame, width=40).grid(row=2, column=1, sticky="W")
    general_frame.pack(fill=X, padx=25, side=TOP)


def output_draw(right_frame):
    # remove old widget items
    for widget in right_frame.winfo_children():
        widget.destroy()

    # general frame
    general_frame = LabelFrame(right_frame, text="Streamování")
    create_option_menu(general_frame, "Bitrate", ["12 Mbps", "7.5 Mbps", "4 Mbps", "1 Mbps"], 0)
    create_option_menu(general_frame, "Enkodér", ["GPU", "Software (x264)"], 1)
    create_option_menu(general_frame, "Audio bitrate", ["320 kbit/s", "256 kbit/s", "192 kbit/s", "96 kbit/s"], 2)
    general_frame.pack(fill=X, padx=25, side=TOP)

    # recording frame
    recording_frame = LabelFrame(right_frame, text="Záznam")
    create_option_menu(recording_frame, "Kvalita", ["Stejná, jako stream", "Vysoká", "Střední", "Nízká"], 0)
    create_option_menu(recording_frame, "Formát videa", ["mp4", "mpeg", "avi"], 1)
    recording_frame.pack(fill=X, padx=25, side=TOP)


def audio_draw(right_frame):
    # remove old widget items
    for widget in right_frame.winfo_children():
        widget.destroy()

    # recording frame
    recording_frame = LabelFrame(right_frame, text="Obecné")
    create_option_menu(recording_frame, "Vzork. frekvence", ["48 kHz", "44.1 kHz"], 0)
    create_option_menu(recording_frame, "Kanály", ["Mono", "Stereo", "5.1", "7.1"], 1)
    recording_frame.pack(fill=X, padx=25, side=TOP)

    # global audio devices
    global_audio_devices = LabelFrame(right_frame, text="Audio zařízení")
    create_option_menu(global_audio_devices, "Desktop audio 1", ["Default", "Reproduktory"], 0)
    create_option_menu(global_audio_devices, "Desktop audio 2", ["Default", "Reproduktory"], 1)
    create_option_menu(global_audio_devices, "Mikrofon audio", ["Mikrofon1", "Mikrofon2"], 2)
    create_option_menu(global_audio_devices, "Mikrofon  audio2", ["Mikrofon1", "Mikrofon2"], 3)
    create_option_menu(global_audio_devices, "Mikrofon  audio3", ["Mikrofon1", "Mikrofon2"], 4)
    create_option_menu(global_audio_devices, "Mikrofon audio4", ["Mikrofon1", "Mikrofon2"], 5)
    create_option_menu(global_audio_devices, "Mikrofon audio5", ["Mikrofon1", "Mikrofon2"], 6)
    global_audio_devices.pack(fill=X, padx=25, side=TOP)

    # meters
    meters = LabelFrame(right_frame, text="Metry")
    create_option_menu(meters, "Rychlost rozpadu", ["Rychlý", "Střední", "Nízký"], 0)
    create_option_menu(meters, "Typ metru", ["Sample peak", "True peak"], 1)
    meters.pack(fill=X, padx=25, side=TOP)

    # advanced
    advanced = LabelFrame(right_frame, text="Pokročilé")
    create_option_menu(advanced, "Monitor. zařízení", ["Default", "Sluchátka 1"], 0)
    advanced.pack(fill=X, padx=25, side=TOP)


def video_draw(right_frame):
    # remove old widget items
    for widget in right_frame.winfo_children():
        widget.destroy()

    # recording frame
    general_frame = LabelFrame(right_frame, text="Obecné")
    create_option_menu(general_frame, "Základní rozlišení", ["1920x1080", "1280x720"], 0)
    create_option_menu(general_frame, "Výstupní rozlišení", ["1920x1080", "1280x720", "640x480"], 1)
    create_option_menu(general_frame, "Downscale filtr", ["Bikubický", "Lanczos", "Bilineární"], 2)
    create_option_menu(general_frame, "FPS", ["30", "60", "24"], 3)
    general_frame.pack(fill=X, padx=25, side=TOP)


def advanced_draw(right_frame):
    # remove old widget items
    for widget in right_frame.winfo_children():
        widget.destroy()

    # video frame
    video_frame = LabelFrame(right_frame, text="Video")
    create_option_menu(video_frame, "Barevný formát", ["NV12", "RGB"], 0)
    create_option_menu(video_frame, "Barevný prostor", ["sRGB", "709"], 1)
    create_option_menu(video_frame, "Barevný rozsah", ["Plný", "Částečný"], 1)
    video_frame.pack(fill=X, padx=25, side=TOP)

    # streaming delay
    streaming_delay = LabelFrame(right_frame, text="Vysílací zpoždění")
    create_checkbox(streaming_delay, "Zapnout", 0)
    create_option_menu(streaming_delay, "Délka zpoždění", ["10s", "5s", "1s", "20s"], 1)
    streaming_delay.pack(fill=X, padx=25, side=TOP)


def settings():
    win = Toplevel()
    win.title('Nastavení')
    win.minsize(900, 700)
    win.maxsize(900, 700)

    # bottom frame
    bottom_frame = Frame(win)

    apply_button = Button(bottom_frame, text="Uložit", width=6, command=win.destroy).pack(side=RIGHT)
    cancel_button = Button(bottom_frame, text="Zrušit", width=6, command=win.destroy).pack(side=RIGHT)
    ok_button = Button(bottom_frame, text="OK", width=6, command=win.destroy).pack(side=RIGHT)

    bottom_frame.pack(side=BOTTOM, fill=BOTH)

    # right frame
    right_frame_main = ScrollableFrame(win)
    right_frame = right_frame_main.scrollable_frame

    # draw general settings window
    general_draw(right_frame)

    right_frame_main.pack(side=RIGHT, expand=1, fill=BOTH)

    # left frame
    left_frame = Frame(win, highlightthickness=1, highlightbackground="grey")
    general_button = Button(left_frame, text="Obecné", width=10, command=lambda: general_draw(right_frame)).pack()
    stream_button = Button(left_frame, text="Stream", width=10, command=lambda: stream_draw(right_frame)).pack()
    output_button = Button(left_frame, text="Výstup", width=10, command=lambda: output_draw(right_frame)).pack()
    audio_button = Button(left_frame, text="Audio", width=10, command=lambda: audio_draw(right_frame)).pack()
    video_button = Button(left_frame, text="Video", width=10, command=lambda: video_draw(right_frame)).pack()
    advanced_button = Button(left_frame, text="Pokročilé", width=10, command=lambda: advanced_draw(right_frame)).pack()
    left_frame.pack(side=LEFT, fill=Y, padx=10, pady=10)
