from Doctor import Doctor

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address
        self.__Doctor = []
    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
        print("-----Login-----")
        
        username = input('Enter the username: ')
        password = input('Enter the password: ')

        if self.__username == username and self.__password == password:
            return "Login successful"
        else:
            return "Login failed please try again"
        pass

    def find_index(self,index,doctors):
        
        """check that the doctor id exists  """        
        if index in range(0,len(doctors)):
            return True
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name=input("Enter the first name:")
        surname=input("Enter the surname name:")
        speciality=input("Enter the speciality:")
        return first_name, surname, speciality
    def doctor_management(self, doctors):
     """
     Manage the doctor records.
     """
     while True:
        print("-----Doctor Management-----")
        
        # Menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')
        print(' 5 - Exit')
        op = input("****\nSelect an option: ")

        # Register
        if op == '1':
            print("-----Register-----")

            # Get the doctor's details
            print('Enter the doctor\'s details:')
            first_name, surname, speciality = self.get_doctor_details()

            # Check if the name is already registered
            if any(first_name == doctor.get_first_name() and surname == doctor.get_surname() for doctor in doctors):
                print('Name already exists.')
            else:
                new_doctor = Doctor(first_name, surname, speciality)
                doctors.append(new_doctor)
                print("Doctor registered successfully.")

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor's Details-----")
                print('ID |          Full Name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    if self.find_index(index, doctors):
                        break
                    else:
                        print("Doctor not found.")
                except ValueError:
                    print('The ID entered is incorrect.')

            # Update menu
            print('Choose the field to be updated:')
            print(' 1 - First Name')
            print(' 2 - Surname')
            print(' 3 - Speciality')
            try:
                op = int(input("Select an option (1-3): "))
                if op == 1:
                    new_first_name = input("Enter the new first name: ")
                    if new_first_name:
                        doctors[index].set_first_name(new_first_name)
                        print("First name updated successfully.")
                    else:
                        print("First name cannot be empty.")

                elif op == 2:
                    new_surname = input("Enter the new surname: ")
                    if new_surname:
                        doctors[index].set_surname(new_surname)
                        print("Surname updated successfully.")
                    else:
                        print("Surname cannot be empty.")

                elif op == 3:
                    new_speciality = input("Enter the new speciality: ")
                    if new_speciality:
                        doctors[index].set_speciality(new_speciality)
                        print("Speciality updated successfully.")
                    else:
                        print("Speciality cannot be empty.")

                else:
                    print("Invalid choice. Please select a valid option.")

            except ValueError:
                print('The ID entered is incorrect.')

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            try:
                doctor_index = int(doctor_index) - 1
                if self.find_index(doctor_index, doctors):
                    del doctors[doctor_index]
                    print("Doctor deleted successfully.")
                else:
                    print("The ID entered is incorrect.")
            except ValueError:
                print("Invalid ID entered. Check your spelling!")

        # Exit
        elif op == '5':
            print("Exiting Doctor Management...")
            break

        # Invalid input
        else:
            print("Invalid choice. Please select a valid option.")


    

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |     Full Name   | Age |    Mobile     | Postcode | Family |Symptoms')
        self.view(patients)


    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |     Full Name   | Age |    Mobile     | Postcode | Family |Symptoms')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
            # link the patients to the doctor and vice versa
             patients[patient_index].link(doctors[doctor_index].full_name())
             doctors[doctor_index].add_patient(patients[patient_index])
             print('The patient is now assign to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')
        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')




    def discharge(self, patients, discharged_patients):
      """
      Allow the admin to discharge a patient when treatment is done.
      Args:
        patients (list<Patients>): the list of all the active patients
        discharged_patients (list<Patients>): the list of all the non-active patients
      """
      while True:
        print("----- Discharge Patient -----")
        print("Current Active Patients:")
        self.view(patients)

        choice = input("Do you want to discharge a patient? (Y/N): ").strip().upper()

        if choice == 'Y' or choice == 'YES':
            patient_id = input("Enter the patient ID to discharge: ").strip()
            try:
                patient_index = int(patient_id) - 1  # Convert to zero-based index
                if self.find_index(patient_index, patients):
                    # Remove the patient from active list and add to discharged
                    discharged_patients.append(patients.pop(patient_index))
                    print("Patient discharged successfully.")
                else:
                    print("Invalid Patient ID. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid numeric ID.")
        elif choice == 'N' or choice == 'NO':
            print("Exiting discharge process.")
            break
        else:
            print("Invalid choice. Please answer with 'Y' or 'N'.")


    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)


    def update_details(self):
    #Allows the admin to update username, password, or address.
     while True:
        print("\n----- Update Details -----")
        print("1. Update Username")
        print("2. Update Password")
        print("3. Update Address")
        print("4. Exit")
        try:
            op = int(input("Select an option (1-4): ").strip())
            if op == 1:
                new_username = input("Enter the new username: ").strip()
                if new_username:
                    self.__username = new_username
                    print("Username updated successfully.")
                else:
                    print("Username cannot be empty.")
            elif op == 2:
                while True:
                    password = input("Enter the new password: ").strip()
                    confirm_password = input("Re-enter the new password: ").strip()
                    if password == confirm_password:
                        self.__password = password
                        print("Password updated successfully.")
                        break
                    else:
                        print("Passwords do not match. Please try again.")
            elif op == 3:
                new_address = input("Enter the new address: ").strip()
                if new_address:
                    self.__address = new_address
                    print("Address updated successfully.")
                else:
                    print("Address cannot be empty.")
            elif op == 4:
                print("Exiting update menu.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            

    def group_patients_by_family(self, patients):
        family_groups = {}
        for patient in patients:
            if patient.family_name not in family_groups:
                family_groups[patient.family_name] = []
            family_groups[patient.family_name].append(patient)
        return family_groups


doctors = [Doctor("John", "Doe", "Cardiology"),
           Doctor("Jane", "Smith", "Neurology"),]
patients = []
discharged_patients = []

admin = Admin("admin", "password123", "123 Admin Lane")

# Example: Registering a doctor
admin.doctor_management(doctors)



            
