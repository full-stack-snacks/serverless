from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api/degine/{word}")
async def define_word(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    r = requests.get(url + word)
    return r.json()