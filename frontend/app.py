import streamlit as st
import requests
import pandas as pd

st.title("Sistema de Conciliação Financeira")

st.write("Envie dois arquivos CSV para conciliação")

file1 = st.file_uploader("Arquivo A", type=["csv"])
file2 = st.file_uploader("Arquivo B", type=["csv"])

if file1 and file2:
    if st.button("Conciliar"):
        files = {
            "file1": file1,
            "file2": file2
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/conciliar",
                files=files
            )

            if response.status_code == 200:
                data = response.json()
                df = pd.DataFrame(data)

                st.success("Conciliação realizada com sucesso!")

                # 🔥 TABELA COM CORES
                def highlight_status(row):
                    if row["status"] == "Conciliado":
                        return ["background-color: #c6f6d5"] * len(row)
                    elif row["status"] == "Divergente":
                        return ["background-color: #fed7d7"] * len(row)
                    else:
                        return ["background-color: #feebc8"] * len(row)

                st.dataframe(df.style.apply(highlight_status, axis=1))

                # 📊 RESUMO
                st.subheader("Resumo")

                st.write("Conciliados:", len(df[df["status"] == "Conciliado"]))
                st.write("Divergentes:", len(df[df["status"] == "Divergente"]))
                st.write("Não encontrados:", len(df[df["status"] == "Não encontrado"]))

            else:
                st.error("Erro ao processar arquivos")

        except:
            st.error("Erro de conexão com a API. Verifique se o backend está rodando.")