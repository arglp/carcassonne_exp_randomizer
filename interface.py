import tkinter as tk

class Button:
    def __init__ (self, text, command, bg="#fff1d9", fg="#775638"):
        self.text = text
        self.command = command
        self.bg = bg
        self.fg = fg
    
    def draw_button (self, root, canvas, x, y):
        btn = tk.Button (root, text=self.text, command=self.command, bg=self.bg, fg=self.fg)
        canvas.create_window(x, y, window=btn)

