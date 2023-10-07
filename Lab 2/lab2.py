# Greeting
print('**** Welcome to the LAB grade calculator! ****\n')
name = input('Who are we calculating grades for? ==> ')

# Input grades (with conditionals)
labs_grade = int(input('\nEnter the LABS grade ==> '))
if labs_grade > 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    labs_grade = 100
elif labs_grade < 0:
    print('The lab value should have been 0 or greater. It has been changed to 0.')
    labs_grade = 0

exams_grade = int(input('\nEnter the EXAMS grade ==> '))
if exams_grade > 100:
    print('The exam value should have been 100 or less. It has been changed to 100.')
    exams_grade = 100
elif exams_grade < 0:
    print('The exam value should have been 0 or greater. It has been changed to 0.')
    exams_grade = 0

attendance_grade = int(input('\nEnter the ATTENDANCE grade ==> '))
if attendance_grade > 100:
    print('The attendance value should have been 100 or less. It has been changed to 100.')
    attendance_grade = 100
elif attendance_grade < 0:
    print('The attendance value should have been 0 or greater. It has been changed to 0.')
    attendance_grade = 0

# Weights
labs_weight = 0.7
exams_weight = 0.2
attendance_weight = 0.1

# Calculate weighted and letter grade
weighted_grade = (labs_grade * labs_weight) + (exams_grade * exams_weight) + (attendance_grade * attendance_weight)
letter_grade = ''

if weighted_grade >= 90:
    letter_grade = 'A'
elif weighted_grade >= 80:
    letter_grade = 'B'
elif weighted_grade >= 70:
    letter_grade = 'C'
elif weighted_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Output results
print(f'\nThe weighted grade for {name} is {weighted_grade:.1f}')
print(f'{name} has a letter grade of {letter_grade}')
print('\n**** Thanks for using the LAB grade calculator ****')