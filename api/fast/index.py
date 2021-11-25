from fastapi import FastAPI

app = FastAPI()


@app.get("/")
@app.get("/api/fast")
async def root():
    return {"message": "Hello World"}
