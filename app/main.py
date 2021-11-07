from typing import Optional

from fastapi import FastAPI, Response, Header

from pydantic import BaseModel


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.patch("/")
async def main(session_id:str = Header(None)):
    print(session_id)
    return Response(status_code=200)