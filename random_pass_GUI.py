import string
import random
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

def generate_password(length):
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    password = ''.join([random.choice(s) for _ in range(length)])
    return password

def on_generate():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")
        password = generate_password(length)
        result_var.set(password)
        messagebox.showinfo("Success", "Password generated successfully!")
    except ValueError as ve:
        messagebox.showerror("Error", f"Invalid input: {ve}")

#tkinter GUI setup
root = Tk()
root.title("Password Generator")

length_var = StringVar()
result_var = StringVar()

Label(root, text="Enter Password Length:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
Entry(root, textvariable=length_var, width=10).grid(row=0, column=1, padx=10, pady=5)

Button(root, text="Generate Password", command=on_generate).grid(row=1, column=0, columnspan=2, pady=10)

Label(root, text="Generated Password:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
Entry(root, textvariable=result_var, width=30, state="readonly").grid(row=2, column=1, padx=10, pady=5)

#Running the GUI loop
root.mainloop()
