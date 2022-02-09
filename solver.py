import string

from sty import fg, ef
from wordle import word_len, words, max_attempt, get_sorted_words, sort_words


def input_word():
    while True:
        word = input(fg.li_magenta + 'Enter the word you used: ' + fg.rs)
        if len(word) == word_len and word.lower() in words:
            break
        print(fg.red + f'Error - invalid answer ' + fg.rs + f'{word}')
    return word.lower()


def input_response():
    print(
        '\nEnter the' + fg.blue + ' color ' + fg.rs + 'from the boxes from ' + ef.bold + 'Wordle' + fg.rs + ':\n\t'
        + ef.bold + 'G' + fg.rs + ' or ' + ef.bold + '1' + fg.rs + ' for ' + fg.green + 'Green' + fg.rs + '\n\t'
        + ef.bold + 'Y ' + fg.rs + 'or ' + ef.bold + '2' + fg.rs + ' for ' + fg.li_yellow + 'Yellow' + fg.rs + '\n\t'
        + ef.bold + '?' + fg.rs + ' or ' + ef.bold + '3' + fg.rs + ' for ' + fg.grey + 'Gray' + fg.rs + '\n')

    while True:
        response = input(fg.li_magenta + 'Response: ' + fg.rs)
        if len(response) == word_len and set(response) <= {'G', 'Y', '?'} or set(response) <= {'1', '2', '3'} or \
                set(response) <= {'g', 'y', '?'}:
            return response
        else:
            print(fg.red + f'Error - invalid answer ' + fg.rs + f'{response}')


def match_word_vector(word, word_vector):
    assert len(word) == len(word_vector)
    for letter, v_letter in zip(word, word_vector):
        if letter not in v_letter:
            return False
    return True


def match(word_vector, possible_words):
    return [word for word in possible_words if match_word_vector(word, word_vector)]


def solve():
    possible_words = words.copy()
    word_vector = [set(string.ascii_lowercase) for _ in range(word_len)]

    for attempt in range(1, max_attempt + 1):
        print(
            f'\nAttempt ' + ef.bold + f'{attempt}' + fg.rs + ' with ' + ef.bold + f'{len(possible_words)}' + fg.rs +
            ' possible words')
        print(get_sorted_words(sort_words(possible_words)[:15]))
        word = input_word()
        response = input_response()

        if response == '1111' or 'GGGGG':
            print(
                ef.bold + '\nCongrats \U0001F389\U0001F389\U0001F389! The word was ' + fg.blue + f'{word}' 
                + fg.rs + ef.bold + '!' + fg.rs)
            break

        for index, letter in enumerate(response):

            if letter.lower() == 'g' or letter == '1':
                word_vector[index] = {word[index]}

            elif letter.lower() == 'y' or letter == '2':
                try:
                    word_vector[index].remove(word[index])
                except KeyError:
                    pass

            elif letter == '?' or letter == '3':
                for word_vec in word_vector:
                    try:
                        word_vec.remove(word[index])
                    except KeyError:
                        pass

        possible_words = match(word_vector, possible_words)


solve()
