"""Model of a Building"""
from models.additional.address import Address
from models.client.client import Client
from models.properties.property import Property
from functions.utilities import check_sqm, check_integer, is_yes


class Building(Property):
    def __init__(self, property_id: str, address: Address, sqm: float, num_of_floors: int,
                 num_of_apartments: int, owner: Client, elevator: bool = False, garage: bool = False):
        super().__init__(property_id, address, sqm, owner)
        self.__num_of_floors = num_of_floors
        self.__num_of_apartments = num_of_apartments
        self.__elevator = elevator
        self.__garage = garage

    def get_num_of_floors(self):
        return self.__num_of_floors

    def get_num_of_apartments(self):
        return self.__num_of_apartments

    def has_elevator(self):
        return self.__elevator

    def has_garage(self):
        return self.__garage

    def __str__(self):
        elevator = "Building does not have an elevator"
        garage = "Building does not have a garage"
        if {self.__elevator} is True:
            elevator = "Building has an elevator"
        if {self.__garage} is True:
            garage = "Building has a garage"
        return f"Building info:\n" \
               f"{self.get_sqm()} m2\n" \
               f"{self.__num_of_floors} floors\n" \
               f"{self.__num_of_apartments} apartments\n" \
               f"{elevator}\n" \
               f"{garage}\n" \
               f"{self.get_address()}\n" \
               f"{self.get_owner()}"

    @classmethod
    def create(cls):
        print("Fill building details")
        property_id = input("Enter property id: ")
        sqm = check_sqm()
        print("Enter number of floors")
        num_of_floors = check_integer()
        print("Enter number of apartments")
        num_of_apartments = check_integer()
        print("Does a building have an elevator?")
        elevator = is_yes()
        print("Does a building have a garage?")
        garage = is_yes()
        address = Address.create()
        owner = Client.create()
        return cls(property_id, address, sqm, num_of_floors, num_of_apartments, owner, elevator, garage)
