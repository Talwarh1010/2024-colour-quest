from tkinter import *


class ChooseRounds:

    def __init__(self):
        button_font = ("Arial", "13", "bold")
        button_fg = "#FFFFFF"
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()
        self.colour_frame = Frame(self.intro_frame)
        self.colour_frame.grid(row=2)
        self.colour_heading = Label(self.intro_frame,
                                    text="Colour Quest",
                                    font=("Arial", "16", "bold")
                                    )
        self.colour_heading.grid(row=0)

        instructions = "In each round you will be given six different colours to choose from. Pick a colour" \
                       " and see if you can beat the computer's score!" \
                       " \nTo begin, choose how many rounds you'd like to play..."
        self.display_instructions = Label(self.intro_frame,
                                          text=instructions,

                                          wraplength=300,
                                          justify="left")

        self.display_instructions.grid(row=1)

        btn_colour_value = [["#CC0000", 3], ["#CC0000", 5], ["#CC0000", 10]]

        for item in range(0, 3):
            self.rounds_button = Button(self.colour_frame,
                                        text="10 Rounds",
                                        bg=btn_colour_value[item][0],
                                        fg=button_fg,
                                        font=button_font,
                                        width=10, )


if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    ChooseRounds()
    root.mainloop()
