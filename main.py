from functions.main_functions import list_property, buy_rent_property, \
    review_owners_by_m_011, review_properties_to_rent_sorted_by_price, review_sales_contract, \
    review_filtered_apartments
from functions.options_data import MAIN_MENU, NAME_OF_DIRECTORY
from functions.utilities import choose_option_from_menu


def main():
    while True:
        print("MAIN MENU")
        option = choose_option_from_menu(MAIN_MENU)
        match option:
            case 0:
                print("Program closed")
                return
            case 1:
                if list_property(NAME_OF_DIRECTORY[option]):
                    print("You have successfully listed your property on sale")
            case 2:
                if list_property(NAME_OF_DIRECTORY[option]):
                    print("You have successfully listed your property for rent")
            case 3:
                if buy_rent_property(NAME_OF_DIRECTORY[option]):
                    print("You have successfully bought a property.")
            case 4:
                if buy_rent_property(NAME_OF_DIRECTORY[option]):
                    print("You have successfully rented a property")
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
