import json
import quran_engine

def letter_counter(message: str):
    resp= quran_engine.count_letters(message)
    response= json.dumps(resp, indent=4)
    return response

