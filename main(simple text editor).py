import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")

# Create text area
text = tk.Text(root, wrap='word', font=('Arial', 12))
text.pack(expand=1, fill=tk.BOTH)

# Function 1 - New file
def new_file():
    text.delete(1.0, tk.END)
    root.title("Untitled - Simple Text Editor")

# Function 2 - Open file
def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt")]
    )
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)

# Function 3 - Save file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt")]
    )
    if file_path:
        with open(file_path, 'w') as file:
            content = text.get(1.0, tk.END)
            file.write(content)
        messagebox.showinfo("Success", "File saved successfully!")

# Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create File menu
file_menu = tk.Menu(menu_bar, tearoff=0)

# Attach File menu to menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Add options inside File menu
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Start app
root.mainloop()