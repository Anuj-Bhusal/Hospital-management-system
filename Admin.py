
from person import Person

class Admin(Person):
    """Admin Class for managing users and doctors"""
    def __init__(self, first_name, surname, username, password, address=''):
        super().__init__(first_name, surname)
        self._username = username  # Changed from __username to _username
        self._password = password  # Changed from __password to _password
        self._address = address  # Changed from __address to _address

    def login(self, username, password):
        """Handles login logic"""
        if self._username == username and self._password == password:
            print("Login successful!")
            return True
        else:
            print("Invalid credentials!")
            return False

    # Added getters and setters for address
    def get_address(self):
        return self._address

    def set_address(self, new_address):
        self._address = new_address

    def __str__(self):
        return f"Admin: {self.full_name()} | Address: {self._address}"
