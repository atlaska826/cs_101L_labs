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
    pass


""" MAIN PROGRAM """

if __name__ == "__main__":
    print(f'{"Linda Hall":^60}')
    print(f'{"Library Card Check":^60}')
    print(f'{"":=^60}')

    # TODO Ask user to input library card number
