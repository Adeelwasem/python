import tkinter as tk

def calculate_product():
    try:
        
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        
        
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, f"Result: {result}")
    except ValueError:
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, "Error: Please enter valid numbers")


window = tk.Tk()
window.title("Getting Started with Widgets")
window.geometry("400x300")
window.configure(bg="#f0f8ff")


desc_label = tk.Label(window, text="Product Calculator", bg="#f0f8ff", fg="#333", font=("Arial", 12, "bold"))
desc_label.pack(pady=5)


tk.Label(window, text="Enter first number:", bg="#f0f8ff", fg="#4b0082").pack()
entry1 = tk.Entry(window, bg="#ffffff", highlightthickness=1, highlightbackground="#4b0082")
entry1.pack(pady=2)


tk.Label(window, text="Enter second number:", bg="#f0f8ff", fg="#4b0082").pack()
entry2 = tk.Entry(window, bg="#ffffff", highlightthickness=1, highlightbackground="#4b0082")
entry2.pack(pady=2)


calc_btn = tk.Button(window, text="Calculate Product", command=calculate_product, 
                     bg="#4caf50", fg="white", font=("Arial", 10, "bold"), cursor="hand2")
calc_btn.pack(pady=15)


result_text = tk.Text(window, height=2, width=30, bg="#e1f5fe", font=("Courier", 10))
result_text.pack(pady=5)

window.mainloop()