import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request

load_dotenv()
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/")
async def say_hello(request: Request):
    data = await request.json()
    name = data.get("name", "World")
    return {"message": f"hello world {name}"}


if __name__ == "__main__":
    config = {
        "host": os.getenv("APP_HOST", "localhost"),
        "port": int(os.getenv("APP_PORT", 8000)),
    }
    uvicorn.run(app=app, **config)
