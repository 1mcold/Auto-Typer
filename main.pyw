"""

Auto Typer — a program for automatic text typing.

Copyright (C) 2025 - 1mcold
This code is distributed under the GNU General Public License v3.0.
You are free to use, modify, and distribute it,
but you must keep the source code open.

Created by 1mcold
GitHub: https://github.com/1mcold

"""

import tkinter as tk
import threading
import time
import pyautogui

class AutoTyperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Typer")
        self.root.geometry("800x600")
        self.root.iconphoto(False, tk.PhotoImage(file="icon/icon.png"))

        custom_font = ("Rubik Light", 13)
        backgroundcolor = "#D09C74"
        foregroundcolor = "#FDEFD6"
        selectbackgroundcolor = "#FFBF8E"
        selectforegroundcolor = "#FDEFD6"
        
        self.text_widget = tk.Text(root, font=custom_font, bg=backgroundcolor, fg=foregroundcolor, 
                                   borderwidth=0, highlightthickness=0, insertbackground="white",
                                   selectbackground=selectbackgroundcolor, selectforeground=selectforegroundcolor)
        self.text_widget.pack(expand=True, fill=tk.BOTH)
        
        self.is_typing = False
        self.thread = None
        
        self.root.bind("<Control-b>", self.toggle_typing)
    
    def type_text(self, text):
        time.sleep(3)
        for char in text:
            if not self.is_typing:
                break
            if char == " ":
                pyautogui.press("space")
            elif char == "\t":
                pyautogui.press("tab")
            elif char == "\n":
                pyautogui.press("enter")
            else:
                pyautogui.write(char, interval=0.01)  
            time.sleep(0.06)
    
    def toggle_typing(self, event=None):
        if self.is_typing:
            self.is_typing = False
        else:
            self.is_typing = True
            text = self.text_widget.get("1.0", tk.END).rstrip()
            self.thread = threading.Thread(target=self.type_text, args=(text,), daemon=True)
            self.thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoTyperApp(root)
    root.mainloop()
