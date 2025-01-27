# Wordle Game Backend - Python API

## Overview
This FastAPI-based Python API serves as the backend for a Wordle-style game. It provides functionality to generate random words, validate word guesses, and check guessed words against a target word. The API supports cross-origin resource sharing (CORS) and is configured to log application events.

## Installation Steps
1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the API:
    ```bash
    python main.py
    ```

## API Endpoints

### 1. Generate Random English Word
**Endpoint:**
```
GET /en/random-word
```
**Description:**
Returns a randomly generated English word in uppercase.

**Response:**
- `200 OK`: Returns the random 5 letter word.
- `500 Internal Server Error`: If an error occurs during processing.

**Example Response:**
```json
"ALERT"
```

---

### 2. Validate Word Guess
**Endpoint:**
```
GET /en/validate-guess?guess=<word>
```
**Description:**
Validates if the guessed word meets length and meaning criteria.

**Query Parameters:**
- `guess` (string): The word to be validated.

**Response:**
- `200 OK`: Returns `true` or `false` based on validation.
- `422 Unprocessable Entity`: If the input word is invalid.

**Example Response:**
```json
true
```

---

### 3. Check Guess Against Word
**Endpoint:**
```
POST /en/check-guess-against-word
```
**Description:**
Compares the guessed word to the target word and returns a color-coded result as used in Wordle-style gameplay.

**Request Body:**
```json
{
  "word": "ALERT",
  "guess": "WORLD"
}
```

**Response:**
- `200 OK`: Returns a dictionary mapping the guessed word to its evaluation.
- `400 Bad Request`: If an error occurs.

**Example Response:**
```json
{
  "WORLD": ["gray", "gray", "yellow", "yellow", "gray"]
}
```

---

## Configuration
The API relies on a configuration file loaded via the `load_config` function, which receives the `CONFIG_FILE_PATH` environment variable (uses the local `config.yaml` file if not provided).


## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request. Please ensure that your contributions are well-documented.
