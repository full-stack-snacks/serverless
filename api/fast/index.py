from fastapi import FastAPI

app = FastAPI()


@app.get("/api/fast")
async def root():
    return {"message": "Hello World!"}

@app.get("/api/fast/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}