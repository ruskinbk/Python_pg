"""
This is photographer_utils.py
"""

from tabulate import tabulate
from Models.photographers import get_last_photographer_id
from .file_io import file_reader, file_appender, file_list_writer

def add_new_photographers():
    """
    This is for adding new Photographers
    """
    photographer_id = get_last_photographer_id() + 1
    name = input('Enter your name: ')
    experience = input('Enter your experience: ')
    price = input('Enter your price: ')

    new_photographers = f"{photographer_id}, {name}, {experience}, {price}\n"
    file_appender("data/photographer.csv", new_photographers)
    print("New photographer in the house!!!")

def view_all_photographers():
    """
    This is for viewing all Photographers
    """
    photographers = file_reader("data/photographer.csv")
    data = []
    for photographer in photographers:
        data.append([photographer.split(',')[0], photographer.split(',')[1], photographer.split(',')[2], photographer.split(',')[3]])
    print(tabulate(data))

def delete_photographers():
    """
    This is for deleting Photographers
    """
    photographer_id = input("Enter id: ")
    photographers = file_reader("data/photographer.csv")
    found = False
    for photographer in photographers:
        if str(photographer.split(',')[0]) == str(photographer_id):  #for searching the id from given id by 
            photographers.remove(photographer)
            found = True
            break
    if found is False:
        print("Invalid ID. Photographer not found.")
    else:
        file_list_writer("data/photographer.csv", photographers)
        print("Photographer deleted successfully.")

def update_photographers():
    """
    This is for updating Photographers
    """
    photographer_id = input("Enter id: ")
    photographers = file_reader("data/photographer.csv")
    for photographer in photographers:
        if str(photographer.split(',')[0]) == str(id):
            photographers.remove(photographer)
            name=input(f"Enter the new name for {photographer.split(',')[1]}: ")
            experience=input(f"Enter the new experience for {photographer.split(',')[2]}: ")
            price=input(f"Enter the new price for {photographer.split(',')[3].strip()}: ")
            
            updated_photographer = f"{photographer_id},{name},{experience},{price}\n"
            photographers.append(updated_photographer)
            # Photographers.append(f"{id}, {name}, {experience}, {price}\n")#it appends the acquired requirements

    file_list_writer("data/photographer.csv", photographers) #writes in the list
    print("Photographer updated successfully.")
