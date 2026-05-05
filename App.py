import tkinter as tk
import base64

FILE = "data.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def load_data():
    try:
        with open(FILE, "r") as file:
            return file.readlines()
    except:
        return []

def save_entry():
    account = account_entry.get()
    password = password_entry.get()

    if account and password:
        with open(FILE, "a") as file:
            file.write(f"{account}:{encode(password)}\n")

        account_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        refresh_list()

def refresh_list():
    listbox.delete(0, tk.END)
    for line in load_data():
        account, password = line.strip().split(":")
        listbox.insert(tk.END, f"{account} → {decode(password)}")

def delete_entry():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        data = load_data()
        data.pop(index)

        with open(FILE, "w") as file:
            file.writelines(data)

        refresh_list()

# GUI setup
root = tk.Tk()
root.title("Password Manager")

tk.Label(root, text="Account").pack()
account_entry = tk.Entry(root, width=40)
account_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack()

tk.Button(root, text="Save", command=save_entry).pack(pady=5)

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

tk.Button(root, text="Delete Selected", command=delete_entry).pack()

refresh_list()

root.mainloop()
