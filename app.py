from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/health1")
def health():
    return {"nom1": True}

handler = Mangum(app) 