import tkinter as tk

def calculate_tip():
    bill = float(bill_entry.get())
    occupation_type = occupation_var.get()
    
    if occupation_type == 'Restaurants' or occupation_type == 'Food delivery' or occupation_type == 'Hotel service':
        tip_percent = 15
    elif occupation_type == 'Driver' or occupation_type == 'Dressing Parlour':
        tip_percent = 10
    elif occupation_type == 'Home service':
        tip_percent = 5
    else:
        tip_percent = 0

    tip = (tip_percent / 100) * bill
    total_bill = bill + tip
    
    result_label.config(text=f"Bill: {bill}\nTip Percent: {tip_percent}%\nTotal Bill: {total_bill}")

# Create the main window
root = tk.Tk()
root.title("Tip Calculator")

# Bill entry
bill_label = tk.Label(root, text="Enter the bill:")
bill_label.pack()
bill_entry = tk.Entry(root)
bill_entry.pack()

# Occupation dropdown
occupation_label = tk.Label(root, text="Select occupation type:")
occupation_label.pack()
occupation_var = tk.StringVar(root)
occupation_var.set("Restaurants")  # Default value
occupations = ['Restaurants', 'Food delivery', 'Hotel service', 'Driver', 'Dressing Parlour', 'Home service']
occupation_dropdown = tk.OptionMenu(root, occupation_var, *occupations)
occupation_dropdown.pack()

# Calculate button
calculate_button = tk.Button(root, text="Calculate Tip", command=calculate_tip)
calculate_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
