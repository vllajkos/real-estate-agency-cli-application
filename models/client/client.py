"""Model of a Client"""
from Projekat.models.additional.address import Address
from Projekat.functions.utilities import is_valid

class Client:
    def __init__(self, name: str, surname: str, id_number: str, jmbg: str, address: Address, phone_number: str):
        """Model of a Client object"""
        self.__name = name
        self.__surname = surname
        self.__id_number = id_number
        self.__jmbg = jmbg
        self.__address = address
        self.__phone_number = phone_number

    def __str__(self):
        return f"\n{self.__name} {self.__surname}\n" \
               f"{self.__address}\n" \
               f"{self.__phone_number}"

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_id(self):
        return self.__id_number

    def get_jmbg(self):
        return self.__jmbg

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

    @classmethod
    def create(cls):
        print("Fill client's details")
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        print("Enter id number")
        id_number = is_valid(2)
        print("Enter JMBG")
        jmbg = is_valid(1)
        print("Enter phone number")
        phone_number = is_valid(4)
        address = Address.create()
        return Client(name, surname, id_number, jmbg, address, phone_number)
