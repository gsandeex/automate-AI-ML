# import tkinter as tk
# import subprocess

# def run_ml_model():
#     # Assuming your ML script is called 'ml_script.py'
#     subprocess.Popen(['python', 'ml-model.py'])

# # Create the main application window
# app = tk.Tk()
# app.title("ML Model Trigger")

# # Create a label
# label = tk.Label(app, text="Click the button to trigger the ML model:")
# label.pack()

# # Create a button to trigger the ML model
# button = tk.Button(app, text="Run ML Model", command=run_ml_model)
# button.pack()

# # Run the application
# app.mainloop()


###############################################

# import tkinter as tk
# import subprocess

# def run_ml_model():
#     # Get the input values from the entry widgets
#     input1_value = entry1.get()
#     input2_value = entry2.get()
#     input3_value = entry3.get()
#     input4_value = entry4.get()
#     input5_value = entry5.get()
    
#     # Assuming your ML script is called 'ml_script.py'
#     subprocess.Popen(['python', 'ml-model.py', input1_value, input2_value, input3_value, input4_value, input5_value])

# # Create the main application window
# app = tk.Tk()
# app.title("ML Model Trigger")

# # Create entry widgets for input values
# tk.Label(app, text="Input 1:").pack()
# entry1 = tk.Entry(app)
# entry1.pack()

# tk.Label(app, text="Input 2:").pack()
# entry2 = tk.Entry(app)
# entry2.pack()

# tk.Label(app, text="Input 3:").pack()
# entry3 = tk.Entry(app)
# entry3.pack()

# tk.Label(app, text="Input 4:").pack()
# entry4 = tk.Entry(app)
# entry4.pack()

# tk.Label(app, text="Input 5:").pack()
# entry5 = tk.Entry(app)
# entry5.pack()

# # Create a button to trigger the ML model
# button = tk.Button(app, text="Run ML Model", command=run_ml_model)
# button.pack()

# # Run the application
# app.mainloop()

#############################################

# import tkinter as tk
# from tkinter import ttk
# import subprocess

# def run_ml_model():
#     # Get the selected values from the dropdown menus
#     input1_value = dropdown1.get()
#     input2_value = dropdown2.get()
#     input3_value = dropdown3.get()
#     input4_value = dropdown4.get()
#     input5_value = dropdown5.get()
    
#     # Assuming your ML script is called 'ml_script.py'
#     subprocess.Popen(['python', 'ml_script.py', input1_value, input2_value, input3_value, input4_value, input5_value])

# # Create the main application window
# app = tk.Tk()
# app.title("ML Model Trigger")

# # Create dropdown menus for input values
# tk.Label(app, text="Input 1:").pack()
# dropdown1 = ttk.Combobox(app, values=["Option 1", "Option 2", "Option 3"])
# dropdown1.pack()

# tk.Label(app, text="Input 2:").pack()
# dropdown2 = ttk.Combobox(app, values=["Option A", "Option B", "Option C"])
# dropdown2.pack()

# tk.Label(app, text="Input 3:").pack()
# dropdown3 = ttk.Combobox(app, values=["Choice X", "Choice Y", "Choice Z"])
# dropdown3.pack()

# tk.Label(app, text="Input 4:").pack()
# dropdown4 = ttk.Combobox(app, values=["Value P", "Value Q", "Value R"])
# dropdown4.pack()

# tk.Label(app, text="Input 5:").pack()
# dropdown5 = ttk.Combobox(app, values=["Item Alpha", "Item Beta", "Item Gamma"])
# dropdown5.pack()

# # Create a button to trigger the ML model
# button = tk.Button(app, text="Run ML Model", command=run_ml_model)
# button.pack()

# # Run the application
# app.mainloop()

###################################

import tkinter as tk
from tkinter import ttk
import subprocess
import os
print(os.getcwd())
#os.chdir("C:\\Users\\GSANDEEX\\Downloads\\own-testing\\")
print(os.getcwd())

def run_ml_model():
    # Get the selected values from the dropdown menus
    input1_value = dropdown1.get()
    input2_value = dropdown2.get()
    input3_value = dropdown3.get()
    input4_value = dropdown4.get()
    input5_value = dropdown5.get()
    
    # Assuming your ML script is called 'ml_script.py'
    process = subprocess.Popen(['python', 'ml-model.py', input1_value, input2_value, input3_value, input4_value, input5_value],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    
    # Clear the console before displaying new logs
    console_output.delete('1.0', tk.END)
    
    # Display live logs in the console
    for stdout_line in iter(process.stdout.readline, ""):
        console_output.insert(tk.END, stdout_line)
        console_output.see(tk.END)
    
    for stderr_line in iter(process.stderr.readline, ""):
        console_output.insert(tk.END, stderr_line)
        console_output.see(tk.END)

# Create the main application window
import os
os.environ["DISPLAY"] = ":0"
app = tk.Tk()
app.title("ML Model Trigger")

# Create dropdown menus for input values
tk.Label(app, text="Input 1:").pack()
dropdown1 = ttk.Combobox(app, values=["Option 1", "Option 2", "Option 3"])
dropdown1.pack()

tk.Label(app, text="Input 2:").pack()
dropdown2 = ttk.Combobox(app, values=["Option A", "Option B", "Option C"])
dropdown2.pack()

tk.Label(app, text="Input 3:").pack()
dropdown3 = ttk.Combobox(app, values=["Choice X", "Choice Y", "Choice Z"])
dropdown3.pack()

tk.Label(app, text="Input 4:").pack()
dropdown4 = ttk.Combobox(app, values=["Value P", "Value Q", "Value R"])
dropdown4.pack()

tk.Label(app, text="Input 5:").pack()
dropdown5 = ttk.Combobox(app, values=["Item Alpha", "Item Beta", "Item Gamma"])
dropdown5.pack()

# Create a button to trigger the ML model
button = tk.Button(app, text="Run ML Model", command=run_ml_model)
button.pack()

# Create a Text widget to display the console output
console_output = tk.Text(app, height=20, width=80)
console_output.pack()

# Run the application
app.mainloop()
