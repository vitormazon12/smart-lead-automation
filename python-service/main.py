from fastapi import FastAPI, HTTPException
from lead_service import processar_lead

app = FastAPI()


@app.get("/")
def home():
    return {
        "status": "ok",
        "message": "Smart Lead Automation API"
    }

@app.get("/leads/{lead_id}")
def obter_lead(lead_id: int):
    resultado = processar_lead(lead_id)

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Lead não encontrado."
        )

    return resultado