import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def _init_(self, root):
        self.root = root
        self.root.title("لعبة X-O")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]

        # إنشاء أزرار اللعبة
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    root,
                    text=" ",
                    font=("Arial", 30),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.on_click(row, col)
                )
                button.grid(row=i, column=j)
                self.buttons.append(button)

        # زر إعادة اللعبة
        reset_button = tk.Button(root, text="إعادة اللعب", command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

    def on_click(self, row, col):
        index = row * 3 + col

        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("فوز", f"اللاعب {self.current_player} فاز!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("تعادل", "اللعبة انتهت بتعادل!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # خطوط الفوز الأفقية
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
                return True

        # خطوط الفوز العمودية
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return True

        # خطوط الفوز القطرية
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True

        return False

    def reset_game(self):
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")


# إنشاء النافذة الرئيسية
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
