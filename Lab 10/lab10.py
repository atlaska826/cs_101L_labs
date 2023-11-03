import string

""" FUNCTIONS """

def get_file():
    """Gets a valid file from user input"""
    while True:
        filename = input('Enter the name of the file to open ==> ')
        try:
            with open(filename, 'r') as test:
                return filename
        except FileNotFoundError:
            print(f'Could not open file {filename}. Please try again.\n')


def cleanup_text(text):
    """Removes all punctuation, whitespace, and any words that are 3 characters or fewer from the file text list"""
    cleanup_lst = []
    for line in text:
        line_lst = [word.strip(string.punctuation).lower() for word in line.split()]
        for word in line_lst:
            if len(word) > 3:
                cleanup_lst.append(word)
    return cleanup_lst


def get_top_ten(words):
    """Returns a sorted dictionary with the word as the key and the value as the frequency of the word"""
    count_dict = {}
    for word in words:
        count_dict[word] = words.count(word)
    return dict({w: c for w, c in sorted(count_dict.items(), key=lambda elem: elem[1], reverse=True)})


def get_used_once(words):
    """Returns the number of words that are only used once"""
    used_once = 0
    for word in words:
        if words.count(word) == 1:
            used_once += 1
    return used_once


""" MAIN PROGRAM """
with open(get_file(), 'r') as file:
    word_list = cleanup_text(file.readlines())

print(f'\n\n{"Most Frequently Used Words":^36}')
print(f'{"#":<12}{"Word":>4}{"Freq.":>20}')
print('=' * 36)

top_words = get_top_ten(word_list)

num = 1
for word, count in top_words.items():
    if num <= 10:
        print(f'{num:<3}{word:>13}{count:>20}')
    num += 1

print(f'\nThere are {get_used_once(word_list)} words that only occur once.')
print(f'There are {len(set(word_list))} unique words in the document.')
