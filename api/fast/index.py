from fastapi import FastAPI

app = FastAPI()


@app.get("/api/fast")
async def root():
    return {"message": "Hello World!"}
