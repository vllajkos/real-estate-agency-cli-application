"""Abstract class of a Property"""
from abc import ABC
from models.additional.address import Address
from models.client.client import Client

class Property(ABC):
    def __init__(self, property_id: str, address: Address, sqm: float, owner: Client):
        self.__property_id = property_id
        self.__address = address
        self.__sqm = sqm
        self.__owner = owner

    def get_id(self):
        return self.__property_id

    def get_address(self):
        return self.__address

    def get_sqm(self):
        return self.__sqm

    def get_owner(self):
        return self.__owner

    def change_owner(self, new_owner: Client) -> None:
        """Changing owner."""
        self.__owner = new_owner
