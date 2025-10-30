from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/health")
def health():
    return {"nom": True}# This is a health check endpoint

handler = Mangum(app) 
#히힣