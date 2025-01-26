import sqlite3
from tkinter import *
# Create or connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FullName TEXT NOT NULL,
    Email TEXT NOT NULL,
    Gender TEXT NOT NULL,
    Age INTEGER NOT NULL
)
""")
conn.commit()
# Function to insert data into the table
def submit_data():
    full_name = entry_1.get()
    email = entry_02.get()
    gender = "Male" if varblbl.get() == 1 else "Female"
    age = entry_03.get()
    cursor.execute("INSERT INTO Users (FullName, Email, Gender, Age) VALUES (?, ?, ?, ?)", 
                   (full_name, email, gender, age))
    conn.commit()
    print("Data submitted successfully!")
# GUI setup
base = Tk()
base.geometry('500x500')
base.title("Signup")
labl_0 = Label(base, text="Signup", width=20, font=("bold", 20))
labl_0.place(x=90, y=53)
labl_1 = Label(base, text="FullName", width=20, font=("bold", 10))
labl_1.place(x=80, y=130)
entry_1 = Entry(base)
entry_1.place(x=240, y=130)
labl_2 = Label(base, text="Email", width=20, font=("bold", 10))
labl_2.place(x=68, y=180)
entry_02 = Entry(base)
entry_02.place(x=240, y=180)
labl_3 = Label(base, text="Gender", width=20, font=("bold", 10))
labl_3.place(x=70, y=230)
varblbl = IntVar()
Radiobutton(base, text="Male", padx=5, variable=varblbl, value=1).place(x=235, y=230)
Radiobutton(base, text="Female", padx=20, variable=varblbl, value=2).place(x=290, y=230)
labl_4 = Label(base, text="Age", width=20, font=("bold", 10))
labl_4.place(x=70, y=280)
entry_03 = Entry(base)
entry_03.place(x=240, y=280)
Button(base, text='Submit', width=20, bg='brown', fg='white', command=submit_data).place(x=180, y=380)
base.mainloop()
# Close the database connection
conn.close()
from tkinter import *

# Function to show the next page
def show_next_page():
    # Hide the current window
    signup_page.withdraw()
    # Create and show the next page
    next_page = Toplevel()
    next_page.geometry('500x500')
    next_page.title("Next Page")
    Label(next_page, text="Welcome to the Next Page!", font=("bold", 20)).pack(pady=50)
    Button(next_page, text="Back to Signup", command=lambda: back_to_signup(next_page)).pack(pady=20)

# Function to go back to the signup page
def back_to_signup(next_page):
    # Close the next page and show the signup page again
    next_page.destroy()
    signup_page.deiconify()

# Create the Signup Page
signup_page = Tk()
signup_page.geometry('500x500')
signup_page.title("Signup Page")

# Add widgets for the Signup Page
Label(signup_page, text="Signup", font=("bold", 20)).pack(pady=20)
Label(signup_page, text="Full Name", font=("bold", 10)).pack(pady=10)
Entry(signup_page).pack(pady=10)
Label(signup_page, text="Email", font=("bold", 10)).pack(pady=10)
Entry(signup_page).pack(pady=10)

# Add a button to navigate to the next page
Button(signup_page, text="Next Page", command=show_next_page, bg="brown", fg="white").pack(pady=20)

# Run the application
signup_page.mainloop()
