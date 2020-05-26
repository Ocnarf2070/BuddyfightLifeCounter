from tkinter import *
from tkinter.font import Font

from PIL import Image, ImageTk

from Controller import Controller
from Model import Player


class PlayerFrameView:
    def __init__(self, master: Frame, player: Player, pos: int, bg="light grey"):
        self.pos = pos
        self.player_frame = Frame(master, bd=1, relief=SUNKEN, bg=bg)
        self.player_frame.columnconfigure(0, weight=1)
        self.player_frame.rowconfigure(0, weight=1)
        self.player_frame.rowconfigure(1, weight=1)
        self.player_frame.rowconfigure(2, weight=1)

        images = Images()

        self.label = Label(self.player_frame, text=player.get_name(), font=Font(size=30), bg=bg)
        self.label.grid(row=0, sticky="nsew")
        self.controlPanel = Frame(self.player_frame, bg=bg)
        self.controlPanel.rowconfigure(0, weight=1)
        self.controlPanel.rowconfigure(1, weight=1)
        self.controlPanel.rowconfigure(2, weight=1)
        self.controlPanel.columnconfigure(0, weight=1)
        self.controlPanel.columnconfigure(1, weight=1)

        self.btn1 = Button(self.controlPanel, image=images.plus)
        self.btn1.image = images.plus
        self.btn1.grid(row=0, column=pos, padx=5, pady=5, sticky=S + N + E + W)
        self.entry = Entry(self.controlPanel, font=Font(size=30), justify="center", width=3)
        self.entry.grid(row=1, column=pos, padx=5, pady=5, sticky=S + N + E + W)
        self.btn2 = Button(self.controlPanel, image=images.minus)
        self.btn2.image = images.minus
        self.btn2.grid(row=2, column=pos, padx=5, pady=5, sticky=S + N + E + W)

        self.labelLife = Label(self.controlPanel, text=str(player.get_life()), font="Helvetica 50 bold", bg=bg)
        self.labelLife.grid(row=0, column=1 - pos, rowspan=3, sticky=S + N + E + W)

        self.controlPanel.grid(row=1, sticky=S + N + E + W)

        self.buddy_call_button = Button(self.player_frame, text="Buddy Call", font=Font(size=20))
        self.buddy_call_button.grid(row=2, sticky="nsew")

    def add_controller(self, controller: Controller):
        self.btn1.bind("<Button>", lambda event, args=self.pos: controller.btn_add(event, args))
        self.btn2.bind("<Button>", lambda event, args=self.pos: controller.btn_sub(event, args))
        self.buddy_call_button.bind("<Button>", lambda event, args=self.pos: controller.btn_buddy_call(event, args))


class Images:
    def __init__(self):
        path = "images/"
        load = Image.open(path + "plus.png").resize((50, 50))
        self.plus = ImageTk.PhotoImage(load)
        load = Image.open(path + "minus.png").resize((50, 50))
        self.minus = ImageTk.PhotoImage(load)
