"""
    This is for User
"""

# from .file_io import file_reader
from Services.file_io import file_reader

# class User:
#     def __init__(self, id, username, email, password):
#         self.id = id
#         self.username = username
#         self.email = email
#         self.password = password

#     def __repr__(self):
#         return f"User{self.id}, {self.username}, {self.password}\n"

#     def __str__(self):
#         return f"{self.id}, {self.username}, {self.password},{self.email}\n"

def get_last_id():
    """
    This is for getting last id
    """
    users = file_reader("data/users.csv")
    if users[-1].split(',')[0] == 'ID':
        return 0
    else:
        return int(users[-1].split(',')[0])