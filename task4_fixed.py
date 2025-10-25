from datetime import datetime; import random; import re;import sys
from pathlib import Path
# Завданя 4
def command_spliting(user_inp):
    cmd, *args = user_inp.split( )
    cmd = cmd.strip().lower()
    return cmd, args
def adding_inf(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

def get_phonenum(name, contacts):
    phone = contacts.get(name)
    if phone:
        return f"{name}: {phone}"   
    else:
        return f"No contact named {name}"
def all(contacts):
    for i in contacts:
        print(f'{i}, {contacts.get(i)}')
def change(args):
    if len(args) != 2:
        return "Error: Use 'change <name> <new_phone>'"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} changed to {phone}."
    else:
        return f"No contact named {name}."
def delete(name):
    contacts.pop(name)
    return 'contact deleted.'
contacts = {}
def main():
    global contacts
    print("Welcome to the assistant bot!")
    while True:
        user_inp = input("Enter a command: ")
        command, args = command_spliting(user_inp)
        try:    
            if command == 'hello':
                print('"How can I help you?"')
            elif command in ['close','exit']:
                print("Good bye!")
                break
            elif command == 'add':
                print(adding_inf(args, contacts))
            elif command == 'phone':
                print(get_phonenum(args[0],contacts))
            elif command == 'all':
                all(contacts)
            elif command == 'change':
                print(change(args))
            elif command == 'delete':
                print(delete(args[0]))
            else:
                print("Invalid command.")
        except ValueError:
            print('Your line is empty, try again later.')
if __name__ == '__main__':
    main()

