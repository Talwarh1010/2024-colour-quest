from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random


# users choose 3, 5 or 10 rounds
class ChooseRounds:
    def __init__(self):
        # invoke play class with three rounds for testing purposes
        self.to_play(3)

    def to_play(self, num_rounds):
        Play(num_rounds)
        # Hide root window (ie: hide rounds choice window).
        root.withdraw()


class Play:
    def __init__(self, how_many):
        self.play_box = Toplevel()
        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()
        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)
        control_buttons = [
            ["#CC6600", "stats", "get stats"],
            ["#004C99", "Statistics", "get stats"],
            ["#808080", "Start Over", "start over"]]

        self.control_button_ref = []

        for item in range(0, 3):
            self.make_control_button = Button(self.control_frame,
                                              fg="#FFFFFF",
                                              bg=control_buttons[item][0],
                                              text=control_buttons[item][1],
                                              width=11, font=("Arial", "12", "bold"),
                                              command=lambda i=item: self.to_do(control_buttons[i][2]))
            self.make_control_button.grid(row=0, column=item, padx=5, pady=5)

            self.control_button_ref.append(self.make_control_button)
        self.to_stats_btn = self.control_button_ref[0]

    def to_do(self, action):

        if action == "get stats":
            Displaystats(self, self.user_scores, self.computer_scores)
        elif action == "get stats":
            pass
        else:
            self.close_play()


class DisplayStats:
    def __init__(self, partner, user_scores, computer_scores):
        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.stats_box = Toplevel()
        # disable stats button
        partner.to_stats_btn.config(state=DISABLED)
        # If users press cross at top, closes stats and
        # 'releases' stats button
        self.stats_box.protocol('WM_DELETE WINDOW',
                                partial(self.close_stats, partner))
        self.stats_frame = Frame(self.stats_box, width=300,
                                 height=200,
                                 bg=background)
        self.stats_frame.grid()
        self.stats_heading_label = Label(self.stats_frame,
                                         bg=background,
                                         text="stats / Hints",
                                         font=("Arial", "14", "bold"))
        self.stats_heading_label.grid(row=0)
        stats_text = (""" Your goal in this game is to beat the computer and you have an
advantage - you get to choose your colour first. The points
associated with the colours are based on the colour's hex code.\n
The higher the value of the colour, the greater your score. To see
your statistics, click on the 'Statistics' button.\n
Win the game by scoring more than the computer overall. Don't
be discouraged if you don't win every round, it's your overall
score that counts. \n

Good luck! Choose carefully.""")

        self.stats_text_label = Label(self.stats_frame, bg=background,
                                      text=stats_text, wrap=350,
                                      justify="left")
        self.stats_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.stats_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_stats,
                                                     partner))

        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes stats dialogue (used by button and x at top of dialogue)
    def close_stats(self, partner):
        # Put stats button back to normal...
        partner.to_stats_btn.config(state=NORMAL)
        self.stats_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    ChooseRounds()
    root.mainloop()
