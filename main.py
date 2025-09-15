from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "/helloworld"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": "deu certo"}