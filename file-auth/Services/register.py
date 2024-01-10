"""
This is register.py
"""
from Models.user import get_last_id
from .file_io import file_appender


def register(username:str, password:str, email: str):
    """
    This is for register
    """
    # users:str = file_reader("data/users.csv")
    register_id = get_last_id() + 1

    new_user = (f"{register_id},{username},{password},{email}\n")

    # {last_id+1},
    # file_writer("data/users.csv",(new_user))
    file_appender("data/users.csv",(new_user))
    print("Register Successfully!")
