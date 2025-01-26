
import tkinter as tk
from tkinter import messagebox

# Step 4: Define User Data
users = {"test_user": {"password": "password123", "prescriptions": ["Medicine A", "Medicine B"]}}

# Step 5: Main App Functions
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in users and users[username]["password"] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        open_dashboard(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def open_dashboard(username):
    login_window.destroy()
    
    dashboard = tk.Tk()
    dashboard.title("Axiom Dashboard")

    tk.Label(dashboard, text=f"Welcome, {username}", font=("Arial", 16)).pack(pady=10)

    tk.Label(dashboard, text="Your Prescriptions:", font=("Arial", 14)).pack(pady=5)
    
    prescriptions = users[username]["prescriptions"]
    for med in prescriptions:
        tk.Label(dashboard, text=f"- {med}", font=("Arial", 12)).pack()

    tk.Button(dashboard, text="Logout", command=dashboard.destroy, font=("Arial", 12)).pack(pady=20)

    dashboard.mainloop()

def register_user():
    new_username = reg_username_entry.get()
    new_password = reg_password_entry.get()

    if new_username in users:
        messagebox.showerror("Registration Failed", "Username already exists.")
    else:
        users[new_username] = {"password": new_password, "prescriptions": []}
        messagebox.showinfo("Registration Success", "User registered successfully.")
        reg_window.destroy()

def open_registration():
    global reg_window, reg_username_entry, reg_password_entry

    reg_window = tk.Toplevel()
    reg_window.title("Register")

    tk.Label(reg_window, text="Register New User", font=("Arial", 16)).pack(pady=10)

    tk.Label(reg_window, text="Username:").pack()
    reg_username_entry = tk.Entry(reg_window)
    reg_username_entry.pack()

    tk.Label(reg_window, text="Password:").pack()
    reg_password_entry = tk.Entry(reg_window, show="*")
    reg_password_entry.pack()

    tk.Button(reg_window, text="Register", command=register_user).pack(pady=10)

# Step 6: Create Login Window
login_window = tk.Tk()
login_window.title("Axiom App Login")

# Login UI
tk.Label(login_window, text="Axiom App", font=("Arial", 20)).pack(pady=10)

tk.Label(login_window, text="Username:").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password:").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=10)

tk.Button(login_window, text="Register", command=open_registration).pack(pady=10)

login_window.mainloop()