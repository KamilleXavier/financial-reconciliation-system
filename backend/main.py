from fastapi import FastAPI, UploadFile, File
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Financial Reconciliation API running"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    return {
        "linhas": len(df),
        "colunas": list(df.columns)
    }