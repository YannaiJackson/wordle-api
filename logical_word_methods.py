import random
import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_random_word(file_path):
    """
    :param file_path: file to generate word from.
    :return: random word from specified file
    """
    try:
        logging.info(f"Attempting to open the file: {file_path}")

        # Open the file and read its content
        with open(file_path, 'r') as file:
            text = file.read()
        logging.info(f"File successfully read: {file_path}")

        # Split the text into words
        words = text.split()
        logging.info(f"Extracted {len(words)} words from the file.")

        # Ensure there are words in the file
        if not words:
            logging.error("The file does not contain any words.")
            return None

        # Return a random word
        random_word = random.choice(words)
        logging.info(f"Random word selected: {random_word}")
        return random_word

    except FileNotFoundError:
        logging.error(f"The file was not found: {file_path}")
        return None
    except Exception as e:
        logging.error(f"An error occurred while processing the file: {e}")
        return None


def split_and_check_word(word_input, word):
    """
    Checks each letter of the input against the target word and assigns a color:
    - 'green' if the letter is correct and in the correct position.
    - 'yellow' if the letter is in the word but in the wrong position.
    - 'gray' if the letter is not in the word.

    :param word_input: A string of letters guessed by the user.
    :param word: The target word to compare against.
    :return: A list of colors representing the correctness of each letter.
    """
    try:
        logging.info(f"Processing input: '{word_input}' against the target word: '{word}'")

        # Validate input and word
        if not isinstance(word_input, str) or not isinstance(word, str):
            raise ValueError("Both input and word must be strings.")
        if len(word) == 0:
            raise ValueError("The target word must not be empty.")

        # Split the input into individual letters
        letters = list(word_input)
        logging.info(f"Split input into letters: {letters}")

        result = []  # Store the color results for each letter

        for index, letter in enumerate(letters):
            if index < len(word) and letter == word[index]:
                result.append('green')  # Correct letter in the correct position
                logging.debug(f"Letter '{letter}' at index {index} is green.")
            elif letter in word:
                result.append('yellow')  # Correct letter in the wrong position
                logging.debug(f"Letter '{letter}' at index {index} is yellow.")
            else:
                result.append('gray')  # Letter not in the word
                logging.debug(f"Letter '{letter}' at index {index} is gray.")

        logging.info(f"Resulting color pattern: {result}")
        return result

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return None

