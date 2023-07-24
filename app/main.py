from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/me")
async def root():
    return {"message": "reilly keating"}
