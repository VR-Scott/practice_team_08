import getpass
import re
from user_storage import *


def main_menu() -> None:
    """
    Displays the main menu of the application.
    :return: None
    """
    menu = '\n'.join([
        'Select an option by entering its number and pressing Enter.',
        '1. Create a user account',
        '2. Log in to existing account',
        '---'
    ])
    print(menu)
    valid_selections = [1, 2]
    input_is_valid = False
    selection = None
    while not input_is_valid:
        try:
            selection = int(input('Selection: '))
            if selection in valid_selections:
                input_is_valid = True
            else:
                print('The number you entered is not a valid selection.')
        except ValueError:
            print('The value you entered is not a number.')
    handle_main_menu_selection(selection)


def handle_main_menu_selection(selection: int) -> None:
    """
    Calls the function related to the selection the user made.
    :param selection: The user's selection.
    :return: None
    """
    if selection == 1:
        create_new_user_menu()
    elif selection == 2:
        user_login_menu()
    else:
        raise ValueError(f'Selection {selection} is invalid.')


def create_new_user_menu() -> None:
    """
    Displays the account creation menu, including asking the user for username and password.
    :return: None
    """
    menu = '\n'.join([
        '---',
        'Account creation',
        'Username must...',
        '\t- be at least 3 characters long',
        '\t- contain only letters, numbers, and underscores',
        'Password must...',
        '\t- be at least 8 characters long',
        '---'
    ])
    print(menu)
    user_added_successfully = False
    username = ''
    while not user_added_successfully:
        try:
            username = get_username_input()
            password = get_password_input()
            user_added_successfully = try_adding_user(username, password)
            if not user_added_successfully:
                print(f'Username "{username}" already exists.')
        except ValueError as error:
            print(str(error))


def try_adding_user(username: str, password: str) -> bool:
    """
    Attempts to add a user to the user database file.
    :param username: The username provided by the user.
    :param password: The password provided to the user, in clear text.
    :return: Whether the user was added successfully.
    """
    try:
        add_user(username, password)
        return True
    except ValueError:
        return False


def user_login_menu() -> None:
    menu = '\n'.join([
        '---',
        'User login',
        '---'
    ])
    print(menu)
    login_successful = False
    while not login_successful:
        username = get_username_input()
        password = get_password_input()
        login_successful = authenticate_username_and_password(username, password)
        if not login_successful:
            print('Incorrect username or password.')
    print('Login successful.')


def get_username_input() -> str:
    """
    Request username input from the user.
    :return: The username entered by the user.
    """
    minimum_length = 3
    username = input('Enter username: ')
    if len(username) < minimum_length:
        raise ValueError('Username must be at least 3 characters.')
    # match upper & lower case letters, numbers, and underscores
    pattern = re.compile('^([a-zA-Z0-9_]+)$')
    if not pattern.match(username):
        raise ValueError('Username must consist of only letters, numbers, and underscores.')
    return username


def get_password_input() -> str:
    """
    Request password input from the user.
    :return: The password entered by the user.
    """
    minimum_length = 8
    password = getpass.getpass('Enter password: ')
    if len(password) < minimum_length:
        raise ValueError('Password must be at least 8 characters.')
    return password


if __name__ == '__main__':
    main_menu()
