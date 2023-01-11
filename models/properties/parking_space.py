"""Model of a Parking space"""
from Projekat.models.additional.address import Address
from Projekat.models.client.client import Client
from Projekat.models.properties.property import Property
from Projekat.functions.utilities import check_integer, check_sqm


class ParkingSpace(Property):

    def __init__(self, property_id: str, address: Address, parking_space_num: int, sqm: float,
                 owner: Client):
        super().__init__(property_id, address, sqm, owner)
        self.__parking_space_num = parking_space_num

    def __str__(self):
        return f"Parking space info:\n" \
               f"Parking space number {self.__parking_space_num}\n" \
               f"{self.get_address()}\n" \
               f"{self.get_owner()}"

    def get_parking_space_num(self):
        return self.__parking_space_num

    @classmethod
    def create(cls):
        print("Fill parking space details")
        property_id = input("Enter property id: ")
        print("Enter parking space number")
        parking_space_num = check_integer()
        sqm = check_sqm()
        address = Address.create()
        owner = Client.create()
        return cls(property_id, address, parking_space_num, sqm, owner)
