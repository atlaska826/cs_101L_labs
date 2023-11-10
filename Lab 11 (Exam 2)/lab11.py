import pandas as pd

""" VARIABLES """
menu = {
    1: 'Create class-specific CSV',
    2: 'Print all classes',
    3: 'Calculate the total scores',
    4: 'Exit'
}

df = None

""" FUNCTIONS """


def print_menu():
    """Prints the menu of choices the user can choose from"""
    print('Welcome to the Student Data Analysis App!')
    print('Please choose an option to proceed:')
    for key, value in menu.items():
        print(f'{key}. {value}')
    print()


def get_menu_choice():
    """Asks the user which choice they want, and then returns it once a valid choice is entered"""
    print_menu()
    while True:
        try:
            choice = int(input('Enter your choice (1-4): '))
            while choice not in menu:
                print('That is not a valid choice! Please try again.\n')
                choice = int(input('Enter your choice (1-4): '))
            return choice
        except ValueError:
            print('That is not a valid choice! Please try again.\n')


def get_input_file(name):
    """Loads the CSV file into a DataFrame"""
    data_frame = pd.read_csv(name)
    return data_frame


""" MAIN PROGRAM """
try:
    while True:
        menu_choice = get_menu_choice()

        if menu_choice == 4:
            break

        if menu_choice == 1:
            df = get_input_file('students_scores.csv')
            print('Data loaded successfully.')

            class_name = input('Enter the class name to create its CSV (e.g., 10-A): ')
            filtered_df = df.loc[df['Class'] == class_name]

            while filtered_df.empty:
                print('That class could not be found! Please try again.\n')
                class_name = input('Enter the class name to create its CSV (e.g., 10-A): ')
                filtered_df = df.loc[df['Class'] == class_name]

            with open(f'C:/Users/niman/Desktop/CS 101/CS101L_Labs/Lab 11 (Exam 2)/class_{class_name}.csv', 'w',
                      newline='\n') as file:
                file.write(filtered_df.to_csv(index=False))
            print(f'CSV file created for class {class_name}.')

        elif menu_choice == 2:
            try:
                class_list = df['Class'].tolist()
                class_set = set(class_list)
                print('\nSet of unique classes:')
                print(class_set)
            except TypeError:
                print('There is no data loaded to perform this function on!')

        elif menu_choice == 3:
            try:
                score_columns = ['Math', 'Science', 'English']
                df['Total'] = df[score_columns].sum(axis=1)

                top_name = df[df.Total == df.Total.max()].iloc[0]['Name']
                print(f'Student with the highest total score: {top_name}\n')

                with open(f'C:/Users/niman/Desktop/CS 101/CS101L_Labs/Lab 11 (Exam 2)/students_totals.csv', 'w',
                          newline='\n') as file:
                    file.write(df.to_csv(index=False))
                print(f'DataFrame with Total score saved to \'students_totals.csv\'.')
            except TypeError:
                print('There is no data loaded to perform this function on!')
        print()
except FileNotFoundError:
    print('File could not be found.')
finally:
    print('Exiting the application. Goodbye!')
