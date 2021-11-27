from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api/define/{word}")
async def define_word(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    r = requests.get(url + word)
    data = r.json()
    return data[0]["meanings"][0]["definitions"][0]["definition"]
