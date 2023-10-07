import string

"""VARIABLES"""
upper_letters = string.ascii_uppercase

"""FUNCTIONS"""
def encrypt(string_text, int_key):
    """Caesar-encrypts string using specified key."""
    new_string = ''
    for letter in string_text:
        new_key = int_key  # Creates a variable to hold the original value of int_key each iteration
        if letter in upper_letters:
            while ord(letter) + new_key > 90:  # Ensures no out of alphabet range letters are outputted
                new_key -= 26
            shifted_letter = chr(ord(letter) + new_key)
            new_string = new_string + shifted_letter
        else:
            new_string = new_string + ' '
    return new_string


def decrypt(string_text, int_key):
    """Decrypts Caesar-encrypted string with specified key."""
    return encrypt(string_text, int(26 - int_key))


def get_input():
    """Interacts with user."""
    menu_option_list = ['1', '2', 'Q']  # List containing valid answer choices

    menu_option = input('Enter your selection ==> ')
    while menu_option not in menu_option_list:  # Runs until user enters valid choice
        print('Invalid menu option! Please try again.\n')
        menu_option = input('Enter your selection ==> ')
    return menu_option


def print_menu():
    """Prints menu. No user interaction."""
    print('MAIN MENU:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')


def main():
    while True:  # Runs until user selects the Quit option from get_input()
        print_menu()
        user_choice = get_input()
        if user_choice == '1':
            text = input('\nEnter (brief) text to encrypt: ').upper()
            shift = int(input('Enter the number to shift letters by: '))
            print('Encrypted:', encrypt(text, shift), '\n')
        elif user_choice == '2':
            text = input('\nEnter (brief) text to decrypt: ').upper()
            shift = int(input('Enter the number to shift letters by: '))
            print('Decrypted:', decrypt(text, shift), '\n')
        else:
            break


"""RUN THE PROGRAM"""
main()
