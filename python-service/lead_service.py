from database import buscar_lead_por_id
from lead_scoring import analisar_lead

def processar_lead(lead_id):
    lead = buscar_lead_por_id(lead_id)

    if not lead:
        return None

    resultado = analisar_lead(lead)

    return {
        "lead": dict(lead),
        "analise": resultado
    }

if __name__ == "__main__":
    resultado = processar_lead(1)

    if not resultado:
        print("Lead não encontrado.")
    else:
        lead = resultado["lead"]
        analise = resultado["analise"]

        print(f"Lead: {lead['nome']}")
        print(f"Empresa: {lead['empresa']}")
        print(f"Score: {analise['score']}")
        print(f"Classificação: {analise['classificacao']}")

        print("Motivos do score:")
        for motivo in analise["motivos"]:
            print(f"  {motivo}")