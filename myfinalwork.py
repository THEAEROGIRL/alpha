
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Step 1: Set up the database
conn = sqlite3.connect("axiom.db")
cursor = conn.cursor()

# Create tables for users and prescriptions
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS prescriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    dosage TEXT NOT NULL,
    amount INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
''')
conn.commit()

# Step 2: User Authentication Functions
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    
    if user:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        open_dashboard(user[0], username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def register_user():
    new_username = reg_username_entry.get()
    new_password = reg_password_entry.get()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
        conn.commit()
        messagebox.showinfo("Registration Successful", "User registered successfully.")
        reg_window.destroy()
    except sqlite3.IntegrityError:
        messagebox.showerror("Registration Failed", "Username already exists.")

# Step 3: Prescription Management Functions
def open_dashboard(user_id, username):
    login_window.destroy()
    
    dashboard = tk.Tk()
    dashboard.title("Axiom Dashboard")

    tk.Label(dashboard, text=f"Welcome, {username}", font=("Arial", 16)).pack(pady=10)
    tk.Label(dashboard, text="Your Prescriptions:", font=("Arial", 14)).pack(pady=5)

    # Fetch prescriptions from the database
    cursor.execute("SELECT id, name, dosage, amount FROM prescriptions WHERE user_id = ?", (user_id,))
    prescriptions = cursor.fetchall()

    # List Prescriptions
    prescription_listbox = tk.Listbox(dashboard, height=10, width=60)
    for pres in prescriptions:
        prescription_listbox.insert(
            tk.END, f"{pres[1]} | Dosage: {pres[2]} | Pills: {pres[3]}"
        )
    prescription_listbox.pack()

    # Add Prescription
    def add_prescription():
        med_name = med_name_entry.get()
        dosage = dosage_entry.get()
        amount = amount_entry.get()

        if med_name and dosage and amount.isdigit():
            cursor.execute("INSERT INTO prescriptions (user_id, name, dosage, amount) VALUES (?, ?, ?, ?)",
                           (user_id, med_name, dosage, int(amount)))
            conn.commit()
            prescription_listbox.insert(
                tk.END, f"{med_name} | Dosage: {dosage} | Pills: {amount}"
            )
            clear_entries()
            messagebox.showinfo("Success", "Prescription added successfully!")
        else:
            messagebox.showerror(
                "Error", "Please fill in all fields correctly (amount should be a number)."
            )
    
    # Remove Selected Prescription
    def remove_prescription():
        selected = prescription_listbox.curselection()
        if selected:
            index = selected[0]
            prescription = prescriptions[index]
            prescription_id = prescription[0]

            cursor.execute("DELETE FROM prescriptions WHERE id = ?", (prescription_id,))
            conn.commit()
            prescription_listbox.delete(index)
            messagebox.showinfo("Success", "Prescription removed successfully!")
        else:
            messagebox.showerror("Error", "Please select a prescription to remove.")
    
    # Update Selected Prescription
    def update_prescription():
        selected = prescription_listbox.curselection()
        if selected:
            index = selected[0]
            prescription = prescriptions[index]
            prescription_id = prescription[0]

            med_name = med_name_entry.get()
            dosage = dosage_entry.get()
            amount = amount_entry.get()
            
            if med_name and dosage and amount.isdigit():
                cursor.execute("UPDATE prescriptions SET name = ?, dosage = ?, amount = ? WHERE id = ?",
                               (med_name, dosage, int(amount), prescription_id))
                conn.commit()
                prescriptions[index] = (prescription_id, med_name, dosage, int(amount))
                prescription_listbox.delete(index)
                prescription_listbox.insert(
                    index, f"{med_name} | Dosage: {dosage} | Pills: {amount}"
                )
                clear_entries()
                messagebox.showinfo("Success", "Prescription updated successfully!")
            else:
                messagebox.showerror(
                    "Error", "Please fill in all fields correctly (amount should be a number)."
                )
        else:
            messagebox.showerror("Error", "Please select a prescription to update.")

    # Clear Entry Fields
    def clear_entries():
        med_name_entry.delete(0, tk.END)
        dosage_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

    # Input Fields for Prescription Management
    tk.Label(dashboard, text="Medicine Name:").pack()
    med_name_entry = tk.Entry(dashboard, width=30)
    med_name_entry.pack()

    tk.Label(dashboard, text="Dosage (e.g., 500mg):").pack()
    dosage_entry = tk.Entry(dashboard, width=30)
    dosage_entry.pack()

    tk.Label(dashboard, text="Amount of Pills:").pack()
    amount_entry = tk.Entry(dashboard, width=30)
    amount_entry.pack()

    tk.Button(dashboard, text="Add Prescription", command=add_prescription).pack(pady=5)
    tk.Button(dashboard, text="Remove Selected", command=remove_prescription).pack(pady=5)
    tk.Button(dashboard, text="Update Selected", command=update_prescription).pack(pady=5)

    # Logout Button
    tk.Button(dashboard, text="Logout", command=dashboard.destroy).pack(pady=20)

    dashboard.mainloop()

# Step 4: Open Registration Window
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

# Step 5: Create Login Window
login_window = tk.Tk()
login_window.title("Axiom App Login")

# Login UI Components
tk.Label(login_window, text="Axiom App", font=("Arial", 20)).pack(pady=10)

tk.Label(login_window, text="Username:").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password:").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=10)
tk.Button(login_window, text="Register", command=open_registration).pack(pady=10)

# Start the Application
login_window.mainloop()
import tkinter as tk
from tkinter import messagebox

# Step 4: Define User Data (In-memory storage)
users = {
    "test_user": {
        "password": "password123",
        "prescriptions": [
            {"name": "Medicine A", "dosage": "500mg", "amount": 30},
            {"name": "Medicine B", "dosage": "250mg", "amount": 15}
        ]
    }
}

# Step 5: Login Functionality
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in users and users[username]["password"] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        open_dashboard(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Step 6: Open Dashboard
def open_dashboard(username):
    login_window.destroy()
    
    dashboard = tk.Tk()
    dashboard.title("Axiom Dashboard")

    tk.Label(dashboard, text=f"Welcome, {username}", font=("Arial", 16)).pack(pady=10)
    tk.Label(dashboard, text="Your Prescriptions:", font=("Arial", 14)).pack(pady=5)
    
    prescriptions = users[username]["prescriptions"]

    # List Prescriptions
    prescription_listbox = tk.Listbox(dashboard, height=10, width=60)
    for pres in prescriptions:
        prescription_listbox.insert(
            tk.END, f"{pres['name']} | Dosage: {pres['dosage']} | Pills: {pres['amount']}"
        )
    prescription_listbox.pack()

    # Add Prescription
    def add_prescription():
        med_name = med_name_entry.get()
        dosage = dosage_entry.get()
        amount = amount_entry.get()

        if med_name and dosage and amount.isdigit():
            prescriptions.append(
                {"name": med_name, "dosage": dosage, "amount": int(amount)}
            )
            prescription_listbox.insert(
                tk.END, f"{med_name} | Dosage: {dosage} | Pills: {amount}"
            )
            clear_entries()
            messagebox.showinfo("Success", "Prescription added successfully!")
        else:
            messagebox.showerror(
                "Error", "Please fill in all fields correctly (amount should be a number)."
            )
    
    # Remove Selected Prescription
    def remove_prescription():
        selected = prescription_listbox.curselection()
        if selected:
            index = selected[0]
            prescriptions.pop(index)
            prescription_listbox.delete(index)
            messagebox.showinfo("Success", "Prescription removed successfully!")
        else:
            messagebox.showerror("Error", "Please select a prescription to remove.")
    
    # Update Selected Prescription
    def update_prescription():
        selected = prescription_listbox.curselection()
        if selected:
            index = selected[0]
            med_name = med_name_entry.get()
            dosage = dosage_entry.get()
            amount = amount_entry.get()
            
            if med_name and dosage and amount.isdigit():
                prescriptions[index] = {"name": med_name, "dosage": dosage, "amount": int(amount)}
                prescription_listbox.delete(index)
                prescription_listbox.insert(
                    index, f"{med_name} | Dosage: {dosage} | Pills: {amount}"
                )
                clear_entries()
                messagebox.showinfo("Success", "Prescription updated successfully!")
            else:
                messagebox.showerror(
                    "Error", "Please fill in all fields correctly (amount should be a number)."
                )
        else:
            messagebox.showerror("Error", "Please select a prescription to update.")

    # Clear Entry Fields
    def clear_entries():
        med_name_entry.delete(0, tk.END)
        dosage_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

    # Input Fields for Prescription Management
    tk.Label(dashboard, text="Medicine Name:").pack()
    med_name_entry = tk.Entry(dashboard, width=30)
    med_name_entry.pack()

    tk.Label(dashboard, text="Dosage (e.g., 500mg):").pack()
    dosage_entry = tk.Entry(dashboard, width=30)
    dosage_entry.pack()

    tk.Label(dashboard, text="Amount of Pills:").pack()
    amount_entry = tk.Entry(dashboard, width=30)
    amount_entry.pack()

    tk.Button(dashboard, text="Add Prescription", command=add_prescription).pack(pady=5)
    tk.Button(dashboard, text="Remove Selected", command=remove_prescription).pack(pady=5)
    tk.Button(dashboard, text="Update Selected", command=update_prescription).pack(pady=5)

    # Logout Button
    tk.Button(dashboard, text="Logout", command=dashboard.destroy).pack(pady=20)

    dashboard.mainloop()

# Step 7: User Registration Functionality
def register_user():
    new_username = reg_username_entry.get()
    new_password = reg_password_entry.get()

    if new_username in users:
        messagebox.showerror("Registration Failed", "Username already exists.")
    else:
        users[new_username] = {"password": new_password, "prescriptions": []}
        messagebox.showinfo("Registration Successful", "User registered successfully.")
        reg_window.destroy()

# Step 8: Open Registration Window
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

# Step 9: Create Login Window
login_window = tk.Tk()
login_window.title("Axiom App Login")

# Login UI Components
tk.Label(login_window, text="Axiom App", font=("Arial", 20)).pack(pady=10)

tk.Label(login_window, text="Username:").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password:").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=10)
tk.Button(login_window, text="Register", command=open_registration).pack(pady=10)

# Start the Application
login_window.mainloop()
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Step 1: Set up the database
conn = sqlite3.connect("axiom.db")
cursor = conn.cursor()

# Create tables for users and prescriptions
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS prescriptions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    dosage TEXT NOT NULL,
    amount INTEGER NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
)
''')
conn.commit()

# Step 2: User Authentication Functions
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    
    if user:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
        open_dashboard(user[0], username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def register_user():
    new_username = reg_username_entry.get()
    new_password = reg_password_entry.get()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, new_password))
        conn.commit()
        messagebox.showinfo("Registration Successful", "User registered successfully.")
        reg_window.destroy()
    except sqlite3.IntegrityError:
        messagebox.showerror("Registration Failed", "Username already exists.")

# Step 3: Prescription Management Functions
def open_dashboard(user_id, username):
    login_window.destroy()
    
    dashboard = tk.Tk()
    dashboard.title("Axiom Dashboard")

    tk.Label(dashboard, text=f"Welcome, {username}", font=("Arial", 16)).pack(pady=10)
    tk.Label(dashboard, text="Your Prescriptions:", font=("Arial", 14)).pack(pady=5)

    # Fetch prescriptions from the database
    cursor.execute("SELECT id, name, dosage, amount FROM prescriptions WHERE user_id = ?", (user_id,))
    prescriptions = cursor.fetchall()

    # List Prescriptions
    prescription_listbox = tk.Listbox(dashboard, height=10, width=60)
    for pres in prescriptions:
        prescription_listbox.insert(
            tk.END, f"{pres[1]} | Dosage: {pres[2]} | Pills: {pres[3]}"
        )
    prescription_listbox.pack()

    # Add Prescription
    def add_prescription():
        med_name = med_name_entry.get()
        dosage = dosage_entry.get()
        amount = amount_entry.get()

        if med_name and dosage and amount.isdigit():
            cursor.execute("INSERT INTO prescriptions (user_id, name, dosage, amount) VALUES (?, ?, ?, ?)",
                           (user_id, med_name, dosage, int(amount)))
            conn.commit()
            prescription_listbox.insert(
                tk.END, f"{med_name} | Dosage: {dosage} | Pills: {amount}"
            )
            clear_entries()
            messagebox.showinfo("Success", "Prescription added successfully!")
        else:
            messagebox.showerror(
                "Error", "Please fill in all fields correctly (amount should be a number)."
            )
    
    # Remove Selected Prescription
    def remove_prescription():
        selected = prescription_listbox.curselection()
        if selected:
            index = selected[0]
            prescription = prescriptions[index]
            prescription_id = prescription[0]

            cursor.execute("DELETE FROM prescriptions WHERE id = ?", (prescription_id,))
            conn.commit()
            prescription_listbox.delete(index)
            messagebox.showinfo("Success", "Prescription removed successfully!")
        else:
            messagebox.showerror("Error", "Please select a prescription to remove.")
    
    # Update Selected Prescription
    def update_prescription():
        selected = prescription_listbox.curselection()
        if selected:
            index = selected[0]
            prescription = prescriptions[index]
            prescription_id = prescription[0]

            med_name = med_name_entry.get()
            dosage = dosage_entry.get()
            amount = amount_entry.get()
            
            if med_name and dosage and amount.isdigit():
                cursor.execute("UPDATE prescriptions SET name = ?, dosage = ?, amount = ? WHERE id = ?",
                               (med_name, dosage, int(amount), prescription_id))
                conn.commit()
                prescriptions[index] = (prescription_id, med_name, dosage, int(amount))
                prescription_listbox.delete(index)
                prescription_listbox.insert(
                    index, f"{med_name} | Dosage: {dosage} | Pills: {amount}"
                )
                clear_entries()
                messagebox.showinfo("Success", "Prescription updated successfully!")
            else:
                messagebox.showerror(
                    "Error", "Please fill in all fields correctly (amount should be a number)."
                )
        else:
            messagebox.showerror("Error", "Please select a prescription to update.")

    # Clear Entry Fields
    def clear_entries():
        med_name_entry.delete(0, tk.END)
        dosage_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)

    # Input Fields for Prescription Management
    tk.Label(dashboard, text="Medicine Name:").pack()
    med_name_entry = tk.Entry(dashboard, width=30)
    med_name_entry.pack()

    tk.Label(dashboard, text="Dosage (e.g., 500mg):").pack()
    dosage_entry = tk.Entry(dashboard, width=30)
    dosage_entry.pack()

    tk.Label(dashboard, text="Amount of Pills:").pack()
    amount_entry = tk.Entry(dashboard, width=30)
    amount_entry.pack()

    tk.Button(dashboard, text="Add Prescription", command=add_prescription).pack(pady=5)
    tk.Button(dashboard, text="Remove Selected", command=remove_prescription).pack(pady=5)
    tk.Button(dashboard, text="Update Selected", command=update_prescription).pack(pady=5)

    # Logout Button
    tk.Button(dashboard, text="Logout", command=dashboard.destroy).pack(pady=20)

    dashboard.mainloop()

# Step 4: Open Registration Window
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

# Step 5: Create Login Window
login_window = tk.Tk()
login_window.title("Axiom App Login")

# Login UI Components
tk.Label(login_window, text="Axiom App", font=("Arial", 20)).pack(pady=10)

tk.Label(login_window, text="Username:").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password:").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=10)
tk.Button(login_window, text="Register", command=open_registration).pack(pady=10)

# Start the Application
login_window.mainloop()
