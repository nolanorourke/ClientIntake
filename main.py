import tkinter as tk
from tkinter import messagebox, ttk
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
    reasons = [
        "Burglary",
        "Driving under the influence (DUI)",
        "Driving while intoxicated (DWI)",
        "Driving while suspended (DWS)",
        "Parole",
        "Probation",
        "Traffic Violation",
        "Other"
    ]
    reasons_variable = tk.StringVar()
    reasons_variable.set("Select a reason")

    #reason_entry = tk.Entry(window) #used to be the way to type in an entry, the more control the better
    reason_entry = tk.OptionMenu(window, reasons_variable, *reasons)
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
        reason = reasons_variable.get().strip()
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
        reasons_variable.set("Select a variable")
        date_occurred_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)

        messagebox.showinfo("Success!", "Data submitted successfully")
    
    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2)

    window.mainloop()

if __name__ == "__main__":
    generate_UI()
    