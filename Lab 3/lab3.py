print('Welcome to Flarsheim Guesser!\n')

# Creates list of numbers between 1 and 100 (inclusive)
numList = []
for i in range(1, 101):
    numList.append(i)

# Creates empty list to store valid numbers for each remainder
list3 = []
list5 = []
list7 = []

# Runs code until playAgain == N
while True:
    print('Please think of a number between 1 and 100 (inclusive).\n')

    # Remainder 3
    remain3 = int(input('What is the remainder when your number is divided by 3? '))
    while not(-1 < remain3 < 3):
        if remain3 < 0:
            print('The value entered must be 0 or greater')
        else:
            print('The value entered must be less than 3')
        remain3 = int(input('\nWhat is the remainder when your number is divided by 3? '))

    for i in numList:
        if i % 3 == remain3:
            list3.append(i)

    # Remainder 5
    remain5 = int(input('What is the remainder when your number is divided by 5? '))
    while not(-1 < remain5 < 5):
        if remain5 < 0:
            print('The value entered must be 0 or greater')
        else:
            print('The value entered must be less than 5')
        remain5 = int(input('\nWhat is the remainder when your number is divided by 5? '))

    for i in list3:
        if i % 5 == remain5:
            list5.append(i)

    # Remainder 7
    remain7 = int(input('What is the remainder when your number is divided by 7? '))
    while not (-1 < remain7 < 7):
        if remain7 < 0:
            print('The value entered must be 0 or greater')
        else:
            print('The value entered must be less than 7')
        remain5 = int(input('\nWhat is the remainder when your number is divided by 7? '))

    for i in list5:
        if i % 7 == remain7:
            list7.append(i)

    # Print final remaining value
    print(f'Your number was {list7[0]} \nHow amazing is that?\n')


    # Ask the user if they want to play again
    playAgain = input('Do you want to play again? Y to continue, N to quit ==> ').upper()
    while (playAgain != 'Y') and (playAgain != 'N'):
        playAgain = input('Do you want to play again? Y to continue, N to quit ==> ').upper()

    if playAgain == 'N':
        break
    else:
        print()
        list3.clear()
        list5.clear()
        list7.clear()