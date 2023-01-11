"""Model of a Contract between Tenant,Owner and Real estate agency"""
from Projekat.models.client.client import Client
from Projekat.models.properties.property import Property
from datetime import datetime, date
from Projekat.functions.utilities import return_expiration_date


class ContractWithTenant:
    def __init__(self, real_estate: Property, tenant: Client, time_span: int, monthly_expenses: float, price: float,
                 agency_fee: float):
        self.__tenant = tenant
        self.__time_span = time_span
        self.__monthly_expenses = monthly_expenses
        # creates unique contract id
        self.__contract_id = str(datetime.now().timestamp()).replace(".", "")
        self.__signing_date = str(date.today())
        self.__expiration_date = return_expiration_date(self.__signing_date, self.__time_span)
        self.__real_estate = real_estate
        self.__price = price
        self.__agency_fee = agency_fee

    def __str__(self):
        return f"\nContract id {self.__contract_id}\n" \
               f"Signing date {self.__signing_date}\n" \
               f"Time span {self.__time_span} months\n" \
               f"Expiration date {self.__expiration_date}\n" \
               f"Monthly expenses {self.__monthly_expenses} $\n" \
               f"Renting price {self.__price} $\n" \
               f"Total monthly expenses {self.__price + self.__monthly_expenses}\n" \
               f"Tenant info\n{self.__tenant}\n" \
               f"Rented property info\n{self.__real_estate}"

    def get_tenant(self):
        return self.__tenant

    def get_time_span(self):
        return self.__time_span

    def get_monthly_expenses(self):
        return self.__monthly_expenses

    def get_id(self):
        return self.__contract_id

    def get_date(self):
        return self.__signing_date

    def get_expiration_date(self):
        return self.__expiration_date

    def get_real_estate(self):
        return self.__real_estate

    def get_price(self):
        return self.__price

    def get_fee(self):
        return self.__agency_fee
