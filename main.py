from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, Earthlings!", "message": "Welcome to FastAPI!"}
