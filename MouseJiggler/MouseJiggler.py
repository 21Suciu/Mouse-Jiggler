import pyautogui
import time
import threading
import tkinter as tk
from tkinter import messagebox


class MouseJigglerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Jiggler")

        self.running = False
        self.interval = tk.IntVar(value=10)
        self.movement_distance = tk.IntVar(value=5)

        tk.Label(root, text='Interval (seconds):').grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.interval).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text='Movement Distance (pixels):').grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(root, textvariable=self.movement_distance).grid(row=1, column=1, padx=10, pady=5)

        self.start_button = tk.Button(root, text='Start', command=self.start_jiggler)
        self.start_button.grid(row=2, column=0, padx=10, pady=10)

        self.stop_button = tk.Button(root, text='Stop', command=self.stop_jiggler, state=tk.DISABLED)
        self.stop_button.grid(row=2, column=1, padx=10, pady=10)

    def jiggle_mouse(self):
        try:
            while self.running:
                x, y = pyautogui.position()
                pyautogui.moveTo(x + self.movement_distance.get(), y)
                time.sleep(0.5)
                pyautogui.moveTo(x, y)
                time.sleep(self.interval.get() - 0.5)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def start_jiggler(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        threading.Thread(target=self.jiggle_mouse, daemon=True).start()

    def stop_jiggler(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = MouseJigglerApp(root)
    root.mainloop()
