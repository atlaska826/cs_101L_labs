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
    # TODO: Handle exceptions
    min_mpg = int(input('Enter the minimum mpg ==> '))
    if 0 < min_mpg <= 100:
        return min_mpg
    else:
        print('FIXME: Wrong number handler')


def get_input_file() -> str:
    pass


def get_output_file() -> str:
    pass


"""MAIN PROGRAM"""
# for vehicle in input file >= min_mpg then output to file

input_file = 'vehicles2.txt'
output_file = 'output.txt'
min_mpg = 50

with open(input_file, 'r') as in_file:
    # FIXME: Add conditional for input file read
    out_file = open(output_file, 'w+')

    for line in in_file:
        lines = in_file.readlines()
        for item in lines:
            item_list = item.split('\t')
            print(item_list)

        try:
            if float(item_list[7]) >= min_mpg:
                out_file.write('Hi')
        except (ValueError, TypeError):  # FIXME: Add exception handler
            print('ERROR THROWN!')

    # FIXME: Output stuff here
    # Year, make, model left justified 40 spaces AND mpg right justified 20 spaces
    out_file.close()
