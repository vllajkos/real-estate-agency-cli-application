"""Model for Address"""


class Address:
    def __init__(self, street_name: str, address_number: str, city: str, country: str):
        self.__street_name = street_name
        self.__address_number = address_number
        self.__city = city
        self.__country = country

    def __str__(self):
        return f"{self.__street_name} {self.__address_number}\n" \
               f"{self.__city}, {self.__country}"

    def get_street(self):
        return self.__street_name

    def get_number(self):
        return self.__address_number

    def get_city(self):
        return self.__city

    def get_country(self):
        return self.__country

    @classmethod
    def create(cls):
        print("Fill address details")
        street = input("Enter street name: ")
        address_number = input("Enter address number: ")
        city = input("Enter name of the city: ")
        country = input("Enter name of the country: ")
        return cls(street, address_number, city, country)
