import tkinter as tk
from tkinter import messagebox
import os
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

class HospitalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")

        # Store lists of doctors and patients
        self.doctors = []
        self.patients = []

        # Load data from files
        self.load_patients()

        # Admin Login Section
        self.frame_login = tk.Frame(self.root)
        self.label_username = tk.Label(self.frame_login, text="Username:")
        self.label_password = tk.Label(self.frame_login, text="Password:")
        self.entry_username = tk.Entry(self.frame_login)
        self.entry_password = tk.Entry(self.frame_login, show='*')
        self.button_login = tk.Button(self.frame_login, text="Login", command=self.login)

        # Layout
        self.label_username.grid(row=0, column=0)
        self.entry_username.grid(row=0, column=1)
        self.label_password.grid(row=1, column=0)
        self.entry_password.grid(row=1, column=1)
        self.button_login.grid(row=2, column=1, pady=5)

        self.frame_login.pack(padx=10, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Sample admin account for demo
        self.admin = Admin('AdminFirst', 'AdminLast', 'admin', '123')
        
        if self.admin.login(username, password):
            self.frame_login.pack_forget()
            self.admin_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def admin_menu(self):
        self.frame_menu = tk.Frame(self.root)
        self.button_register_doctor = tk.Button(self.frame_menu, text="Register Doctor", command=self.register_doctor)
        self.button_register_patient = tk.Button(self.frame_menu, text="Register Patient", command=self.register_patient)
        self.button_assign_doctor = tk.Button(self.frame_menu, text="Assign Doctor to Patient", command=self.assign_doctor)
        self.button_delete_patient = tk.Button(self.frame_menu, text="Delete Patient", command=self.delete_patient)
        self.button_delete_doctor = tk.Button(self.frame_menu, text="Delete Doctor", command=self.delete_doctor)
        self.button_view_patients = tk.Button(self.frame_menu, text="View Patients", command=self.view_patients)
        self.button_exit = tk.Button(self.frame_menu, text="Exit", command=self.root.quit)

        # Layout
        self.button_register_doctor.pack(fill='x', padx=5, pady=5)
        self.button_register_patient.pack(fill='x', padx=5, pady=5)
        self.button_assign_doctor.pack(fill='x', padx=5, pady=5)
        self.button_delete_patient.pack(fill='x', padx=5, pady=5)
        self.button_delete_doctor.pack(fill='x', padx=5, pady=5)
        self.button_view_patients.pack(fill='x', padx=5, pady=5)
        self.button_exit.pack(fill='x', padx=5, pady=5)

        self.frame_menu.pack(padx=10, pady=10)

    def register_doctor(self):
        self.frame_menu.pack_forget()
        
        self.frame_register_doctor = tk.Frame(self.root)
        tk.Label(self.frame_register_doctor, text="Doctor First Name:").grid(row=0, column=0)
        tk.Label(self.frame_register_doctor, text="Doctor Last Name:").grid(row=1, column=0)
        tk.Label(self.frame_register_doctor, text="Speciality:").grid(row=2, column=0)
        
        entry_firstname = tk.Entry(self.frame_register_doctor)
        entry_surname = tk.Entry(self.frame_register_doctor)
        entry_speciality = tk.Entry(self.frame_register_doctor)
        
        entry_firstname.grid(row=0, column=1)
        entry_surname.grid(row=1, column=1)
        entry_speciality.grid(row=2, column=1)
        
        tk.Button(self.frame_register_doctor, text="Submit", 
                  command=lambda: self.save_doctor(entry_firstname.get(), entry_surname.get(), entry_speciality.get())
                  ).grid(row=3, column=1, pady=10)
        
        self.frame_register_doctor.pack(padx=10, pady=10)
        
    def save_doctor(self, first_name, surname, speciality):
        doctor = Doctor(first_name, surname, speciality)
        self.doctors.append(doctor)
        messagebox.showinfo("Success", f"Doctor {doctor.full_name()} registered successfully!")
        self.frame_register_doctor.pack_forget()
        self.admin_menu()

    def register_patient(self):
        self.frame_menu.pack_forget()
        
        self.frame_register_patient = tk.Frame(self.root)
        tk.Label(self.frame_register_patient, text="First Name:").grid(row=0, column=0)
        tk.Label(self.frame_register_patient, text="Last Name:").grid(row=1, column=0)
        tk.Label(self.frame_register_patient, text="Age:").grid(row=2, column=0)
        tk.Label(self.frame_register_patient, text="Mobile:").grid(row=3, column=0)
        tk.Label(self.frame_register_patient, text="Postcode:").grid(row=4, column=0)
        tk.Label(self.frame_register_patient, text="Symptoms:").grid(row=5, column=0)

        # Create Entry fields for each label
        entry_firstname = tk.Entry(self.frame_register_patient)
        entry_surname = tk.Entry(self.frame_register_patient)
        entry_age = tk.Entry(self.frame_register_patient)
        entry_mobile = tk.Entry(self.frame_register_patient)
        entry_postcode = tk.Entry(self.frame_register_patient)
        entry_symptoms = tk.Entry(self.frame_register_patient)

        # Place Entry fields in grid
        entry_firstname.grid(row=0, column=1)
        entry_surname.grid(row=1, column=1)
        entry_age.grid(row=2, column=1)
        entry_mobile.grid(row=3, column=1)
        entry_postcode.grid(row=4, column=1)
        entry_symptoms.grid(row=5, column=1)

        tk.Button(self.frame_register_patient, text="Submit",
                  command=lambda: self.save_patient(
                      entry_firstname.get(),
                      entry_surname.get(),
                      entry_age.get(),
                      entry_mobile.get(),
                      entry_postcode.get(),
                      entry_symptoms.get(),
                  )).grid(row=6, column=1, pady=10)

        self.frame_register_patient.pack(padx=10, pady=10)

    def save_patient(self, first_name, surname, age, mobile, postcode, symptom):
        patient = Patient(first_name, surname, age, mobile, postcode, symptom)
        self.patients.append(patient)  # Add patient to the list
        self.update_patient_file()      # Now update the file
        messagebox.showinfo("Success", f"Patient {patient.full_name()} registered successfully!")
        self.frame_register_patient.pack_forget()
        self.admin_menu()


    def update_patient_file(self):
        try:
        # Open the file in write mode
            with open("patients.txt", "w") as file:
            # Write the header for the table
                file.write(f"{'First Name':<15}{'Last Name':<15}{'Age':<5}{'Mobile':<15}{'Postcode':<10}{'Symptoms':<20}{'Assigned Doctor':<20}\n")
            file.write("-" * 100 + "\n")
            
            # Iterate through the list of patients and write their data
            for patient in self.patients:
                # Get the assigned doctor or set to 'None' if no doctor is assigned
                doctor = patient.get_doctor() if patient.get_doctor() else "None"
                file.write(f"{patient._first_name:<15}{patient._surname:<15}{patient._age:<5}{patient._mobile:<15}{patient._postcode:<10}{', '.join(patient.get_symptoms()):<20}{doctor:<20}\n")
        except Exception as e:
            print(f"An error occurred while updating the patient file: {e}")





    def load_patients(self):
        # Load patient data from the text file if it exists
        if os.path.exists("patients.txt"):
            with open("patients.txt", "r") as file:
                lines = file.readlines()[2:]  # Skip the headers
                for line in lines:
                    data = line.strip().split()
                    first_name = data[0]
                    surname = data[1]
                    age = data[2]
                    mobile = data[3]
                    postcode = data[4]
                    symptoms = data[5]
                    doctor = data[6] if data[6] != "None" else None
                    patient = Patient(first_name, surname, age, mobile, postcode, symptoms)
                    if doctor:
                        patient.set_doctor(doctor)
                    self.patients.append(patient)

    def assign_doctor(self):
        self.frame_menu.pack_forget()

        if not self.doctors or not self.patients:
            messagebox.showerror("Error", "Please make sure both doctors and patients are registered.")
            self.admin_menu()
            return

        self.frame_assign_doctor = tk.Frame(self.root)
        tk.Label(self.frame_assign_doctor, text="Select Patient:").grid(row=0, column=0)
        tk.Label(self.frame_assign_doctor, text="Select Doctor:").grid(row=1, column=0)

        patient_var = tk.StringVar(self.frame_assign_doctor)
        doctor_var = tk.StringVar(self.frame_assign_doctor)

        patient_var.set(self.patients[0].full_name())
        doctor_var.set(self.doctors[0].full_name())

        patient_menu = tk.OptionMenu(self.frame_assign_doctor, patient_var, *[p.full_name() for p in self.patients])
        doctor_menu = tk.OptionMenu(self.frame_assign_doctor, doctor_var, *[d.full_name() for d in self.doctors])

        patient_menu.grid(row=0, column=1)
        doctor_menu.grid(row=1, column=1)

        tk.Button(self.frame_assign_doctor, text="Assign", 
                  command=lambda: self.assign_doctor_to_patient(patient_var.get(), doctor_var.get())
                 ).grid(row=2, column=1, pady=10)

        self.frame_assign_doctor.pack(padx=10, pady=10)

    def assign_doctor_to_patient(self, patient_name, doctor_name):
        patient = next(p for p in self.patients if p.full_name() == patient_name)
        doctor = next(d for d in self.doctors if d.full_name() == doctor_name)
        patient.set_doctor(doctor)
        self.update_patient_file()
        messagebox.showinfo("Success", f"Doctor {doctor.full_name()} assigned to patient {patient.full_name()}!")
        self.frame_assign_doctor.pack_forget()
        self.admin_menu()

    def delete_patient(self):
        self.frame_menu.pack_forget()

        self.frame_delete_patient = tk.Frame(self.root)
        tk.Label(self.frame_delete_patient, text="Select Patient:").grid(row=0, column=0)

        patient_var = tk.StringVar(self.frame_delete_patient)
        patient_var.set(self.patients[0].full_name())

        patient_menu = tk.OptionMenu(self.frame_delete_patient, patient_var, *[p.full_name() for p in self.patients])
        patient_menu.grid(row=0, column=1)

        tk.Button(self.frame_delete_patient, text="Delete", 
                  command=lambda: self.delete_patient_confirm(patient_var.get())
                 ).grid(row=1, column=1, pady=10)

        self.frame_delete_patient.pack(padx=10, pady=10)

    def delete_patient_confirm(self, patient_name):
        self.patients = [p for p in self.patients if p.full_name() != patient_name]
        self.update_patient_file()
        messagebox.showinfo("Success", f"Patient {patient_name} deleted successfully!")
        self.frame_delete_patient.pack_forget()
        self.admin_menu()

    def delete_doctor(self):
        self.frame_menu.pack_forget()

        self.frame_delete_doctor = tk.Frame(self.root)
        tk.Label(self.frame_delete_doctor, text="Select Doctor:").grid(row=0, column=0)

        doctor_var = tk.StringVar(self.frame_delete_doctor)
        doctor_var.set(self.doctors[0].full_name())

        doctor_menu = tk.OptionMenu(self.frame_delete_doctor, doctor_var, *[d.full_name() for d in self.doctors])
        doctor_menu.grid(row=0, column=1)

        tk.Button(self.frame_delete_doctor, text="Delete", 
                  command=lambda: self.delete_doctor_confirm(doctor_var.get())
                 ).grid(row=1, column=1, pady=10)

        self.frame_delete_doctor.pack(padx=10, pady=10)

    def delete_doctor_confirm(self, doctor_name):
        self.doctors = [d for d in self.doctors if d.full_name() != doctor_name]
        messagebox.showinfo("Success", f"Doctor {doctor_name} deleted successfully!")
        self.frame_delete_doctor.pack_forget()
        self.admin_menu()

    def view_patients(self):
        # Display patients' info from the text file
        if not os.path.exists("patients.txt"):
            messagebox.showinfo("No Data", "No patients are registered.")
            return

        with open("patients.txt", "r") as file:
            content = file.read()

        self.frame_menu.pack_forget()
        self.frame_view_patients = tk.Frame(self.root)
        text_widget = tk.Text(self.frame_view_patients, height=20, width=80)
        text_widget.insert(tk.END, content)
        text_widget.pack(padx=10, pady=10)

        tk.Button(self.frame_view_patients, text="Back", command=self.back_to_menu).pack(pady=10)

        self.frame_view_patients.pack(padx=10, pady=10)

    def back_to_menu(self):
        self.frame_view_patients.pack_forget()
        self.admin_menu()

if __name__ == "__main__":
    root = tk.Tk()
    gui = HospitalGUI(root)
    root.mainloop()
