import httpx
import quran_engine

def letter_counter(message: str):
    response= quran_engine.count_letters(message)
    print(response)
    return response.json().get("response")