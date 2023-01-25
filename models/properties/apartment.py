"""Model of an Apartment"""
from models.additional.address import Address
from models.client.client import Client
from models.properties.property import Property
from functions.utilities import check_integer, check_sqm, is_yes, check_room


class Apartment(Property):
    def __init__(self, property_id: str, address: Address, apartment_number: int, floor: int,
                 rooms: int, sqm: float, owner: Client, terrace: bool = False, parking_space: bool = False,
                 air_conditioning: bool = False, heating: bool = False, cable: bool = False):
        super().__init__(property_id, address, sqm, owner)

        self.__apartment_number = apartment_number
        self.__floor = floor
        self.__rooms = rooms
        self.__terrace = terrace
        self.__parking_space = parking_space
        self.__air_conditioning = air_conditioning
        self.__heating = heating
        self.__cable = cable

    def __str__(self):
        additional_features = "Additional features: "
        if self.__terrace is True:
            additional_features += "Terrace, "
        if self.__air_conditioning is True:
            additional_features += "Parking space, "
        if self.__heating is True:
            additional_features += "Heating, "
        if self.__air_conditioning is True:
            additional_features += "Air conditioning, "
        if self.__cable is True:
            additional_features += "Cable, "
        if additional_features[-2] == ",":
            additional_features = additional_features[:-2]

        return f"Apartment info:\n" \
               f"{self.__rooms} rooms\n" \
               f"{self.get_sqm()} m2\n" \
               f"Apartment number {self.__apartment_number}\n" \
               f"Floor number {self.__floor}\n" \
               f"{additional_features}\n" \
               f"{self.get_address()}\n" \
               f"{self.get_owner()}"

    def get_number(self):
        return self.__apartment_number

    def get_floor(self):
        return self.__floor

    def get_rooms(self):
        return self.__rooms

    def get_terrace(self):
        return self.__terrace

    def get_parking_space(self):
        return self.__parking_space

    def get_air_conditioning(self):
        return self.__air_conditioning

    def get_heating(self):
        return self.__heating

    def get_cable(self):
        return self.__cable

    @classmethod
    def create(cls):
        print("Fill apartment details")
        property_id = input("Enter property id: ")
        print("Enter apartment number")
        apartment_number = check_integer()
        print("Enter floor number")
        floor = check_integer()
        rooms = check_room()
        sqm = check_sqm()
        print("Terrace?")
        terrace = is_yes()
        print("Parking space?")
        parking_space = is_yes()
        print("Air conditioning?")
        air_conditioning = is_yes()
        print("Heating?")
        heating = is_yes()
        print("Cable?")
        cable = is_yes()
        address = Address.create()
        owner = Client.create()
        return cls(property_id, address, apartment_number, floor, rooms, sqm, owner, terrace, parking_space,
                   air_conditioning, heating, cable)


