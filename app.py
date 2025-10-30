from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/health1")
def health():
    return {"ok": True}

handler = Mangum(app)