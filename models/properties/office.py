"""Model of an Office as property type"""
from Projekat.models.additional.address import Address
from Projekat.models.client.client import Client
from Projekat.models.properties.property import Property
from Projekat.functions.utilities import check_sqm, check_integer, return_bool


class Office(Property):
    def __init__(self, property_id: str, address: Address, sqm: float, owner: Client,
                 office_number: int, number_of_offices: int, terrace: bool = False, parking_spaces: int = 0,
                 air_conditioning: bool = False, heating: bool = False):
        super().__init__(property_id, address, sqm, owner)
        self.__office_number = office_number
        self.__number_of_offices = number_of_offices
        self.__terrace = terrace
        self.__parking_spaces = parking_spaces
        self.__air_conditioning = air_conditioning
        self.__heating = heating

    def __str__(self):
        additional_features = "Additional features: "
        if self.__terrace is True:
            additional_features += "Terrace, "
        if self.__heating is True:
            additional_features += "Heating, "
        if self.__air_conditioning is True:
            additional_features += "Air conditioning, "
        if additional_features[-2] == ",":
            additional_features = additional_features[:-2]

        return f"Office info:\n" \
               f"Office number {self.__office_number}\n" \
               f"Number of offices {self.__number_of_offices}\n" \
               f"{self.get_sqm()} m2\n" \
               f"Number of parking spaces {self.__parking_spaces}\n" \
               f"{additional_features}\n" \
               f"{self.get_address()}\n" \
               f"{self.get_owner()}"

    def get_number(self):
        return self.__office_number

    def get_number_of_offices(self):
        return self.__number_of_offices

    def get_terrace(self):
        return self.__terrace

    def get_parking_spaces(self):
        return self.__parking_spaces

    def get_air_conditioning(self):
        return self.__air_conditioning

    def get_heating(self):
        return self.__heating

    @classmethod
    def create(cls):
        print("Fill office details")
        property_id = input("Enter property id: ")
        print("Enter office number")
        office_number = check_integer()
        print("Enter number of offices")
        number_of_offices = check_integer()
        sqm = check_sqm()
        print("Enter number of available parking spaces for employees")
        parking_space = check_integer()
        print("Terrace?")
        terrace = return_bool()
        print("Air conditioning?")
        air_conditioning = return_bool()
        print("Heating?")
        heating = return_bool()
        address = Address.create()
        owner = Client.create()
        return cls(property_id, address, sqm, owner, office_number, number_of_offices, terrace, parking_space,
                   air_conditioning, heating)
