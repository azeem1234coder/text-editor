from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Initialize window
window = Tk()
window.title("Codingal Text Editor")
window.geometry("600x500")
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)  # Allow text area to expand

# Function to open a file
def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f"Codingal's Text Editor - {filepath}")

# Function to save a file
def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
    window.title(f"Codingal's Text Editor - {filepath}")

# UI Widgets
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)

btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
