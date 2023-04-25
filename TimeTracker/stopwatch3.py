import tkinter as tk
from datetime import timedelta

class TimerWidget(tk.Frame):
    def __init__(self, master, label, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
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

        self.remove_button = tk.Button(self, text="Remove", bg="orange", font=("Arial", 12), command=self.remove)
        self.remove_button.grid(row=0, column=5)

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

    def remove(self):
        self.stop()
        self.master.timers.remove(self)
        self.destroy()

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Timer")
        self.timers = []
        self.total_elapsed = 0

        self.total_elapsed_label = tk.Label(master, text="Total Elapsed: 00:00:00", font=("Arial", 14))
        self.total_elapsed_label.pack(pady=10)

        self.create_timer_button = tk.Button(master, text="Create Timer", bg="blue", font=("Arial", 12), command=self.open_label_window)
        self.create_timer_button.pack(pady=10)

    def open_label_window(self):
        self.label_window = tk.Toplevel(self.master)
        self.label_window.title("Enter Timer Label")
        
        self.label_entry = tk.Entry(self.label_window, font=("Arial", 12))
        self.label_entry.pack(padx=10, pady=10)
        
        self.submit_label_button = tk.Button(self.label_window, text="Submit", bg="blue", font=("Arial", 12), command=self.create_timer)
        self.submit_label_button.pack(pady=5)

    def create_timer(self):
        label = self.label_entry.get()
        if not label:
            label = f"Timer {len(self.timers) + 1}:"
        
        timer_widget = TimerWidget(self.master, label)
        timer_widget.pack(pady=5)
        self.timers.append(timer_widget)
        self.update_total_elapsed()
        
        self.label_window.destroy()

    def update_total_elapsed(self):
        self.total_elapsed = sum([timer.time for timer in self.timers if timer.winfo_exists()])
        self.total_elapsed_label.configure(text=f"Total Elapsed: {str(timedelta(seconds=self.total_elapsed))}")
        self.master.after(1000, self.update_total_elapsed)

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = TimerApp(root)
    root.mainloop()
