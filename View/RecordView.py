from tkinter import *
from tkinter.font import Font

from Model import Game


class RecordView:
    def __init__(self, master: Frame, model: Game, colours, scroll: Scrollbar):
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        master.columnconfigure(3, weight=1)
        master.rowconfigure(0, weight=1)

        height = 10
        width = 5
        font = Font(size=20)

        rp1 = model.get_player(0).last_update()
        rp2 = model.get_player(1).last_update()

        self.record_player1_1 = Text(master, font=font, relief=FLAT, height=height, width=width, bg=colours[0])
        self.record_player1_1.tag_configure("center", justify='center')
        self.record_player1_1.insert(END, rp1[0], 'center')
        self.record_player1_1.grid(row=0, column=0, sticky="nsew")

        self.record_player1_2 = Text(master, font=font, relief=FLAT, height=height, width=width, bg=colours[0])
        self.record_player1_2.tag_configure("center", justify='center')
        self.record_player1_2.insert(END, rp1[1], 'center')
        self.record_player1_2.grid(row=0, column=1, sticky="nsew")

        self.record_player2_1 = Text(master, font=font, relief=FLAT, height=height, width=width, bg=colours[1])
        self.record_player2_1.tag_configure("center", justify='center')
        self.record_player2_1.insert(END, rp2[0], 'center')
        self.record_player2_1.grid(row=0, column=2, sticky="nsew")

        self.record_player2_2 = Text(master, font=font, relief=FLAT, height=height, width=width, bg=colours[1])
        self.record_player2_2.tag_configure("center", justify='center')
        self.record_player2_2.insert(END, rp2[1], 'center')
        self.record_player2_2.grid(row=0, column=3, sticky="nsew")

        self.record_player1_1.tag_configure("red", foreground='red')  # Drain life
        self.record_player1_1.tag_configure("green", foreground='green')  # Obtain life
        self.record_player1_1.tag_configure("blue", foreground='blue')  # Buddy Call
        self.record_player2_1.tag_configure("red", foreground='red')
        self.record_player2_1.tag_configure("green", foreground='green')
        self.record_player2_1.tag_configure("blue", foreground='blue')

        scroll.config(command=lambda *args: self.onscroll(*args))
        self.record_player1_1.configure(yscrollcommand=scroll.set)
        self.record_player1_2.configure(yscrollcommand=scroll.set)
        self.record_player2_1.configure(yscrollcommand=scroll.set)
        self.record_player2_2.configure(yscrollcommand=scroll.set)

    def onscroll(self, *args):
        self.record_player1_1.yview(*args)
        self.record_player1_2.yview(*args)
        self.record_player2_1.yview(*args)
        self.record_player2_2.yview(*args)


if __name__ == "__main__":
    root = Tk()
    game = Game()
    players = game.get_players()
    players[0].add_life(999)
    players[1].sub_life(1)
    RecordView(root, game, 'red', None)
    root.mainloop()
