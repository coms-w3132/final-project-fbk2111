import tkinter as tk

def check_name():
    name = entry.get()
    if name == "Filimon":
        word.config(text="Authorized")
    else:
        word.config(text="")

def on_enter(event):
    entry.focus_set()

root = tk.Tk()
root.title("Crypto Trading App")

label = tk.Label(root, text="Name:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="Check Name", command=check_name)
check_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

word = tk.Label(root, text="")
word.grid(row=2, column=0, columnspan=2)

root.bind("<Enter>", on_enter)  # Bind mouse enter event to set focus on entry

root.mainloop()

