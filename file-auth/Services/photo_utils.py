"""
This is photo_utils.py
"""

from tabulate import tabulate
from Models.photos import get_last_photo_id
from .file_io import file_appender, file_reader, file_list_writer

def add_photos():
    """
    This is for adding photos
    """
    photo_id = get_last_photo_id() + 1
    photo_name = input("Enter the name of the photo: ")
    size = input("Enter the size of the photo: ")
    alt_text = input("Enter the description of the photo: ")

    new_photo = f"{photo_id}, {photo_name}, {size}, {alt_text}\n"
    file_appender("data/photo.csv", new_photo)
    print("New photo added Successfully!")

def view_all_photos():
    """
    This is for viewing all photos
    """
    photo = file_reader("data/photo.csv")
    data = []
    for photos in photo:
        data.append([photos.split(',')[0], photos.split(',')[1], photos.split(',')[2], photos.split(',')[3]])
    print(tabulate(data))

def delete_photos():
    """
    This is for deleting photos
    """

    #after deleting id 1, sync id from 1 on csv

    photo_id = input("Enter id: ")
    photos = file_reader("data/photo.csv")
    found = False
    for photo in photos:
        if str(photo.split(',')[0]) == str(photo_id):  #for searching the id from given id by 
            photos.remove(photo)
            found = True
            break
    if found is False:
        print("Invalid ID. Photo not found.")
    else:
        file_list_writer("data/photo.csv", photos)
        print("Photo deleted successfully.")
