import json
import sys


def load_from_json():
    try:
        with open('PhoneBook.json', 'r') as json_file:
            phone_book = json.load(json_file)
        return phone_book
    except FileNotFoundError:
        raise Exception("File not found")


def upload_to_json(phone_book):
    with open('PhoneBook.json', 'w') as json_file:
        json.dump(phone_book, json_file)


def main():
    phone_book = load_from_json()
    mode = input("Choose type of actions: \n"
                 '1 - Adding of data: \n'
                 '2 - Searching of data: \n'
                 '3 - Update of data: \n'
                 '4 - Deleting of data: \n'
                 '5 - exit\n ==> ')
    match mode:
        case '1':
            add_data(phone_book)
        case '2':
            operation = 'search'
            select_data(phone_book, operation)
        case '3':
            operation = 'update'
            modify_data(phone_book, operation)
        case '4':
            operation = 'delete'
            delete_data(phone_book, operation)
        case '5':
            operation = 'exit'
            exit()
            print("Exiting the program")

        case default:
            print("Wrong type")
    upload_to_json(phone_book)
    print("Data was reload")


def add_data(phone_book):
    phone_number = input("Enter Phone number: +")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    full_name = first_name + " " + last_name
    location = input("Enter your region code: ")
    if phone_number.isdigit() and first_name.isalpha() and last_name.isalpha():
        if check_data_integrity(phone_number, phone_book):
            print("Data is right")
            insert_data = {"Phone number": int(phone_number),
                           "First name": first_name,
                           "Last name": last_name,
                           "Full name": first_name + " " + last_name,
                           "Region": location
                           }
            phone_book['Phone Book'].append(insert_data)
        else:
            print("This number already registered")
    else:
        print("Was entered incorrect data.")


def select_data(phone_book, operation):
    selector_mode = input(f"Select that are you searching: \n"
                          '1 - Region\n'
                          '2 - First name\n'
                          '3 - Last name\n'
                          '4 - Phone number\n')
    match selector_mode:
        case '1':
            field = 'Region'
            print_selected_data(phone_book, field, operation)
        case '2':
            field = 'First name'
            print_selected_data(phone_book, field, operation)
        case '3':
            field = 'Last name'
            print_selected_data(phone_book, field, operation)
        case '4':
            field = 'Phone number'
            print_selected_data(phone_book, field, operation)
        case default:
            print("Wrong data")


def print_selected_data(phone_book, field, operation):
    value = input(f" Input {field} to {operation} user: ")
    if field == 'Region':
        print_text(phone_book, value, field, operation)
    elif field == 'First name':
        print_text(phone_book, value, field, operation)
    elif field == 'Last name':
        print_text(phone_book, value, field, operation)
    elif field == 'Phone number':
        print_number(phone_book, value, field, operation)


def print_text(phone_book, value, field, operation):
    for i in phone_book['Phone Book']:
        if value in i[f'{field}']:
            if operation == 'search':
                print(i)
            else:
                phone_book['Phone Book'].remove(i)
        else:
            print(f"{value} is not registered")


def print_number(phone_book, value, field, operation):
    for i in phone_book['Phone Book']:
        if int(value) == i[f'{field}']:
            if operation == 'search':
                print(i)
                return i
            else:
                phone_book['Phone Book'].remove(i)
        else:
            print("Dont have this number")


def modify_data(phone_book, phone_number):
    phone_number = input("Enter phone number, that you want to update: +")
    if phone_number.isdigit():
        if check_data_integrity(phone_number, phone_book):
            print(f"Dont have this {phone_number} phone number...")
        else:
            field = 'Phone number'
            record = print_int_data(phone_book, phone_number, field)
            type_type = input('Enter parameters, that you want to update: \n"1" - Region \n"2" - Full name \n ==>')
            match type_type:
                case "1":
                    value = input(f"Enter new region for phone {phone_number}: ")
                    record['Region'] = value
                case "2":
                    try:
                        first_name = input("Enter first name: ")
                        last_name = input("Enter last name: ")
                        for entry in phone_book["Phone Book"]:
                            entry["First name"] = first_name
                            entry["Last name"] = last_name
                            entry["Full name"] = f"{first_name} {last_name}"
                    except:
                        print("Wrong data")
    else:
        print("Phone number should be a digits")


def check_data_integrity(phone_number, phone_book):
    for i in phone_book['Phone Book']:
        if i['Phone number'] == int(phone_number):
            return False
    return True


def print_int_data(phone_book, value, field):
    for i in phone_book['Phone Book']:
        if int(value) == i[f'{field}']:
            print(i)
            return i


def delete_data(phone_book, operation):
    phone_number = int(input("Enter phone, that data you want to delete: +"))
    if not check_data_integrity(phone_number, phone_book):
        phone_book["Phone Book"] = [entry for entry in phone_book["Phone Book"] if entry["Phone number"] != phone_number]
        print(f'All data that related to number {phone_number} was deleted!')
    else:
        print(f"This number - {phone_number} is not registered")



def exit_program():
    print("Exiting the program...")
    sys.exit()


main()
