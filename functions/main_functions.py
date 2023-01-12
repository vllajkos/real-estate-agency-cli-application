import os
from models.client.client import Client
from models.contracts.contract_with_tenant import ContractWithTenant
from models.contracts.with_owner_for_rent import ContractWithOwnerForRent
from models.properties.office import Office
from models.properties.building import Building
from models.properties.parking_space import ParkingSpace
from functions.utilities import choose_option_from_menu, archive_file, choose_id_return_contract_and_path, \
    display_properties_by_type_returns_list_by_type, search_key, save_progress, get_database_path, \
    from_file_return_object, sort_contract_list_by_price, check_conditions, return_bool
from functions.options_data import TYPE_OF_PROPERTY, NAME_OF_DIRECTORY
from models.properties.apartment import Apartment
from models.properties.land import Land
from models.properties.garage import Garage
from models.contracts.with_owner_for_sale import ContractWithOwnerForSale
from models.contracts.contract_with_buyer import ContractWithBuyer


def list_property(directory_name: str) -> bool:
    """Creates contract between owner and real estate agency for listing a property on sale/rent"""
    option = choose_option_from_menu(TYPE_OF_PROPERTY)
    # for chosen type creates property
    match option:
        case 1:
            real_estate = Land.create()
        case 2:
            real_estate = Apartment.create()
        case 3:
            real_estate = Building.create()
        case 4:
            real_estate = Office.create()
        case 5:
            real_estate = Garage.create()
        case 6:
            real_estate = ParkingSpace.create()
        case other:
            return False
    if directory_name == NAME_OF_DIRECTORY[1]:
        contract = ContractWithOwnerForSale.create(real_estate)
    else:
        contract = ContractWithOwnerForRent.create(real_estate)
    print(contract)
    print("Sign contract?")
    if return_bool():
        save_progress(directory_name, contract)
        return True


def buy_rent_property(directory_name: str) -> None | bool:
    """Creates contract for sale/rent between client, owner and real estate agency"""
    if directory_name == NAME_OF_DIRECTORY[3]:
        search_directory_name = NAME_OF_DIRECTORY[1]
    else:
        search_directory_name = NAME_OF_DIRECTORY[2]
    while True:
        # prompts user for type of property to buy or to return to previous menu
        search_keyword = search_key()
        if search_keyword == 0:
            break
        path_list = display_properties_by_type_returns_list_by_type(search_directory_name, search_keyword)
        # if there is no directory for chosen type of property exits
        if path_list is False:
            break

        if bool(path_list):
            # if there are properties listed for sale prompts user to choose one of the contract id presented
            # or to return to previous menu
            option = choose_id_return_contract_and_path(path_list)
            if option is not False:
                # creating sale contract
                contract, path = option
                if directory_name == NAME_OF_DIRECTORY[3]:
                    print("New owner details")
                    new_owner = Client.create()
                    real_estate = contract.get_real_estate()

                    previous_owner = real_estate.get_owner()
                    # changing owner
                    real_estate.change_owner(new_owner)
                    new_contract = ContractWithBuyer(real_estate, previous_owner,
                                                     contract.get_price(),
                                                     contract.get_fee())

                else:
                    print("Tenant details")
                    tenant = Client.create()
                    new_contract = ContractWithTenant(contract.get_real_estate(), tenant, contract.get_time_span(),
                                                      contract.get_monthly_expenses(), contract.get_price(),
                                                      contract.get_fee())
                print(new_contract)
                print("Sign contract?")
                if return_bool():
                    save_progress(directory_name, new_contract)
                    archive_file(path)
                    return True
        else:
            print("There are no properties of chosen type on sale/rent\n"
                  "Chose other type of property or return to Main Menu")

def review_owners_by_m_011() -> None:
    """Listing filtered owners by certain conditions"""
    print("\nOwners filtered by first letter M, phone number starting with 011")
    i = 0
    # searching through all directories in database for owners except archive
    for dir_name in NAME_OF_DIRECTORY.values():
        try:
            file_name_list = os.listdir(os.path.join(get_database_path(), dir_name))
        except OSError:
            # if there is no directory of given name continues to another
            continue
        if bool(file_name_list) is False:
            continue
        else:
            # if there are contracts in directory it filters it by conditions
            for file_name in file_name_list:
                # returns contract object from file
                contract = from_file_return_object(os.path.join(get_database_path(), dir_name, file_name))
                if contract.get_real_estate().get_owner().get_name()[0].lower() == "m" and \
                        contract.get_real_estate().get_owner().get_phone_number()[:3] == "011":
                    print(contract.get_real_estate().get_owner())
                    i += 1
    print(f"\nSearch result: {i}")


def review_properties_to_rent_sorted_by_price() -> None:
    """List all properties listed for rent sorted by price"""
    print(f"\nProperties to rent sorted from lowest price\n")
    i = 0
    try:
        # tries to access directory with contracts pending to rent
        file_name_list = os.listdir(os.path.join(get_database_path(), NAME_OF_DIRECTORY[2]))
    except OSError:
        print("No properties listed for renting\n")
        return
    if bool(file_name_list) is False:
        print("No properties listed for renting\n")
        return
    list_of_contracts = []
    # creates list of contracts
    for file_name in file_name_list:
        list_of_contracts.append(from_file_return_object(os.path.join(get_database_path(), NAME_OF_DIRECTORY[2],
                                                                      file_name)))
    # sorts list of contracts by price starting from the lowest price
    list_of_contracts = sort_contract_list_by_price(list_of_contracts)

    for i in range(len(list_of_contracts)):
        print(f"Property and owner's information\n\n{list_of_contracts[i].get_real_estate()}\n"
              f"\nPrice >>> {list_of_contracts[i].get_price()} $\n")
        i += 1
    print(f"\nSearch result: {i}")


def review_sales_contract(year: str = "2023") -> None:
    """List current owners and previous owners and selling price of property in given year"""
    # I've filtered for 2023 instead of 2013 because I've used date.today() for creating signing date,
    # but it can be changed for any year
    print(f"\nNames of current owners and previous owners and selling price of a property in {year}\n")
    i = 0
    try:
        # tries to access directory for sold properties
        file_name_list = os.listdir(os.path.join(get_database_path(), NAME_OF_DIRECTORY[3]))
    except OSError:
        print("There are no sold properties yet\n")
        return
    if bool(file_name_list) is False:
        print("There are no sold properties yet\n")
        return
    for file_name in file_name_list:
        contract = from_file_return_object(os.path.join(get_database_path(), NAME_OF_DIRECTORY[3], file_name))
        # if meets conditions
        if contract.get_date()[:4] == year:
            print(
                f"Property type: {contract.get_real_estate().__class__.__name__}\n"
                f"Current owner : {contract.get_real_estate().get_owner().get_name()} "
                f"{contract.get_real_estate().get_owner().get_surname()}\n"
                f"Previous owner : {contract.get_previous_owner().get_name()} "
                f"{contract.get_previous_owner().get_surname()}\n"
                f"Sold for: {contract.get_price()} $\n")
        i += 1
    print(f"\nSearch result: {i}")


def review_filtered_apartments() -> None:
    """Lists owners and price for the apartment that satisfy given conditions"""
    print(f"\nDisplays apartment prices and owners who meet the required conditions\n"
          f"Conditions: terrace, parking space, air conditioning, area greater than 50 m2,"
          f" floor higher than second, Nis, Srbija\n")
    i = 0
    try:
        file_name_list = os.listdir(os.path.join(get_database_path(), NAME_OF_DIRECTORY[1]))
    except OSError:
        print("There are no properties on sale yet\n")
        return
    if bool(file_name_list) is False:
        print("There are no properties on sale yet\n")
        return
    for file_name in file_name_list:
        contract = from_file_return_object(os.path.join(get_database_path(), NAME_OF_DIRECTORY[1], file_name))
        # if contract is for an apartment
        if contract.get_real_estate().__class__.__name__ == TYPE_OF_PROPERTY[2] and \
                check_conditions(contract.get_real_estate()):
            print(f"Apartment owner: {contract.get_real_estate().get_owner().get_name()} "
                  f"{contract.get_real_estate().get_owner().get_surname()}\n"
                  f"Apartment selling for >> {contract.get_price()} $")
            i += 1
    print(f"\nSearch result: {i}")
