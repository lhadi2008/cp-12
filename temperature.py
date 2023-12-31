import tkinter as tk

def fahrenheit_to_celsius():
    try:
        # Convert Fahrenheit to Celsius
        fahrenheit = float(ent_temperature.get())
        celsius = (fahrenheit - 32) * 5/9
        # Display the result
        lbl_result.config(text=f"{celsius:.2f} \N{DEGREE CELSIUS}")
    except ValueError:
        # Handle the case where the input is not a valid number
        lbl_result.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create a frame to hold the Fahrenheit entry widget and label
frm_entry = tk.Frame(master=window)

# Create an entry widget to accept the temperature in Fahrenheit
ent_temperature = tk.Entry(master=frm_entry, width=10)

# Create a label widget to display the degree symbol and the text "F"
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Arrange the entry and label widgets in the frame
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create a button widget to initiate the conversion process
btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius)

# Create a label widget to display the result of the conversion in Celsius
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Arrange the frame, button, and result label widgets
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Start the application
window.mainloop()
exit()
