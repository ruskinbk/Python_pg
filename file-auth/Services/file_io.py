"""
    This is for file_io
"""

def file_reader(file):
    """
        This is for reading the file
    """
    with open(file, 'r', encoding="utf-8") as f:
        data = f.readlines()
    return data

def file_writer(file, data):
    """
        This is for writing the file
    """
    with open(file, 'w', encoding="utf-8") as f:
        f.write(data)
    return True

def file_appender(file, data):
    """
        This is for appending the file
    """ 
    with open(file, 'a', encoding="utf-8") as f:
        f.write(data)
    return True

def file_list_writer(file, list_data):
    """
        This is for writing the list
    """
    with open(file, 'w', encoding="utf-8") as f:
        f.writelines(list_data)
    return True
