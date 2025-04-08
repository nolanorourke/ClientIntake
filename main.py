import tkinter as tk
from tkinter import messagebox
import datetime

def display_data(name, reason, date_ocurred, location_ocurred):
    print(f"Name: {name}")
    print(f"Reason: {reason}")
    print(f"Date Occurred: {date_ocurred}")
    print(f"Location: {location_ocurred}")


def generate_UI():
    window = tk.Tk()
    window.title("Client Intake Form")    
    window_width = int(window.winfo_screenwidth() * .6)
    window_height = int(window.winfo_screenheight() * .6)
    window.geometry(f"{window_width}x{window_height}")

    name_label = tk.Label(window, text="Name:")
    name_label.grid(row=0, column=0)
    name_entry = tk.Entry(window)
    name_entry.grid(row=0, column=1)

    reason_label = tk.Label(window, text="Reason:")
    reason_label.grid(row=1, column=0)
    reason_entry = tk.Entry(window)
    reason_entry.grid(row=1, column=1)

    date_occurred_label = tk.Label(window, text="Date Occurred:")
    date_occurred_label.grid(row=2, column=0)
    date_occurred_entry = tk.Entry(window)
    date_occurred_entry.grid(row=2, column=1)

    location_label = tk.Label(window, text="Location:")
    location_label.grid(row=3, column=0)
    location_entry = tk.Entry(window)
    location_entry.grid(row=3, column=1)

    def submit():
        name = name_entry.get().strip()
        reason = reason_entry.get().strip()
        date = date_occurred_entry.get().strip()
        location = location_entry.get().strip()

        if not name:
            name = "NO NAME"
        if not reason:
            reason = "NO REASON"
        if not date:
            date = "NO DATE"
        if not location:
            location = "NO LOCATION"

        display_data(name, reason, date, location)

        name_entry.delete(0, tk.END)
        reason_entry.delete(0, tk.END)
        date_occurred_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)

        messagebox.showinfo("Success!", "Data submitted successfully")
    
    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2)

    window.mainloop()

if __name__ == "__main__":
    generate_UI()
    