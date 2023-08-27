import psutil
import tkinter as tk
from tkinter import Label
import threading
import time

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("System Monitor")

        self.cpu_label = Label(root, text="CPU 사용량:")
        self.cpu_label.pack()

        self.ram_label = Label(root, text="RAM 사용량:")
        self.ram_label.pack()

        self.update_labels()

    def update_labels(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        ram_percent = ram.percent

        self.cpu_label.config(text=f"CPU 사용량: {cpu_percent:.2f}%")
        self.ram_label.config(text=f"RAM 사용량: {ram_percent:.2f}%")

        self.root.after(1000, self.update_labels)

def main():
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
