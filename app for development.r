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
