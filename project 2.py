import tkinter as tk
from tkinter import ttk

# Mocked Exchange Rates (Static Values, Base = USD)
exchange_rates = {
    "USD": 1,
    "INR": 83,
    "EUR": 0.92,
    "GBP": 0.79,
    "AED": 3.67,
    "JPY": 156.5,
    "AUD": 1.53,
    "CAD": 1.36
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        source = source_var.get()
        target = target_var.get()

        if source == "" or target == "":
            result_label.config(text="Select both currencies!", fg="red")
            return

        # Convert source → USD → target
        amount_in_usd = amount / exchange_rates[source]
        converted_amount = amount_in_usd * exchange_rates[target]

        result_label.config(
            text=f"Converted Amount: {round(converted_amount, 2)} {target}",
            fg="#0047AB"  # nice blue
        )

    except ValueError:
        result_label.config(text="Enter a valid number!", fg="red")


# ------------------------------
# GUI WINDOW SETUP
# ------------------------------
app = tk.Tk()
app.title("Currency Converter App")
app.geometry("360x350")
app.configure(bg="#f2f2f2")
app.resizable(False, False)

# Title
title = tk.Label(
    app,
    text="💱 Currency Converter",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2",
    fg="#333"
)
title.pack(pady=15)

# Amount Label + Entry
tk.Label(app, text="Enter Amount:", font=("Arial", 12), bg="#f2f2f2").pack()
amount_entry = tk.Entry(app, font=("Arial", 13), width=18)
amount_entry.pack(pady=5)

# From Currency Dropdown
tk.Label(app, text="From Currency:", font=("Arial", 12), bg="#f2f2f2").pack(pady=(10, 0))
source_var = tk.StringVar()
source_dropdown = ttk.Combobox(
    app,
    textvariable=source_var,
    values=list(exchange_rates.keys()),
    state="readonly",
    font=("Arial", 11),
    width=15
)
source_dropdown.pack()

# To Currency Dropdown
tk.Label(app, text="To Currency:", font=("Arial", 12), bg="#f2f2f2").pack(pady=(10, 0))
target_var = tk.StringVar()
target_dropdown = ttk.Combobox(
    app,
    textvariable=target_var,
    values=list(exchange_rates.keys()),
    state="readonly",
    font=("Arial", 11),
    width=15
)
target_dropdown.pack()

# Convert Button
convert_btn = tk.Button(
    app,
    text="Convert",
    font=("Arial", 12, "bold"),
    bg="#0047AB",
    fg="white",
    width=12,
    command=convert_currency
)
convert_btn.pack(pady=18)

# Result Label
result_label = tk.Label(app, text="", font=("Arial", 14, "bold"), bg="#f2f2f2")
result_label.pack(pady=5)

app.mainloop()
