"""
This is login.py
"""
    
from .file_io import file_reader

def login(username, password):
    """
    This is for login
    """
    # print(username, password, "Here is it")
    status = False
    users = file_reader("data/users.csv")
    for user in users:
        if username.strip() == str(user.split(',')[1].strip()):  #for checking username and password from menu.py login menu
            print("username", username)
            if password.strip() == user.split(',')[2].strip():
                print(password, user.split(',')[2].strip())
                status = True
        else:     
            status = False
    return status