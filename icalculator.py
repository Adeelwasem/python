import tkinter as tk
import math

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())

        simple_interest = (principal * rate * time) / 100
        compound_interest = principal * (pow((1 + rate / 100), time)) - principal

        label_simple_result.config(text=f"Simple Interest: ₹{simple_interest:.2f}", fg="blue")
        label_compound_result.config(text=f"Compound Interest: ₹{compound_interest:.2f}", fg="red")

    except ValueError:
        label_simple_result.config(text="Invalid Input", fg="orange")
        label_compound_result.config(text="Invalid Input", fg="orange")

root = tk.Tk()
root.geometry("400x400")
root.title("Interest Calculator App")
root.configure(background="light yellow")

label_title = tk.Label(root, text="Interest Calculator", font=("Arial", 16, "bold"), bg="light yellow", fg="green")
label_title.pack(pady=10)

frame_input = tk.Frame(root, bg="light yellow")
frame_input.pack(pady=10)

label_principal = tk.Label(frame_input, text="Principal Amount:", bg="light yellow")
label_principal.grid(row=0, column=0, pady=5, sticky='e')
entry_principal = tk.Entry(frame_input, bg="white", fg="black")
entry_principal.grid(row=0, column=1, pady=5)

label_rate = tk.Label(frame_input, text="Rate of Interest (%):", bg="light yellow")
label_rate.grid(row=1, column=0, pady=5, sticky='e')
entry_rate = tk.Entry(frame_input, bg="white", fg="black")
entry_rate.grid(row=1, column=1, pady=5)

label_time = tk.Label(frame_input, text="Time (Years):", bg="light yellow")
label_time.grid(row=2, column=0, pady=5, sticky='e')
entry_time = tk.Entry(frame_input, bg="white", fg="black")
entry_time.grid(row=2, column=1, pady=5)

button_calculate = tk.Button(root, text="Calculate Interest", command=calculate_interest, bg="blue", fg="white", font=("Arial", 12, "bold"))
button_calculate.pack(pady=15)

label_simple_result = tk.Label(root, text="Simple Interest: ₹0.00", font=("Arial", 12), bg="light yellow")
label_simple_result.pack(pady=5)

label_compound_result = tk.Label(root, text="Compound Interest: ₹0.00", font=("Arial", 12), bg="light yellow")
label_compound_result.pack(pady=5)

root.mainloop()