import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def validate_word_length(word_input):
    """
    Validates that the input word is exactly 5 characters long.

    :param word_input: The word to be validated.
    :return: true or false if the word is valid length
    """
    try:
        logging.info(f"Validating length of word: {word_input}")

        # Check if the word length is exactly 5
        if len(word_input) != 5:
            logging.error(f"Word '{word_input}' has invalid length: {len(word_input)}. Expected length is 5.")
            return False

        logging.info(f"Word '{word_input}' is valid with length 5.")
        return True

    except Exception as e:
        logging.error(f"An error occurred while validating word length: {e}")
        raise e


def validate_word_meaning(word_input, validate_word_endpoint):
    """
    Validates that the input word exists by sending a GET request to an external validation endpoint.

    :param word_input: The word to be validated.
    :param validate_word_endpoint: The endpoint URL to check the word's existence.
    :return: true or false if the word is valid meaning
    """
    word_input = word_input.upper()
    try:
        # Make the GET request to validate the word
        url = f"{validate_word_endpoint}/{word_input}"
        logging.info(f"Validating meaning of word: {word_input} against {url}")
        response = requests.get(url=url)

        if response.status_code == 200:
            logging.info(f"Word '{word_input}' is valid and exists.")
            return True
        else:
            logging.warning(f"Word '{word_input}' not found. Received status code: {response.status_code} from dictionary API")
            return False

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while validating word meaning: {e}")
        raise e

