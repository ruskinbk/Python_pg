"""
Photographer Class
"""

class Photographer:
    def __init__(self, id, first_name, last_name, age, phone_no, email, photos, address, datetime):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

        # This one-liner cannot be used if photos is not a list 

        self.photos = photos if self.validate_photos(photos) else list()

        self.email = email if self.validate_email(email) else "Incorrect Email!"

        self.phone_no = phone_no if self.validate_phone_no(phone_no) else "Invalid Phone Number!"

        self.age = age if self.validate_age(age) else "Sorry! You are underage."

        # if self.validate_photos(photos):
        #     print("Photographer created with valid data")
        #     self.photos = photos
        # else:
        #     print("Invalid data is inserted")
        #     self.photos = list()

        self.photos = photos
        self.address = address
        self.datetime = datetime

    def get_photos_desc(self):
        print(f"\nThe photos of the photographer { self.first_name } { self.last_name}:")
        for photo in (self.photos):
            print("ID: ", photo.id)
            print("Name: " , photo.photo_name)
            print("Size of the photo: ", photo.size)
            print("Description: ", photo.alt_text)
            print()

    def validate_photos(self, _photos):
        status = False
        if isinstance(_photos, list):
            for _photo in _photos:
                status = False
                if isinstance(_photo, Photos):
                    status = True
                else:
                    status = False
        return status

    def validate_email(self, _email):
        return True if (isinstance(_email, str)) and (("@" in _email) and ("." in _email) and (_email.endswith(".com"))) else False
        # if isinstance(_email, str):
        #     if ("@" in _email) and ("." in _email) and (_email.endswith(".com")): return True
        #     else: return False

    def validate_age(self,_age):
        return True if ((_age > 12 ) and (_age < 120)) else False
        # if (_age>12) and (_age<120):
        #     return True
        # else:
        #     return False

    def validate_phone_no(self,_phone_no):
        if isinstance(_phone_no, str):
            if(_phone_no.startswith("+977")): return True
    def validate_address(self,):
        pass

    def validate_datetime(self,):
        pass

    def validate_id(self,):
        pass

    def photographer_details(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Phone No.: {self.phone_no}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        self.get_photos_desc()
        # print(f"Photos: {self.photos}")
        print("------------------------------------------------------------------")
    def __str__(self) -> str:
        return str(self.first_name)


class Photos:
    def __init__(self, id, photo_name="", size=0.0, alt_text=''):
        self.id = int(id)
        self.photo_name = str(photo_name)
        self.size = float(size)
        self.alt_text = str(alt_text)

    def __str__(self) -> str:
        return str(self.photo_name)
