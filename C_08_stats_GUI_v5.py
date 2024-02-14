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
        self.user_scores = [20, 14, 14, 13, 14, 11, 20, 10, 20, 11]
        self.computer_scores = [12, 4, 6, 20, 20, 14, 10, 14, 16, 12]
        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()
        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)
        control_buttons = [
            ["#CC6600", "Help", "get help"],
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
        self.to_stats_btn = self.control_button_ref[1]

    def to_do(self, action):

        if action == "get stats":
            DisplayStats(self, self.user_scores, self.computer_scores)
        elif action == "get help":
            pass
        else:
            self.close_play()


class DisplayStats:
    def __init__(self, partner, user_scores, computer_scores):
        # setup dialogue box and background colour
        stats_bg_colour = "#DAE8FC"
        self.stats_box = Toplevel()
        # disable stats button
        partner.to_stats_btn.config(state=DISABLED)
        # If users press cross at top, closes stats and
        # 'releases' stats button
        self.stats_box.protocol('WM_DELETE WINDOW',
                                partial(self.close_stats, partner))
        self.stats_frame = Frame(self.stats_box, width=300,
                                 height=200,
                                 bg=stats_bg_colour)
        self.stats_frame.grid()
        self.stats_heading_label = Label(self.stats_frame,
                                         bg=stats_bg_colour,
                                         text="Statistics",
                                         font=("Arial", "14", "bold"))
        self.stats_heading_label.grid(row=0)
        stats_text = "Here are your game statistics"

        self.stats_text_label = Label(self.stats_frame, bg=stats_bg_colour,
                                      text=stats_text, wrap=350,
                                      justify="left")
        self.stats_text_label.grid(row=1, padx=10)

        self.data_frame = Frame(self.stats_frame, bg=stats_bg_colour, borderwidth=1, relief="solid")
        self.data_frame.grid(row=2, padx=10, pady=10)
        self.user_stats = self.get_stats(user_scores, "User")
        self.comp_stats = self.get_stats(computer_scores, "Computer")
        head_back = "#FFFFFF"
        odd_rows = "#C9D6E8"
        even_rows = stats_bg_colour
        row_names = ["", "Total", "Best Score", "Worst Score", "Average Score"]
        row_formats = [head_back, odd_rows, even_rows, odd_rows, even_rows]
        all_labels = []
        count = 0

        for item in range(0, len(self.user_stats)):
            all_labels.append([row_names[item], row_formats[count]])
            all_labels.append([self.user_stats[item], row_formats[count]])
            all_labels.append([self.comp_stats[item], row_formats[count]])
            count += 1

        for item in range(0, len(all_labels)):
            self.data_label = Label(self.data_frame, text=all_labels[item][0], bg=all_labels[item][1], width="10",
                                    height="2", padx=10)
            self.data_label.grid(row=item // 3, column=item % 3, padx=0, pady=0)

        self.dismiss_button = Button(self.stats_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_stats,
                                                     partner))

        self.dismiss_button.grid(row=5, padx=10, pady=10)

    @staticmethod
    def get_stats(score_list, entity):
        total_score = sum(score_list)
        best_score = max(score_list)
        worst_score = min(score_list)
        average = total_score / len(score_list)

        return [entity, total_score, best_score, worst_score, average]

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
