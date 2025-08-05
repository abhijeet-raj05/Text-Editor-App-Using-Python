import tkinter as tk
from tkinter import filedialog, messagebox

def note_text():
    text.delete(1.0, tk.END)
## Open Note: 

def open_note():
    note_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Note File","*.txt")])
    if note_path:
        with open(note_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

## Save Note:

def save_note():
    note_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Note File","*.txt")])
    if note_path:
        with open(note_path, 'w') as file:
            file.write(text.get(1.0,tk.END))
            messagebox.showinfo("Info", "File Saved Successfully!!")



root = tk.Tk()
root.title("Text Editor")
root.geometry("1000x1000")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="New", command=note_text)
file_menu.add_command(label="Open", command=open_note) 
file_menu.add_command(label="Save", command=save_note) 
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Consolas", 15),
    fg="#2C3E50",
    bg="#FAFAFA",
    insertbackground="#2C3E50",
    selectbackground="#3498DB",
    selectforeground="#FFFFFF", 
    relief="flat",
    borderwidth=0,
    padx=10,
    pady=10
)


text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()
