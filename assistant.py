def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: list, contacts: dict):
    name, phone = args
    if name not in contacts:
        # contacts[name.lower()] = phone
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact already exists."

def change_contact(args: list, contacts: dict):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact does not exist."

def show_phone(args: list, contacts: dict):
    # name = str(args[0]).lower()
    name = str(args[0])
    return f"{contacts[name]}"

def show_all(contacts):
    if contacts:
        for key, value in contacts.items():
            print(f"{key.capitalize()} {value}")
    else:
        print("There are no contacts.")
    
def usage():
    return "Invalid command. Usage: 'hello'\n'close'\n'exit'\n'all'\n'add name phone_number'\n"\
            "'change name phone_number'\n'phone name'"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone" and len(args) == 1:
                print(show_phone(args, contacts))
            elif command == "all":
                show_all(contacts)
            else:
                print(usage())
        except ValueError:
            print(usage())

if __name__ == "__main__":
    main()