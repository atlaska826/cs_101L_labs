import math

# TODO: Add in docstrings and comments

""" VARIABLES """
menu = {
    '1': 'Add Test',
    '2': 'Remove Test',
    '3': 'Clear Tests',
    '4': 'Add Assignment',
    '5': 'Remove Assignment',
    '6': 'Clear Assignments',
    'D': 'Display Scores',
    'Q': 'Quit'
}
program_choices = set(menu.keys())

test_scores = []
assignment_scores = []

test_weight = 0.6
assignment_weight = 0.4

""" FUNCTIONS """


def program_choice():
    print(f'{"":<12}Grade Menu')
    for char, desc in menu.items():
        print(f'{char} - {desc}')

    choice = input('\n==> ').upper()
    while choice not in program_choices:
        print('Invalid program choice!')
        choice = input('==> ').upper()

    return choice


def add_test():
    while True:
        try:
            new_score = float(input('\nEnter the new Test score 0 - 100 ==> '))
            if new_score < 0:
                print('Score must be greater than 0!\n')
                continue
            else:
                test_scores.append(new_score)
                break
        except (ValueError, TypeError):
            print('Invalid input type!\n')


def remove_test():
    while True:
        try:
            del_test = float(input('\nEnter the Test to remove 0-100 ==> '))
            if del_test not in test_scores:
                print('Could not find that score to remove!\n')
            else:
                test_scores.remove(del_test)
            break
        except (ValueError, TypeError):
            print('Invalid input type!\n')


def clear_tests():
    test_scores.clear()


def add_assignment():
    while True:
        try:
            new_score = float(input('\nEnter the new Assignment score 0 - 100 ==> '))
            if new_score < 0:
                print('Score must be greater than 0!\n')
                continue
            else:
                assignment_scores.append(new_score)
                break
        except (ValueError, TypeError):
            print('Invalid input type!\n')


def remove_assignment():
    while True:
        try:
            del_assignment = float(input('\nEnter the Assignment to remove 0-100 ==> '))
            if del_assignment not in assignment_scores:
                print('Could not find that score to remove!\n')
            else:
                assignment_scores.remove(del_assignment)
            break
        except (ValueError, TypeError):
            print('Invalid input type!\n')


def clear_assignments():
    assignment_scores.clear()


def display_scores():
    print(f'\n{"Type":<19}{"#":<8}{"min":<10}{"max":<10}{"avg":<10}{"std"}')
    print('=' * 60)

    mean_test_score = 0
    mean_assignment_score = 0

    # Handles test score calculations
    if len(test_scores) == 0 :
        print(f'{"Tests":<19}{0:<8}{"n/a":<10}{"n/a":<10}{"n/a":<10}n/a')
    else:
        mean_test_score = sum(test_scores) / len(test_scores)
        std_test_score = 0

        for score in test_scores:
            std_test_score += math.pow(score - mean_test_score, 2)
        std_test_score /= len(test_scores)
        std_test_score = math.sqrt(std_test_score)

        print(f'{"Tests":<19}{len(test_scores):<7}{min(test_scores):<10.1f}{max(test_scores):<9.1f}{mean_test_score:<11.2f}{std_test_score:.2f}')

    # Handles assignment score calculations
    if len(assignment_scores) == 0:
        print(f'{"Programs":<19}{0:<8}{"n/a":<10}{"n/a":<10}{"n/a":<10}n/a')
    else:
        mean_assignment_score = sum(assignment_scores) / len(assignment_scores)
        std_assignment_score = 0

        for score in assignment_scores:
            std_assignment_score += math.pow(score - mean_assignment_score, 2)
        std_assignment_score /= len(assignment_scores)
        std_assignment_score = math.sqrt(std_assignment_score)

        print(f'{"Programs":<19}{len(assignment_scores):<7}{min(assignment_scores):<10.1f}{max(assignment_scores):<9.1f}{mean_assignment_score:<11.2f}{std_assignment_score:.2f}')

    weighted_scores = (mean_test_score * test_weight) + (mean_assignment_score * assignment_weight)
    print(f'\nThe weighted score is:\t{weighted_scores:.2f}')


""" MAIN PROGRAM """
while True:
    program = program_choice()

    if program == '1':
        add_test()
    elif program == '2':
        remove_test()
    elif program == '3':
        clear_tests()
    elif program == '4':
        add_assignment()
    elif program == '5':
        remove_assignment()
    elif program == '6':
        clear_assignments()
    elif program == 'D':
        display_scores()
    else:
        break
    print()
