import pandas as pd

def conciliar(df_a, df_b):
    resultado = []

    for _, row_a in df_a.iterrows():
        valor_a = row_a["valor"]
        data_a = row_a["data"]

        match = df_b[
            (df_b["valor"] == valor_a) &
            (df_b["data"] == data_a)
        ]

        if not match.empty:
            status = "Conciliado"
        else:
            # tenta achar só pela data (pra detectar divergência)
            match_data = df_b[df_b["data"] == data_a]

            if not match_data.empty:
                status = "Divergente"
            else:
                status = "Não encontrado"

        resultado.append({
            "data": data_a,
            "valor": valor_a,
            "status": status
        })

    return pd.DataFrame(resultado)
