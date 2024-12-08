from logical_word_methods import *
from validate_guess import *
from load_config_file import load_config


def game_flow():
    config_dict = load_config()
    validate_word_endpoint = config_dict['validate_word_endpoint']
    word_generator = config_dict['word_generator']
    random_word = generate_random_word(file_path=f"{word_generator}/english.txt").upper()
    guesses = 0
    list_result = []
    while guesses < 6 and list_result != ['green', 'green', 'green', 'green', 'green']:
        guess = input('Enter 5 letter word:\n').upper()
        length_validation = validate_word_length(word_input=guess)
        if length_validation == 422:
            print('Invalid word length, try again')
            continue
        meaning_validation = validate_word_meaning(word_input=guess, validate_word_endpoint=validate_word_endpoint)
        if meaning_validation == 404:
            print('Word does not exist in database, try again')
            continue
        if meaning_validation == 500 or length_validation == 500:
            print('Internal server error, please come back later')
            break
        guesses += 1
        list_result = split_and_check_word(word_input=guess, word=random_word)
        print(list_result)


def main():
    game_flow()


if __name__ == "__main__":
    main()
