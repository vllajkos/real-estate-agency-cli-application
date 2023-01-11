"""Model of a contract with Owner for listing a property on sale"""
from models.properties.property import Property
from datetime import datetime, date
from functions.utilities import check_float, is_valid


class ContractWithOwnerForSale:
    def __init__(self, real_estate: Property, price: float, agency_fee: float):
        # creates unique contract id
        self.__contract_id = str(datetime.now().timestamp()).replace(".", "")
        self.__signing_date = str(date.today())
        self.__real_estate = real_estate
        self.__price = price
        self.__agency_fee = agency_fee

    def __str__(self):
        return f"\nContract id {self.__contract_id}\n" \
               f"Signing date {self.__signing_date}\n" \
               f"Selling price {self.__price} $\n" \
               f"Agency fee {self.__agency_fee} %\n\n" \
               f"{self.__real_estate}"

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

    @classmethod
    def create(cls, real_estate):
        print("Selling price")
        price = check_float()
        print("Agency fee in %")
        agency_fee = is_valid(3)
        return cls(real_estate, price, agency_fee)
