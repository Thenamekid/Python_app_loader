import tkinter as tk
import random

# Function to generate a random number
def generate_random_number():
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    if min_val <= max_val:
        random_num = random.randint(min_val, max_val)
        result_label.config(text=f"Random Number: {random_num}")
    else:
        result_label.config(text="Min value must be less than or equal to Max value")

# Create the main application window
app = tk.Tk()
app.title("Random Number Generator")
app.geometry("330x200")

# Create and pack widgets with improved spacing
min_label = tk.Label(app, text="Min Value:")
min_label.pack(pady=5)

min_entry = tk.Entry(app)
min_entry.pack(pady=5)

max_label = tk.Label(app, text="Max Value:")
max_label.pack(pady=5)

max_entry = tk.Entry(app)
max_entry.pack(pady=5)

generate_button = tk.Button(app, text="Generate Random Number", command=generate_random_number)
generate_button.pack(pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=5)

# Start the Tkinter main loop
app.mainloop()
