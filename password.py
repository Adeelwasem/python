import tkinter as tk

def check_password(event=None):
    password = entry.get()
    length = len(password)
    if length == 0:
        label_result.config(text="", bg="#f0f0f0")
    elif length <= 5:
        label_result.config(text="Weak", bg="red", fg="white")
    elif 6 <= length <= 8:
        label_result.config(text="Medium", bg="yellow", fg="black")
    elif 8 < length <= 12:
        label_result.config(text="Good", bg="green", fg="white")
    elif length > 12:
        label_result.config(text="Strong", bg="dark green", fg="white")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x400")

label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=20)

entry = tk.Entry(root, show="*", font=("Arial", 12))
entry.pack(pady=10)
entry.bind("<KeyRelease>", check_password)

label_result = tk.Label(root, text="", font=("Arial", 14, "bold"), width=15)
label_result.pack(pady=30)

root.mainloop()