
import tkinter as tk
from tkinter import messagebox
import copy

PLAYER = "X"
AI = "O"

class TicTacToe:
    def _init_(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - AI vs You")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text=" ", font="Helvetica 32", width=5, height=2,
                                command=lambda r=i, c=j: self.player_move(r, c))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def player_move(self, row, col):
        if self.board[row][col] == " ":
            self.buttons[row][col].config(text=PLAYER, state="disabled")
            self.board[row][col] = PLAYER
            if self.check_winner(self.board) or self.is_full(self.board):
                self.end_game()
            else:
                self.root.after(500, self.ai_move)  # slight delay for better UX

    def ai_move(self):
        best = self.best_move(self.board)
        if best:
            row, col = best
            self.board[row][col] = AI
            self.buttons[row][col].config(text=AI, state="disabled")
            if self.check_winner(self.board) or self.is_full(self.board):
                self.end_game()

    def check_winner(self, board):
        for line in board + list(zip(*board)):
            if line[0] == line[1] == line[2] != " ":
                return line[0]
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]
        return None

    def is_full(self, board):
        return all(cell != " " for row in board for cell in row)

    def minimax(self, board, is_max):
        winner = self.check_winner(board)
        if winner == AI:
            return 1
        elif winner == PLAYER:
            return -1
        elif self.is_full(board):
            return 0

        if is_max:
            best = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = AI
                        val = self.minimax(board, False)
                        board[i][j] = " "
                        best = max(best, val)
            return best
        else:
            best = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = PLAYER
                        val = self.minimax(board, True)
                        board[i][j] = " "
                        best = min(best, val)
            return best

    def best_move(self, board):
        best_val = -float('inf')
        move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = AI
                    move_val = self.minimax(board, False)
                    board[i][j] = " "
                    if move_val > best_val:
                        best_val = move_val
                        move = (i, j)
        return move

    def end_game(self):
        winner = self.check_winner(self.board)
        if winner:
            messagebox.showinfo("Game Over", f"{winner} wins!")
        else:
            messagebox.showinfo("Game Over", "It's a draw!")
        self.root.after(100, self.reset_game)

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for btn in row:
                btn.config(text=" ", state="normal")

if __name__ == "_main_":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()