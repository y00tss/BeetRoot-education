"""Я не успел. Оказалось, что модифицировать готовый код сложнее, чем создавать новый. Я доделаю в течении нескольких дней( до след урока)
Ровно сутки пытался сделать так, чтобы работала функция добавления. Но никак не работал. Причина была в том, что я вручную создавал новый готовый json. Когда взял из урока и изменил данные - все заработало(((("""
import json
import sys
from file import *


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
                 '5 - exit\n -- ')
    match mode:
        case '1':
            add_data(phone_book)
        case '2':
            operation = 'search'
            select_data(phone_book, operation)
        case '3':
            operation = 'update'
            modify_data(phone_book)
        case '4':
            operation = 'delete'
            delete_data()
        case '5':
            operation = 'exit'
            exit()
            print("Exiting the program")

        case default:
            print("Wrong type")
    upload_to_json(phone_book)
    print("Data was reload")


def add_data(phone_book):
    phone_number = input("Enter Phone number: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    full_name = first_name + " " + last_name
    location = input("Enter your region code: ")
    if phone_number.isdigit() and first_name.isalpha() and last_name.isalpha():
        print("Data is right")
        insert_data = {"Phone number": int(phone_number),
                       "First name": first_name,
                       "Last name": last_name,
                       "Full name": first_name + " " + last_name,
                       "Region": location
                       }
        phone_book['Phone Book'].append(insert_data)
    else:
        print("Was entered incorrect data.")


def select_data(phone_book, operation):
    selector_mode = input(f"Select that are you searching: \n"
                          '1 - Region\n'
                          '2 - Full name\n'
                          '3 - Phone number\n')
    match selector_mode:
        case '1':
            field = 'Region'
            print_selected_data(phone_book, field, operation)
        case '2':
            field = 'Full name'
            print_selected_data(phone_book, field, operation)
        case '3':
            field = 'Phone number'
            print_selected_data(phone_book, field, operation)
        case default:
            print("Wrong data")


def print_selected_data(phone_book, field, operation):
    value = input(f" Input {field} to {operation} user: ")
    if field == 'Region':
        print_text(phone_book, value, field, operation)
    elif field == 'Full name':
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


def print_number(phone_book, value, field, operation):
    for i in phone_book['Phone Book']:
        if int(value) == i[f'{field}']:
            if operation == 'search':
                print(i)
                return i
            else:
                phone_book['Phone Book'].remove(i)



def modify_data(phone_book):
    phone_number = input("Enter phone number, that you want to update: ")
    if phone_number.isdigit():
        if check_data_integrity(phone_number, phone_book):
            print(f"Dont have this {phone_number}")
        else:
            field = 'Phone number'
            fields = input("With comma enter parameters, that you want to update: ").title()
            try:
                for field in fields.split(","):
                    value = input(f"Enter new parameter for {field}: ")
                    value = int(value) if field in ['Phone number'] else value
                    if field == 'Phone number' and not check_data_integrity(value, phone_book):
                        print(f"Phone number - {phone_number} already registered")
###################################################################################################################################################
            except:
                print("Wrong parameters")
    else:
        print("Wrong data")


def check_data_integrity(phone_number, phone_book):
    for i in phone_book['Phone Book']:
        if i['Phone number'] == int(phone_number):
            return False
    return True


def exit_program():
    print("Exiting the program...")
    sys.exit()


main()
