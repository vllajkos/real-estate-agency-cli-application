"""Model of a contract with Owner for listing a property on rent"""
from models.properties.property import Property
from datetime import datetime, date
from functions.utilities import check_float, check_integer, is_valid


class ContractWithOwnerForRent:
    def __init__(self, real_estate: Property, time_span: int, monthly_expenses: float, price: float, agency_fee: float):
        self.__time_span = time_span
        self.__monthly_expenses = monthly_expenses
        # creates unique contract id
        self.__contract_id = str(datetime.now().timestamp()).replace(".", "")
        self.__signing_date = str(date.today())
        self.__real_estate = real_estate
        self.__price = price
        self.__agency_fee = agency_fee

    def __str__(self):
        return f"\nContract id {self.__contract_id}\n" \
               f"Signing date {self.__signing_date}\n" \
               f"Monthly expenses {self.__monthly_expenses} $\n" \
               f"Renting price {self.__price} $\n" \
               f"Total monthly expenses {self.__monthly_expenses + self.__price} $\n" \
               f"Time span {self.__time_span} months\n" \
               f"Agency fee {self.__agency_fee} %\n\n" \
               f"{self.__real_estate}"

    def get_time_span(self):
        return self.__time_span

    def get_monthly_expenses(self):
        return self.__monthly_expenses

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
        print("Number of months for renting")
        time_span = check_integer()
        print("Regular monthly expenses for property")
        monthly_expenses = check_float()
        print("Renting price")
        price = check_float()
        print("Agency fee in %")
        agency_fee = is_valid(3)
        return cls(real_estate, time_span, monthly_expenses, price, agency_fee)
