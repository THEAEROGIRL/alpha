
import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Database setup
def init_db():
    conn = sqlite3.connect("axiom_tkinter.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS prescriptions (
        
        name TEXT NOT NULL,
        dosage TEXT NOT NULL,
        amount INTEGER NOT NULL,
        
    )
    ''')
    conn.commit()
    conn.close()

init_db()

# Login window
def login_window():
    def login():
        username = username_entry.get()
        password = password_entry.get()

        conn = sqlite3.connect("axiom_tkinter.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            main_window(user[0])
            login_win.destroy()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_register_window():
        login_win.destroy()
        register_window()

    login_win = tk.Tk()
    login_win.title("Login")

    tk.Label(login_win, text="Login", font=("Arial", 16)).pack(pady=10)
    tk.Label(login_win, text="Username:").pack()
    username_entry = tk.Entry(login_win)
    username_entry.pack()

    tk.Label(login_win, text="Password:").pack()
    password_entry = tk.Entry(login_win, show="*")
    password_entry.pack()

    tk.Button(login_win, text="Login", command=login).pack(pady=10)
    tk.Button(login_win, text="Register", command=open_register_window).pack(pady=5)

    login_win.mainloop()

# Registration window
def register_window():
    def register():
        username = username_entry.get()
        password = password_entry.get()

        conn = sqlite3.connect("axiom_tkinter.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful! Please log in.")
            register_win.destroy()
            login_window()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        finally:
            conn.close()

    register_win = tk.Tk()
    register_win.title("Register")

    tk.Label(register_win, text="Register", font=("Arial", 16)).pack(pady=10)
    tk.Label(register_win, text="Username:").pack()
    username_entry = tk.Entry(register_win)
    username_entry.pack()

    tk.Label(register_win, text="Password:").pack()
    password_entry = tk.Entry(register_win, show="*")
    password_entry.pack()

    tk.Button(register_win, text="Register", command=register).pack(pady=10)

    register_win.mainloop()

# Main dashboard
def main_window(username):
    def refresh_prescription_list():
        prescription_list.delete(*prescription_list.get_children())
        conn = sqlite3.connect("axiom_tkinter.db")
        cursor = conn.cursor()
        cursor.execute("SELECT  medicine name, dosage, amount FROM prescriptions WHERE username = ?", (user_id,))
        prescriptions = cursor.fetchall()
        conn.close()

        for pres in prescriptions:
            prescription_list.insert("", tk.END, values=pres)

    def add_prescription():
        name =  name_entry.get()
        dosage = dosage_entry.get()
        amount = amount_entry.get()

        if name and dosage and amount.isdigit():
            conn = sqlite3.connect("axiom_tkinter.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO prescriptions ( name, dosage, amount) VALUES (?, ?, ?)",
                           (name, dosage, int(amount)))
            conn.commit()
            conn.close()
            refresh_prescription_list()
            name_entry.delete(0, tk.END)
            dosage_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Prescription added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields correctly.")

    def delete_prescription():
        selected_item = prescription_list.selection()
        if selected_item:
            prescription_id = prescription_list.item(selected_item)['values'][0]
            conn = sqlite3.connect("axiom_tkinter.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM prescriptions WHERE id = ?", (prescription_id,))
            conn.commit()
            conn.close()
            refresh_prescription_list()
            messagebox.showinfo("Success", "Prescription deleted successfully!")
        else:
            messagebox.showerror("Error", "Please select a prescription to delete.")

    def update_prescription():
        selected_item = prescription_list.selection()
        if selected_item:
            name = name_entry.get()
            dosage = dosage_entry.get()
            amount = amount_entry.get()

            if name and dosage and amount.isdigit():
                conn = sqlite3.connect("axiom_tkinter.db")
                cursor = conn.cursor()
                cursor.execute("UPDATE prescriptions SET name = ?, dosage = ?, amount = ? ",
                               (name, dosage, int(amount), prescription_id))
                conn.commit()
                conn.close()
                refresh_prescription_list()
                name_entry.delete(0, tk.END)
                dosage_entry.delete(0, tk.END)
                amount_entry.delete(0, tk.END)
                messagebox.showinfo("Success", "Prescription updated successfully!")
            else:
                messagebox.showerror("Error", "Please fill in all fields correctly.")
        else:
            messagebox.showerror("Error", "Please select a prescription to update.")

    main_win = tk.Tk()
    main_win.title("Dashboard")

    tk.Label(main_win, text="Your Prescriptions", font=("Arial", 16)).pack(pady=10)

    # Prescription list
    columns = ("ID", "Name", "Dosage", "Amount")
    prescription_list = ttk.Treeview(main_win, columns=columns, show="headings")
    for col in columns:
        prescription_list.heading(col, text=col)
    prescription_list.pack()

    # Input fields
    tk.Label(main_win, text="Medicine Name:").pack()
    name_entry = tk.Entry(main_win)
    name_entry.pack()

    tk.Label(main_win, text="Dosage (e.g., 500mg):").pack()
    dosage_entry = tk.Entry(main_win)
    dosage_entry.pack()

    tk.Label(main_win, text="Amount of Pills:").pack()
    amount_entry = tk.Entry(main_win)
    amount_entry.pack()

    # Buttons
    tk.Button(main_win, text="Add Prescription", command=add_prescription).pack(pady=5)
    tk.Button(main_win, text="Update Selected Prescription", command=update_prescription).pack(pady=5)
    tk.Button(main_win, text="Delete Selected Prescription", command=delete_prescription).pack(pady=5)

    # Logout button
    tk.Button(main_win, text="Logout", command=main_win.destroy).pack(pady=10)

    refresh_prescription_list()
    main_win.mainloop()

# Start the app
login_window()
