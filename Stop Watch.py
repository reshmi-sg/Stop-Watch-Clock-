import tkinter as tk
import time

class Stopwatch:
    def _init_(self, root):
        self.root = root
        self.root.title("Stopwatch and Clock")
        
        # Stopwatch variables
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        
        # Stopwatch UI elements
        self.display = tk.Label(root, text="00:00:00", font=("Helvetica", 48), width=8)
        self.display.pack()

        # Start, Stop, Reset buttons for Stopwatch
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.TOP, pady=20)

        self.start_button = tk.Button(self.button_frame, text="Start", font=("Helvetica", 14), command=self.start)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(self.button_frame, text="Stop", font=("Helvetica", 14), command=self.stop)
        self.stop_button.grid(row=0, column=1, padx=10)

        self.reset_button = tk.Button(self.button_frame, text="Reset", font=("Helvetica", 14), command=self.reset)
        self.reset_button.grid(row=0, column=2, padx=10)


        # Clock display
        self.clock_display = tk.Label(root, text="", font=("Helvetica", 14))
        self.clock_display.pack(pady=60)

        self.update_clock()
        self.update_stopwatch()

    def start(self):
        """Start or resume the stopwatch."""
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")

    def stop(self):
        """Stop the stopwatch."""
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")

    def reset(self):
        """Reset the stopwatch."""
        self.elapsed_time = 0
        self.update_display(0)
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def update_display(self, elapsed_time):
        """Update the stopwatch display."""
        seconds = int(elapsed_time)
        minutes = seconds // 60
        hours = minutes // 60
        seconds %= 60
        minutes %= 60
        self.display.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

    def update_stopwatch(self):
        """Update the stopwatch every 100 ms."""
        if self.running:
            elapsed_time = time.time() - self.start_time
            self.update_display(elapsed_time)
        self.root.after(100, self.update_stopwatch)

    def update_clock(self):
        """Update the clock every second."""
        current_time = time.strftime("%H:%M:%S")
        self.clock_display.config(text=current_time)
        self.root.after(1000, self.update_clock)

# Create the Tkinter window and start the application
root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()
