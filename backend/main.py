from fastapi import FastAPI, UploadFile, File
import pandas as pd
from services.conciliacao import conciliar

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

@app.post("/conciliar")
async def conciliar_arquivos(file1: UploadFile = File(...), file2: UploadFile = File(...)):
    df_a = pd.read_csv(file1.file)
    df_b = pd.read_csv(file2.file)

    resultado = conciliar(df_a, df_b)

    return resultado.to_dict(orient="records")