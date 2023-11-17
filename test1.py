import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class RentBikeForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Rent a Bike Form")

        # Create a frame for the start time widgets
        self.start_frame = ttk.Frame(self.master, padding="10")
        self.start_frame.place(relx=0.5, rely=0.3, anchor="center")

        # Add a label for the start time
        ttk.Label(self.start_frame, text="Start Time:").grid(row=0, column=0, padx=5, pady=5)

        # Add a combobox for the start time
        self.start_time = tk.StringVar()
        self.start_time.set("09:00 AM")
        start_time_combobox = ttk.Combobox(self.start_frame, textvariable=self.start_time, values=self._get_time_range(), state="readonly")
        start_time_combobox.grid(row=0, column=1, padx=5, pady=5)

        # Create a frame for the end time widgets
        self.end_frame = ttk.Frame(self.master, padding="10")
        self.end_frame.place(relx=0.5, rely=0.4, anchor="center")

        # Add a label for the end time
        ttk.Label(self.end_frame, text="End Time:").grid(row=0, column=0, padx=5, pady=5)

        # Add a combobox for the end time
        self.end_time = tk.StringVar()
        self.end_time.set("09:00 AM")
        end_time_combobox = ttk.Combobox(self.end_frame, textvariable=self.end_time, values=self._get_time_range(), state="readonly")
        end_time_combobox.grid(row=0, column=1, padx=5, pady=5)

        # Add a button to submit the form
        submit_button = ttk.Button(self.master, text="Submit", command=self.submit_form)
        submit_button.place(relx=0.5, rely=0.5, anchor="center")

    def _get_time_range(self):
        # Generate a list of time strings from 9:00 AM to 6:00 PM in 30-minute increments
        times = []
        current_time = datetime.strptime("09:00 AM", "%I:%M %p")
        end_time = datetime.strptime("06:00 PM", "%I:%M %p")
        while current_time <= end_time:
            times.append(current_time.strftime("%I:%M %p"))
            current_time += timedelta(minutes=30)
        return times

    def submit_form(self):
        # Get the selected start time and end time
        start_time = self.start_time.get()
        end_time = self.end_time.get()

        # Print the selected start time and end time
        print(f"Start Time: {start_time}, End Time: {end_time}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RentBikeForm(root)
    root.mainloop()