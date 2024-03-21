def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):  # Decorator to handle input errors and exceptions
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide all required arguments."
        except Exception as e:
            return f"An error ocurred: {str(e)}"
        

    return inner


@input_error
def add_contact(args, contacts):  # Handler function to add a new contact
    if len(args)!=2:
        return IndexError
    name, phone = args
    if not phone.isdigit():
        return ValueError
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):  # Handler function to change an existing contact's phone number
    if len(args)!=2:
        return IndexError
    name, new_phone=args
    if name not in contacts:
        return KeyError
    if not new_phone.isdigit():
        return ValueError
    contacts[name]=new_phone
    return "Phone number for {name} is updated to {new_phone}"
   

@input_error
def display_contact(args, contacts):  # Handler function to display phone number of a contact
    if len(args)!=1:
        return IndexError
    name=args[0]
    if name not in contacts:
        return KeyError
    return f"Phone number for {name} is {contacts[name]}"
    
    
def display_all(contacts):  # Function to display all contacts and their phone numbers
    if not contacts:
        return "No contacts found."
    output=""
    for name, phone in contacts.items():
        output+= f"{name}:{phone}\n"
    return output
    
def main():   # Main function to execute the contact
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command=="change":
            print (change_contact(args, contacts))
        elif command=="phone":
            print(display_contact(args, contacts))
        elif command=="all":
            print(display_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()





