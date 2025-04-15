import tkinter as tk
from tkinter import messagebox

# Function to calculate simple and compound interest
def calculate_interest():
    try:
        p = float(principal_entry.get())
        t = float(time_entry.get())
        r = float(rate_entry.get())

        # Simple Interest formula
        si = (p * t * r) / 100

        # Compound Interest formula (compounded annually)
        ci = p * ((1 + r / 100) ** t) - p

        result_label.config(
            text=f"Simple Interest: ₹{si:.2f}\nCompound Interest: ₹{ci:.2f}"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create main window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Simple & Compound Interest Calculator", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Principal amount
tk.Label(root, text="Principal Amount (₹):").pack()
principal_entry = tk.Entry(root)
principal_entry.pack()

# Time period
tk.Label(root, text="Time Period (years):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

# Rate of interest
tk.Label(root, text="Rate of Interest (%):").pack()
rate_entry = tk.Entry(root)
rate_entry.pack()

# Calculate button
calc_button = tk.Button(root, text="Calculate Interest", command=calculate_interest)
calc_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
