from tkinter import *

from Model import Game
from View import PrincipalView


class Controller:
    def __init__(self, model: Game, view: PrincipalView):
        self.model = model
        self.view = view

    def btn_add(self, event, pos):
        self.add(pos)

    def btn_sub(self, event, pos):
        self.sub(pos)

    def btn_buddy_call(self, event, pos):
        self.buddy_call(pos)

    def btn_record(self, event):
        self.record()

    def btn_restart(self, event):
        self.restart()

    def add(self, pos):
        # Pass data to view
        if pos == 0 and not self.view.player1.entry.get() == "":
            amount = int(self.view.player1.entry.get())
            self.model.get_player(0).add_life(amount)
            self.view.player1.entry.delete(0, "end")
            self.view.player1.labelLife.config(text=str(self.model.get_player(0).get_life()))
            self.__update_record(pos)
        elif pos == 1 and not self.view.player2.entry.get() == "":
            amount = int(self.view.player2.entry.get())
            self.model.get_player(1).add_life(amount)
            self.view.player2.entry.delete(0, "end")
            self.view.player2.labelLife.config(text=str(self.model.get_player(1).get_life()))
            self.__update_record(pos)

    def sub(self, pos):
        changed = False
        if pos == 0 and not self.view.player1.entry.get() == "":
            amount = int(self.view.player1.entry.get())
            changed = self.model.get_player(0).sub_life(amount)
            self.view.player1.entry.delete(0, "end")
            self.view.player1.labelLife.config(text=str(self.model.get_player(0).get_life()))
        elif pos == 1 and not self.view.player2.entry.get() == "":
            amount = int(self.view.player2.entry.get())
            changed = self.model.get_player(1).sub_life(amount)
            self.view.player2.entry.delete(0, "end")
            self.view.player2.labelLife.config(text=str(self.model.get_player(1).get_life()))
        if changed:
            self.__update_record(pos)

    def buddy_call(self, pos):
        if pos == 0:
            self.model.get_player(0).buddy_call()
            self.view.player1.labelLife.config(text=str(self.model.get_player(0).get_life()))
            # self.view.player1.buddy_call_button.config(state=DISABLED)
            # self.view.player1.buddy_call_button.unbind("<Button>")
        else:
            self.model.get_player(1).buddy_call()
            self.view.player2.labelLife.config(text=str(self.model.get_player(1).get_life()))
            # self.view.player2.buddy_call_button.config(state=DISABLED)
            # self.view.player2.buddy_call_button.unbind("<Button>")
        self.__update_record(pos)

    def __update_record(self, pos):
        if pos == 0:
            change, amount = self.model.get_player(0).last_update()
            if not change.find('+') == -1:
                self.view.record.record_player1_1.insert(END, change, ('center', 'green'))
            elif not change.find('-') == -1:
                self.view.record.record_player1_1.insert(END, change, ('center', 'red'))
            else:
                self.view.record.record_player1_1.insert(END, change, ('center', 'blue'))
            self.view.record.record_player1_2.insert(END, amount, 'center')
        elif pos == 1:
            change, amount = self.model.get_player(1).last_update()
            if not change.find('+') == -1:
                self.view.record.record_player2_1.insert(END, change, ('center', 'green'))
            elif not change.find('-') == -1:
                self.view.record.record_player2_1.insert(END, change, ('center', 'red'))
            else:
                self.view.record.record_player2_1.insert(END, change, ('center', 'blue'))
            self.view.record.record_player2_2.insert(END, amount, 'center')

    def record(self):
        if self.view.record_button.cget("relief") == RAISED:
            self.view.record_frame.grid()
            self.view.scroll.grid()
            self.view.record_button.config(relief=SUNKEN)
        else:
            self.view.record_frame.grid_remove()
            self.view.scroll.grid_remove()
            self.view.record_button.config(relief=RAISED)

    def restart(self):
        self.model = self.model.restart()
        self.view.player1.labelLife.config(text=str(self.model.get_player(0).get_life()))
        self.view.player2.labelLife.config(text=str(self.model.get_player(1).get_life()))

        # self.view.player1.buddy_call_button.config(state=NORMAL)
        # self.view.player1.buddy_call_button.bind("<Button>", lambda event, args=0: self.btn_buddy_call(event, args))
        # self.view.player2.buddy_call_button.config(state=NORMAL)
        # self.view.player2.buddy_call_button.bind("<Button>", lambda event, args=1: self.btn_buddy_call(event, args))

        self.view.record.record_player1_1.delete("1.0", "end")
        self.view.record.record_player1_2.delete("1.0", "end")
        self.view.record.record_player2_1.delete("1.0", "end")
        self.view.record.record_player2_2.delete("1.0", "end")
        rp1 = self.model.get_player(0).last_update()
        rp2 = self.model.get_player(1).last_update()
        self.view.record.record_player1_1.insert(END, rp1[0], 'center')
        self.view.record.record_player1_2.insert(END, rp1[1], 'center')
        self.view.record.record_player2_1.insert(END, rp2[0], 'center')
        self.view.record.record_player2_2.insert(END, rp2[1], 'center')
