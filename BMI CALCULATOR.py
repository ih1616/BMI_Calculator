import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = int(weight_entry.get())
        height = int(height_entry.get())
        name = name_entry.get()

        BMI = (weight * 703) / (height * height)

        if BMI > 0:
            if BMI < 18.5:
                result = f"{name}, you are underweight."
            elif BMI <= 24.9:
                result = f"{name}, you are normal weight."
            elif BMI <= 29.9:
                result = f"{name}, you are overweight. Start considering to exercise and eat healthier."
            elif BMI <= 34.9:
                result = f"{name}, you are obese."
            elif BMI <= 39.9:
                result = f"{name}, you are severely obese."
            else:
                result = f"{name}, you are morbidly obese."
        else:
            result = "Enter valid input."

        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid input for weight and height.")

root = tk.Tk()
root.title("BMI Calculator")

name_label = tk.Label(root, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

weight_label = tk.Label(root, text="Enter your weight in pounds:")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Enter your height in inches:")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()