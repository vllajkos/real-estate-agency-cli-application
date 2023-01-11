import os
import pickle
from Projekat.functions.options_data import TYPE_OF_PROPERTY


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


def return_bool() -> bool:
    """Prompts user for input, checks if input satisfy conditions"""
    while True:
        user_input = input("Enter yes or no: ").lower()
        if user_input == "yes":
            option = True
            return option
        elif user_input == "no":
            option = False
            return option
        else:
            print("Please enter yes or no as an option choice")


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
        if 0 < option <= len(menu):
            return option
        else:
            print("Choose valid option number! Try again")
            continue


def choose_option_from_menu(menu: dict) -> int:
    """Prompts user for input, checks if input satisfy conditions"""
    print("MENU")
    show_options(menu)
    while True:
        try:
            option = int(input("Choose option number: "))
        except ValueError:
            print("Enter the number for given options")
            continue
        if option in menu.keys():
            print(f"Chosen option >> {menu[option]}")
            return option
        print("Choose valid option number! Try again")
        continue


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
    dir_path = os.path.join(os.getcwd(), "database", dir_name)
    try:
        os.mkdir(dir_path)
    except OSError:
        pass
    return dir_path


"""Koristio sam pickle modul za serializaciju i deserializaciju objekta.
Objekat prebacujem u bajtove i njih upisujem u fajl, a kasnije citanjem
iz fajla vracam objekat, imao sam problema sa json modulom pa sam probao
na ovaj nacin i radi."""


def object_to_file(contract, path: str) -> None:
    """Serialize object as bytes and write it to .txt file"""
    content = pickle.dumps(contract)
    name = os.path.join(path, create_contract_name(contract) + ".txt")
    with open(name, "wb") as f:
        f.write(content)


def from_file_return_object(path: str):
    """Read file and deserialize object, returns object"""
    with open(path, "rb") as f:
        return pickle.loads(f.read())


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


def create_contract_name(contract) -> str:
    """Creates unique contract name"""
    contract_name = ""
    contract_name += contract.get_real_estate().__class__.__name__ + " "
    contract_name += contract.get_id()
    return contract_name


def archive_file(path) -> None:
    """Moves file from original directory to archive"""
    contract = from_file_return_object(path)
    os.remove(path)
    create_database()
    new_path = create_directory("archive")
    object_to_file(contract, new_path)


def choose_id_return_contract_and_path(path_list) -> bool | tuple:
    """Prompts user for input and checks if input satisfy conditions  """
    while True:
        option = input("Enter contract id for property you want to purchase/rent or 0 to return to previous menu: ")
        if option == "0":
            print("Chosen option >> return to previous menu")
            return False
        for path in path_list:
            contract = from_file_return_object(path)
            if contract.get_id() == option:
                #  returns contract and path to it
                return contract, path
        print("You have entered wrong id, try again")


def search_key() -> int | str:
    """Returns chosen option"""
    option = choose_option_from_menu(TYPE_OF_PROPERTY)
    if option == 0:
        # returns 0 to go back to previous menu
        return option
    # from dict returns chosen property type to search file names for
    return TYPE_OF_PROPERTY[option]


def display_properties_by_type_returns_list_by_type(directory_name: str, search_keyword: str) -> bool | list[str]:
    """Lists properties filtered by type and returns list of paths of filtered contracts"""
    try:
        path = os.path.join(os.getcwd(), "database", directory_name)
        file_list = os.listdir(path)
    except OSError:
        print("There are no properties listed on sale")
        return False
    path_list = []
    i = 0
    for file in file_list:
        contract = from_file_return_object(os.path.join(path, file))
        # checks if type of property matches chosen type
        if contract.get_real_estate().__class__.__name__ == search_keyword:
            path_list.append(os.path.join(path, file))
            print(contract)
            i += 1
    print(f"\nSearch result: {i}")
    return path_list


def save_progress(directory_name: str, contract) -> None:
    """Creates database if database do not exist, creates directory for type of contract if directory do not exist,
    writes object to file"""
    create_database()
    path = create_directory(directory_name)
    object_to_file(contract, path)


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
                    continue
            else:
                srt = True
    return contract_list


def check_conditions(real_estate) -> bool:
    """Checks if property satisfy given conditions"""
    if real_estate.get_terrace() is True and \
            real_estate.get_air_conditioning() is True and \
            real_estate.get_parking_space() and \
            real_estate.get_sqm() > 50 and \
            real_estate.get_floor() > 2 and \
            real_estate.get_address().get_city().lower() == "nis" and \
            real_estate.get_address().get_country().lower() == "srbija":
        return True
    return False
