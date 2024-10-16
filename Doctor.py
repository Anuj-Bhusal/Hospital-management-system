
from person import Person

class Doctor(Person):
    """Doctor Class"""
    def __init__(self, first_name, surname, speciality):
        super().__init__(first_name, surname)
        self._speciality = speciality  # Changed from __speciality to _speciality

    def get_speciality(self):
        return self._speciality

    def set_speciality(self, speciality):
        self._speciality = speciality

    def __str__(self):
        return f"Doctor: {self.full_name()} | Speciality: {self._speciality}"
