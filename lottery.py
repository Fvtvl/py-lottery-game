import random
import tkinter as tk


class LotteryGame:
    def __init__(self, master):
        self.master = master
        self.master = master
        self.master.title("Lottery Game")
        master.geometry("1000x720+0+0")

        # create labels for displaying game info
        self.title_label = tk.Label(
            self.master, text="Lottery Game", font=("Arial Bold", 20)
        )
        self.title_label.grid(row=0, column=0, columnspan=6, pady=10)

        self.user_label = tk.Label(
            self.master, text="Your numbers:", font=("Arial", 14)
        )
        self.user_label.grid(row=1, column=0, padx=10, pady=5)
        self.winning_label = tk.Label(
            self.master, text="Winning numbers:", font=("Arial", 14)
        )
        self.winning_label.grid(row=2, column=0, padx=10, pady=5)
        self.matches_label = tk.Label(
            self.master, text="Matches:", font=("Arial", 14))
        self.matches_label.grid(row=3, column=0, padx=10, pady=5)
        self.percent_label = tk.Label(
            self.master, text="Match percentage:", font=("Arial", 14)
        )
        self.percent_label.grid(row=4, column=0, padx=10, pady=5)
        self.prize_label = tk.Label(
            self.master, text="Prize:", font=("Arial", 14))
        self.prize_label.grid(row=5, column=0, padx=10, pady=5)

        # create buttons for user input
        self.buttons = []
        for i in range(1, 51):
            button = tk.Button(
                self.master,
                text=str(i),
                command=lambda num=i: self.add_number(num),
                height=3,
                width=6,
                font=("Arial", 12),
                bg="white",
                fg="black",
            )
            row = (i - 1) // 10 + 6
            col = (i - 1) % 10
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)

        # create buttons for starting a new game and quitting
        self.new_game_button = tk.Button(
            self.master, text="New Game", command=self.new_game, font=("Arial", 14)
        )
        self.new_game_button.grid(row=16, column=0, columnspan=5, pady=10)
        self.quit_button = tk.Button(
            self.master, text="Quit", command=self.master.quit, font=("Arial", 14)
        )
        self.quit_button.grid(row=16, column=5, columnspan=5, pady=10)

        # initialize variables for game state
        self.user_numbers = []
        self.random_numbers = set(random.sample(range(1, 51), 6))
        self.matches = set()

    def add_number(self, num):
        if len(self.user_numbers) < 6 and num not in self.user_numbers:
            self.user_numbers.append(num)
            self.user_label.config(
                text="Your numbers: " +
                " ".join(str(num) for num in self.user_numbers)
            )
        if len(self.user_numbers) == 6:
            self.play_game()

    def play_game(self):
        self.matches = set(self.user_numbers).intersection(self.random_numbers)
        percent = int(len(self.matches) / 6 * 100)
        prize = 10 * percent
        self.winning_label.config(
            text="Winning numbers: " +
            " ".join(str(num) for num in self.random_numbers)
        )
        self.matches_label.config(
            text="Matches: " + " ".join(str(num) for num in self.matches)
        )
        self.percent_label.config(
            text="Match percentage: " + str(percent) + "%")
        self.prize_label.config(text="Prize: $" + str(prize))

    def new_game(self):
        self.user_numbers = []
        self.random_numbers = set(random.sample(range(1, 51), 6))
        self.matches = set()
        self.user_label.config(text="Your numbers:")
        self.winning_label.config(text="Winning numbers:")
        self.matches_label.config(text="Matches:")
        self.percent_label.config(text="Match percentage:")
        self.prize_label.config(text="Prize:")

        # reset button colors
        for button in self.buttons:
            button.config(bg="white", fg="black")

    def highlight_matches(self):
        for button in self.buttons:
            if int(button["text"]) in self.matches:
                button.config(bg="green", fg="white")

    def run(self):
        self.master.mainloop()


root = tk.Tk()
game = LotteryGame(root)
game.run()
