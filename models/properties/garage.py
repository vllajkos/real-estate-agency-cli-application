"""Model of a Garage"""
from models.additional.address import Address
from models.client.client import Client
from models.properties.property import Property
from functions.utilities import check_integer, check_sqm


class Garage(Property):
    def __init__(self, property_id: str, address: Address, garage_number: int,
                 number_of_parking_spaces: int, sqm: float, owner: Client):
        super().__init__(property_id, address, sqm, owner)
        self.__number_of_parking_spaces = number_of_parking_spaces
        self.__garage_number = garage_number

    def __str__(self):
        return f"Garage info:\n" \
               f"Garage number {self.__garage_number}\n" \
               f"Number of parking spaces {self.__number_of_parking_spaces}\n" \
               f"{self.get_address()}\n" \
               f"{self.get_owner()}"

    def get_number_of_parking_spaces(self):
        return self.__number_of_parking_spaces

    def get_garage_number(self):
        return self.__garage_number

    @classmethod
    def create(cls):
        print("Fill garage details")
        property_id = input("Enter property id: ")
        print("Enter garage number")
        garage_number = check_integer()
        print("Enter number of parking spaces")
        number_of_parking_spaces = check_integer()
        sqm = check_sqm()
        address = Address.create()
        owner = Client.create()
        return Garage(property_id, address, garage_number, number_of_parking_spaces, sqm, owner)
