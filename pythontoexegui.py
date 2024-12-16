import tkinter as tk
from tkinter import ttk
import os
from tkinter import filedialog

root = tk.Tk()
root.geometry("800x600")
root.title("Python to EXE GUI")

header = ttk.Label(root, text="Python to EXE GUI", font=("Noto Sans", 20))
header.pack()


def browse_file():
    # Open a file dialog window to select a .py or .pyw file
    filename = filedialog.askopenfilename(title="Select a Python File", filetypes=[("Python Files", "*.py *.pyw")])

    # Update the input field with the selected filename
    input_field.delete(0, tk.END)
    input_field.insert(0, filename)


# Create the input field
input_field = ttk.Entry(root, width=100)
input_field.pack(fill='x')

# Create the browse button
browse_button = ttk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)


var_windowed = tk.IntVar()
c1 = ttk.Checkbutton(root, text='Windowed',variable=var_windowed, onvalue=1, offvalue=0)
c1.pack()

def convert_to_exe():
    if var_windowed.get() == 1:
        os.system("pyinstaller --onefile -w " + input_field.get())
        from tkinter import messagebox
        messagebox.showinfo(title="EXE Build Complete", message="The EXE was finished building successfully. Check the 'dist' folder for the EXE.")
    else:
        os.system("pyinstaller --onefile " + input_field.get())
        from tkinter import messagebox
        messagebox.showinfo(title="EXE Build Complete", message="The EXE was finished building successfully. Check the 'dist' folder for the EXE.")
        
convert_button = ttk.Button(root, text="Convert to EXE", command=convert_to_exe)
convert_button.pack(pady=10)

root.mainloop()