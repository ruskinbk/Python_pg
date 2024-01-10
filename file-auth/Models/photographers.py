"""
    This is for Photographers
"""

from Services.file_io import file_reader

# class Photographers:
#     """
#         This is for Photographers Class
#     """
#     def __init__(self, id, name, experience, price):
#         """
#             This is for initializing
#         """
#         self.id = id
#         self.name = name
#         self.experience = experience
#         self.price = price

#     def __str__(self):
#         """
#             This is for str
#         """
#         return f"ID: {self.id}\nName: {self.name}\nExperience: {self.experience}\nPrice: {self.price}"

def get_last_photographer_id():
    """
        This is for getting the last id
    """
    photographers = file_reader("data/photographer.csv")
    if photographers[-1].split(',')[0] == 'ID':
        return 0
    return int(photographers[-1].split(',')[0])