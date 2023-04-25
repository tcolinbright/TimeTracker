import tkinter as tk
from datetime import timedelta

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Timer")

        self.time = 0
        self.is_running = False

        self.time_label = tk.Label(master, text=self.format_time(self.time), font=("Arial", 30))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start", bg="green", font=("Arial", 16), command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(master, text="Stop", bg="red", font=("Arial", 16), command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(master, text="Reset", bg="gray", font=("Arial", 12), command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def update_time(self):
        if self.is_running:
            self.time += 1
            self.time_label.configure(text=self.format_time(self.time))
            self.master.after(1000, self.update_time)

    def format_time(self, time):
        return str(timedelta(seconds=time))

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.update_time()

    def stop(self):
        self.is_running = False

    def reset(self):
        self.is_running = False
        self.time = 0
        self.time_label.configure(text=self.format_time(self.time))

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = TimerApp(root)
    root.mainloop()
