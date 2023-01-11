from Projekat.functions.main_functions import put_property_on_sale, put_property_on_rent, buy_property, rent_property, \
    review_owners_by_m_011, review_properties_to_rent_sorted_by_price, review_sales_contract, review_filtered_apartments
from Projekat.functions.options_data import MAIN_MENU, NAME_OF_DIRECTORY
from Projekat.functions.utilities import choose_option_from_menu


def main():
    while True:
        option = choose_option_from_menu(MAIN_MENU)
        match option:
            case 0:
                print("Program closed")
                break
            case 1:
                if put_property_on_sale(NAME_OF_DIRECTORY[option]):
                    print("You have successfully listed your property for sale")
            case 2:
                if put_property_on_rent(NAME_OF_DIRECTORY[option]):
                    print("You have successfully listed your property for rent")
            case 3:
                if buy_property(NAME_OF_DIRECTORY[option]):
                    print("You have successfully bought a property.")
            case 4:
                if rent_property(NAME_OF_DIRECTORY[option]):
                    print("You have successfully rented property")
            case 5:
                review_owners_by_m_011()
            case 6:
                review_properties_to_rent_sorted_by_price()
            case 7:
                review_sales_contract()
            case 8:
                review_filtered_apartments()


if __name__ == '__main__':
    main()
