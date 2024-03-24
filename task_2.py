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
            raise ValueError("Phone number must be a 10 digit string.")
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
        else:
            print(f"Record with name {name}, not found.")

# Creation of a new address book 
book = AddressBook()

# Creation of a entry for John
john_record = Record("John")
john_record.add_phone_number("1234567890")
john_record.add_phone_number("5555555555")

# Add a John entry to the address book
book.add_record(john_record)

# Creating and adding a new entry for Jane
jane_record = Record("Jane")
jane_record.add_phone_number("9876543210")
book.add_record(jane_record)

# Displaying all entries in the contact list
for name, record in book.data.items():
    print(record)

# Find and edit a phone number for John
john = book.search_record_by_name("John")
john.edit_phone_number("1234567890", "1112223333")

print(john)  # Displaying: Contact name: John, phones: 1112223333; 5555555555

# Searching for a specific phone number in John's entry
found_phone = john.find_phone_number("5555555555")
print(f"{john.name}: {found_phone}")  
# Deletion: 5555555555
john.remove_phone_number("5555555555")

print(john)

# Deletion Jane's entry
book.delete_record_by_name("Jane")

