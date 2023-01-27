import os
import pickle
from functions.options_data import TYPE_OF_PROPERTY

"""
FUNCTIONS FOR VALIDATION OF CONDITIONS
"""


def is_valid(key: int) -> str | float:
    """Validate different inputs by key"""
    while True:
        user_input = input("Enter number: ")
        # is JMBG valid
        if key == 1:
            if user_input.isnumeric() and len(user_input) == 13:
                return user_input
            else:
                print("Enter valid JMBG (13 digits)")
                continue
        # is id number valid
        if key == 2:
            if user_input.isnumeric() and len(user_input) == 9:
                return user_input
            else:
                print("Enter valid id number (9 digits)")
                continue
        # is agency fee valid
        if key == 3:
            try:
                user_input = float(user_input)
            except ValueError:
                print("Agency fee must be a number, try again")
                continue
            if user_input > 20:
                print("Agency fee can not be greater than 20 %, try again")
                continue
            return user_input
        # is phone number valid
        if key == 4:
            if user_input.isnumeric():
                return user_input
            else:
                print("Phone number should have only numbers, try again")


def check_room() -> int:
    """Prompts user for input, checks if input satisfy conditions"""
    while True:
        try:
            integer = int(input("Enter number of rooms: "))
            if integer < 1:
                print("Room number should be greater than 0, try again")
                continue
            return integer
        except ValueError:
            print("Wrong input value, try again")


def check_sqm() -> float:
    """Prompts user for input, checks if input satisfy conditions"""
    while True:
        try:
            sqm = float(input("Enter square meters: "))
            break
        except ValueError:
            print("Wrong input value, try again")
    return sqm


def check_float() -> float:
    """Prompts user for input, checks if input satisfy conditions"""
    while True:
        try:
            f = float(input("Enter number: "))
            if f < 0:
                continue
            return f
        except ValueError:
            print("Wrong input value, try again")


def check_integer() -> int:
    """Prompts user for input, checks if input satisfy conditions"""
    while True:
        try:
            integer = int(input("Enter number: "))
            if integer < 0:
                print("Wrong input value, try again")
                continue
            return integer
        except ValueError:
            print("Wrong input value, try again")


def is_yes() -> bool:
    """Prompts user for input, checks if input satisfy conditions"""
    while True:
        user_input = input("Y/N: ").lower()
        if user_input == "y":
            option = True
            return option
        elif user_input == "n":
            option = False
            return option
        else:
            print("Please enter Y for Yes or N for No")


def return_expiration_date(signing_date: str, time_span: int) -> str:
    """Creates expiration date"""
    date: list = signing_date.split("-")
    year = int(date[0])
    month = int(date[1]) + time_span
    day = date[2]
    while month > 12:
        month = month - 12
        year += 1
    return f"{year}-{month}-{day}"


def check_conditions(real_estate) -> bool:
    """Checks if property satisfy given conditions"""
    if not real_estate.get_terrace():
        return False
    if not real_estate.get_air_conditioning():
        return False
    if not real_estate.get_parking_space():
        return False
    if real_estate.get_sqm() <= 50:
        return False
    if real_estate.get_floor() <= 2:
        return False
    if real_estate.get_address().get_city().lower() != "nis":
        return False
    if real_estate.get_address().get_country().lower() != "srbija":
        return False
    return True


"""
FUNCTIONS FOR PRINTING OPTIONS AND RECEIVING AN OPTION
"""


def show_options(main_menu: dict) -> None:
    """Prints dictionary"""
    for key, value in main_menu.items():
        print(f"{key} - {value}")


def choose_option(menu: dict) -> int:
    """Prompts user for input, checks if input satisfy conditions"""
    while True:
        try:
            option = int(input("Choose option number: "))
        except ValueError:
            print("Enter the number for given options")
            continue
        if option in menu.keys():
            print(f"Chosen option >> {menu.get(option)}")
            return option
        print("Choose valid option number! Try again")


def choose_option_from_menu(menu: dict) -> int:
    """Prompts user for input, checks if input satisfy conditions, returns option"""
    show_options(menu)
    return choose_option(menu)


"""
FUNCTIONS FOR FILE-BASED DATA MANAGEMENT SYSTEM
"""


def create_database() -> None:
    """Create database"""
    try:
        os.mkdir(os.path.join(os.getcwd(), "database"))
    except OSError:
        pass


def get_database_path() -> str:
    """Returns database path"""
    return os.path.join(os.getcwd(), "database")


def create_directory(dir_name: str) -> str:
    """Creates directory inside database for type of contract"""
    dir_path = os.path.join(get_database_path(), dir_name)
    try:
        os.mkdir(dir_path)
    except OSError:
        pass
    return dir_path


def create_contract_name(contract) -> str:
    """Creates unique contract name"""
    contract_name = contract.get_real_estate().__class__.__name__.lower() + "-" + contract.get_id() + ".txt"
    return contract_name


def object_to_file(contract, path: str) -> None:
    """Serialize object as bytes and write it to .txt file"""
    content = pickle.dumps(contract)
    name = os.path.join(path, create_contract_name(contract))
    with open(name, "wb") as f:
        f.write(content)


def from_file_return_object(path: str):
    """Read file and deserialize object, returns object"""
    with open(path, "rb") as f:
        return pickle.loads(f.read())


def archive_contract(path) -> None:
    """Moves file from original directory to archive"""
    contract = from_file_return_object(path)
    os.remove(path)
    new_path = create_directory("archive")
    object_to_file(contract, new_path)


def save_contract(directory_name: str, contract) -> None:
    """Creates database if database do not exist, creates directory for type of contract if directory do not exist,
    writes object to file"""
    create_database()
    path = create_directory(directory_name)
    object_to_file(contract, path)


"""
FUNCTIONS FOR LISTING CONTRACTS FROM GIVEN DIRECTORIES AND CHOOSING DESIRED PROPERTY 
"""


def search_key() -> int | str:
    """Returns chosen option"""
    print("CHOOSE TYPE OF PROPERTY")
    option = choose_option_from_menu(TYPE_OF_PROPERTY)
    if option == 0:
        print("Chosen option >> Return to Main Menu")
        # returns 0 to go back to previous menu
        return option
    # from dict returns chosen property type to search file names for
    return TYPE_OF_PROPERTY.get(option)


def choose_property(directory_name: str, search_keyword: str) -> None | tuple:
    """Show's properties for chosen type of property, if client decides to sign contract with agency and owner,
    returns previous contract between agency and owner and path to its location"""
    try:
        path = os.path.join(get_database_path(), directory_name)
        filename_list = os.listdir(path)
    except OSError:
        raise Exception(f"There are no properties listed {directory_name.split('-', 1)[1].replace('-', ' ')}")
    contracts_dict = {}
    i = 0
    for filename in filename_list:
        # checks if file name contains chosen type of property
        if filename.split("-")[0] == search_keyword.lower().replace(" ", ""):
            contract_path = os.path.join(path, filename)
            contract = from_file_return_object(contract_path)
            contracts_dict.setdefault(filename.split("-")[1].split(".")[0], contract_path)
            print(contract)
            i += 1
    print(f"\nSearch result: {i}")
    if i == 0:
        print(f"No {search_keyword} listed {directory_name.split('-', 1)[1].replace('-', ' ')}\n"
              "Choose different type of property or return to Main Menu")
        return
    while True:
        option = input("Enter contract ID to begin the process of signing a contract or 0 to return to previous Menu: ")
        if option == "0":
            print("Chosen option >> Return to previous Menu")
            return
        if option in contracts_dict.keys():
            contract_path = contracts_dict.get(option)
            return from_file_return_object(contract_path), contract_path
        print("You have entered wrong id, try again")


"""
SORTING FUNCTION
"""


def sort_contract_list_by_price(contract_list) -> list:
    """Sorts contract list by price"""
    srt = False
    j = 0
    while not srt:
        for i in range(len(contract_list) - j):
            if i < len(contract_list) - 1:
                if contract_list[i].get_price() > contract_list[i + 1].get_price():
                    contract_list[i], contract_list[i + 1] = contract_list[i + 1], contract_list[i]
        else:
            j += 1
            for i in range(len(contract_list) - 1):
                if contract_list[i].get_price() > contract_list[i + 1].get_price():
                    break
            else:
                srt = True
    return contract_list
