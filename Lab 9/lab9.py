import csv

""" VARIABLES """
months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

""" FUNCTIONS """


def read_in_file(filename):
    input_file_list = []
    with open(filename, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)

        for line in reader:
            input_file_list.append(line)
    return input_file_list


def month_from_number(num):
    if num in months:
        return months[num]
    raise ValueError("Not a valid month!")


def create_reported_date_dict(data):
    reported_date = {}
    for line in data[1:]:
        if reported_date.get(line[1], 0) == 0:
            reported_date[line[1]] = 1
        else:
            reported_date[line[1]] += 1
    return reported_date


def create_reported_month_dict(data):
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
    offense = {}
    for line in data[1:]:
        if offense.get(line[7], 0) == 0:
            offense[line[7]] = 1
        else:
            offense[line[7]] += 1
    return offense


def create_offense_by_zip(data):
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

    print(f'\nThe month with the highest # of crimes is {high_month} with {num_per_month} offenses')
    print(f'The offense with the highest # of crimes is {high_offense} with {num_per_offense} offenses\n')

    date_dict = create_reported_date_dict(data_list)
    month_dict = create_reported_month_dict(data_list)
    offense_dict = create_offense_dict(data_list)
    offense_zip_dict = create_offense_by_zip(data_list)