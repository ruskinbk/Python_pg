"""
This is menu.py
"""
from Services.photographer_utils import (
    add_new_photographers,
    view_all_photographers,
    delete_photographers,
    update_photographers)
from Services.photo_utils import add_photos, view_all_photos, delete_photos
from Services.register import register
from Services.login import login

def login_menu():
    """
    This is login menu
    """
    print("\n##################LOGIN########################\n")
    print("WELCOME! WELCOME! WELCOME!")
    print("Register menu for photographer")
    print()
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("\n###############################################\n")
    choice = int(input("Enter your choice from [1-3]: "))

    if choice == 1:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        email = input("Enter your email: ")

        print(f"You entered username {username}, password {password} and email {email}")       
        if register(username, password, email):
            main_menu()
            print("Registration successful!")
        else:
            login_menu()
            print("Registration failed.  Please try again.")
    elif choice == 2:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        print(f"You entered username {username} and password {password}")

        if login(username, password) is True:
            print("Login successful!")
            main_menu()
        else:
            print("Login failed.  Please try again.")
            login_menu()

    elif choice == 3:
        print("You are exiting Register Menu...")
    else:
        print("Invalid choice")

def main_menu():
    """
    This is main menu
    """
    print("Welcome to the Main Menu.")
    print("Please choose from the following options:")
    print("1. Photographer Menu")
    print("2. Photo Menu")
    print("3. Go Back")
    print("\n###############################################\n") 
    choice = int(input("Enter your choice: "))
    if choice == 1:
        photographer_menu()
    elif choice == 2:
        photo_menu()
    elif choice == 3:
        print("You are exiting Main Menu...")
        login_menu()
    else:
        print("Invalid choice")

def photographer_menu():
    """
    This is photographer menu
    """
    print("Welcome to the Photographers Information menu.")
    print("Please choose from the following options:")
    print("1. Add Photographers")
    print("2. View All Photographers")
    print("3. Delete Photographers")
    print("4. Update Photographers")
    print("5. Logout")
    print("6. Change Password")
    print("7. Go Back")
    print("\n###############################################\n")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_new_photographers()
        main_menu()
    elif choice == 2:
        view_all_photographers()
        main_menu()
    elif choice == 3:
        delete_photographers()
        main_menu()
    elif choice == 4:
        update_photographers()
        main_menu()
    elif choice == 5:
        login_menu()
    elif choice == 6:
        print("Change Password")
    elif choice == 7:
        main_menu()
    else:
        print("Invalid choice")

def photo_menu():
    """
    This is photo menu
    """
    print("\n###############################################\n")
    print("Welcome to the Photos Information menu.")
    print("Please choose from the following options:")
    print("1. Add Photo")
    print("2. View All Photos")
    print("3. Delete Photo")
    print("4. Go Back")
    print("\n###############################################\n") 
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_photos()
        main_menu()
    elif choice == 2:
        view_all_photos()
        main_menu()
    elif choice == 3:
        delete_photos()
        photo_menu()
    elif choice == 4:
        main_menu()
    else:
        print("Invalid choice")
