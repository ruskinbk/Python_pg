"""
This is Photos.py
"""

from Services.file_io import file_reader

# class Photo:
#     """
#     This is for Photos Class
#     """
#     def __init__(self, id, photo_name="", size=0.0, alt_text=''):
#         """
#         This is for initializing
#         """
#         self.id = int(id)
#         self.photo_name = str(photo_name)
#         self.size = float(size)
#         self.alt_text = str(alt_text)

#     def __str__(self):
#         """
#         This is for str
#         """
#         return f"ID: {self.id}\nPhoto Name: {self.photo_name}\Size: {self.size}\nDescription: {self.alt_text}\n"


def get_last_photo_id():
    """
    This is for getting the last id
    """
    photos = file_reader("data/photo.csv")
    if photos[-1].split(',')[0] == 'ID':
        return 0
    return int(photos[-1].split(',')[0])