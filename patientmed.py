
import sqlite3

# Step 1: Initialize the SQLite Database
def initialize_database():
    # Connect to SQLite database (creates a file if it doesn't exist)
    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        dosage TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prescriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        medicine_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients(id),
        FOREIGN KEY (medicine_id) REFERENCES medicines(id)
    )
    """)

    # Insert sample data (if the database is empty)
    cursor.execute("INSERT OR IGNORE INTO patients (id, name) VALUES (1, 'Alice'), (2, 'Bob')")
    cursor.execute("INSERT OR IGNORE INTO medicines (id, name, dosage) VALUES "
                   "(1, 'Paracetamol', '500mg'), "
                   "(2, 'Ibuprofen', '200mg'), "
                   "(3, 'Amoxicillin', '250mg')")
    cursor.execute("INSERT OR IGNORE INTO prescriptions (id, patient_id, medicine_id, quantity) VALUES "
                   "(1, 1, 1, 10), "
                   "(2, 1, 2, 5), "
                   "(3, 2, 3, 7)")

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Step 2: Display all patients
def list_patients():
    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()

    # Fetch all patients
    cursor.execute("SELECT id, name FROM patients")
    patients = cursor.fetchall()
    conn.close()

    # Display patient list
    print("\nPatients:")
    print("--------------------")
    for patient in patients:
        print(f"ID: {patient[0]} | Name: {patient[1]}")
    print("--------------------")
    return [patient[0] for patient in patients]  # Return list of patient IDs

# Step 3: Fetch and display prescriptions for a specific patient
def view_prescriptions(patient_id):
    conn = sqlite3.connect("medicines.db")
    cursor = conn.cursor()

    # Query to fetch prescriptions
    query = """
    SELECT medicines.name, medicines.dosage, prescriptions.quantity
    FROM prescriptions
    JOIN medicines ON prescriptions.medicine_id = medicines.id
    WHERE prescriptions.patient_id = ?
    """
    cursor.execute(query, (patient_id,))
    prescriptions = cursor.fetchall()
    conn.close()

    # Display prescriptions
    if prescriptions:
        print(f"\nPrescriptions for Patient ID {patient_id}:")
        print("------------------------------")
        print(f"{'Medicine':<20} {'Dosage':<10} {'Quantity':<10}")
        print("------------------------------")
        for prescription in prescriptions:
            print(f"{prescription[0]:<20} {prescription[1]:<10} {prescription[2]:<10}")
        print("------------------------------")
    else:
        print(f"\nNo prescriptions found for Patient ID {patient_id}.")

# Step 4: Main program
def main():
    initialize_database()
    print("Welcome to the Prescription Viewer!")
    
    # Display patients
    patient_ids = list_patients()
    
    # Ask user to select a patient
    try:
        patient_id = int(input("Enter the Patient ID to view their prescriptions: "))
        if patient_id in patient_ids:
            view_prescriptions(patient_id)
        else:
            print("Invalid Patient ID. Please select a valid ID from the list.")
    except ValueError:
        print("Invalid input. Please enter a numeric Patient ID.")

if __name__ == "__main__":
    main()
