import tkinter as tk
from tkinter import messagebox, simpledialog
#import winsound

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe Game - لعبة X-O")

        self.player_x = simpledialog.askstring("Player Name", "Enter Player X Name:") or "Player X"
        self.player_o = simpledialog.askstring("Player Name", "Enter Player O Name:") or "Player O"
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.scores = {"X": 0, "O": 0}

        self.score_label = tk.Label(root, text=self.get_score_text(), font=("Arial", 14), bg="lightgray")
        self.score_label.grid(row=0, column=0, columnspan=3, sticky="we")

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    root, 
                    text=" ", 
                    font=("Arial", 30, "bold"), 
                    width=5, 
                    height=2,
                    bg="white",
                    fg="black",
                    command=lambda row=i, col=j: self.on_click(row, col)
                )
                button.grid(row=i+1, column=j, padx=2, pady=2)
                self.buttons.append(button)

        reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12, "bold"), bg="orange", command=self.reset_game)
        reset_button.grid(row=4, column=0, columnspan=3, sticky="we", pady=5)

    def get_score_text(self):
        return f"{self.player_x} (X): {self.scores['X']}     {self.player_o} (O): {self.scores['O']}"

    def on_click(self, row, col):
        index = row * 3 + col

        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, fg="blue" if self.current_player == "X" else "green")

            winner_cells = self.check_winner()
            if winner_cells:
                self.highlight_winner(winner_cells)
                winsound.MessageBeep()
                winner_name = self.player_x if self.current_player == "X" else self.player_o
                self.scores[self.current_player] += 1
                messagebox.showinfo("Winner", f"{winner_name} wins!")
                self.update_score()
                self.root.after(1500, self.reset_board)
            elif " " not in self.board:
                winsound.MessageBeep()
                messagebox.showinfo("Draw", "The game ended in a draw!")
                self.root.after(1500, self.reset_board)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        lines = [
            (0,1,2), (3,4,5), (6,7,8),  # rows
            (0,3,6), (1,4,7), (2,5,8),  # columns
            (0,4,8), (2,4,6)            # diagonals
        ]
        for a, b, c in lines:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return (a, b, c)
        return None

    def highlight_winner(self, cells):
        for index in cells:
            self.buttons[index].config(bg="lightgreen")

    def reset_board(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ", bg="white")
        self.current_player = "X"

    def reset_game(self):
        self.scores = {"X": 0, "O": 0}
        self.update_score()
        self.reset_board()

    def update_score(self):
        self.score_label.config(text=self.get_score_text())

# Launch game
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()