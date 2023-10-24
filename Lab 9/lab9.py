import csv

""" VARIABLES """
months = {
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
}

""" FUNCTIONS """


def read_in_file(filename):
    """Reads file with specific name and returns a list of its contents"""
    input_file_list = []
    with open(filename, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)

        for line in reader:
            input_file_list.append(line)
    return input_file_list


def month_from_number(num):
    """Returns name of the month when given a number"""
    if num in months:
        return months[num]
    raise ValueError("Not a valid month!")


def create_reported_date_dict(data):
    """Returns a dictionary of the number of crime occurrences on each specific date"""
    reported_date = {}
    for line in data[1:]:
        if reported_date.get(line[1], 0) == 0:
            reported_date[line[1]] = 1
        else:
            reported_date[line[1]] += 1
    return reported_date


def create_reported_month_dict(data):
    """Returns a dictionary of the number of crime occurrences during each month"""
    reported_month = {}
    for line in data[1:]:
        date_list = line[1].split("/")
        month = int(date_list[0])

        if reported_month.get(month, 0) == 0:
            reported_month[month] = 1
        else:
            reported_month[month] += 1
    return reported_month


def create_offense_dict(data):
    """Returns a dictionary of the number of occurrences of each specific crime"""
    offense = {}
    for line in data[1:]:
        if offense.get(line[7], 0) == 0:
            offense[line[7]] = 1
        else:
            offense[line[7]] += 1
    return offense


def create_offense_by_zip(data):
    """Returns a dictionary of the number of occurrences in each zipcode of each individual crime."""
    offense_zip = {}
    for line in data[1:]:
        offense = line[7]
        zip_code = line[13]

        if offense_zip.get(offense, 0) == 0:
            offense_zip[offense] = dict([(zip_code, 1)])
        else:
            if offense_zip[offense].get(zip_code, 0) == 0:
                offense_zip[offense][zip_code] = 1
            else:
                offense_zip[offense][zip_code] += 1
    return offense_zip


""" MAIN PROGRAM """
if __name__ == "__main__":
    while True:
        user_filename = input('Enter the name of the crime data file ==> ')
        try:
            data_list = read_in_file(user_filename)
            break
        except FileNotFoundError:
            print(f'Could not find the file specified. {user_filename} not found.')

    # Initializes variables to store the return value of each dictionary creation function
    month_dict = create_reported_month_dict(data_list)
    offense_dict = create_offense_dict(data_list)
    offense_zip_dict = create_offense_by_zip(data_list)

    # Gets highest crime month and number of crimes committed that month
    high_month = 0
    num_per_month = 0
    for month, count in month_dict.items():
        if count > num_per_month:
            high_month = month
            num_per_month = count
    print(f'\nThe month with the highest # of crimes is {months[high_month]} with {num_per_month} offenses')

    # Gets highest occurring event and the number of times the crime was committed
    high_offense = ''
    num_per_offense = 0
    for offense, count in offense_dict.items():
        if count > num_per_offense:
            high_offense = offense
            num_per_offense = count
    print(f'The offense with the highest # of crimes is {high_offense} with {num_per_offense} offenses\n')

    # Gets zip codes for a specific offense
    crime = input('Enter an offense ==> ')
    while crime not in offense_zip_dict:
        print('Not a valid offense. Please try again.')
        crime = input('Enter an offense ==> ')

    print(f'\n{crime} offenses by Zip Code')
    print(f'Zip Code{"# Offenses":>22}')
    print('=' * 30)
    for zip_code, count in offense_zip_dict[crime].items():
        print(f'{zip_code:<8}{count:>22}')