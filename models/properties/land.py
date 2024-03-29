"""Model of a Land"""
from models.client.client import Client
from models.properties.property import Property
from functions.options_data import TYPE_OF_LAND
from models.additional.address import Address
from functions.utilities import show_options, check_sqm, choose_option_from_menu


class Land(Property):
    def __init__(self, property_id: str, address: Address, type_of_land: int, sqm: float, owner: Client):
        super().__init__(property_id, address, sqm, owner)
        self.__type_of_land = type_of_land

    def __str__(self):
        return f"Land info:\n" \
               f"{TYPE_OF_LAND[self.__type_of_land]}\n" \
               f"{self.get_sqm()} m2\n" \
               f"{self.get_address()}\n" \
               f"{self.get_owner()}"

    def get_type_of_land(self):
        return self.__type_of_land

    def change_type_of_land(self, new_type_of_land: int):
        self.__type_of_land = new_type_of_land

    @classmethod
    def create(cls):
        print("Fill land details")
        property_id = input("Enter property id: ")
        type_of_land = choose_option_from_menu(TYPE_OF_LAND)
        sqm = check_sqm()
        address = Address.create()
        owner = Client.create()
        return cls(property_id, address, type_of_land, sqm, owner)
