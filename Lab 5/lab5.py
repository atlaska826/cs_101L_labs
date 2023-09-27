# import statements

""" FUNCTIONS """


def get_school(library_card):
    if library_card[5] == '1':
        return 'School of Computing and Engineering SCE'
    elif library_card[5] == '2':
        return 'School of Law'
    elif library_card[5] == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'


def get_grade(library_card):
    if library_card[6] == '1':
        return 'Freshman'
    elif library_card[6] == '2':
        return 'Sophomore'
    elif library_card[6] == '3':
        return 'Junior'
    elif library_card[6] == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'


def character_value(string_char):
    return ord(string_char[0]) - 65


def get_check_digit(library_card):
    index = 0
    check_digit = 0
    for i in library_card[:9]:
        char_value = character_value(i)
        index += 1
        check_digit += (index * char_value)
    return check_digit % 10


def verify_check_digit(library_card):
    if len(library_card) != 10:  # Checks the length
        return False, "The length of the number given must be 10"

    for i in library_card[:5]:
        if not (i.isalpha()):
            bad_index = library_card.index(i)
            return False, f"The first 5 characters must be A-Z, the invalid character is at {bad_index} is {i}"

    for i in library_card[7:]:
        if not (i.isdigit()):
            bad_index = library_card.index(i)
            return False, "The last 3 characters must be 0-9, the invalid character is at " + bad_index + " is " + i

    if library_card[5] != '1' and library_card[5] != '2' and library_card[5] != '3':
        return False, "The sixth character must be 1 2 or 3"

    if library_card[6] != '1' and library_card[6] != '2' and library_card[6] != '3' and library_card[6] != '4':
        return False, "The seventh character must be 1 2 3 or 4"

    if get_check_digit(library_card) != int(library_card[9]):
        digit = get_check_digit(library_card)
        return False, "Check Digit " + library_card[9] + " does not match calculated value " + str(digit) + "."

    return True, ""


""" MAIN PROGRAM """

if __name__ == "__main__":
    print(f'{"Linda Hall":^60}')
    print(f'{"Library Card Check":^60}')
    print(f'{"":=^60}')

    while True:
        user_library_card = input("\nEnter Library Card. Hit Enter to Exit ==> ").upper()
        if user_library_card == "":
            break

        value, string = verify_check_digit(user_library_card)

        if not value:
            print('Library card is invalid.')
            print(string)
        else:
            print('Library card is valid.')
            print('The card belongs to a student in the', get_school(user_library_card))
            print('The card belongs to a', get_grade(user_library_card))