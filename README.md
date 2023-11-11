Checkpoint Objective
 

Description: 

Build a simple temperature converter program using Python and Tkinter GUI framework. The program should convert temperature from Fahrenheit to Celsius.

Statement: 

You are tasked with building a temperature converter program using Python and Tkinter GUI framework that converts temperature from Fahrenheit to Celsius.

 

Instructions
Import the Tkinter module by writing import tkinter as tk at the beginning of your code.
Define a function named fahrenheit_to_celsius() that will be called when the conversion button is clicked. This function should convert the entered temperature from Fahrenheit to Celsius and display the result in the label.
Create a Tkinter window by writing window = tk.Tk(). Set the title of the window to "Temperature Converter" by writing window.title("Temperature Converter").
Set the window to a fixed size by writing window.resizable(width=False, height=False).
Create a frame to hold the Fahrenheit entry widget and label. Write frm_entry = tk.Frame(master=window) to create the frame.
Create an entry widget to accept the temperature in Fahrenheit. Write ent_temperature = tk.Entry(master=frm_entry, width=10) to create the entry widget.
Create a label widget to display the degree symbol and the text "F". Write lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}") to create the label widget.
Use the grid() geometry manager to arrange the entry and label widgets in the frame. Write ent_temperature.grid(row=0, column=0, sticky="e") and lbl_temp.grid(row=0, column=1, sticky="w") to arrange the widgets.
Create a button widget to initiate the conversion process. Write btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius) to create the button widget.
Create a label widget to display the result of the conversion in Celsius. Write lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}") to create the label widget.
Use the grid() geometry manager to arrange the frame, button, and result label widgets. Write frm_entry.grid(row=0, column=0, padx=10), btn_convert.grid(row=0, column=1, pady=10), and lbl_result.grid(row=0, column=2, padx=10) to arrange the widgets.
Call the mainloop() method of the window object to start the application.
Notes:

Make sure to use the float() method to convert the temperature entered in the entry widget to a float value.
Use the round() method to round off the Celsius value to two decimal places.
Use the \N{DEGREE CELSIUS} and \N{DEGREE FAHRENHEIT} Unicode characters to display the degree symbol in the label widgets.
Test your program by entering a temperature value in Fahrenheit and clicking the conversion button. Check if the converted value is correct.
Evaluation Specifics

Your instructor will evaluate your checkpoint based on the criterias mentioned below. All criteria are rated from 0 to 5

 Checkpoint Criteria

Implementation: Evaluate the student's ability to translate the problem statement and instructions into a functional program using Python and Tkinter. Check if the program works as expected, produces the correct output, and follows the requirements and guidelines specified in the exercise.
Interface Usability: Evaluate the student's ability to create a usable and intuitive user interface that meets the needs of the intended users. Check if the user interface provides clear instructions, feedback, and prompts, and if it is easy to navigate and interact with
Code Efficiency: Evaluate the student's ability to write efficient and optimized code that runs smoothly and quickly. Check if the student avoided unnecessary computations, optimized loops and data structures, and used built-in functions and modules whenever possible.
Error Prevention: Evaluate the student's ability to anticipate and prevent errors by implementing input validation, boundary checking, and other preventive measures. Check if the student used appropriate error handling techniques, such as try-except blocks, to catch and handle errors and prevent program crashes.
Checkpoint Assessment

Technical mastery
Work quality
Problem resolution
Deadline ( If not respected , automatically score is 0 )
