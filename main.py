import tkinter as tk
import os
from tkinter import messagebox, ttk
import datetime
from tkcalendar import DateEntry

def display_data(name, reason, date_ocurred, location_ocurred):
    print(f"Name: {name}")
    print(f"Reason: {reason}")
    print(f"Date Occurred: {date_ocurred}")
    print(f"Location: {location_ocurred}")

def formatted_name(name):
    value = name.strip().split()

    if len(value) < 2:
        return name
    
    first_name = value[0]
    rest = " ".join(value[1:])
    formatted_name = f"{rest}, {first_name}"
    return formatted_name


def create_folder(name):
    folder_name = formatted_name(name)

    base_path = os.path.join(os.getcwd(), "Potential Clients")
    full_path = os.path.join(base_path, folder_name)

    os.makedirs(base_path, exist_ok=True)
    os.makedirs(full_path, exist_ok=True)

    print(f"Folder create at: {full_path}")

    return full_path

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

    # if reasons_variable == "Burglary":
            #ask burglary questions
        # case "Driving under the influence (DUI)":
        #     #ask dui questions
        # case "Driving while intoxicated (DWI)":
        #     #ask dwi questions
        # case "Driving while suspended (DWS)":
        #     # ask dws questions
        # case "Parole":
        #     #ask parole questions
        # case "Probation":
        #     #ask probation questions
        # case "Traffic Violation":
        #     #ask numerous questions 
        # case "Other":
        #     #ask questions


    date_occurred_label = tk.Label(window, text="Date Occurred:")
    date_occurred_label.grid(row=2, column=0)
    date_occurred_entry = DateEntry(window, date_pattern='mm-dd-yyyy')
    #date_occurred_entry = tk.Entry(window) #ability to enter date, this way it is formatted the same eveyr time
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
        if reason == "Select a reason":
            reason = "NO REASON"
        if not date:
            date = "NO DATE"
        if not location:
            location = "NO LOCATION"

        display_data(name, reason, date, location)
        if name:
            create_folder(name)

        name_entry.delete(0, tk.END)
        reasons_variable.set("Select a reason")
        date_occurred_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)

        messagebox.showinfo("Success!", "Data submitted successfully")
    
    submit_button = tk.Button(window, text="Submit", command=submit)
    submit_button.grid(row=4, column=0, columnspan=2)

    window.mainloop()



if __name__ == "__main__":
    generate_UI()
    