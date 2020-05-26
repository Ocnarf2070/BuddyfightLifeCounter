from tkinter import *

from Controller import Controller
from Model import Game
from View import PrincipalView as View


def runApp(root):
    game = Game()
    view = View(root, game)
    controller = Controller(game, view)
    view.addController(controller)
    root.title("Life Counter")
    root.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    runApp(root)
