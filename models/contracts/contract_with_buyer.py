"""Model of a contract between Buyer,Owner and Real estate agency"""
from Projekat.models.client.client import Client
from Projekat.models.properties.property import Property
from datetime import datetime, date


class ContractWithBuyer:
    def __init__(self, real_estate: Property, previous_owner: Client, price: float, agency_fee: float):
        # creates unique contract id
        self.__contract_id = str(datetime.now().timestamp()).replace(".", "")
        self.__signing_date = str(date.today())
        self.__real_estate = real_estate
        self.__previous_owner = previous_owner
        self.__price = price
        self.__agency_fee = agency_fee

    def __str__(self):
        return f"\nContract id {self.__contract_id}\n" \
               f"Signing date {self.__signing_date}\n" \
               f"Selling price {self.__price} $\n" \
               f"Agency fee {self.__agency_fee} %\n\n" \
               f"Bought from{self.__previous_owner}\n\n" \
               f"Property details and current owner\n{self.__real_estate}"

    def get_previous_owner(self):
        return self.__previous_owner

    def get_id(self):
        return self.__contract_id

    def get_date(self):
        return self.__signing_date

    def get_real_estate(self):
        return self.__real_estate

    def get_price(self):
        return self.__price

    def get_fee(self):
        return self.__agency_fee
