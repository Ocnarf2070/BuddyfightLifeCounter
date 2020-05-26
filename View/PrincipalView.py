from tkinter import *
from tkinter.font import Font

from Controller import Controller
from Model import Game
from View import PlayerFrameView
from View import RecordView


class PrincipalView:
    def __init__(self, master: Frame, model: Game):
        self.model = model

        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=1)

        colour_p1 = 'light sky blue'
        colour_p2 = 'light salmon'

        self.player1 = PlayerFrameView(master, model.get_player(0), 0, colour_p1)
        self.player1.player_frame.grid(row=0, column=0)
        self.player2 = PlayerFrameView(master, model.get_player(1), 1, colour_p2)
        self.player2.player_frame.grid(row=0, column=1)

        self.restart_button = Button(master, text='\n'.join(list("RESTART")), font=Font(size=15, weight='bold'))
        self.restart_button.grid(row=0, column=2, sticky=S + N)

        self.record_button = Button(master, text="Record", relief=RAISED, font=Font(size=15))
        self.record_button.grid(row=1, columnspan=2, sticky=S + N + E + W)

        self.scroll = Scrollbar(master, orient='vertical')
        self.record_frame = Frame(master, bd=1, relief=SUNKEN)
        self.record = RecordView(self.record_frame, model, (colour_p1, colour_p2), self.scroll)

        self.scroll.grid(row=2, column=2, sticky="nsew")
        self.record_frame.grid(row=2, columnspan=2)

        self.scroll.grid_remove()
        self.record_frame.grid_remove()

        self.master = master

    def addController(self, controller: Controller):
        self.player1.add_controller(controller)
        self.player2.add_controller(controller)
        self.record_button.bind("<Button>", controller.btn_record)
        self.restart_button.bind("<1>", controller.btn_restart)


if __name__ == "__main__":
    master = Tk()
    PrincipalView(master, Game())
    master.mainloop()
