from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from validate_guess import validate_word_length, validate_word_meaning
from logical_word_methods import generate_random_word, split_and_check_word
from load_config_file import load_config
import logging
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()


class GuessRequest(BaseModel):
    word: str
    guess: str


@app.get("/en/random-word")
def generate_random_english_word():
    try:
        path_to_words = f"{load_config()['word_generator']}/english.txt"
        return generate_random_word(file_path=path_to_words)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")


@app.post("/en/check-guess")
def check_guess(request: GuessRequest):
    try:
        word_validation_endpoint = load_config()['validate_word_endpoint']
        validate_word_length(word_input=request.guess)
        validate_word_meaning(word_input=request.guess, validate_word_endpoint=word_validation_endpoint)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Invalid word input: {e}")

    return split_and_check_word(word_input=request.guess, word=request.word)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
