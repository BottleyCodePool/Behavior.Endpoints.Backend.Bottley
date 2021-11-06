from typing import Optional

from fastapi import FastAPI, Request

from pydantic import BaseModel


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.put("/behavior", status_code=201)
async def put(request: Request):
    session_Id = request.headers.get('sessionId')
    print(session_Id)
    return {}