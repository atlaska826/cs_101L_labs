"""
TODO:
    - Add docstrings
    - Exception handling
    - Write main code

Errors needed:
    - FileNotFound
    - IOError
    - ValueError
    - etc

"""

"""INITIALIZATION"""


def get_min_mpg() -> int:
    while True:
        try:
            min_mpg = int(input('Enter the minimum mpg ==> '))
            if 0 < min_mpg <= 100:
                print()
                return min_mpg
            else:
                if min_mpg <= 0:
                    print('Fuel economy must be greater than 0.\n')
                else:
                    print('Fuel economy must be less than or equal to 100.\n')
        except ValueError:
            print('You must enter a number for the fuel economy.\n')


def get_input_file() -> str:
    while True:
        input_filename = input('Enter the name of the input vehicle file ==> ')
        try:
            with open(input_filename, 'r') as file:
                print()
                return input_filename
        except FileNotFoundError:
            print(f'Could not open file {input_filename}.\n')


def get_output_file() -> str:
    while True:
        output_filename = input('Enter the name of the file to output to ==> ')
        try:
            with open(output_filename, 'w+') as out_file:
                return output_filename
        except IOError:
            print(f'There is an IO Error {output_filename}')


"""MAIN PROGRAM"""
min_mpg = get_min_mpg()

with open(get_input_file(), 'r') as input_file:
    out_file = open(get_output_file(), 'w')
    print()

    for line in input_file:
        lines = input_file.readlines()
        for item in lines:
            item_list = item.split('\t')
            try:
                if float(item_list[7]) >= min_mpg:
                    out_file.write(f'{item_list[0] + " " + item_list[1]:<40}{item_list[2]:<40}{float(item_list[7]):>40.3f}\n')
            except (ValueError, TypeError):
                print(f'Could not convert value {item_list[7]} for vehicle {item_list[0]} {item_list[1]} {item_list[2]}')

    out_file.close()