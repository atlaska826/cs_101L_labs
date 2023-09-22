import random

def play_again():
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    play_again = input('Do you want to play again? ==> ').upper()
    while play_again != 'N' and play_again != 'NO' and play_again != 'Y' and play_again != 'YES':
        print('\nYou must enter Y/YES/N/NO to continue. Please try again.')
        play_again = input('Do you want to play again? ==> ').upper()
    if play_again == 'N' or play_again == 'NO':
        return False
    return True


def get_wager(bank):
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    wager_amount = int(input('How many chips do you want to wager? ==> '))
    while not(0 < wager_amount <= bank):
        if wager_amount <= 0:
            print('\nThe wager amount must be greater than 0. Please enter again.')
        elif wager_amount > bank:
            print(f'\nThe wager amount cannot be greater than what you have. {bank}')
        wager_amount = int(input('How many chips do you want to wager? ==> '))
    return wager_amount


def get_slot_results():
    ''' Returns the result of the slot pull '''
    reel_1 = random.randint(1, 10)
    reel_2 = random.randint(1, 10)
    reel_3 = random.randint(1, 10)
    return reel_1, reel_2, reel_3


def get_matches(reela, reelb, reelc):
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb == reelc:
        return 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):
        return 2
    return 0


def get_bank():
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    user_bank = int(input('How many chips do you want to start with? ==> '))
    while not(0 < user_bank < 101):
        if user_bank <= 0:
            print('\nToo low a value, you can only choose 1 - 100 chips.')
        elif user_bank >= 101:
            print('\nToo high a value, you can only choose 1 - 100 chips.')
        user_bank = int(input('How many chips do you want to start with? ==> '))
    return user_bank


def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    payout = 0
    if matches == 3:
        payout = (10 * wager) - wager
    elif matches == 2:
        payout = (3 * wager) - wager
    else:
        payout = -wager
    return payout


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        initial_bank = bank
        spins = 0
        max_chips = bank

        while bank > 0:  # Replace with condition for if they still have money.

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()
            spins += 1

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            if bank > max_chips:
                max_chips = bank

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

        print("You lost all", initial_bank, "in", spins, "spins")
        print("The most chips you had was", max_chips)
        playing = play_again()