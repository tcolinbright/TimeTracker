import tkinter as tk
from datetime import timedelta

class TimerWidget(tk.Frame):
    def __init__(self, master, label, **kwargs):
        super().__init__(master, **kwargs)
        self.time = 0
        self.is_running = False
        self.label_text = tk.StringVar()
        self.label_text.set(label)

        self.timer_label = tk.Label(self, textvariable=self.label_text, font=("Arial", 14))
        self.timer_label.grid(row=0, column=0)

        self.time_label = tk.Label(self, text=self.format_time(self.time), font=("Arial", 14))
        self.time_label.grid(row=0, column=1)

        self.start_button = tk.Button(self, text="Start", bg="green", font=("Arial", 12), command=self.start)
        self.start_button.grid(row=0, column=2)

        self.stop_button = tk.Button(self, text="Stop", bg="red", font=("Arial", 12), command=self.stop)
        self.stop_button.grid(row=0, column=3)

        self.reset_button = tk.Button(self, text="Reset", bg="gray", font=("Arial", 12), command=self.reset)
        self.reset_button.grid(row=0, column=4)

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


class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Timer")
        self.timers = []
        self.total_elapsed = 0

        self.total_elapsed_label = tk.Label(master, text="Total Elapsed: 00:00:00", font=("Arial", 14))
        self.total_elapsed_label.pack(pady=10)

        self.create_timer_button = tk.Button(master, text="Create Timer", bg="blue", font=("Arial", 12), command=self.create_timer)
        self.create_timer_button.pack(pady=10)

    def create_timer(self):
        label = f"Timer {len(self.timers) + 1}:"
        timer_widget = TimerWidget(self.master, label)
        timer_widget.pack(pady=5)
        self.timers.append(timer_widget)
        self.update_total_elapsed()

    def update_total_elapsed(self):
        self.total_elapsed = sum([timer.time for timer in self.timers])
        self.total_elapsed_label.configure(text=f"Total Elapsed: {str(timedelta(seconds=self.total_elapsed))}")
        self.master.after(1000, self.update_total_elapsed)

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = TimerApp(root)
    root.mainloop()
