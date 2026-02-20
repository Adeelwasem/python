import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        inches = float(entry.get())
        cms = inches * 2.54
        result_label.config(text=f"{inches} inches = {cms:.2f} cm")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

app = tk.Tk()
app.title("Length Converter App")
app.geometry("400x400")
app.configure(bg="#2C3E50")

label_font = ("Helvetica", 14)
entry_font = ("Helvetica", 12)

label = tk.Label(app, text="Enter inches:", fg="white", bg="#2C3E50", font=label_font)
label.pack(pady=20)

entry = tk.Entry(app, font=entry_font)
entry.pack(pady=10)

button = tk.Button(app, text="Convert to CM", command=convert, bg="#E74C3C", fg="white", font=label_font)
button.pack(pady=20)

result_label = tk.Label(app, text="", fg="#2ECC71", bg="#2C3E50", font=("Helvetica", 16, "bold"))
result_label.pack(pady=30)

app.mainloop()