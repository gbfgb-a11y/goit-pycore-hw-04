from datetime import datetime; import random; import re;import sys
from pathlib import Path
from colorama import Fore, Style, init
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

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_inp = input("Enter a command: ")
        command, args = command_spliting(user_inp)
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
            print(contacts)
        else:
            print("Invalid command.")
if __name__ == '__main__':
    main()
