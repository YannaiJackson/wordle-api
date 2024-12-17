from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware
from validate_guess import validate_word_length, validate_word_meaning
from logical_word_methods import generate_random_word, split_and_check_word
from load_config_file import load_config
import logging
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# Allow CORS for all origins (or specify a list of origins as needed)
origins = ["*"]  # You can replace "*" with specific URLs, e.g., ["http://localhost:3000"]

# Add the CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of origins that are allowed to make cross-origin requests
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


class GuessRequest(BaseModel):
    word: str
    guess: str


@app.get("/en/random-word")
def generate_random_english_word():
    try:
        path_to_words = f"{load_config()['word_generator']}/english.txt"
        return generate_random_word(file_path=path_to_words).upper()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")


@app.get("/en/validate-guess")
def validate_guess(guess: str):
    try:
        word_validation_endpoint = load_config()['validate_word_endpoint']
        if (validate_word_length(word_input=guess) and
                validate_word_meaning(word_input=guess, validate_word_endpoint=word_validation_endpoint)):
            return True
        return False
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Invalid word input: {e}")


@app.post("/en/check-guess-against-word")
def check_guess(request: GuessRequest):
    try:
        color_list = split_and_check_word(word_input=request.guess, word=request.word)
        res = {
            request.guess: color_list
        }
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {e}")
