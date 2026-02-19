import tkinter as tk
from datetime import date

def calculate_age():
    try:
        user_name = name_entry.get()
        birth_day = int(day_entry.get())
        birth_month = int(month_entry.get())
        birth_year = int(year_entry.get())

        today = date.today()
        age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
        
        result_label.config(text=f"Hello {user_name}!\nYou are {age} years old.", fg="#f1c40f")
    except ValueError:
        result_label.config(text="Please enter valid numbers!", fg="#e74c3c")

window= tk.Tk()
window.title("Age Calculator App")
window.geometry("400x400")
window.configure(bg="#34495e")

header = tk.Label(window, text="Age Calculator", font=("Arial", 20, "bold"), bg="#34495e", fg="#ecf0f1")
header.pack(pady=20)

input_frame = tk.Frame(window, bg="#34495e")
input_frame.pack(pady=10)

def create_row(text, row):
    lbl = tk.Label(input_frame, text=text, font=("Arial", 12), bg="#34495e", fg="#ecf0f1", width=8, anchor="e")
    lbl.grid(row=row, column=0, padx=5, pady=5)
    ent = tk.Entry(input_frame, font=("Arial", 12))
    ent.grid(row=row, column=1, padx=5, pady=5)
    return ent

name_entry = create_row("Name:", 0)
day_entry = create_row("Date:", 1)
month_entry = create_row("Month:", 2)
year_entry = create_row("Year:", 3)

calc_btn = tk.Button(window, text="Calculate Age", font=("Arial", 12, "bold"), bg="#1abc9c", fg="white", command=calculate_age)
calc_btn.pack(pady=20)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#34495e")
result_label.pack(pady=10)

window.mainloop()