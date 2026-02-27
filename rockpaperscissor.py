import tkinter as tk
import random

def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    
    if user_choice == computer_choice:
        result = "Tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    
    result_label.config(text=f"Computer: {computer_choice}\nResult: {result}")

root = tk.Tk()
root.title("Rock Paper Scissor App")
root.geometry("400x400")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play("Rock"))
rock_btn.pack(side=tk.LEFT, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play("Paper"))
paper_btn.pack(side=tk.LEFT, padx=10)

scissor_btn = tk.Button(button_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play("Scissors"))
scissor_btn.pack(side=tk.LEFT, padx=10)

result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14), fg="blue")
result_label.pack(pady=40)

root.mainloop()