from task2 import *
import unittest
from unittest.mock import patch


class Test_phonebook(unittest.TestCase):
    def test_main_menu(self):
        mode = input("Choose type of actions: \n"
                     '1 - Adding of data: \n'
                     '2 - Searching of data: \n'
                     '3 - Update of data: \n'
                     '4 - Deleting of data: \n'
                     '5 - exit\n ==> ')
        right_answer = ['1', '2', '3', '4', '5']
        self.assertIn(mode, right_answer, msg="Input data should be in range from 1 to 5")

    def test_add_data(self):
        phone_book = load_from_json()
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
                               "Full name": full_name,
                               "Location": location}
                phone_book.append(insert_data)
                print("Data was added")
            else:
                print("This phone number already exists")
        else:
            print("Data is wrong")
        self.assertTrue(phone_number.isdigit(), msg="Phone number should be digit")
        self.assertTrue(first_name.isalpha(), msg="First name should be alpha")
        self.assertTrue(last_name.isalpha(), msg="Last name should be alpha")
        self.assertTrue(check_data_integrity(phone_number, phone_book), msg="Phone number should be unique")

    def select_data(self):
        selector_mode = input(f"Select that are you searching: \n"
                              '1 - Region\n'
                              '2 - First name\n'
                              '3 - Last name\n'
                              '4 - Phone number\n')
        right_answer = ['1', '2', '3', '4']
        self.assertIn(selector_mode, right_answer, msg="Input data should be in range from 1 to 4")



