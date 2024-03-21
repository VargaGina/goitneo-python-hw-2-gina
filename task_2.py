from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value): # Check if the phone number is a 10-digit string
        if not isinstance(value, str) or len(value) != 10 or not value.isdigit():
            return ValueError("Phone number must be a 10 digit string.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone_number(self, phone):  # Add a phone number to the record
        self.phones.append(Phone(phone))

    def remove_phone_number(self, phone):  # Delete a phone number from the record
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone_number(self, old_phone, new_phone):  # Edit a phone number 
        for idx, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[idx] = Phone(new_phone)
                break

    def find_phone_number(self, phone):  # Search for a phone number
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
   
    def add_record(self, record):   # Add a record to the address book
        self.data[record.name.value] = record

    def search_record_by_name(self, name): # Search for a record by name in the address book
        return self.data.get(name)

    def delete_record_by_name(self, name): # Delete a record by name from the address book
        if name in self.data:
            del self.data[name]

