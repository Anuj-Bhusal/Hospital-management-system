
from person import Person

class Patient(Person):
    """Patient Class"""
    def __init__(self, first_name, surname, age, mobile, postcode, symptom, family_id=None):
        super().__init__(first_name, surname)
        self._age = age  # Changed from __age to _age
        self._mobile = mobile  # Changed from __mobile to _mobile
        self._postcode = postcode  # Changed from __postcode to _postcode
        self._doctor = None  # Changed from __doctor to _doctor
        self._symptoms = [symptom]  # Changed from __symptoms to _symptoms
        self._family_id = family_id

    def get_doctor(self):
        return self._doctor

    def set_doctor(self, doctor):
        self._doctor = doctor

    def add_symptom(self, symptom):
        self._symptoms.append(symptom)

    def print_symptoms(self):
        print(f"Symptoms of {self.full_name()}: {', '.join(self._symptoms)}")

    def get_symptoms(self):
        return self._symptoms

    def __str__(self):
        return f"Patient: {self.full_name()} | Doctor: {self._doctor} | Age: {self._age} | Mobile: {self._mobile} | Postcode: {self._postcode} | Symptoms: {', '.join(self._symptoms)}"
