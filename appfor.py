from tkinter import *
# Function to show the next page
def show_next_page():
    # Hide the current window
    signup_page.withdraw()
    # Create and show the next page
    next_page = Toplevel()
    next_page.geometry('500x500')
    next_page.title("Next Page")
    Label(next_page, text="choose the correct option", font=("bold", 20)).pack(pady=50)
    Button(next_page, text="doctor", command=lambda: back_to_signup(next_page)).pack(pady=20)
    Button(next_page, text="patient", command=lambda: back_to_signup(next_page)).pack(pady=20)
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
from tkinter import *
# Function to show the doctor page
def show_doctor_page():
    # Hide the signup page
    signup_page.withdraw()  
    # Create and show the doctor page
    doctor_page = Toplevel()
    doctor_page.geometry('500x500')
    doctor_page.title("Doctor Page")   
    # Doctor Page Widgets
    Label(doctor_page, text="Doctor Information", font=("bold", 20)).pack(pady=20)
    Label(doctor_page, text="Full Name", font=("bold", 10)).pack(pady=10)
    Entry(doctor_page).pack(pady=10)
    Label(doctor_page, text="Specialization", font=("bold", 10)).pack(pady=10)
    Entry(doctor_page).pack(pady=10)
    Label(doctor_page, text="Years of Experience", font=("bold", 10)).pack(pady=10)
    Entry(doctor_page).pack(pady=10)
    Label(doctor_page, text="Clinic Address", font=("bold", 10)).pack(pady=10)
    Entry(doctor_page).pack(pady=10)
    
    Label(doctor_page, text="Availability", font=("bold", 10)).pack(pady=10)
    Entry(doctor_page).pack(pady=10)
    
    # Button to go back to the signup page
    Button(doctor_page, text="Back to Signup", command=lambda: back_to_signup(doctor_page), bg="brown", fg="white").pack(pady=20)

# Function to go back to the signup page
def back_to_signup(current_page):
    # Close the current page and show the signup page again
    current_page.destroy()
    signup_page.deiconify()

# Create the Signup Page
signup_page = Tk()
signup_page.geometry('500x500')
signup_page.title("Signup Page")

# Signup Page Widgets
Label(signup_page, text="Signup", font=("bold", 20)).pack(pady=20)
Label(signup_page, text="Full Name", font=("bold", 10)).pack(pady=10)
Entry(signup_page).pack(pady=10)
Label(signup_page, text="Email", font=("bold", 10)).pack(pady=10)
Entry(signup_page).pack(pady=10)
# Button to navigate to the Doctor Page
Button(signup_page, text="Next (Doctor Page)", command=show_doctor_page, bg="brown", fg="white").pack(pady=20)
# Run the application
signup_page.mainloop()

from tkinter import *

# Function to show the patient page
def show_patient_page():
    # Hide the signup page
    signup_page.withdraw()
    
    # Create and show the patient page
    patient_page = Toplevel()
    patient_page.geometry('500x500')
    patient_page.title("Patient Page")
    
    # Patient Page Widgets
    Label(patient_page, text="Patient Information", font=("bold", 20)).pack(pady=20)
    Label(patient_page, text="Full Name", font=("bold", 10)).pack(pady=10)
    Entry(patient_page).pack(pady=10)
    
    Label(patient_page, text="Age", font=("bold", 10)).pack(pady=10)
    Entry(patient_page).pack(pady=10)
    
    Label(patient_page, text="Contact Number", font=("bold", 10)).pack(pady=10)
    Entry(patient_page).pack(pady=10)
    
    Label(patient_page, text="Symptoms", font=("bold", 10)).pack(pady=10)
    Entry(patient_page, width=40).pack(pady=10)
    
    Label(patient_page, text="Medical History", font=("bold", 10)).pack(pady=10)
    Text(patient_page, height=5, width=40).pack(pady=10)
    
    # Button to go back to the signup page
    Button(patient_page, text="Back to Signup", command=lambda: back_to_signup(patient_page), bg="brown", fg="white").pack(pady=20)

# Function to go back to the signup page
def back_to_signup(current_page):
    # Close the current page and show the signup page again
    current_page.destroy()
    signup_page.deiconify()

# Create the Signup Page
signup_page = Tk()
signup_page.geometry('500x500')
signup_page.title("Signup Page")

# Signup Page Widgets
Label(signup_page, text="Signup", font=("bold", 20)).pack(pady=20)
Label(signup_page, text="Full Name", font=("bold", 10)).pack(pady=10)
Entry(signup_page).pack(pady=10)
Label(signup_page, text="Email", font=("bold", 10)).pack(pady=10)
Entry(signup_page).pack(pady=10)

# Button to navigate to the Patient Page
Button(signup_page, text="Next (Patient Page)", command=show_patient_page, bg="brown", fg="white").pack(pady=20)

# Run the application
signup_page.mainloop()

from tkinter import *

# Function to show the prescription page
def show_prescription_page():
    # Hide the signup page
    signup_page.withdraw()
    
    # Create and show the prescription page
    prescription_page = Toplevel()
    prescription_page.geometry('500x500')
    prescription_page.title("Prescription Page")
    
    # Prescription Page Widgets
    Label(prescription_page, text="Prescription Details", font=("bold", 20)).pack(pady=20)
    
    Label(prescription_page, text="Patient's Full Name", font=("bold", 10)).pack(pady=10)
    Entry(prescription_page).pack(pady=10)
    
    Label(prescription_page, text="Symptoms", font=("bold", 10)).pack(pady=10)
    Entry(prescription_page, width=40).pack(pady=10)
    
    Label(prescription_page, text="Diagnosis", font=("bold", 10)).pack(pady=10)
    Entry(prescription_page, width=40).pack(pady=10)
    
    Label(prescription_page, text="Prescribed Medications", font=("bold", 10)).pack(pady=10)
    Text(prescription_page, height=5, width=40).pack(pady=10)
    
    Label(prescription_page, text="Dosage Instructions", font=("bold", 10)).pack(pady=10)
    Text(prescription_page, height=3, width=40).pack(pady=10)
    
    # Button to submit the prescription
    Button(prescription_page, text="Submit Prescription", bg="green", fg="white").pack(pady=20)
    
    # Button to go back to the signup page
    Button(prescription_page, text="Back to Signup", command=lambda: back_to_signup(prescription_page), bg="brown", fg="white").pack(pady=10)

# Function to go back to the signup page
def back_to_signup(current_page):
    # Close the current page and show the signup page again
    current_page.destroy()
    signup_page.deiconify()

# Create the Signup Page
signup_page = Tk()
signup_page.geometry('500x500')
signup_page.title("Signup Page")

# Signup Page Widgets
Label(signup_page, text="Signup", font=("bold", 20)).pack(pady=20)
Label(signup_page, text="Full Name", font=("bold", 10)).pack(pady=10)
Entry(signup_page).pack(pady=10)
Label(signup_page, text="Email", font=("bold", 10)).pack(pady=10)
Entry(signup_page).pack(pady=10)

# Button to navigate to the Prescription Page
Button(signup_page, text="Next (Prescription Page)", command=show_prescription_page, bg="brown", fg="white").pack(pady=20)

# Run the application
signup_page.mainloop()

from tkinter import *

# Function to show the receipt page
def show_receipt_page():
    # Hide the signup page
    signup_page.withdraw()
    
    # Create and show the receipt page
    receipt_page = Toplevel()
    receipt_page.geometry('500x500')
    receipt_page.title("Receipt Page")
    
    # Receipt Page Widgets
    Label(receipt_page, text="Receipt Details", font=("bold", 20)).pack(pady=20)
    
    Label(receipt_page, text="Patient's Full Name", font=("bold", 10)).pack(pady=10)
    Entry(receipt_page, width=40).pack(pady=10)
    
    Label(receipt_page, text="Doctor's Full Name", font=("bold", 10)).pack(pady=10)
    Entry(receipt_page, width=40).pack(pady=10)
    
    Label(receipt_page, text="Services Provided", font=("bold", 10)).pack(pady=10)
    Text(receipt_page, height=5, width=40).pack(pady=10)
    
    Label(receipt_page, text="Total Cost ($)", font=("bold", 10)).pack(pady=10)
    Entry(receipt_page, width=20).pack(pady=10)
    
    Label(receipt_page, text="Payment Status", font=("bold", 10)).pack(pady=10)
    Entry(receipt_page, width=20).pack(pady=10)
    
    # Button to submit receipt information
    Button(receipt_page, text="Generate Receipt", bg="green", fg="white").pack(pady=20)
    
    # Button to go back to the signup page
    Button(receipt_page, text="Back to Signup", command=lambda: back_to_signup(receipt_page), bg="brown", fg="white").pack(pady=10)

# Function to go back to the signup page
def back_to_signup(current_page):
    # Close the current page and show the signup page again
    current_page.destroy()
    signup_page.deiconify()

# Create the Signup Page
signup_page = Tk()
signup_page.geometry('500x500')
signup_page.title("Signup Page")

# Signup Page Widgets
Label(signup_page, text="Signup", font=("bold", 20)).pack(pady=20)
Label(signup_page, text="Full Name", font=("bold", 10)).pack(pady=10)
Entry(signup_page).pack(pady=10)
Label(signup_page, text="Email", font=("bold", 10)).pack(pady=10)
Entry(signup_page).pack(pady=10)

# Button to navigate to the Receipt Page
Button(signup_page, text="Next (Receipt Page)", command=show_receipt_page, bg="brown", fg="white").pack(pady=20)

# Run the application
signup_page.mainloop()
