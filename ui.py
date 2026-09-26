import tkinter as tk
from tkinter import messagebox

from game_logic import TicTacToeGame

BG_OUTER = "#C9A9DD"
BG_CARD = "#FBF8FF"
PURPLE = "#8E6FA8"
PURPLE_DARK = "#6E4C8A"
YELLOW = "#FFEDA1"
YELLOW_HOVER = "#FFE07A"
YELLOW_TEXT = "#D9A400"
TEXT_DARK = "#4B3A5A"
WHITE = "#FFFFFF"

FONT_TITLE = ("Segoe UI", 24, "bold")
FONT_SUBTITLE = ("Segoe UI", 11)
FONT_STATUS = ("Segoe UI", 13, "bold")
FONT_CELL = ("Segoe UI", 32, "bold")
FONT_BUTTON = ("Segoe UI", 12, "bold")

game = TicTacToeGame()


def on_click(index):
    if not game.make_move(index):
        return

    symbol = game.board[index]
    color = PURPLE_DARK if symbol == "X" else YELLOW_TEXT
    buttons[index].config(text=symbol, fg=color, disabledforeground=color)

    if game.winner:
        for btn in buttons:
            btn.config(state="disabled")
        if game.winner == "Tie":
            status_label.config(text="It's a tie!")
            messagebox.showinfo("Game Over", "It's a tie!")
        else:
            status_label.config(text=f"Player {game.winner} wins!")
            messagebox.showinfo("Game Over", f"Player {game.winner} wins!")
    else:
        status_label.config(text=f"Player {game.current_player}'s turn")


def reset_game():
    game.reset()
    for btn in buttons:
        btn.config(text="", state="normal")
    status_label.config(text=f"Player {game.current_player}'s turn")


def on_hover(event):
    if event.widget["state"] == "normal":
        event.widget.config(bg=YELLOW_HOVER)


def on_leave(event):
    if event.widget["state"] == "normal":
        event.widget.config(bg=YELLOW)


window = tk.Tk()
window.title("Tic-Tac-Toe")
window.configure(bg=BG_OUTER)
window.resizable(False, False)

card = tk.Frame(window, bg=BG_CARD, padx=30, pady=25)
card.pack(padx=25, pady=25)

title_label = tk.Label(card, text="Tic • Tac • Toe", font=FONT_TITLE, bg=BG_CARD, fg=PURPLE_DARK)
title_label.pack()

subtitle_label = tk.Label(card, text="Play with a friend", font=FONT_SUBTITLE, bg=BG_CARD, fg=TEXT_DARK)
subtitle_label.pack(pady=(0, 12))

status_label = tk.Label(card, text="Player X's turn", font=FONT_STATUS, bg=BG_CARD, fg=PURPLE_DARK)
status_label.pack(pady=(0, 15))

board_frame = tk.Frame(card, bg=BG_CARD)
board_frame.pack()

buttons = []
for i in range(9):
    btn = tk.Button(
        board_frame, text="", font=FONT_CELL, width=3, height=1,
        bg=YELLOW, activebackground=YELLOW_HOVER,
        relief="flat", bd=0, cursor="hand2",
        highlightthickness=1, highlightbackground=BG_CARD,
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5, ipadx=8, ipady=8)
    btn.bind("<Enter>", on_hover)
    btn.bind("<Leave>", on_leave)
    buttons.append(btn)

reset_button = tk.Button(
    card, text="Restart", font=FONT_BUTTON,
    bg=PURPLE, fg=WHITE, activebackground=PURPLE_DARK,
    relief="flat", bd=0, padx=14, pady=8, cursor="hand2",
    command=reset_game
)
reset_button.pack(pady=(20, 0))

window.eval('tk::PlaceWindow . center')

window.mainloop()